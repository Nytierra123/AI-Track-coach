import streamlit as st
import requests

# Streamlit UI
st.title("AI Track Coach")
st.write("Tell me your training goals and any physical concerns (e.g. tight hamstrings).")

user_input = st.text_area("Enter your info here:")

# Hugging Face setup
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B"
HF_TOKEN = st.secrets["HUGGINGFACE_API_TOKEN"]  # <-- You'll need to add this in secrets.toml

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if st.button("Generate My Plan"):
    if not user_input:
        st.warning("Please enter your training goals and physical concerns.")
    else:
       prompt = (
    f"You are a track and field coach. Based on this athlete input:\n"
    f"{user_input}\n"
    f"Please create a customized training plan including warm-up, main workout, "
    f"cool-down, and any advice to address physical concerns."
)
        with st.spinner("Generating your plan..."):
            result = query({"inputs": full_prompt})

        if isinstance(result, dict) and "error" in result:
            st.error(f"Error from Hugging Face: {result['error']}")
        else:
            st.write("### Your Customized Training Plan:")
            st.write(result[0]["generated_text"])
