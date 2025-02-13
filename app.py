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

# Function to load the whitelist
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

# Load whitelist (now always fetching the latest version)
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
st.markdown(
    """
    <div style="text-align:center;">
        <h3>Welcome to the PRIMOS Whitelist Checker!</h3>
        <p>Your gateway to verifying your spot in our exclusive whitelist!</p>
        <h4>How to Use the Whitelist Checker?</h4>
        <ul style="text-align:center;">
            <b>Enter Your Wallet Address</b> – Simply input the wallet you used for registration.
            <b>Check Status</b> – Our system will instantly verify whether your wallet is on the whitelist.
            <b>Get Ready to Mint!</b> – If you're whitelisted, you're all set for the upcoming sale.
        </ul>
        <h4>Need Help?</h4>
        <p>If you encounter any issues or believe there's a mistake, reach out via our official channels:</p>
        <p>
            🔹 <a href="https://x.com/PrimosWarriors" target="_blank">Twitter</a><br>
            🔹 <a href="https://discord.gg/npWJSwpsj4" target="_blank">Discord</a><br>
            🔹 <a href="https://primos.games" target="_blank">Website</a><br>
        </p>
        <p>Stay tuned for updates, sneak peeks, and more exclusive content! 🎉</p>
    </div>
    """,
    unsafe_allow_html=True
)
