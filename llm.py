import random

class LLM:
    def __init__(self, provider="mock"):
        self.provider = provider

    def generate(self, prompt):
        # Simulated response (replace with real API later)
        responses = [
            "Analyzed and generated response.",
            "Task processed successfully.",
            "Generated optimized output."
        ]
        return f"[{self.provider.upper()}] {random.choice(responses)} -> {prompt}"
