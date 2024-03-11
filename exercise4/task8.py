# File: task8.py
# Author: Jasmin Fränti
# Description: Task 8 of exercise 4 
# Order book

import itertools

class Task:
    task_id = itertools.count(start=1)
    
    def __init__(self, description, employee, hours) -> None:
        self.description = description
        self.time_estimate = hours
        self.employee = employee
        self.finished = False
        self.id = next(Task.task_id)
        
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True
        
    def __str__(self) -> str:
        return f"{self.id} {self.description} ({self.time_estimate} hours), programmer: {self.employee} FINISHED: {self.finished}"
   
class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description, programmer, workload):
        # Create a new Task and add it to the order book
        task = Task(description, programmer, workload)
        self.tasks.append(task)
        
    def mark_finished(self, task_id):
        # Mark the task with the given ID as finished
        for task in self.tasks:
            if task_id == task.id:
                task.mark_finished()
                return
        raise ValueError(f"No task found with ID {task_id}")

    def finished_orders(self):
        # Return a list of finished tasks
        return [task for task in self.tasks if task.finished]
    
    def unfinished_orders(self):
        # Return a list of unfinished tasks
        return [task for task in self.tasks if not task.finished]

    def all_orders(self):
        # Return a list of all tasks in the order book
        return self.tasks

    def programmers(self):
        # Return a list of unique programmer names
        programmer_set = set(task.employee for task in self.tasks)
        return list(programmer_set)
    
    def status_of_programmer(self, programmer):
        # Calculate the status for the given programmer
        finished_count = 0
        unfinished_count = 0
        finished_workload = 0
        unfinished_workload = 0

        for task in self.tasks:
            if task.programmer == programmer:
                if task.finished:
                    finished_count += 1
                    finished_workload += task.workload
                else:
                    unfinished_count += 1
                    unfinished_workload += task.workload

        if finished_count == 0 and unfinished_count == 0:
            raise ValueError(f"No programmer found with name {programmer}")

        return finished_count, unfinished_count, finished_workload, unfinished_workload
        
     
t1 = Task("Program Hello World", "Eric", 3)
print(t1.id,t1.description,t1.employee,t1.time_estimate)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2=Task("program webstore","Adele",10)
t3=Task("program mobile app for workload accounting","Eric",25)
print(t2)
print(t3)

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

# Print all orders
for order in orders.all_orders():
    print(order)

print()

# Print unique programmer names
for programmer in orders.programmers():
    print(programmer)
    
# Mark tasks as finished
orders.mark_finished(4)
orders.mark_finished(6)

# Print all orders
for order in orders.all_orders():
    print(order)