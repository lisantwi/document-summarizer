# Document Summarizer

An AI-powered document summarization tool that processes text files and returns structured summaries using the OpenAI API.

## What it does
- Reads all text files from a documents folder
- Sends each document to GPT-3.5-turbo for analysis
- Returns structured JSON with summary, key points, and document type
- Tracks token usage per document

## Tech stack
- Python 3.13
- OpenAI API
- python-dotenv

## Setup
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install openai python-dotenv`
5. Create a `.env` file and add your OpenAI API key:
   `OPENAI_API_KEY=your-key-here`
6. Add text files to the `documents/` folder
7. Run: `python3 summarizer.py`

## Example output
```json
{
"summary": "This document covers key compliance requirements and outlines..",
  "key_points": ["point 1", "point 2", "point 3"],
  "doc_type": "guidance",
  "filename": "test1.txt"
}
```

## Use case
Built as part of an AI engineering portfolio focused on enterprise document processing for regulated industries.