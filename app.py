import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from flask import request, jsonify
from langchain_community.vectorstores import Chroma
from src.RAG_end_to_end.components import utils
from src.RAG_end_to_end.components.prompt import prompt_template

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Setup Vector Store and Retriever
vectorstores = utils.vectorstores
retriever = vectorstores.as_retriever(search_kwargs={'k': 1})

# Setup Prompt and Model
prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
chat_model = ChatOpenAI(temperature=0, model_name='gpt-4o')

# Setup Retrieval QA Chain
qa = RetrievalQA.from_chain_type(llm=chat_model, 
                                 chain_type='stuff', 
                                 retriever=retriever, 
                                 chain_type_kwargs={"prompt": prompt})

# Chat function for Flask app
def chat():
    msg = request.form["msg"]
    print(f"User Input: {msg}")
    
    response = qa.invoke({"input": msg})
    print("Response: ", response["answer"])
    
    return str(response["answer"])