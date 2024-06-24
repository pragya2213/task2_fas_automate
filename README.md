# test_0001

# Task Automate Fake Story API Endpoints


1. **Clone the repository**.
   Open a terminal, change to your desired workspace folder, and run the following command to clone this repository:

   ```bash
   git clone https://github.com/pragya2213/task2_fas_automate.git
   ```

2. **Create a virtual environment**.
   Run the following command to create the virtual environment:


   ```bash
   python -m venv env1
   ```

3. **Activate virtual environment**.
   Activate the virtual environment depending upon the operating systems:
   - On Windows (using Command Prompt):

    ```bash
     env1\Scripts\activate
    ```

   - On Windows (using PowerShell):

    ```bash
     .\env1\Scripts\Activate.ps1
    ```

   - on macOS and Linux:

    ```bash
     source env1/bin/activate
    ```

4. **Installing dependencies in a virtual environment**.
   Once the virtual environment is activated, install dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```
5. **Run Tests**.
   Once the dependencies are installed, run existing tests using the following command:

   ```shell
   pytest
   ```
6. **Writing/adding test cases**.
   An example test file is located in the 'tests' folder which can be extended with further scenarios. Make changes to the test files, commit and push the code.


7. **Run tests on CI**.
   An example workflow yaml file (below) is created to run tests on CI. Modify the file if changes are needed and push the code to effect the changes.

   ```yaml

    name: Pytest API Testing

    on:
      push:
        branches: [ "main" ]
      pull_request:
        branches: [ "main" ]

    permissions:
      contents: read

    jobs:
      Pytes-API-Testing:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: "3.10"
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
            
        - name: Test with pytest
          run: |
            pytest

    ```  



# Future Improvements
  * Add more test cases.
  * Add config for different environments.
  * Add test report generation and storage on CI.
  * Implement data driven testing.
  * Implement pytest parallel testing.


