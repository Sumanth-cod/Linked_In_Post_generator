from dotenv import load_dotenv
from langchain_groq import  ChatGroq
import os

load_dotenv()


llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="llama3-8b-8192")

if __name__=="__main__":
    response=llm.invoke("what are the ingrediebts of somosa")
    print(response.content)
