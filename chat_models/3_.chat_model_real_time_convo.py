from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

llm = ChatOpenAI()

chat_history = []


system_messages = SystemMessage(content= "You are an helpful assistant")
chat_history.append(system_messages)

while True:
    input_1 = input("you: ")
    chat_history.append(HumanMessage(content = input_1))
    

    if (input_1 in ["end", "escape", "bye"]):
        break
    else:
        response = llm.invoke(chat_history)
        AI_message = response.content
        chat_history.append(AIMessage(content = AI_message))
        print(AI_message)

