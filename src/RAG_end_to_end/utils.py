
from component.helper import load_pdf, text_split, initialise_embeddings
from langchain_community.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

extracted_data = load_pdf(data = '../data/')
text_chunks = text_split(extracted_data)
embeddings = initialise_embeddings()


vectorstores = Chroma.from_documents(documents=extracted_data, 
                                     embedding=embeddings)