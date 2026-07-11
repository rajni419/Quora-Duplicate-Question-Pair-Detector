import streamlit as st
import helper
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="Duplicate Question Detector",
    page_icon="❓",
    layout="centered"
)

st.title("❓ Quora Duplicate Question Pair Detector")

st.write("Enter two questions to check whether they are duplicates or not.")

st.markdown("---")

q1 = st.text_input("Question 1")

q2 = st.text_input("Question 2")

if st.button("Find Duplicate"):

    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions.")
    else:

        query = helper.query_point_creator(q1, q2)

        result = model.predict(query)[0]

        if result == 1:
            st.success("✅ Duplicate Questions")
        else:
            st.error("❌ Not Duplicate Questions")