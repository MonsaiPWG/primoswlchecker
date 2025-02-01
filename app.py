import streamlit as st
import pandas as pd
import time

# Function to add background
def add_bg_from_url():
    bg_url = "https://raw.githubusercontent.com/primoswlchecker/main/background.jpg"  # Change to your image URL
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
add_bg_from_url()

# Show PRIMOS logo
st.image("https://raw.githubusercontent.com/primoswlchecker/main/logo.png", width=300)

# Animated Title
st.markdown(
    """
    <h1 style="text-align:center; font-size:50px; color:#FFD700; text-shadow: 3px 3px 5px #000;">
        🚀 PRIMOS Whitelist Checker 🔥
    </h1>
    """,
    unsafe_allow_html=True
)

# Function to load the whitelist with animation
@st.cache_data
def load_whitelist():
    url = "https://raw.githubusercontent.com/MonsaiPWG/primoswlchecker/refs/heads/main/WL.csv"

    with st.spinner("🔄 Loading PRIMOS Whitelist..."):
        time.sleep(2)  # Simulate loading time

    try:
        df = pd.read_csv(url, usecols=[2], dtype=str, skiprows=1)
        df.columns = ["Wallet Address"]
        df["Wallet Address"] = df["Wallet Address"].str.strip().str.lower()
        return set(df["Wallet Address"].dropna())
    except Exception as e:
        st.error("⚠️ Error loading the whitelist. Ensure the CSV file is accessible online.")
        return set()

# Load whitelist
whitelist = load_whitelist()

# UI Input Field
wallet_address = st.text_input("🔑 Enter Your Wallet Address", "")

# Check whitelist status
if wallet_address:
    if wallet_address.strip().lower() in whitelist:
        st.success("✅ Your wallet is **whitelisted**! 🎉")
        st.balloons()  # 🎈 Confetti Animation
    else:
        st.error("❌ Your wallet is **not whitelisted**.")

# Footer
st.markdown("---")
st.markdown("🔒 This tool only checks wallet addresses. Editing the whitelist is not allowed.")
