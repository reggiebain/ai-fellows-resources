# Monty Hall Problem - AI-Enhanced Lesson for Grades 9-10

## Overview
This lesson uses hands-on simulation and computational verification to teach conditional probability through the famous Monty Hall problem. Students experience the power of large-scale computational experiments—a fundamental principle underlying modern AI and machine learning.

## Materials Included

### 1. Teacher Lesson Plan (`monty_hall_lesson_plan.docx`)
A comprehensive lesson plan including:
- Learning objectives
- Discussion questions and talking points
- Ideas for differentiation
- Common misconceptions and how to address them
- Printable student handout with data recording table

### 2. Python Simulation Code (`monty_hall_simulation.py`)
Interactive simulation with three visualizations:
- **Static visualization** (10,000 trials) - Best for quick classroom projection
- **Sample size comparison** (100, 1,000, 10,000 trials) - Great for discussing the Law of Large Numbers
- **Animated visualization** - Live simulation that students can watch

### 3. Pre-generated Visualizations
- `monty_hall_static.png` - Complete results with bar chart and convergence graph
- `monty_hall_comparison.png` - Side-by-side comparison showing effect of sample size

## Quick Start Guide

### For Teachers New to Python
1. **Use the pre-generated images** - Simply project `monty_hall_static.png` on your smart board during Part 3 of the lesson, no coding required!

### For Teachers Comfortable with Python

#### Setup (One-time)
```bash
# Install required libraries
pip install matplotlib numpy
```

#### Running the Simulation
```bash
# Option 1: Generate static images (recommended for first time)
python monty_hall_simulation.py

# Option 2: Run just the animation in class (exciting!)
# Edit the file and uncomment the animation section at the bottom
```

#### Customization Options
You can modify the simulation parameters:
- Change number of trials: `create_static_visualization(5000)` instead of 10000
- Adjust animation speed: `interval=50` (milliseconds between frames)
- Compare different sample sizes: `run_comparison([50, 500, 5000])`

## Lesson Implementation Tips

### Before Class
1. ✅ Print student handouts (included in lesson plan, pages 9-11)
2. ✅ Gather materials: 3 cups + 1 small object per group of 3-4 students
3. ✅ Test the simulation OR verify pre-generated images display correctly
4. ✅ Read through the "Common Misconceptions" section - students WILL be confused!

### During Class - Critical Success Factors
- **Part 1**: Build anticipation! Poll students BEFORE revealing the answer
- **Part 2**: Model the protocol clearly - groups must stick to "always switch" or "always stay"
- **Part 3**: Let the simulation results sink in - embrace the shocked silence
- **Part 4**: Guide discussion gently - this is where real learning happens

### Common Pitfalls to Avoid
- ❌ Don't explain the math before the hands-on activity
- ❌ Don't rush the discussion after the simulation reveal
- ❌ Don't let groups accidentally switch strategies mid-experiment
- ✅ DO embrace the cognitive dissonance - confusion is learning!

## Connection to AI & Data Science

This lesson introduces students to several key concepts:
- **Monte Carlo Methods** - Named after casinos, used throughout AI/ML
- **Reinforcement Learning** - How AI learns by playing millions of simulated games
- **Law of Large Numbers** - Why AI needs massive datasets to learn effectively
- **Computational Verification** - Using simulation to test mathematical principles

## Standards Alignment

**Common Core Mathematics:**
- HSS.CP.A.1 (Understand and use conditional probability)
- HSS.IC.B.3 (Recognize purposes and differences in sample surveys)

**NGSS Science & Engineering Practices:**
- Using mathematics and computational thinking

## Extensions & Follow-Up

### For Advanced Students
- Modify the code to test: What if there were 4 doors? 100 doors?
- Calculate theoretical probabilities using probability trees
- Research other famous paradoxes (Birthday Paradox, Simpson's Paradox)

### Cross-Curricular Connections
- **History**: Research Marilyn vos Savant's famous 1990 Parade magazine column
- **Computer Science**: Analyze the simulation code, modify parameters
- **Psychology**: Why does human intuition fail on this problem?

## Technical Notes

### Python Visualization Details
The simulation uses matplotlib for visualization with two main components:
1. **Bar charts** showing final win percentages for each strategy
2. **Line graphs** showing how percentages converge over time

Color coding:
- Green = Switch strategy (~67% win rate)
- Red = Stay strategy (~33% win rate)
- Dashed lines = Expected theoretical probabilities

### Troubleshooting

**Problem**: Python script won't run
**Solution**: Check that matplotlib and numpy are installed: `pip install matplotlib numpy`

**Problem**: Animation creates errors
**Solution**: Use the static images instead - they're just as effective pedagogically

**Problem**: Students don't believe the results
**Solution**: Perfect! Show them the code. Discuss sample size. Run it again with different parameters.

## Assessment Rubric

### Exit Ticket Scoring
**Proficient (3 points):**
- Correctly explains why switching wins 2/3 of the time
- Accurately describes the role of sample size
- Makes connections to computational thinking

**Developing (2 points):**
- Describes the outcome but struggles with explanation
- Recognizes sample size matters but can't explain why
- Acknowledges connection to computation but vaguely

**Beginning (1 point):**
- Still believes it's 50/50 or insists simulation is wrong
- Doesn't recognize role of sample size
- Minimal engagement with computational thinking

## Additional Resources

### Videos
- Numberphile's "The Monty Hall Problem" (YouTube) - Great for visual learners
- Khan Academy's probability series - For students needing math review

### Reading
- "The Curious Incident of the Dog in the Night-Time" by Mark Haddon - Features the Monty Hall problem in the narrative

### For Teachers
- "The Drunkard's Walk" by Leonard Mlodinow - Excellent background on probability and randomness

## Contact & Feedback

This lesson was developed as part of the GSSM AI Faculty Fellows program.

**Questions?** Contact your AI Fellows program coordinator.

**Improvements?** We'd love to hear how the lesson went and any modifications you made!

---

## Quick Reference: Lesson Timeline

| Time | Activity | Key Points |
|------|----------|------------|
| 0-5 min | Setup & Prediction | Poll students, create cognitive dissonance |
| 5-20 min | Hands-on Simulation | 20 trials per group, expect messy results |
| 20-35 min | Computer Simulation | Show 10,000 trials, watch faces! |
| 35-45 min | Discussion & Explanation | Guide understanding, connect to AI |
| 45-50 min | Exit Ticket | Assess understanding |

**Remember:** The confusion IS the lesson. Embrace it!
