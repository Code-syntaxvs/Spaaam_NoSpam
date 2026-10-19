
import streamlit as st
import joblib

model = joblib.load("sms_spam_pipeline.pkl")

st.title("SMS Spam Detector")
st.write("Enter an SMS message to classify it.")

message = st.text_area("SMS message")

if st.button("Check Message"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("This message is classified as SPAM.")
        else:
            st.success("This message is classified as HAM.")

pip install -r requirements.txt
streamlit run app.py
