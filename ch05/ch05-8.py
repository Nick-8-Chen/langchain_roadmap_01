import os
import sys
sys.path.append("..")

from env.key_ini import key_ini
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI
from langchain_community.llms import Ollama

from langchain_core.prompts import (
    ChatPromptTemplate, 
    HumanMessagePromptTemplate,
    MessagesPlaceholder)

from langchain_core.messages import HumanMessage, AIMessage

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

# ChatPromptTemplate with MessagesPlaceholder -----------------------
human_prompt  = "Summarize the text above in {word_count}"
human_msg_tpl = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="article"),
     human_msg_tpl]
)

# new_chat_prompt with human_message and ai_message
human_message = HumanMessage(content="Tell me about a major event in programming last year.")
ai_message = AIMessage(content="""
    In 2023, one of the major events in the programming world was the 
    continued rise and widespread adoption of AI-powered tools, particularly 
    OpenAI’s GPT-4 and the incorporation of generative AI into various developer platforms.

    Notably, GitHub Copilot X, launched in 2023, integrated GPT-4 technology 
    to assist developers with more advanced code completion, debugging, and documentation. This was a significant step toward making AI a more integral part of the programming workflow, with AI tools increasingly used to automate routine coding tasks, generate code, and even enhance code reviews.
""")

new_chat_prompt = chat_prompt.format_prompt(article=[human_message,ai_message], word_count="20")

print(model.invoke(new_chat_prompt))
