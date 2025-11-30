# Setup Guide

This guide covers how to set up and use the AI Fellows Resources for both teachers and developers.

## For Teachers: Using Google Colab (Recommended)

**No installation needed!** This is the easiest way to use these resources.

### Steps:

1. **Open any notebook** in this repository
2. **Click the "Open in Colab" badge** at the top of the notebook
3. **Sign in** with your Google account (if not already signed in)
4. **Run the first code cell** - it will automatically install required packages
5. **Start teaching!** All cells will work just like a regular Jupyter notebook

### Benefits of Colab:
- ✅ No software installation required
- ✅ Works on any device with a web browser
- ✅ Free access to computing resources
- ✅ Easy to share with students
- ✅ Automatic package management

### Sharing with Students:

You can share notebooks with students in two ways:

1. **Direct Link**: Share the Colab URL after clicking the badge
2. **Google Classroom**: Upload the `.ipynb` file to Google Classroom, students can open it in Colab

---

## For Developers: Local Setup with UV

If you're contributing to this repository or prefer working locally, we use [UV](https://github.com/astral-sh/uv) for package management.

### Why UV?

- **Fast**: 10-100x faster than pip
- **Reliable**: Reproducible environments across machines
- **Simple**: Single tool for virtual environments and package management
- **Compatible**: Works with standard Python packaging (pyproject.toml)

### Installation

#### macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Alternative (using pip):
```bash
pip install uv
```

### Setting Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/reggiebain/ai-fellows-resources.git
   cd ai-fellows-resources
   ```

2. **Create a virtual environment**:
   ```bash
   uv venv
   ```

3. **Activate the environment**:
   
   **macOS/Linux**:
   ```bash
   source .venv/bin/activate
   ```
   
   **Windows**:
   ```cmd
   .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

### Running Jupyter Notebooks Locally

```bash
# Option 1: Using uv run (recommended)
uv run jupyter notebook

# Option 2: After activating the environment
source .venv/bin/activate
jupyter notebook
```

### Running Scripts

```bash
# Run the grading script
uv run python calculating-pi/grade_monte_carlo.py student_notebook.ipynb

# Or with activated environment
source .venv/bin/activate
python calculating-pi/grade_monte_carlo.py student_notebook.ipynb
```

### Adding New Dependencies

If you need to add a new package:

```bash
# Add to pyproject.toml dependencies, then:
uv pip install -e .

# Or install directly:
uv pip install package-name
```

---

## Package Requirements

All notebooks use the following Python packages:
- **numpy** (≥1.24.0) - Numerical computations
- **matplotlib** (≥3.7.0) - Visualizations and animations
- **jupyter** (≥1.0.0) - Notebook interface
- **ipython** (≥8.0.0) - Interactive Python

These are automatically installed in both Colab and UV environments.

---

## Troubleshooting

### Google Colab Issues

**Problem**: "Package not found" error  
**Solution**: Make sure to run the first code cell that installs packages

**Problem**: Notebook won't open in Colab  
**Solution**: Try downloading the `.ipynb` file and uploading it directly to Colab at [colab.research.google.com](https://colab.research.google.com)

**Problem**: Visualizations not showing  
**Solution**: Colab should display matplotlib plots automatically. Try restarting the runtime (Runtime → Restart runtime)

### UV/Local Setup Issues

**Problem**: `uv: command not found`  
**Solution**: Make sure UV is installed and in your PATH. Try closing and reopening your terminal.

**Problem**: Python version mismatch  
**Solution**: UV will use Python 3.10 as specified in `.python-version`. Make sure you have Python 3.10+ installed on your system.

**Problem**: Import errors after installation  
**Solution**: Make sure you've activated the virtual environment:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

**Problem**: Jupyter kernel not found  
**Solution**: Install ipykernel in the UV environment:
```bash
uv pip install ipykernel
uv run python -m ipykernel install --user --name=ai-fellows
```

---

## Development Workflow

For contributors working on these materials:

1. **Create a new branch** for your changes
2. **Set up UV environment** as described above
3. **Make your changes** to notebooks or code
4. **Test thoroughly**:
   - Run notebooks locally with UV
   - Test in Google Colab
   - Run any grading scripts
5. **Commit and push** your changes
6. **Create a pull request**

### Testing Notebooks in Colab

Before committing notebook changes:

1. Upload the notebook to your Google Drive
2. Open in Colab
3. Run all cells to ensure they work
4. Verify the "Open in Colab" badge links correctly

---

## Additional Resources

- [UV Documentation](https://github.com/astral-sh/uv)
- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

---

## Getting Help

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/reggiebain/ai-fellows-resources/issues)
2. Create a new issue with:
   - Your operating system
   - Python version
   - Error message (if any)
   - Steps to reproduce the problem
