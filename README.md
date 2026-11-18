# ChatMate AI

A beginner-friendly customer-support chatbot built with Python, Flask, TF-IDF NLP matching, and SQLite conversation logs.

## Features
- Chat interface built with HTML, CSS, and JavaScript
- NLP-style FAQ matching using TF-IDF and cosine similarity
- Editable FAQ knowledge base in `data/faqs.json`
- SQLite storage for conversation logs
- Per-browser-session chat history
- Responsive layout for desktop and mobile

## Requirements
- Python 3.10 or newer
- VS Code (recommended)

## Setup on Windows

1. Open this folder in VS Code.
2. Open Terminal → New Terminal.
3. Create a virtual environment:

   ```bash
   py -m venv .venv
   ```

4. Activate it in PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:

   ```cmd
   .venv\Scripts\activate.bat
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Run the app:

   ```bash
   python app.py
   ```

7. Open the local address printed in the terminal, usually `http://127.0.0.1:5000`.

## Customize answers
Edit `data/faqs.json`. Add more question examples and an answer to each entry. Keep the same JSON structure.

## Important project note
This starter version uses TF-IDF similarity to match questions against an FAQ knowledge base. It is an NLP-based retrieval chatbot, not a generative Transformer model. A pretrained Transformer can be added as a later enhancement for the internship's advanced NLP requirement.

## Before publishing
- Change `app.secret_key` to a private random value (use an environment variable).
- Do not commit `chat_history.db`, passwords, or API keys.
- Test the chatbot and update the FAQ answers for your chosen use case.
