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

    def add_task(self, task, state="todo", eot=None, span=None, tags=None, note=None):
        #tags tags with #, Context with @, project with +, priority with !
        self.task_list[str(self.task_id)] = {
            "task": task,
            "state": state,
            "eot": eot,
            "span": span,
            "tags": tags,
            "note": note,
        }
        self.task_id =  self.task_id + 1
        self._save_tasks()

    def view_task(self):
        print("| ID | task | state | eot | span | tags | note |")
        print("----------------------------------------------------------")
        for key, values in self.task_list.items():
            print(f"| {key} | {values["task"]} | {values["state"]} | {values["eot"]} | {values["span"]} | {values["tags"]} | {values["note"]} | ")

    def del_task(self, task_id):
        try:
            del self.task_list[str(task_id)]
            self._save_tasks()
        except:
            print("Task does not exist")

    def sort_task(self, sort_by="eot"):
        sorted_dict = {}
        for key in sorted(self.task_list, key=lambda k: self.task_list[k][sort_by]):
            sorted_dict[key] = self.task_list[key]
        print(sorted_dict)


    def _save_tasks(self):
        with open(self.file, "w") as f:
                json.dump(self.task_list,f)



if __name__ == "__main__":
    t1 = task_manager("task.json")
    t1.add_task("get milk")
    t1.add_task("get grocery")
    for i in range(1,20):
        t1.del_task(i)
    t1.view_task()
    