from flask import Flask
import fire
from src.task import task_manager


def api():  
    app = Flask(__name__)

    @app.route("/add")
    def add():
        pass

    app.run(debug=True)


def cli():
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




def main():
    cli()
    #api()
main()
 

