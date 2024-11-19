from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


class LLM:
    def __init__(self, model_type:str='gpt-4o', temperature:float=0.9):
        self.model_type = model_type
        self.temperature = temperature
        self.model = self.init_model()
    
    def init_model(self):
        llm = None
        if self.model_type == 'gpt-4o':
            llm = ChatOpenAI(model=self.model_type, temperature=self.temperature)
        if self.model_type == 'llama3.1':
            llm = ChatOllama(model=self.model_type, temperature=self.temperature)
        else:
            raise NotImplementedError("Only gpt-4o and llama3.1 are currently implemented.")
        return llm
