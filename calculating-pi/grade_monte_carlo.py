"""
Monte Carlo Simulation Grading Script
======================================

This script automatically grades student submissions for the Monte Carlo π simulation notebook.

Usage:
    python grade_monte_carlo.py <student_notebook.ipynb>

Grading Criteria:
- Task 1: generate_random_points() function (20 points)
- Task 2: is_inside_circle() function (20 points)
- Task 3: estimate_pi() function (25 points)
- Task 4: analyze_convergence() function (15 points)
- Task 5: run_multiple_simulations() function (15 points)
- Code style and documentation (5 points)

Total: 100 points
"""

import sys
import json
import numpy as np
import math
from typing import Dict, List, Tuple

class MonteCarloGrader:
    def __init__(self):
        self.total_points = 0
        self.max_points = 100
        self.feedback = []
        np.random.seed(42)  # For consistent grading
    
    def grade_generate_random_points(self, func) -> Tuple[float, str]:
        """Grade the generate_random_points function."""
        points = 0
        feedback = []
        
        try:
            # Test 1: Function exists and is callable
            if not callable(func):
                feedback.append("❌ Function is not callable")
                return 0, "\n".join(feedback)
            points += 2
            
            # Test 2: Returns tuple of correct length
            result = func(100)
            if not isinstance(result, tuple) or len(result) != 2:
                feedback.append("❌ Function should return a tuple of (x, y)")
                return points, "\n".join(feedback)
            points += 3
            
            x, y = result
            
            # Test 3: Returns numpy arrays
            if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
                feedback.append("❌ Function should return numpy arrays")
                return points, "\n".join(feedback)
            points += 3
            
            # Test 4: Correct number of points
            if len(x) != 100 or len(y) != 100:
                feedback.append(f"❌ Should generate exactly 100 points, got {len(x)} x-coords and {len(y)} y-coords")
                return points, "\n".join(feedback)
            points += 4
            
            # Test 5: Points within correct range
            if not (np.all(x >= -1) and np.all(x <= 1)):
                feedback.append("❌ x-coordinates should be between -1 and 1")
                return points, "\n".join(feedback)
            points += 4
            
            if not (np.all(y >= -1) and np.all(y <= 1)):
                feedback.append("❌ y-coordinates should be between -1 and 1")
                return points, "\n".join(feedback)
            points += 4
            
            feedback.append("✓ generate_random_points() works correctly!")
            
        except Exception as e:
            feedback.append(f"❌ Error testing function: {str(e)}")
        
        return points, "\n".join(feedback)
    
    def grade_is_inside_circle(self, func) -> Tuple[float, str]:
        """Grade the is_inside_circle function."""
        points = 0
        feedback = []
        
        try:
            # Test 1: Function exists and is callable
            if not callable(func):
                feedback.append("❌ Function is not callable")
                return 0, "\n".join(feedback)
            points += 2
            
            # Test 2: Known points
            test_cases = [
                ([0], [0], [True]),  # Origin
                ([1], [0], [True]),  # On circle
                ([0.5], [0.5], [True]),  # Inside
                ([1.5], [0], [False]),  # Outside
                ([0.8], [0.8], [False]),  # Outside
            ]
            
            for x, y, expected in test_cases:
                result = func(np.array(x), np.array(y))
                if not isinstance(result, np.ndarray):
                    feedback.append("❌ Function should return numpy array")
                    return points, "\n".join(feedback)
                
                if not np.array_equal(result, expected):
                    feedback.append(f"❌ For point ({x[0]}, {y[0]}), expected {expected[0]}, got {result[0]}")
                    return points, "\n".join(feedback)
                points += 3
            
            # Test 3: Array of points
            x_array = np.array([0, 0.5, 1.5, 0, -0.7])
            y_array = np.array([0, 0.5, 0, 1.5, -0.7])
            result = func(x_array, y_array)
            
            if len(result) != len(x_array):
                feedback.append("❌ Output array should have same length as input")
                return points, "\n".join(feedback)
            points += 3
            
            feedback.append("✓ is_inside_circle() works correctly!")
            
        except Exception as e:
            feedback.append(f"❌ Error testing function: {str(e)}")
        
        return points, "\n".join(feedback)
    
    def grade_estimate_pi(self, func) -> Tuple[float, str]:
        """Grade the estimate_pi function."""
        points = 0
        feedback = []
        
        try:
            # Test 1: Function exists and is callable
            if not callable(func):
                feedback.append("❌ Function is not callable")
                return 0, "\n".join(feedback)
            points += 3
            
            # Test 2: Returns correct number of values
            result = func(1000)
            if not isinstance(result, tuple) or len(result) != 4:
                feedback.append("❌ Function should return tuple of (pi_estimate, x, y, inside)")
                return points, "\n".join(feedback)
            points += 4
            
            pi_est, x, y, inside = result
            
            # Test 3: π estimate is reasonable
            if not isinstance(pi_est, (int, float, np.number)):
                feedback.append("❌ π estimate should be a number")
                return points, "\n".join(feedback)
            points += 4
            
            if not (2.5 < pi_est < 4.0):
                feedback.append(f"❌ π estimate {pi_est:.4f} is unreasonable (should be between 2.5 and 4.0)")
                return points, "\n".join(feedback)
            points += 4
            
            # Test 4: Arrays have correct length
            if len(x) != 1000 or len(y) != 1000 or len(inside) != 1000:
                feedback.append("❌ Arrays should have length equal to n")
                return points, "\n".join(feedback)
            points += 4
            
            # Test 5: Estimate improves with more samples
            pi_est_small = func(100)[0]
            pi_est_large = func(100000)[0]
            
            error_small = abs(pi_est_small - math.pi)
            error_large = abs(pi_est_large - math.pi)
            
            if error_large <= error_small:
                points += 3
                feedback.append("✓ Estimate improves with more samples")
            else:
                feedback.append("⚠ Estimate should generally improve with more samples")
                points += 1
            
            # Test 6: Reasonable accuracy with large n
            if error_large < 0.1:
                points += 3
                feedback.append("✓ Good accuracy with large sample size")
            elif error_large < 0.2:
                points += 2
                feedback.append("⚠ Moderate accuracy with large sample size")
            else:
                points += 1
                feedback.append("⚠ Accuracy could be better")
            
            feedback.append("✓ estimate_pi() works correctly!")
            
        except Exception as e:
            feedback.append(f"❌ Error testing function: {str(e)}")
        
        return points, "\n".join(feedback)
    
    def grade_analyze_convergence(self, func) -> Tuple[float, str]:
        """Grade the analyze_convergence function."""
        points = 0
        feedback = []
        
        try:
            # Test 1: Function exists and is callable
            if not callable(func):
                feedback.append("❌ Function is not callable")
                return 0, "\n".join(feedback)
            points += 3
            
            # Test 2: Returns correct structure
            result = func(max_n=10000, num_points=10)
            if not isinstance(result, tuple) or len(result) != 2:
                feedback.append("❌ Function should return tuple of (sample_sizes, pi_estimates)")
                return points, "\n".join(feedback)
            points += 4
            
            sample_sizes, pi_estimates = result
            
            # Test 3: Correct lengths
            if len(sample_sizes) != 10 or len(pi_estimates) != 10:
                feedback.append(f"❌ Should return 10 values, got {len(sample_sizes)} and {len(pi_estimates)}")
                return points, "\n".join(feedback)
            points += 4
            
            # Test 4: Sample sizes are increasing
            if not np.all(np.diff(sample_sizes) > 0):
                feedback.append("❌ Sample sizes should be increasing")
                return points, "\n".join(feedback)
            points += 4
            
            feedback.append("✓ analyze_convergence() works correctly!")
            
        except Exception as e:
            feedback.append(f"❌ Error testing function: {str(e)}")
        
        return points, "\n".join(feedback)
    
    def grade_run_multiple_simulations(self, func) -> Tuple[float, str]:
        """Grade the run_multiple_simulations function."""
        points = 0
        feedback = []
        
        try:
            # Test 1: Function exists and is callable
            if not callable(func):
                feedback.append("❌ Function is not callable")
                return 0, "\n".join(feedback)
            points += 3
            
            # Test 2: Returns dictionary with correct keys
            result = func(n=1000, num_runs=10)
            if not isinstance(result, dict):
                feedback.append("❌ Function should return a dictionary")
                return points, "\n".join(feedback)
            points += 3
            
            required_keys = ['mean', 'std', 'min', 'max', 'mean_error']
            for key in required_keys:
                if key not in result:
                    feedback.append(f"❌ Dictionary should contain key '{key}'")
                    return points, "\n".join(feedback)
            points += 3
            
            # Test 3: Values are reasonable
            if not (2.5 < result['mean'] < 4.0):
                feedback.append(f"❌ Mean estimate {result['mean']:.4f} is unreasonable")
                return points, "\n".join(feedback)
            points += 2
            
            if result['std'] <= 0:
                feedback.append("❌ Standard deviation should be positive")
                return points, "\n".join(feedback)
            points += 2
            
            if result['min'] >= result['max']:
                feedback.append("❌ Minimum should be less than maximum")
                return points, "\n".join(feedback)
            points += 2
            
            feedback.append("✓ run_multiple_simulations() works correctly!")
            
        except Exception as e:
            feedback.append(f"❌ Error testing function: {str(e)}")
        
        return points, "\n".join(feedback)
    
    def generate_report(self) -> str:
        """Generate a grading report."""
        report = []
        report.append("="*70)
        report.append("MONTE CARLO SIMULATION - GRADING REPORT")
        report.append("="*70)
        report.append("")
        
        for item in self.feedback:
            report.append(item)
        
        report.append("")
        report.append("="*70)
        report.append(f"TOTAL SCORE: {self.total_points}/{self.max_points}")
        report.append("="*70)
        
        # Letter grade
        percentage = (self.total_points / self.max_points) * 100
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        report.append(f"Percentage: {percentage:.1f}%")
        report.append(f"Letter Grade: {grade}")
        report.append("")
        
        return "\n".join(report)


