import openai
import streamlit as st

# Set the API key
openai.api_key = "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"

# Take input from the user
prompt = st.text_area("Enter a prompt: ")

# Use GPT-3 to generate text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024
)

# Output the generated text
st.write(response["choices"][0]["text"])

# Output the results
#st.write("Sum: ", sum)
