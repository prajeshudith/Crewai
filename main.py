from textwrap import dedent
import os
from crewai import Crew, Task
import agents
from agents import editor, idea_analyst, writer
from tasks import CreateTasks
from crewai.process import Process

class ContentWritingrew():
    def __init__(self, idea):
        self.idea = idea

    def __call__(self):
        tasks = self._create_tasks()
        crew = Crew(
            tasks=tasks,
            agents=[idea_analyst, writer, editor],
            verbose=True,
            )
        result = crew.kickoff()
        return result

    def _create_tasks(self):
        idea = CreateTasks.expand_idea().format(idea=self.idea)
        expand_idea_task = Task(
            description=idea,
            agent = idea_analyst,
            expected_output=""
        )
        write_task =  Task(
            description=CreateTasks.write(),
            agent=writer,
            expected_output=""
        )
        edit_task = Task(
            description=CreateTasks.edit(),
            agent=editor,
            expected_output=""
        )
        return [expand_idea_task, write_task, edit_task]

if __name__ == "__main__":
    dir = "./lore"
    if not os.path.exists(dir):
        os.mkdir(dir)
    idea = input("idea: ")
    my_crew = ContentWritingrew(idea=idea)
    result = my_crew()
    print(dedent(result))