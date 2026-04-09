from llm import LLM
from utils import log_step

class Agent:
    def __init__(self, name):
        self.name = name
        self.llm = LLM()

    def execute(self, task):
        log_step(f"{self.name} processing...")
        return self.llm.generate(task)


class TaskManager:
    def __init__(self):
        self.research = Agent("Research Agent")
        self.writer = Agent("Writer Agent")
        self.executor = Agent("Execution Agent")

    def process_task(self, task):
        r = self.research.execute(task)
        w = self.writer.execute(r)
        e = self.executor.execute(w)
        return e
