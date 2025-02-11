import os
import textwrap
import warnings
from pathlib import Path as p

import pandas as pd
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import google.generativeai as genai

warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Function to convert text to markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY, temperature=0.2)

# List all PDF files in the 'doc' folder
pdf_folder = "doc"
pdf_files = [os.path.join(pdf_folder, file) for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

# Load and split PDFs
all_texts = []
for pdf_file in pdf_files:
    pdf_loader = PyPDFLoader(pdf_file)
    pages = pdf_loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    context = "\n\n".join(str(p.page_content) for p in pages)
    texts = text_splitter.split_text(context)
    all_texts.extend(texts)

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

# Create vector index with a specific directory for ChromaDB
try:
    vector_index = Chroma.from_texts(all_texts, embeddings, persist_directory="chroma_db").as_retriever(search_kwargs={"k": 5})
    # print("vector index created")
except Exception as e:
    st.error(f"An error occurred while creating the vector index: {e}")
    raise

# Define QA chain prompt template
template = """Use the following pieces of context to answer the question. Only give response based on the PDFs content, If you don't know the answer, please please dont say random words just say that you don't know, don't try to make up an answer by yourself. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = ChatPromptTemplate.from_template(template)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_index,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

# Streamlit app
st.title("PDF QA Chatbot")

# Initialize session state for the question input and history
if "question" not in st.session_state:
    st.session_state.question = ""
if "history" not in st.session_state:
    st.session_state.history = []

def submit_question():
    question = st.session_state.question
    if question:
        try:
            result = qa_chain.invoke({"query": question})
            answer = result["result"]
            st.session_state.history.insert(0, {"question": question, "answer": answer})  # Insert at the beginning
            st.session_state.question = ""  # Clear the input field after processing
        except Exception as e:
            st.error(f"An error occurred while processing the question: {e}")
    else:
        st.error("Please enter a question.")

# Input field for the question
st.text_input("Please enter your question:", key="question", on_change=submit_question)

# Button to submit the question
st.button("Submit", on_click=submit_question)

# Display the history of questions and answers
if st.session_state.history:
    st.markdown("## History")
    for entry in st.session_state.history:
        st.markdown(f"**Question:** {entry['question']}")
        st.markdown(to_markdown(entry['answer']))
        st.markdown("---")