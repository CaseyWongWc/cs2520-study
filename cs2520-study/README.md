# Project Overview

This project, `cs2520-study`, is designed to facilitate learning and experimentation with file management and command execution in Python, particularly through the use of Jupyter notebooks. It includes various tools and templates to streamline project creation and management.

## Project Structure

- **UnOrdered/4_23_2026.ipynb**: A Jupyter notebook containing Python code for managing files and directories. It includes functions for creating directories, files, removing paths, and running shell commands.

- **tools/**: A directory containing utility modules for file system operations and shell command execution.
  - **`__init__.py`**: Marks the `tools` directory as a Python package.
  - **fs.py**: Contains functions and classes related to file system operations, such as creating, reading, and writing files or directories.
  - **shell.py**: Includes functions for executing shell commands and interacting with the system shell.
  - **widgets.py**: Defines GUI components or widgets for user interaction within the project.

- **templates/new_project.ipynb**: A Jupyter notebook template for creating new projects, providing a predefined structure and content.

- **requirements.txt**: Lists the Python dependencies required for the project, specifying the packages that need to be installed for successful execution.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/CaseyWongWc/cs2520-study.git
   ```

2. Navigate to the project directory:
   ```
   cd cs2520-study
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

- Open the Jupyter notebook `UnOrdered/4_23_2026.ipynb` to explore file management functionalities.
- Use the `templates/new_project.ipynb` as a starting point for new projects.
- Utilize the tools in the `tools` directory for additional functionalities related to file systems and shell commands.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.