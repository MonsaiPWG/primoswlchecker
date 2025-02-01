import streamlit as st
import pandas as pd

# Function to load the whitelist from GitHub
@st.cache_data
def load_whitelist():
    url = "https://raw.githubusercontent.com/MonsaiPWG/primoswlchecker/refs/heads/main/WL.csv"
    try:
        df = pd.read_csv(url, usecols=[2], dtype=str, skiprows=1)  # Skip header row, use correct column
        df.columns = ["Wallet Address"]
        df["Wallet Address"] = df["Wallet Address"].str.strip().str.lower()  # Normalize case & remove spaces
        whitelist_set = set(df["Wallet Address"].dropna())
        st.write("✅ Loaded Wallets:", whitelist_set)  # Debugging
        return whitelist_set
    except Exception as e:
        st.error(f"⚠️ Error loading the whitelist: {e}")
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
    if wallet_address.strip().lower() in whitelist:
        st.success("✅ Your wallet is **whitelisted**! 🎉")
    else:
        st.error("❌ Your wallet is **not whitelisted**.")

# Footer
st.markdown("---")
st.markdown("🔒 This tool only checks wallet addresses. Editing the whitelist is not allowed.")
