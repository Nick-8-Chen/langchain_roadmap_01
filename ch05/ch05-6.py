from langchain_core.prompts import PromptTemplate

# Define current datetime function ----------------------------------
import pytz     # Python timezone
from datetime import datetime

timezone = pytz.timezone('Asia/Taipei')

def get_datetime():
    now = datetime.now(timezone)
    return now.strftime("%Y-%m-%d, %H:%M:%S")


prompt_tpl = PromptTemplate.from_template(template="Current: {datetime}")
prompt_part= prompt_tpl.partial(datetime=get_datetime)
print(prompt_tpl)  # input_variables=['datetime'] input_types={} partial_variables={} template='Current: {datetime}'
print(prompt_part) # input_variables=[] input_types={} partial_variables={'datetime': <function get_datetime at 0x7f7d48c90540>} template='Current: {datetime}'

prompt_value = prompt_part.format()
print(prompt_value)
