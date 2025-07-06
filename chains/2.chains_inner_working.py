from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI()

messages =  [("system","You are a commedian who tells joke about {topic}"),
            ("human","tell me {joke_count} jokes")]

prompt_template = ChatPromptTemplate.from_messages(messages=messages)

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x : model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x :x.content)

chain = RunnableSequence(first = format_prompt,middle=[invoke_model], last = parse_output)

response = chain.invoke({"topic": "apple", "joke_count":2})
print (response)