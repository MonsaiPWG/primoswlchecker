import streamlit as st
import pandas as pd

# Function to load the whitelist from a CSV file hosted on GitHub
@st.cache_data
def load_whitelist():
    url = "https://raw.githubusercontent.com/MonsaiPWG/primoswlchecker/refs/heads/main/WL.csv"  # Change to your actual GitHub URL
    try:
        df = pd.read_csv(url, usecols=[0])  # Assuming wallet addresses are in the first column
        df.columns = ["Wallet Address"]
        return set(df["Wallet Address"].dropna())
    except Exception as e:
        st.error("⚠️ Error loading the whitelist. Ensure the CSV file is accessible online.")
        return set()  # Return an empty set if the file fails to load

# Load whitelist automatically from GitHub
whitelist = load_whitelist()

# Streamlit UI
st.title("🔍 Whitelist Checker (CSV from GitHub)")
st.write("Enter your wallet address below to check if you're whitelisted.")

# User input field
wallet_address = st.text_input("🔑 Wallet Address", "")

# Check whitelist status
if wallet_address:
    if wallet_address in whitelist:
        st.success("✅ Your wallet is **whitelisted**! 🎉")
    else:
        st.error("❌ Your wallet is **not whitelisted**.")

# Footer
st.markdown("---")
st.markdown("🔒 This tool only checks wallet addresses. Editing the whitelist is not allowed.")
