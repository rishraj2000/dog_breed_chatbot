import streamlit as st
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8000/query"

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI
st.title("🐶 Dog Breed Assistant")

user_id = st.text_input("Enter your User ID:", key="user_id")

if user_id:
    user_query = st.text_input("Ask a question about dog breeds:")

    if st.button("Submit") and user_query:
        payload = {"user_id": user_id, "query": user_query}
        response = requests.post(FASTAPI_URL, json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "No response received.")
            st.session_state.history.append({"query": user_query, "answer": answer})
        else:
            st.error("Error fetching response from the server.")

# Display conversation history
st.subheader("Conversation History")
for chat in st.session_state.history:
    st.write(f"**You:** {chat['query']}")
    st.write(f"**Bot:** {chat['answer']}")
