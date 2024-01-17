# authentication.py

import streamlit as st
from hashlib import sha256
import hashlib



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hash the password 'powerfull'
hashed_password = hash_password("powerfull")
print(hashed_password)  # You store this hashed value in Streamlit secrets

def is_user_logged_in():
    return st.session_state.get('logged_in', False)


def show_login():
    st.subheader("Login")

    # Add login form elements here
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Change these values to your desired credentials
        # These lines are no longer needed as you're now using Streamlit secrets
        # desired_username = "a"
        # desired_password = "a"

    if check_password(username, password):
        st.success("Login successful!")
        set_user_logged_in(True)
        st.balloons()
        st.experimental_rerun()
    else:
        # Debugging: Print out the hashed password from secrets and the entered hashed password
        stored_hashed_password = users.get(username, "")
        entered_hashed_password = hashlib.sha256(password.encode()).hexdigest()
        st.error(f"Stored Hashed Password: {stored_hashed_password}")
        st.error(f"Entered Hashed Password: {entered_hashed_password}")
        st.error("Invalid username or password")

def check_password(username, password):
    # Get the dictionary of users from Streamlit secrets
    users = st.secrets.get("users", {})

    # Check if the username exists in the secrets
    if username in users:
        # Retrieve the stored hashed password
        stored_hashed_password = users[username]

        # Hash the entered password
        entered_hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Compare the entered hashed password with the stored hashed password
        return entered_hashed_password == stored_hashed_password
    else:
        # Username not found in secrets
        return False

