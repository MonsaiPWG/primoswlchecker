import streamlit as st
import pandas as pd
import time




# Animated Title
st.markdown(
    """
    <h1 style="text-align:center; font-size:50px; color:#FFD700; text-shadow: 3px 3px 5px #000;">
    PRIMOS Whitelist Checker
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
        st.success("✅ Your wallet is **whitelisted**! AHOOOOOOO")
        st.balloons()  # 🎈 Confetti Animation
    else:
        st.error("❌ Your wallet is **NOT whitelisted**.")

# Footer
st.markdown("---")
st.markdown("Welcome to the PRIMOS Whitelist Checker – your gateway to verifying your spot in our exclusive whitelist! If you've secured a whitelist spot, this tool will confirm your eligibility and ensure you're ready for mint day.

How to Use the Whitelist Checker?
Enter Your Wallet Address – Simply input the wallet you used for registration.
Check Status – Our system will instantly verify whether your wallet is on the whitelist.
Get Ready to Mint! – If you're whitelisted, you're all set for the upcoming drop.
Need Help?
If you encounter any issues or believe there's a mistake, feel free to reach out via our official channels:

🔹 Twitter: @YourTwitterHandle
🔹 Discord: Join the Community
🔹 Website: www.yourwebsite.com

Stay tuned for updates, sneak peeks, and more exclusive content.")

