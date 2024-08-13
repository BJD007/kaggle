Setting up a virtual environment is an essential step when starting a new Python project, as it helps you manage dependencies and keep your project isolated from other Python projects. Here's how you can set up a virtual environment each time you start a new project:

### Step 1: Install Python and `virtualenv`
- Ensure you have Python installed. You can check by running:
  ```bash
  python3 --version
  ```
- Install `virtualenv` (if not already installed) using pip:
  ```bash
  pip3 install virtualenv
  ```

### Step 2: Create a Project Directory
- Create a directory for your new project:
  ```bash
  mkdir my_project
  cd my_project
  ```

### Step 3: Create a Virtual Environment
- Create a virtual environment inside your project directory:
  ```bash
  virtualenv venv
  ```
  - `venv` is the name of the virtual environment folder. You can choose any name, but `venv` is commonly used.

### Step 4: Activate the Virtual Environment
- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

After activation, your terminal prompt will change to show the name of the virtual environment, indicating that it's active.

### Step 5: Install Project Dependencies
- Now that your virtual environment is active, you can install any dependencies your project needs using pip. For example:
  ```bash
  pip install numpy pandas
  ```

### Step 6: Deactivate the Virtual Environment
- When you're done working in your project, you can deactivate the virtual environment by simply running:
  ```bash
  deactivate
  ```

### Step 7: Reactivate the Virtual Environment Later
- Whenever you return to your project and want to reactivate the virtual environment, navigate to your project directory and run the activation command again:
  - **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### Step 8: Using `requirements.txt` (Optional)
- To freeze the current dependencies into a `requirements.txt` file, run:
  ```bash
  pip freeze > requirements.txt
  ```
- To install dependencies from an existing `requirements.txt` file in a new environment:
  ```bash
  pip3 install -r requirements.txt
  ```

### Summary
By following these steps, you create a clean, isolated environment for each of your Python projects, ensuring that dependencies do not conflict with other projects.