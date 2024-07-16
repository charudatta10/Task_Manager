from pathlib import Path
import json
import fire
import pandas as pd


class task_manager:

    def __init__(self) -> None:
        self.task_list = {}
        self.task_id = 0
        self.add_file(file="todo.json")

    def add_file(self, file="todo.json"):
        self.file = Path(file)
        if self.file.exists():
            with open(self.file, "r") as f:
                self.task_list = json.load(f)
                self.task_id = len(self.task_list)
        else:
            with open(self.file, "w") as f:
                json.dump(self.task_list, f)

    def add_task(self, task=None, state="todo", tags=None, note=None):
        # tags
        # tags with #
        # Context with @
        # project with +
        # priority with !
        # deadline with *
        # repeat with ~
        if task == None:
            task=input("Task field can not be blank. Enter the task: ")
        self.task_list[str(self.task_id)] = {
            "task": task,
            "state": state,
            "tags": tags,
            "note": note,
        }
        self.task_id = self.task_id + 1
        self.save_tasks()

    def view_task(self):
        df = pd.DataFrame.from_dict(self.task_list).transpose()
        print(df)

    def del_task(self, task_id=None):
        if task_id == None:
            task_id=input("Task ID field can not be blank. Enter the task id: ")
        try:
            del self.task_list[str(task_id)]
            self.save_tasks()
        except:
            print("Task does not exist")

    def sort_task(self, sort_by="state"):
        sorted_dict = {}
        for key in sorted(self.task_list, key=lambda k: self.task_list[k][sort_by]):
            sorted_dict[key] = self.task_list[key]
        print(pd.DataFrame.from_dict(sorted_dict).transpose())

    def sort_tags(self, sort_tags="@me"):
        keys = []
        for key, values in self.task_list.items():
            if values["tags"] == None:
                continue
            elif sort_tags in values["tags"]:
                keys.append(key)
        # print([self.task_list[x] for x in sorted_task_list])
        print(
            pd.DataFrame.from_dict(
                {key: self.task_list[key] for key in keys}
            ).transpose()
        )

    def edit_task(self, task_id=None, task_key=None, task_value=None):
        if task_id == None:
            task_id=input("Task ID field can not be blank. Enter the task id: ")
        if task_key == None:
            task_key=input("Task KEY field can not be blank. Enter the task key: ")
        if task_value == None:
            task_value=input("Task VALUE field can not be blank. Enter the task value: ")
        try:
            if str(task_id) in self.task_list:
                if task_key in self.task_list[str(task_id)]:
                    self.task_list[str(task_id)][task_key] = task_value
                    self.save_tasks()
                else:
                    print("Task key doesn't exist")
            else:
                print("Task id doesn't exist")
        except:
            print("Unknown Error")

    def edit_status(self, task_id, task_value="done"):
        try:
            self.task_list[str(task_id)]["status"] = task_value
            self.save_tasks()
        except:
            print("Error task id is invalid")

    def save_tasks(self):
        with open(self.file, "w") as f:
            json.dump(self.task_list, f)


if __name__ == "__main__":
    fire.Fire(
        {
            "a": task_manager().add_task,
            "b": task_manager().sort_task,
            "c": task_manager().edit_status,
            "d": task_manager().del_task,
            "e": task_manager().edit_task,
            "f": task_manager().add_file,
            "r": task_manager().view_task,
            "s": task_manager().save_tasks,
            "t": task_manager().sort_tags,
        }
    )
