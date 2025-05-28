import openai
import streamlit as st

# Load your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("AI Track Coach")
st.write("Tell me your training goals and any physical concerns (e.g. tight hamstrings).")

user_input = st.text_area("Enter your info here:")

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

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
                messages=[
                    {"role": "system", "content": "You are a helpful and expert track coach."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=500,
                temperature=0.7,
            )

            plan = response.choices[0].message.content.strip()
            st.write("### Your Customized Training Plan:")
            st.write(plan)

        except Exception as e:
            st.error(f"Error generating plan: {e}")
