# GenAI App - AI Code Reviewer

GenAI App is a Python application that allows users to submit Python code for review. The application analyzes the submitted code, identifies potential bugs, provides feedback for improvement, and returns fixed or optimized code snippets. It features a user-friendly interface built with Streamlit and leverages OpenAI's API for code analysis.

Features

Code Review: Submit your Python code and get detailed feedback on:

Potential bugs or errors.

Suggestions for improvement.

Fixed or optimized code snippets.


Clean User Interface: Built using Streamlit for simplicity and ease of use.


Prerequisites

1. Python: Install Python 3.8 or higher.


2. API Key: Obtain an API key from OpenAI.


3. Libraries: Install the required Python libraries:

pip install streamlit openai



Installation

1. Clone this repository or download the source code:

git clone https://github.com/SURESHKUMAR-007/GenAI-CODE-REVIEWER.git
cd genai-code-reviewer


2. Install the required dependencies:

pip install -r requirements.txt


3. Set up your OpenAI API key:

Open the genai_code_reviewer.py file.

Replace "your_openai_api_key_here" with your OpenAI API key.



Usage

1. Run the application:

streamlit run genai_code_reviewer.py


2. Open the provided local URL in your browser (e.g., http://localhost:8501).


3. Paste your Python code into the input box and click "Generate Review".


4. Review the feedback, suggestions, and fixed code snippets displayed on the page.
