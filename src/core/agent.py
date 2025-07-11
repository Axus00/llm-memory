from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Cargamos el agente (modelo de IA)


load_dotenv()


api_key = "AGENT_API_KEY not found"


llm = ChatOpenAI(model='gpt-4o-mini', api_key=api_key,
                 max_completion_tokens=50)