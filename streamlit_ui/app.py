import streamlit as st
import requests

st.set_page_config(page_title="Oracle AI Agent", page_icon="🧠")

st.title("🧠 Oracle Text Cleaning AI Agent")

st.markdown("Describe what you want the agent to do:")

user_input = st.text_area("📝 Enter a CRM log, survey comment, or training note")

if st.button("🧠 Run Agent"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/route-and-clean",
                    json={"text": user_input}
                )
                result = response.json()
                st.success("✅ Cleaned Successfully!")

                st.markdown(f"**🧠 Intent:** `{result['intent']}`")
                st.markdown("**📥 Original Text:**")
                st.code(result['original'])

                st.markdown("**📤 Cleaned Output:**")
                st.code(result['cleaned'])

            except Exception as e:
                st.error(f"Something went wrong: {e}")
