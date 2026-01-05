from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#from streamlit as st
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that helps people find information."),
    ("user","Question:{question}")
    
])
## streamlit framework
st.title("Langchain with OpenAI Chat Model")
input_question = st.text_input("Enter your question here")

# llm model
llm = OllamaLLM(model="llama3.2:1b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_question:
    st.write(chain.invoke({"question":input_question}))