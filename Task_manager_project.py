from datetime import datetime, date

class Task:

    all_task = []
    incomplete = []
    complete = []
    create_time = {}
    updated_time = {}
    complete_time = {}
    
    def add_new_task(self, task):
        self.all_task.append(task)
        self.incomplete.append(task)

    def show_all_task(self):
        for i in range(len(self.all_task)):
            print('\n', end="")
            print("ID -", id(self.all_task[i]))
            print("Task -", self.all_task[i])
            print("Created time -", self.create_time[self.all_task[i]])
            if self.all_task[i] in self.updated_time:
                print("Update time -", self.updated_time[self.all_task[i]])
            else:
                print("Update time -","NA")
            if self.all_task[i] in self.complete:
                print("Completed -", 'True')
            else:
                print("Completed -","False")
            if self.all_task[i] in self.complete_time:
                print("Completed time -", self.complete_time[self.all_task[i]])
            else:
                print("Completed time -","NA")

    def show_all_incomplete_task(self):
        if(len(self.incomplete)==0):
            print("\nNo Incompleted Task")

        for i in range(len(self.incomplete)):
            print('\n',end="")
            print("ID -", id(self.incomplete[i]))
            print("Task -", self.incomplete[i])
            print("Created Time -", self.create_time[self.incomplete[i]])
            if self.incomplete[i] in self.updated_time:
                print("Update time -", self.updated_time[self.incomplete[i]])
            else:
                print("Update time -", "NA")
            print("Completed -", "False")
            print("Completed time -", "NA")

    def show_all_complete_task(self):
        if(len(self.complete)==0):
            print("\nNo Completed Task")

        for i in range(len(self.complete)):
            print("\n",end="")
            print("ID -", id(self.complete[i]))
            print("Task -", self.complete[i])
            print("Created Time -", self.create_time[self.complete[i]])
            if self.complete[i] in self.updated_time:
                print("Update time -", self.updated_time[self.complete[i]])
            else:
                print("Update time -", "NA")
            print("Completed -", "True")
            print("Completed time -", self.complete_time[self.complete[i]])
      
    def update_task(self):
        print("\nSelect Which Task To Update")
        if(len(self.incomplete)==0):
            print("\nNo Task To Update\n")
            return
        for i in range(len(self.incomplete)):
            print('\n',end="")
            print("Task No -", i+1)
            print("ID -", id(self.incomplete[i]))
            print("Task -", self.incomplete[i])
            print("Created time -", self.create_time[self.incomplete[i]])
            if self.incomplete[i] in self.updated_time:
                print("Update time -", self.updated_time[self.incomplete[i]])
            else:
                print("Update time -","NA")
            if self.incomplete[i] in self.complete:
                print("Completed -", 'True')
            else:
                print("Completed -","False")
            if self.incomplete[i] in self.complete_time:
                print("Completed time -", self.complete_time[self.incomplete[i]])
            else:
                print("Completed time -","NA")
                    
        print('\n',end="")
        up_option = int(input("Enter Task No: "))
        previous = self.incomplete[up_option-1]
        new_task = input("Enter New Task: ")
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H: %M: %S")
        self.updated_time[new_task] = str(today) + "  " +current_time
        self.all_task[up_option-1] = new_task
        
        if previous in self.incomplete:
            self.incomplete[self.incomplete.index(previous)] = new_task
        if previous in self.complete:
            self.complete[self.complete.index(previous)] = new_task

        self.create_time[new_task] = self.create_time[previous]
        del self.create_time[previous]
        
    
    def mark_a_task_complete(self):
        print("\nSelect Which Task To Complete")
        if(len(self.incomplete)==0):
            print("\nNo Task To Complete\n")
            return
        for i in range(len(self.incomplete)):
            print('\n',end="")
            print("Task No -", i+1)
            print("ID -", id(self.incomplete[i]))
            print("Task -", self.incomplete[i])
            print("Created Time -", self.create_time[self.incomplete[i]])
            if self.incomplete[i] in self.updated_time:
                print("Update time -", self.updated_time[self.incomplete[i]])
            else:
                print("Update time -", "NA")
            print("Completed -", "False")
            print("Completed time -", "NA")
        
        print("\n",end="")
        com_option = int(input("Enter Task No: "))
        self.complete.append(self.incomplete[com_option-1])
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H: %M: %S")
        self.complete_time[self.incomplete[com_option-1]] = str(today) + "  " +current_time
        del self.incomplete[com_option-1]
        print("\n",end="")
        print("Task Completed Successfully\n")


    def main(self):
        while True:
            print("1. Add New Task")
            print("2. Show All Task")
            print("3. Show Incomplete Tasks")
            print("4. Show Complete Tasks")
            print("5. Update Task")
            print("6. Mark A Task Complete")

            option = int(input("Enter Option: "))

            if(option == 1):
                task = input("Enter New Task: ")
                self.add_new_task(task)
                now = datetime.now()
                today = date.today()
                current_time = now.strftime("%H: %M: %S")
                self.create_time[task] = str(today) + "  " +current_time 

                print("\nTask Created Successfully\n")

            elif option == 2:
                self.show_all_task()
                print('\n', end="")

            elif option == 3:
                self.show_all_incomplete_task()
                print("\n",end="")
            
            elif option == 4:
                self.show_all_complete_task()
                print("\n",end="")

            elif option == 5:
                self.update_task()

            elif option == 6:
                self.mark_a_task_complete()

            
        
task = Task()
task.main()