def extract_functions_from_notebook(notebook_path: str) -> Dict:
    """Extract student functions from Jupyter notebook."""
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    # Combine all code cells
    code = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code.append(''.join(cell['source']))
    
    full_code = '\n'.join(code)
    
    # Create namespace and execute code
    namespace = {}
    exec(full_code, namespace)
    
    return namespace


def main():
    if len(sys.argv) != 2:
        print("Usage: python grade_monte_carlo.py <student_notebook.ipynb>")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    
    print(f"Grading notebook: {notebook_path}")
    print("="*70)
    
    grader = MonteCarloGrader()
    
    try:
        # Extract functions from notebook
        namespace = extract_functions_from_notebook(notebook_path)
        
        # Grade each task
        tasks = [
            ('generate_random_points', 20, grader.grade_generate_random_points),
            ('is_inside_circle', 20, grader.grade_is_inside_circle),
            ('estimate_pi', 25, grader.grade_estimate_pi),
            ('analyze_convergence', 15, grader.grade_analyze_convergence),
            ('run_multiple_simulations', 15, grader.grade_run_multiple_simulations),
        ]
        
        for func_name, max_pts, grading_func in tasks:
            grader.feedback.append(f"\nTask: {func_name} (Max: {max_pts} points)")
            grader.feedback.append("-" * 70)
            
            if func_name in namespace:
                points, feedback = grading_func(namespace[func_name])
                grader.total_points += points
                grader.feedback.append(feedback)
                grader.feedback.append(f"Points earned: {points}/{max_pts}")
            else:
                grader.feedback.append(f"❌ Function '{func_name}' not found in notebook")
                grader.feedback.append(f"Points earned: 0/{max_pts}")
        
        # Code style points (basic check)
        grader.feedback.append("\nCode Style and Documentation (Max: 5 points)")
        grader.feedback.append("-" * 70)
        style_points = 5  # Default full points, deduct for major issues
        grader.total_points += style_points
        grader.feedback.append(f"✓ Code style acceptable")
        grader.feedback.append(f"Points earned: {style_points}/5")
        
        # Generate and print report
        report = grader.generate_report()
        print(report)
        
        # Save report to file
        report_path = notebook_path.replace('.ipynb', '_grade_report.txt')
        with open(report_path, 'w') as f:
            f.write(report)
        print(f"\nGrading report saved to: {report_path}")
        
    except Exception as e:
        print(f"Error during grading: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
