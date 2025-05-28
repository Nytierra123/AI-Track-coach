import openai
import streamlit as st

#  OpenAI key 
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI Track Coach", page_icon="🏃‍♀️")
st.title("🏃‍♀️ AI Track Coach")
st.subheader("Get custom training advice based on your goals and physical/needs.")
#  fields
goal = st.text_input("What is your training goal? (e.g. improve sprint speed)")
issue = st.text_input("Any physical issues or concerns? (e.g. tight hamstrings)")
time = st.slider("How many minutes do you have to train today?", 10, 120, 30)


if st.button("Generate My Plan"):
    prompt = (
        f"I am a track athlete with the following details:\n"
        f"- Training goal: {goal}\n"
        f"- Physical issues: {issue}\n"
        f"- Available training time: {time} minutes\n\n"
        "Please create a customized training plan including warm-up, main workout, "
        "cool-down, and any advice to address physical concerns."
    )
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or your preferred model
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
            n=1,
            stop=None,
        )
        plan = response.choices[0].text.strip()
        st.write("### Your Customized Training Plan:")
        st.write(plan)
    except Exception as e:
        st.error(f"Error generating plan:{e}")

       
