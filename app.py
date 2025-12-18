import streamlit as st
from langchain_openai import ChatOpenAI

st.title("🤖 My First Agent App")

passcode = st.text_input("Enter access code:", type="password")
if passcode != '123456789!"#¤%&/()':  # Change this
    st.warning("Wrong code!")
    st.stop()

# Initialize the model (uses secret key)
llm = ChatOpenAI(api_key=st.secrets["OPENAI_API_KEY"], model="gpt-4o")

# Create a simple chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Get AI response
    response = llm.invoke(prompt).content

    # 3. Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
