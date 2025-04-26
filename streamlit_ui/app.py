import streamlit as st
import requests

st.set_page_config(page_title="Oracle AI Agent", page_icon="🧠")

st.title("🧠 Oracle Text Cleaning AI Agent")

st.markdown("Describe what you want the agent to do:")

user_input = st.text_area("📝 Enter a CRM log, survey comment, or training note")

survey_on = st.toggle("🧽 SurveyCleanMOD Agent", key="survey_toggle")
crm_on = st.toggle("📋 CRM Clean Agent", key="crm_toggle")

if st.button("🧠 Run Agent"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            try:
                # Default: Use LLM route
                response = requests.post(
                    "http://127.0.0.1:8000/route-and-clean",
                    json={"text": user_input}
                )
                result = response.json()

                st.success("✅ LLM Intent Detection Completed!")
                st.markdown(f"**🧠 Detected Intent:** `{result['intent']}`")
                st.markdown("**📥 Original Text:**")
                st.code(result['original'])
                st.markdown("**📤 Cleaned Output:**")
                st.code(result['cleaned'])

                # If survey agent is toggled ON, run SurveyCleanMOD too
                if survey_on:
                    st.divider()
                    st.info("SurveyCleanMOD agent also running...")

                    survey_response = requests.post(
                        "http://127.0.0.1:8000/toggle-agent",
                        json={"agent": "survey_clean_mod", "texts": [user_input]}
                    )
                    if survey_response.status_code == 200:
                        survey_result = survey_response.json()
                        if survey_result.get("result"):
                            cleaned_output = survey_result["result"][0]
                            st.markdown("### 🧽 SurveyCleanMOD Output")
                            st.markdown(f"**Original:** {cleaned_output['original']}")
                            st.markdown(f"**Cleaned:** {cleaned_output['cleaned']}")
                    else:
                        st.error(f"Survey Agent Error: {survey_response.text}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
