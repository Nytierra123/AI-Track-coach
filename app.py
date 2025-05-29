import streamlit as st
import requests

st.title("AI Track Coach")
st.write("Tell me your training goals and any physical concerns (e.g. tight hamstrings).")

user_input = st.text_area("Enter your info here:")

API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_TOKEN = st.secrets["HUGGINGFACE_API_TOKEN"]

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        st.write(f"Status code: {response.status_code}")
        st.write(f"Response text: {response.text}")

        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}

    except requests.exceptions.JSONDecodeError:
        st.error("Response was not valid JSON.")
        return {"error": "Invalid JSON response from API."}

    except Exception as err:
        st.erro
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
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                st.write(f"Status code: {response.status_code}")
                st.write(f"Response text: {response.text}")

                response.raise_for_status()
                result = response.json()

                if isinstance(result, dict) and "error" in result:
                    st.error(f"Error from Hugging Face: {result['error']}")
                else:
                    st.write("### Your Customized Training Plan:")
                    st.write(result[0]["generated_text"])

            except Exception as e:
                st.error(f"Error during API call: {e}")
