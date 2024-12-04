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

# Parse the result --------------------------------------------------
parser = StrOutputParser()

# Add Prompt Template -----------------------------------------------
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

resp = prompt_template.invoke(
    {"language": "Traditional Chinese", 
     "text": "The key question isn't what AI can do, but what we should do with it."})
print(resp)
"""
messages=[
    SystemMessage(content='Translate the following into traditional chinese:', additional_kwargs={}, response_metadata={}), 
    HumanMessage(content='The key question isn't what AI can do, but what we should do with it.', additional_kwargs={}, response_metadata={})
]
"""

chain = prompt_template | model | parser
resp = chain.invoke(
   {"language": "traditional chinese", 
    "text": "The key question isn't what AI can do, but what we should do with it."})
print(resp)

