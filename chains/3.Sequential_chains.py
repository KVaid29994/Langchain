from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate
llm = ChatOpenAI()

messages = [("system", "you give facts about {animal}")
            ,("human, give me {number} facts about animals")]

prompt = ChatPromptTemplate.from_messages(messages=messages)

translation_template = ChatPromptTemplate.from_messages(
    
    
    [("system", "you are translator and translate text into {language}"),
     ("human", "translate the text into {language} :{text}")]
    )

count_words = RunnableLambda(lambda x : f'Word count : {len(x.split())}\n{x}')
prepare_for_translation = RunnableLambda(lambda output : {"text":output, "language":"French"})

chain = prompt | llm | StrOutputParser() | prepare_for_translation | translation_template | llm | StrOutputParser() | count_words

print (chain.invoke({"animal":"dog", "number":2}))