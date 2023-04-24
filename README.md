# fast_ds

Data science at high speed

# 0. How to set up git repository

1. Go to git, press + and create new repository
2. Copy the SSH clone
3. Type `git clone <repository> fast_ds/` in terminal
4. Open up new VSCode window clicking on the directory fast_ds BUT NOT OPENING IT.
5. Make fast_ds directory within fast_ds for future imports
6. Create **init**.py file in EVERY subfolder (it can be empty)
7. If you use conda, you should be fine. you can always make a conda environment if you would like. If you use pip, then set up a virtual environment using `python -m venv venv/`. Then activate it using `source venv/bin/activate`
8. Add in a `.vscode` directory, and inside put the launch.json and settings.json. Copy everything, but you can skip the default interpreter path, which is specific to my computer.

# 1. Create models

Structure in five functions for reuse

# 2. Groupby-apply + Github

1. Create a new repository and add your model creation code
2. Create categorical variables in your data
3. Use groupby-apply in 3 ways: Series vs. DataFrame, as a "reduce". In the case of map, you can just run groupby().apply()
   - https://realpython.com/pandas-groupby/
   - https://www.youtube.com/watch?v=qy0fDqoMJx8
4. Test out the idea of a class
