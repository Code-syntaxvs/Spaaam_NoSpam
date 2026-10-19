
from pathlib import Path
import joblib
import streamlit as st

MODEL_PATH = Path(__file__).parent / "sms_spam_pipeline.pkl"

model = joblib.load(MODEL_PATH)

st.title("SMS Spam Detector")
st.write("Enter an SMS message to classify it.")

message = st.text_area("Enter your SMS message")

if st.button("Check Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("This message is classified as SPAM.")
        else:
            st.success("This message is classified as HAM.")
