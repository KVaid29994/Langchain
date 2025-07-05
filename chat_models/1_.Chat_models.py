from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model = "gpt-4o")

while True:
    user_input = input("What is your question ")
    if (user_input in ("end")):
        break
    else:
        result =  (llm.invoke(user_input))
        print (result.content)