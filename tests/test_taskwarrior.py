import subprocess

class TestTaskWarrior:
    def test_add_task(self):       
        #create a task
        p = subprocess.Popen(['task','add','test_task_add'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        p.stdin.write("yes\n")
        output, errors = p.communicate()
        p.stdin.close()

        # Verify created task string in response
        assert "Created task" in output
    
    def test_list_all_task(self):       
        #create a task
        subprocess.run(['task','add','test_task_list'], capture_output=True, text=True, check=True)
        #list all tasks
        response = subprocess.run(['task','list'], capture_output=True, text=True, check=True)

        # Verify task list structure in response
        assert "ID" in response.stdout
        assert "Age" in response.stdout
        assert "Description" in response.stdout
        assert "Urg" in response.stdout
        assert "test_task_list" in response.stdout
   

    def test_complete_task(self):       
        #create a test task
        subprocess.run(['task','add','test_task_complete'], capture_output=True, text=True, check=True)
        #complete a task
        p = subprocess.Popen(['task','/test_task_complete/','done'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        p.stdin.write("yes\n")
        output, errors = p.communicate()
        p.stdin.close()
        # Verify Completed task in response
        assert "Completed task" in output