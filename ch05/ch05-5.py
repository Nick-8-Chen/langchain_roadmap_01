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

# Add ChatPrompTemplate ----------------------------------------------
from langchain.prompts import ChatPromptTemplate

chat_tpl = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a programming language assistant."),
        ("human",  "Hello, I have a question about {topic}."),
        ("ai",     "Sure! I'd be happy to help. What specifically would you like to know?"),
        ("human",  "{question}"),
    ]
)

# Using Partial Input -----------------------------------------------
chat_tpl_part = chat_tpl.partial(topic="python")
chat_value = chat_tpl_part.format(question="how to implement a quick sort algorithm?")
print(type(chat_value))
resp  = model.invoke(chat_value)

print(resp.content)

