# Task Automate Task warrior CLI and Fake Story API Endpoints

In this repository, below tasks are implemented
* Taskwarrior CLI automation
* Fake Story API Endpoint automation
  
1. **Install Taskwarrior CLI**.
   Open a terminal and install taskwarrior CLI application:
   - on macOS and Linux:
   ```bash
   sudo apt-get install taskwarrior
   ```
2. **Clone the repository**.
   Open a terminal, change to your desired workspace folder, and run the following command to clone this repository:

   ```bash
   git clone https://github.com/pragya2213/task_fas_twcli_automate.git
   ```

3. **Create a virtual environment**.
   Run the following command to create the virtual environment:


   ```bash
   python -m venv env1
   ```

4. **Activate virtual environment**.
   Activate the virtual environment depending upon the operating systems:
   
   - on macOS and Linux:

    ```bash
     source env1/bin/activate
    ```
   - On Windows (using Command Prompt):

    ```bash
     env1\Scripts\activate
    ```

   - On Windows (using PowerShell):

    ```bash
     .\env1\Scripts\Activate.ps1
    ```

5. **Installing dependencies in a virtual environment**.
   Once the virtual environment is activated, install dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```
6. **Run Tests**.
   Once the dependencies are installed, run existing tests using the following command:

   ```shell
   pytest
   ```
7. **Writing/adding test cases**.
   In the tests folder following two files are implemented:
   * test_taskwarrior.py: Contains 3 scenarios for adding a task, listing all tasks and completing a atask using taskwarrior CLI  
   * test_fakeapistory_cart.py: Contains 5 scenarios related to fakestory api endpoints from 'carts' section
   
   Both files can be extended with further scenarios specific to the applications. Make changes to the test files, commit and push the code.


8. **Run tests on CI**.
   An example workflow yaml file (below) is created to run tests on CI. Modify the file if changes are needed and push the code to effect the changes.

   ```yaml

    name: FakeStoryAPI Test

    on:
      push:
        branches: [ "main" ]
      pull_request:
        branches: [ "main" ]

    permissions:
      contents: read

    jobs:
      FakeStoryAPI-Testing:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: "3.10"
        - name: Install Taskwarrior
          run: sudo apt-get install taskwarrior
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


