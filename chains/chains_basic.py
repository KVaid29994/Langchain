from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
model = ChatOpenAI()

messages =  [("system","You are a commedian who tells joke about {topic}"),
            ("human","tell me {joke_count} jokes")]

prompt_template = ChatPromptTemplate.from_messages(messages=messages)

chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic":"AI", "joke_count":2})

print (result)