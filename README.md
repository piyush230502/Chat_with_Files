Here's a detailed **project report** (~1000 words) and **step-by-step instructions** for running your app based on the `main.py` and `requirements.txt` files you provided:

---

## 🔍 Project Title: **AI-Powered Document Chat Using LangChain & Groq**

---

## 📄 Overview

This project is a **Streamlit-based AI application** that allows users to upload documents in various formats and interact with them using natural language queries. Powered by **LangChain** and **Groq's LLM (gemma2-9b-it)**, the application extracts content from documents and enables intelligent Q&A over the extracted text. It supports multiple file types including **PDF, DOCX, TXT, HTML, EPUB, Markdown, XLSX**, and more.

The core goal is to make document understanding and exploration **interactive, fast, and AI-driven** without requiring users to manually read and interpret lengthy files.

---

## 🎯 Objectives

- Allow users to upload and parse different document formats.
- Automatically extract and structure the document text.
- Provide a conversational interface to query the document.
- Use LLM (Groq + LangChain) to generate accurate and context-aware answers.
- Maintain a smooth and responsive UI using Streamlit.

---

## 🛠️ Features

1. **Multi-format Document Support:**
   - Supports `.pdf`, `.docx`, `.txt`, `.html`, `.epub`, `.md`, and `.xlsx`.
   - Uses appropriate libraries for each format to extract textual content.

2. **Real-time Q&A:**
   - Once content is extracted, users can ask questions.
   - The app sends both the document and the question to Groq's LLM for analysis.

3. **LLM Integration:**
   - Uses LangChain and the `gemma2-9b-it` model via Groq API for generating AI responses.
   - Handles prompt creation and formatting dynamically based on the user's input.

4. **Memory Buffer:**
   - Optionally designed to allow maintaining conversational state using LangChain memory (though not heavily utilized in the current version).

5. **Session Management:**
   - Uploaded document content is saved in the session, and there's a reset button to clear and restart the session.

---

## 🧩 File Descriptions

### 1. `main.py`
The main application script, written in Python using Streamlit.

Key components:
- UI setup and sidebar input fields.
- File upload logic with conditional processing.
- Text extraction using libraries like `pypdf`, `python-docx`, `ebooklib`, `bs4`, `markdown2`, and `pandas`.
- Query input field and LangChain-based LLM invocation using Groq.
- Display of AI-generated response.

### 2. `requirements.txt`
Contains all required Python packages:
- **Core Packages:** `streamlit`, `pandas`, `langchain`, `langchain_groq`
- **File Parsers:** `pypdf`, `python-docx`, `beautifulsoup4`, `ebooklib`, `markdown2`, `unstructured`
- Optional comment mentions compatibility fix using `pydantic==2.10.3` (helpful if dependency conflicts arise)

---

## 🔄 How It Works (Backend Flow)

1. **User Interface Initialization:**
   - Streamlit sets up the layout and requests the Groq API key via sidebar.

2. **Document Upload:**
   - User uploads a document via the sidebar.
   - Based on the file extension, appropriate parser is called.

3. **Text Extraction:**
   - The file content is read and converted into plain text.
   - Displayed in a text area for verification.

4. **Prompt Construction:**
   - Combines a system instruction with document content and user query.
   - The message is sent to the Groq LLM via LangChain’s `ChatGroq` interface.

5. **AI Response Generation:**
   - The response is parsed and shown in the main panel below the user input.
   - If any error occurs (e.g., invalid API key), it's displayed using Streamlit's `st.error`.

6. **Session Management:**
   - Document content is stored in `st.session_state`.
   - A “Clear Session” button resets the content and reruns the app.

---

## 🚀 How to Run the Project (Step-by-Step)

### 📁 1. **Clone or Prepare the Project Directory**
If you're working locally:
```bash
mkdir ai_doc_chat
cd ai_doc_chat
# Place main.py and requirements.txt inside this folder
```

### 🐍 2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

✅ If any issue arises due to LangChain versioning or Pydantic errors, try:
```bash
pip install pydantic==2.10.3
```

### ▶️ 4. **Run the Application**
```bash
streamlit run main.py
```

Your browser will open automatically at `http://localhost:8501`

---

## 🔐 5. **Get Groq API Key**
To use the LLM, you’ll need an API key from Groq:
- Visit: [https://console.groq.com](https://console.groq.com)
- Sign up and generate your API key.
- Paste the key in the sidebar input when prompted.

---

## 📄 6. **Upload Documents and Chat**
- Upload any document (PDF, DOCX, EPUB, etc.)
- Wait for it to be processed.
- Type your question in the chat input.
- The AI will return a detailed response based on your document.

---

## 💡 Example Use Cases

| Use Case                    | Example |
|----------------------------|---------|
| Academic Q&A               | Upload a PDF research paper and ask “What’s the main conclusion?” |
| Legal Document Review      | Upload a DOCX contract and ask “What are the payment terms?” |
| Resume Parsing             | Upload a resume and ask “What skills does this person have?” |
| EPUB Book Summarization    | Upload a book and ask “Give me a summary of chapter 1.” |
| Spreadsheet Analysis       | Upload an Excel sheet and ask “What are the top 3 performing products?” |

---

## 📈 Future Enhancements (Optional Ideas)

- Add multi-document support with FAISS/ChromaDB.
- Integrate conversational memory for more fluid back-and-forth interaction.
- Allow saving/exporting of chat history.
- Add summarization before querying for long documents.
- Embed citation/source-tracking into responses.

--- 
