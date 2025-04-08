import streamlit as st
import pandas as pd
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from pypdf import PdfReader
from docx import Document
from bs4 import BeautifulSoup
import markdown2
from ebooklib import epub
from io import StringIO

# Initialize Streamlit app
st.set_page_config(page_title="Document Chat", layout="wide")
st.title("📄 AI Document Chat")

# Initialize session state for storing document content
if 'document_content' not in st.session_state:
    st.session_state.document_content = None

# User inputs API key
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

# Initialize LangChain with Groq
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="gemma2-9b-it",
    streaming=True
)

# Function to extract text from different file types
def extract_text(file):
    file_extension = file.name.split(".")[-1].lower()
    text = ""
    
    try:
        if file_extension == "pdf":
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        elif file_extension == "docx":
            doc = Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file_extension == "txt":
            text = str(file.read(), "utf-8")
        elif file_extension == "html":
            soup = BeautifulSoup(file, "html.parser")
            text = soup.get_text()
        elif file_extension == "epub":
            book = epub.read_epub(file)
            for item in book.get_items():
                if item.get_type() == 9:  # EPUB Text
                    text += item.get_content().decode("utf-8") + "\n"
        elif file_extension == "md":
            text = markdown2.markdown(file.read().decode("utf-8"))
        elif file_extension == "xlsx":
            df = pd.read_excel(file)
            text = df.to_csv(index=False)
        
        return text.strip()
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# Upload file
uploaded_file = st.sidebar.file_uploader("Upload a document", type=["xlsx", "pdf", "docx", "rtf", "txt", "html", "epub", "md"])

# Process uploaded file
if uploaded_file:
    extracted_text = extract_text(uploaded_file)
    if extracted_text:
        st.session_state.document_content = extracted_text
        st.text_area("Extracted Content", extracted_text, height=300)

        # Chat input
        user_query = st.text_input("Ask a question about the document:")
        
        if user_query:
            # Create a prompt that includes both the document content and the user's question
            system_prompt = """You are an AI assistant helping to analyze documents. 
            Below is the document content followed by a user question. 
            Please provide a detailed and accurate response based on the document content."""
            
            document_and_query = f"""
            Document Content:
            {st.session_state.document_content}
            
            User Question: {user_query}
            
            Please answer the question based on the document content above."""
            
            # Use LangChain to generate response
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=document_and_query)
            ]
            
            try:
                response = llm(messages)
                st.write("**AI Response:**", response.content)
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
else:
    st.info("Please upload a document to begin.")

# Add a clear button to reset the session
if st.sidebar.button("Clear Session"):
    st.session_state.document_content = None
    st.experimental_rerun()