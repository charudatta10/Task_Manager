from pathlib import Path
import json


class task_manager:

    def __init__(self, file="task.json") -> None:
        self.file = Path(file)
        self.task_list = {}
        self.task_id = 0
        if self.file.exists():
            with open(self.file,"r") as f:
                self.task_list = json.load(f)
                self.task_id = len(self.task_list)
        else:
            with open(self.file, "w") as f:
                json.dump(self.task_list,f)

    def add_task(self, task, state="todo", tags=None, note=None):
        #tags 
        #tags with #
        #Context with @ 
        #project with +
        #priority with !
        #deadline with *
        #repeat with ~ 
        self.task_list[str(self.task_id)] = {
            "task": task,
            "state": state,
            "tags": tags,
            "note": note,
        }
        self.task_id =  self.task_id + 1
        self._save_tasks()

    def view_task(self):
        print("| ID | task | state | eot | span | tags | note |")
        print("----------------------------------------------------------")
        for key, values in self.task_list.items():
            print(f"| {key} | {values["task"]} | {values["state"]} | {values["tags"]} | {values["note"]} | ")

    def del_task(self, task_id):
        try:
            del self.task_list[str(task_id)]
            self._save_tasks()
        except:
            print("Task does not exist")

    def sort_task(self, sort_by="state"):
        sorted_dict = {}
        for key in sorted(self.task_list, key=lambda k: self.task_list[k][sort_by]):
            sorted_dict[key] = self.task_list[key]
        print(sorted_dict)

    def sort_tags(self, sort_tags="@me"):
        sorted_task_list = []
        for key, values in self.task_list.items():
            if values["tags"] == None:
                continue
            elif sort_tags in  values["tags"]:
                sorted_task_list.append(key) 
        print([self.task_list[x] for x in sorted_task_list])

    def edit_task(self, task_id, task_key, task_value):
        try:
            self.task_list[str(task_id)][task_key]= task_value
            self._save_tasks()
        except:
            print("Error either task id is invalid or task key doesn't exist")


    def _save_tasks(self):
        with open(self.file, "w") as f:
                json.dump(self.task_list,f)



if __name__ == "__main__":
    t1 = task_manager("task.json")
    t1.add_task("get milk")
    t1.add_task("get grocery")
    t1.view_task()
    t1.edit_task(1,"tags",["@me","+patent","*tomorrow"])
    t1.edit_task(10,"tags",["@suma","+patent","*tomorrow","@me"])
    t1.edit_task(7,"tags",["@me","+patent","*tomorrow"])
    t1.edit_task(13,"tags",["@me","+patent","*tomorrow"])
    t1.edit_task(17,"tags",["@u","+patent","*tomorrow"])
    t1.edit_task(1,"tags",["@to","+patent","*tomorrow"])
    t1.view_task()
    t1.sort_task()
    t1.sort_tags()