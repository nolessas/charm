import streamlit as st
from hashlib import sha256
from streamlit_tags import st_tags

# Function to generate a random session token
def generate_session_token():
    return str(uuid.uuid4())

# Function to check if the user is logged in based on session token
def is_user_logged_in():
    session_token = st.session_state.get("session_token")
    return session_token is not None

def show_login():
    st.subheader("Login")

    # Custom HTML for the email input field
    st.markdown("""
    <style>
    .input-email {
        width: 100%;
        padding: 8px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        box-sizing: border-box;
    }
    </style>
    <input class="input-email" type="email" id="email" placeholder="Enter Username" name="email">
    """, unsafe_allow_html=True)

    # Password field
    password = st.text_input("Password", type="password")

    # Using JavaScript to get the value of the email input
    email = st_tags(label='',
                    text='Enter your email',
                    value=[''],
                    suggestions=[],
                    maxtags=1,
                    key='1')[0]

    if st.button("Login"):
        # Change these values to your desired credentials
        desired_username = st.secrets["username2"]
        desired_password = st.secrets["password2"]

        if check_password(email, password, desired_username, desired_password):
            st.success("Login successful!")
            
            # Generate a session token and store it in a cookie
            session_token = generate_session_token()
            st.session_state.session_token = session_token
            
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def check_password(username, password, desired_username, desired_password):
    # Change this to your preferred password hashing method
    hashed_input_password = sha256(password.encode()).hexdigest()
    
    return username == desired_username and hashed_input_password == sha256(desired_password.encode()).hexdigest()

def set_user_logged_in(logged_in):
    # Set the logged-in state
    st.session_state.logged_in = logged_in

# Check for the session token on app startup
if "session_token" in st.session_state:
    # You may want to perform additional validation here to ensure the session token is valid
    set_user_logged_in(True)

