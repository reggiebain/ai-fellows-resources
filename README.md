# AI Resources for Educators
#### Developed by Reggie Bain

## About This Repository

This repository contains curriculum materials, lesson plans, and teaching resources created as part of the South Carolina Governor's School for Science and Mathematics (GSSM) Google AI Faculty Fellows program. The goal is to provide **free, appropriate, and practical curriculum** for K-12 teachers to integrate AI and data science concepts across subject areas.

### Program Overview

The AI Faculty Fellows program develops resources to:
- Introduce AI and data science concepts to K-12 students
- Support teachers in incorporating AI as a teaching and learning tool
- Bridge the opportunity gap in AI education across school districts
- Create accessible entry points to computational thinking and AI applications

## Repository Structure

```
ai-fellows-resources/
└── monte-carlo/          # Monte Carlo simulation lesson for estimating π
    ├── monte_carlo_pi_simulation.ipynb        # Student Jupyter notebook
    ├── grade_monte_carlo.py                    # Automated grading script
    ├── monte_carlo_teacher_guide.pdf           # Comprehensive teacher guide
    └── monte_carlo_ai_connection.md            # Why Monte Carlo matters for AI
```

## Current Resources

### Monte Carlo Simulation

**Grade Level:** 11th-12th grade (adaptable for 9th-10th)  
**Duration:** 2-3 class periods (90-135 minutes)  
**Topics:** Probability, computational thinking, random sampling, convergence

An introduction to Monte Carlo methods through calculating π using random sampling. Students learn probabilistic algorithms that underpin modern AI and machine learning.

**What's Included:**
- **Student Notebook:** Interactive Jupyter notebook with 5 coding tasks, visualizations, and reflection questions
- **Grading Script:** Automated Python script that tests student functions and generates detailed feedback reports
- **Teacher Guide:** 10-page PDF with lesson plans, differentiation strategies, common issues, and assessment rubrics
- **AI Connections:** Explanation of how Monte Carlo methods relate to neural networks, reinforcement learning, and real-world AI

**Prerequisites:**
- Basic Python programming (variables, functions, loops)
- Coordinate geometry
- Basic probability concepts
- Familiarity with Jupyter notebooks

## How to Use These Resources

### For Teachers

1. **Review the teacher guide** to understand lesson objectives, structure, and timing
2. **Test the student notebook** yourself to familiarize with the coding tasks
3. **Set up student environment:**
   - Jupyter notebooks (JupyterLab, Google Colab, or VS Code)
   - Python 3.x with `numpy` and `matplotlib` libraries
4. **Adapt as needed** for your classroom context and student level
5. **Use the grading script** to efficiently assess student work

### For Students

1. Open the Jupyter notebook for your lesson in Google Colab
2. Follow the instructions in each cell
3. Complete the TODO tasks in the code cells
4. Run cells to test your work
5. Answer reflection questions
6. Submit your completed notebook to your instructor


## Quick Start

### Option 1: Google Colab (Easiest for Teachers)

**No installation required!** Click the "Open in Colab" badge at the top of any notebook to run it directly in your browser.

1. Click the Colab badge in the notebook
2. Sign in with your Google account
3. Run all cells - packages install automatically
4. Start teaching!

### Option 2: Local Development with UV

For developers or those who prefer local environments:

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/reggiebain/ai-fellows-resources.git
cd ai-fellows-resources

# Create environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .

# Launch Jupyter
uv run jupyter notebook
```

See [SETUP.md](SETUP.md) for detailed installation instructions.

### Running the Grading Script
```bash
# With UV
uv run python calculating-pi/grade_monte_carlo.py student_notebook.ipynb

# Or activate the environment first
source .venv/bin/activate
python calculating-pi/grade_monte_carlo.py student_notebook.ipynb
```

This generates a detailed grade report saved as `student_notebook_grade_report.txt`.

## Future Resources

Additional curriculum modules are under development, including:
- AI-assisted teaching tools for educators
- Ethical AI integration frameworks
- Subject-specific AI applications
- Assessment and evaluation tools

*Last Updated: November 2025*
