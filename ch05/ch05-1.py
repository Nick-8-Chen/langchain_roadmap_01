import os
import sys
sys.path.append("..")

from env.key_ini import key_ini
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_core.output_parsers import StrOutputParser

# Load LLM model ----------------------------------------------------
LLM = os.getenv("LLM", "OPEN_AI")
key_ini("../env/.keys")

if LLM == "OPEN_AI":
    model = ChatOpenAI(model="gpt-4")
elif LLM == "GOOGLE_AI":
    model = ChatVertexAI(model="gemini-1.5-flash")
elif LLM == "OLLAMA":
    model = Ollama(model="llama3:8b")
else:
    model = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()

# Add PrompTemplate --------------------------------------------------
from langchain.prompts import PromptTemplate

prompt_tpl   = PromptTemplate.from_template("Introducing {city}")
prompt_value = prompt_tpl.invoke("Taipei")
print(type(prompt_value))
resp  = model.invoke(prompt_value)

print(resp)

