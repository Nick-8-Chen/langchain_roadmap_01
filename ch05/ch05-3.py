from langchain.prompts import PromptTemplate
prompt_tpl = PromptTemplate(input_variables=["foo"], template="Hi {foo}!")
print(prompt_tpl)
# input_variables=['foo'] input_types={} partial_variables={} template='Hi {foo}!’

# Using format  String
prompt_str = prompt_tpl.format(foo="Nick")
print(prompt_str)
# Hi Nick!

# Using invoke  StringPromptValue Object
prompt_obj = prompt_tpl.invoke({"foo":"Nick"})
print(prompt_obj)
# text=‘Hi Nick!’
print(type(prompt_obj))
# <class 'langchain_core.prompt_values.StringPromptValue’>

prompt_tpl_new = ( PromptTemplate.from_template("Hi {foo}!" ) + " {Say}" )
print(prompt_tpl_new)
# input_variables=['Say', 'foo'] input_types={} partial_variables={} template='Hi {foo}! {Say}'

