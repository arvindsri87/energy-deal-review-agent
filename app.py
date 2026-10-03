import streamlit as st
import pandas as pd

st.set_page_config(page_title="B2B Energy Deal Review Agent", layout="wide")

st.title("⚡ B2B Energy Deal Review & Risk Agent")
st.caption("Commercial Sales, Trading & Controlling Enablement System")

st.sidebar.header("Configuration")
mock_mode = st.sidebar.checkbox("Use Mock API Mode", value=True)
model_choice = st.sidebar.selectbox("Extraction Model", ["Claude 3.5 Sonnet", "Llama 3 70B (On-Prem)"])

st.subheader("Contract Upload & Parsing")
uploaded_file = st.file_uploader("Upload B2B Energy Term Sheet (PDF)", type=["pdf"])

if uploaded_file or mock_mode:
    st.success("Term Sheet Loaded: `Synthetic_LNG_Supply_Deal_024.pdf`")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Contract Volume", "150,000 MWh")
    col2.metric("Indexation Ticker", "TTF Month-Ahead")
    col3.metric("Margin Check", "+4.2 €/MWh", delta="Pass")

    st.subheader("Extracted Terms & Risk Flags")
    data = {
        "Clause": ["Payment Terms", "Price Indexation", "Credit Rating Required", "Liability Cap"],
        "Extracted Value": ["45 Days", "TTF DA + 0.85 €/MWh", "BBB+ or Parent Guarantee", "100% of Contract Value"],
        "Risk Status": ["⚠️ Flag: Exceeds 30-Day Policy", "✅ Approved", "✅ Approved", "✅ Approved"]
    }
    st.table(pd.DataFrame(data))

    st.subheader("Human-in-the-Loop Sign-off")
    st.button("Approve Deal Review & Forward to Controlling")
