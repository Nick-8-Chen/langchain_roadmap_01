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

from fastapi import FastAPI
from langserve import add_routes

# Load LLM model ----------------------------------------------------
LLM = os.getenv("LLM", "OPEN_AI")
key_ini("../env/.keys")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] ="Ch04.Simple.LLM"

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

# Create Chain ------------------------------------------------------
chain = prompt_template | model | parser

# Adding Chain Route ------------------------------------------------
app = FastAPI(
  title="LangChain Server",
  version="1.00",
  description="A simple API server using LangChain's Runnable interfaces.",
)

add_routes(app,chain,path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


