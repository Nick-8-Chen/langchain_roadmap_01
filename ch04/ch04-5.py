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
from langchain_community.utilities import OpenWeatherMapAPIWrapper

# Load LLM model ----------------------------------------------------
LLM = os.getenv("LLM", "OPEN_AI")
key_ini("../env/.keys")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] ="Ch04.LLM.Weather"

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

# Get Weather information -------------------------------------------
def GetWeather(city):
    try:
        weather = OpenWeatherMapAPIWrapper()
        weather_info = weather.run(city)
        return weather_info
    except Exception as e:
        return f"Error: {e}"

# Define a Chain --------------------------------------------------------------
from langchain.chains.base import Chain

class WeatherChain(Chain):
    @property
    def input_keys(self):
        return ["city"]

    @property
    def output_keys(self):
        return ["city_weather"]

    def _call(self, inputs: dict) -> dict:
        city = inputs['city']
        result = GetWeather(city=city)
        return {"city_weather": result}

# Add Prompt Template -----------------------------------------------
system_template = "You are a weather assistant who can give you suggestions for going out today based on the weather."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{city_weather}")]
)

# Create Chain ------------------------------------------------------
MyWeatherChain = WeatherChain()
chain = MyWeatherChain | prompt_template | model | parser
resp  = chain.invoke({"city": "Taipei"})

print(resp)

chain.get_graph().print_ascii()
