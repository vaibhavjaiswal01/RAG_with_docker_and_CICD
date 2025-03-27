import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from flask import Flask, render_template, jsonify, request
from langchain_community.vectorstores import Chroma

from src.RAG_end_to_end.components.prompt import *
from src.RAG_end_to_end.components import utils

app = Flask(__name__)

load_dotenv()

OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

vectorstores = utils.vectorstores
retriever = vectorstores.as_retriever(search_kwarg={'k':1})

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

chat_model = ChatOpenAI(temperature = 0, model_name = 'gpt-4o')

qa = RetrievalQA.from_chain_type(llm = chat_model, 
                                 chain_type = 'stuff', 
                                 retriever = retriever, 
                                 chain_type_kwargs = {"prompt":prompt})

@app.route("/get", methods = ["GET", "Post"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = qa.invoke({"input":msg})
    print("Response: ", response["answer"])
    return str(response["answer"])

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

