from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# System message: guiding the conversation and defining the teacher role
system_prompt_tpl = SystemMessagePromptTemplate.from_template(
    template="You are a programming language assistant."
)

# Human message: simulating a student question
human_prompt_tpl = HumanMessagePromptTemplate.from_template(
    template="Hello, I have a question about {topic}."
)

# AI message: defining the AI's response template
ai_prompt_tpl = AIMessagePromptTemplate.from_template(
    template="Sure! I'd be happy to help. What specifically would you like to know?"
)

# Human message: Question
human_prompt_qtpl = HumanMessagePromptTemplate.from_template(
    template="{question}"
)

# Combine all prompt templates into a single chat prompt
chat_prompt_template = ChatPromptTemplate.from_messages(
    messages=[
        system_prompt_tpl,
        human_prompt_tpl,
        ai_prompt_tpl,
        human_prompt_qtpl,
    ]
)

# Set variables
topic    = "python"
question = "Give me quick sort algorithm."

# Invoke the template with the dynamic subject variable
chat_fmt  = chat_prompt_template.format(topic=topic,question=question)
chat_fmt_pmt = chat_prompt_template.format_prompt(topic=topic, question=question)
chat_value = chat_prompt_template.invoke(input={"topic": topic, "question": question})

# Print the generated prompt
print(type(chat_fmt))
print(type(chat_fmt_pmt))
print(type(chat_value))

