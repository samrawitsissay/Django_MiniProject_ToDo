import task
import os
import json


class TodoManager:   
    def  __init__(self,filename):
        self.filename = filename
        self.tasks =[]
        self.load_tasks()
        
    def load_tasks(self):    
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                data = json.load(file)
                self.tasks = [task.Task.from_dict(item) for item in data]
        else:
            self.tasks =[]
            
    def save_tasks(self):
        with open(self.filename,'w') as file:
            data = [t.to_dict() for t in self.tasks]
            json.dump(data,file,indent=4)
            
    def add_task(self,title):
        new_id = len(self.tasks) +1
        new_task = task.Task(new_id,title)
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task   
         
    def view_tasks(self):
        for t in self.tasks:
            status = "Done" if t.completed else "Pending"
            print(f"{t.id}. {t.title} - {status}")
     
    def update_task(self,task_id,new_title=None ,completed=None):
        for t in self.tasks:
            if t.id == task_id:
                if new_title is not None:
                    t.title = new_title
                if completed is not None:
                    t.completed = completed
                self.save_tasks()
                return t
        return None      
    def delete_task(self,task_id):
        for t in self.tasks:
            if t.id ==task_id:
                self.tasks.remove(t)
                self.save_tasks() 
                return True
        return False