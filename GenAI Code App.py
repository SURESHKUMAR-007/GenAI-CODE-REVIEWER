import streamlit as st
import openai

# Set OpenAI API Key
openai.api_key = "your_openai_api_key_here"

# Function to analyze Python code and suggest fixes
def analyze_code(code):
    try:
        # Define the prompt for the AI
        prompt = f"""
        You are an AI code reviewer. Analyze the following Python code and provide:
        1. Any potential bugs or errors.
        2. Suggestions for improvement.
        3. The fixed or improved version of the code.

        Code:
        {code}

        Your response:
        """
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit User Interface
st.title("GenAI App - AI Code Reviewer")

st.write("""
Submit your Python code below, and the AI will provide:
- Feedback on potential bugs.
- Suggestions for improvements.
- Fixed or optimized code snippets.
""")

# Code input box
user_code = st.text_area("Enter your Python code here:", height=300)

if st.button("Generate Review"):
    if user_code.strip():
        st.info("Analyzing your code...")
        # Get analysis result
        review_result = analyze_code(user_code)
        st.success("Code Review Completed!")
        
        # Display the results
        st.subheader("Code Review Feedback")
        st.text(review_result)
    else:
        st.warning("Please enter Python code before submitting.")