# streamlit_ui/app.py (full updated version to handle your new product reviews CSV)

import streamlit as st
import requests
import pandas as pd
import io

st.set_page_config(page_title="Oracle AI Agent", page_icon="🧠")
st.title("🧠 Oracle Text Cleaning AI Agent")

# File uploader
uploaded_file = st.file_uploader("📎 Upload a text or CSV file for cleaning", type=["txt", "csv"])

st.markdown("Describe what you want the agent to do:")
user_input = st.text_area("📝 Enter a CRM log, survey comment, or training note")

# Toggles
survey_on = st.toggle("🧽 SurveyCleanMOD Agent", key="survey_toggle")
crm_on = st.toggle("📋 CRM Clean Agent", key="crm_toggle")

# Button to run agent
if st.button("🧠 Run Agent"):
    if not uploaded_file and user_input.strip() == "":
        st.warning("Please upload a file or enter text.")
    else:
        with st.spinner("Processing..."):
            try:
                texts_to_clean = []

                # If file uploaded, read its contents
                if uploaded_file is not None:
                    if uploaded_file.name.endswith(".txt"):
                        content = uploaded_file.read().decode("utf-8")
                        texts_to_clean = content.splitlines()
                    elif uploaded_file.name.endswith(".csv"):
                        # Read with ISO-8859-1 encoding to handle messy characters
                        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

                        # If Review and Summary columns exist, combine them
                        if "Review" in df.columns and "Summary" in df.columns:
                            texts_to_clean = (
                                df[["Review", "Summary"]]
                                .fillna("")
                                .agg(" ".join, axis=1)
                                .tolist()
                            )
                            # Clean up empty entries after merging Review and Summary
                            texts_to_clean = [t for t in texts_to_clean if t.strip() != ""]

                        else:
                            st.error("Uploaded CSV must contain 'Review' and 'Summary' columns.")
                            st.stop()

                # Otherwise, use text area input
                if user_input.strip() != "" and not uploaded_file:
                    texts_to_clean = [user_input]

                # Always run LLM classification on first item
                response = requests.post(
                    "http://127.0.0.1:8000/route-and-clean",
                    json={"text": texts_to_clean[0]}
                )
                result = response.json()

                st.success("✅ LLM Intent Detection Completed!")
                st.markdown(f"**🧠 Detected Intent:** `{result['intent']}`")
                st.markdown("**📥 Original Text:**")
                st.code(result['original'])
                st.markdown("**📤 Cleaned Output:**")
                st.code(result['cleaned'])

                # If survey agent toggle is ON, process full list
                if survey_on:
                    st.divider()
                    st.info("SurveyCleanMOD agent also running on full input...")

                    survey_response = requests.post(
                        "http://127.0.0.1:8000/toggle-agent",
                        json={"agent": "survey_clean_mod", "texts": texts_to_clean}
                    )

                    if survey_response.status_code == 200:
                        survey_result = survey_response.json()
                        cleaned_entries = survey_result.get("result", [])

                        if cleaned_entries:
                            cleaned_texts = [entry['cleaned'] for entry in cleaned_entries]
                            cleaned_output = "\n".join(cleaned_texts)

                            st.success("✅ Cleaning Completed!")
                            st.download_button("📥 Download Cleaned File", data=cleaned_output, file_name="cleaned_output.txt")
                        else:
                            st.warning("Nothing new was cleaned. Maybe all texts were already processed.")
                    else:
                        st.error(f"Survey Agent Error: {survey_response.text}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
