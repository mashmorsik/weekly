import uuid
import random


class Task:
    tasks = []
    categories = {'1': 'Tasks'}

    def add_task(self, title, category_id=1): # What if somebody deletes category 'Tasks'?
        self.tasks.append(
            {
                "task_id": str(uuid.uuid4()),
                "title": title,
                "is_done": False,
                "category_id": category_id
            }
        )

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['task_id'] == task_id:
                self.tasks.remove(task)

    def add_category(self, name):
        category_id = str(uuid.uuid4())
        self.categories[category_id] = name

    def delete_category(self, category_id):
        self.categories.pop(category_id)



