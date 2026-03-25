import streamlit as st
from chain import answer_question

st.set_page_config(
    page_title="ClimateIQ-zw",
    page_icon="zw",
    layout="wide"
)

st.title("ClimateIQ-zw")
st.caption("AI-powered climate policy research assistant for Zimbabwe policymakers, government and NGOs")

st.divider()

col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_area(
        "Ask a question about Zimbabwe climate policy",
        height=120,
        placeholder="e.g. What are Zimbabwe's emission reduction targets? What adaptation measures are planned for agriculture?"
    )

with col2:
    st.markdown("**Output mode**")
    mode = st.radio(
        "Choose output type",
        ["Q&A answer", "Policy brief"],
        label_visibility="collapsed"
    )
    submit = st.button("Ask ClimateIQ", use_container_width=True, type="primary")

if submit and query:
    with st.spinner("Searching documents and generating response..."):
        result = answer_question(
            question=query,
            mode="brief" if "brief" in mode else "qa"
        )
    st.markdown("### Response")
    st.markdown(result)
    st.divider()
    st.caption("Response generated from official Zimbabwe and international climate policy documents.")

elif submit and not query:
    st.warning("Please type a question first.")
