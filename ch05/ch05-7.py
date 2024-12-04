from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import MessagesPlaceholder

human_prompt  = "Summarize the text above in {word_count}"
human_msg_tpl = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [MessagesPlaceholder(variable_name="article"),
     human_msg_tpl]
)

print(chat_prompt)

