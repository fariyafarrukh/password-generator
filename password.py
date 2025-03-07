import streamlit as st
import random
import string

# Set Page Config (Only Run Once)
st.set_page_config(page_title="Password Generator", page_icon="🔑")

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# Title
st.title("🔐 Secure Password Generator")

# User Inputs
length = st.slider("🔢 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("✅ Include Numbers")
use_special = st.checkbox("✨ Include Special Characters")

# Generate Password
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("🔑 **Generated Password:**")
    st.code(password, language="")

    # Copy to Clipboard (Alternative Way)
    st.text_input("📋 Copy Password", password)

    # Password Strength Indicator
    strength = "Weak ❌" if length < 8 else "Medium ⚠️" if length < 12 else "Strong ✅"
    st.write(f"🛡️ **Password Strength:** {strength}")

# Footer
st.write("---")
st.markdown("🔹 **Built with ❤️ by [Fariya Farrukh](https://github.com/FariyaFarrukh)**")

