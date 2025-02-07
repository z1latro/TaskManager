class Task:
    def __init__(self,name,priority,status=False):
        self.name = name
        self.priority = priority
        self.status = status
    def __str__(self):
        return f"{self.name} | {self.priority} | {'Completed' if self.status else 'Not Completed'}"
class taskManager:
    def __init__(self):
        self.task_list = []
    def create(self):
        task_name = input("Enter task name:")
        task_priority = input("Enter priority [High,Medium,Low]")
        task =Task(task_name,task_priority,status=False)
        self.task_list.append(task)
        print("\nTask Sucessfully added")

    def delete(self):
        task_deletion = int(input("Enter task number to delete"))
        self.task_list.pop(task_deletion-1)
        print("\nTask sucessfully deleted")
    def view(self):
        for index,task in enumerate(self.task_list):
            print(f"{index+1}. {task}")

    def edit(self):
        self.view()
        task_edit = int(input("Enter task number to edit"))
        task_to_edit = self.task_list[task_edit -1]
        task_name = input("Enter new task name")
        task_priority = input("Enter new priority [High,Medium,Low]")
        task_status = task_to_edit.status
        task = Task(task_name,task_priority,task_status)
        self.task_list[task_edit-1] = task


    def main(self):
        while True:
            print("")
            print("1.Add task")
            print("2.Delete task")
            print("3.View task")
            print("4.Edit task")
            print("5.Exit")
            choice = input("Please enter your choice:").strip()

            if choice == '5':
                print("Thank you for Tasking")
                break
            elif choice == '1':
                self.create()
            elif choice == '2':
                self.delete()
            elif choice == '3':
                self.view()
            elif choice == '4':
                self.edit()
            else:
                print("\nInvalid Choice Please Try again")

        
if __name__ == '__main__':
    task_manager = taskManager()
    task_manager.main()