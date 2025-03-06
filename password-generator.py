import re
import random
import streamlit as st

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "#28a745", suggestions  # Green
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "#ff9800", suggestions  # Orange
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "#e63946", suggestions  # Red

# Function to generate a strong password
def generate_strong_password(length=12):
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digit = random.choice("0123456789")
    special = random.choice("!@#$%^&*")
    
    remaining_chars = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*") for _ in range(length - 4))
    
    password = list(lower + upper + digit + special + remaining_chars)
    random.shuffle(password)
    
    return ''.join(password)

# Streamlit UI Styling
st.markdown(
    """
    <style>
     header, .css-18e3th9 {
            background: linear-gradient(to right, #D4BEE4, #9B7EBD) !important;
        }
        body {
            background: linear-gradient(to right, #D4BEE4, #9B7EBD );
            color: white;
        }
        .stApp {
            background: linear-gradient(to right, #D4BEE4, #9B7EBD);
            color: white;
        }
        .stTextInput label {
            color: white !important;  /* Red Color for "Enter your password:" */
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button {
            background: linear-gradient(45deg, #D91656, #D91656);
            color: #ffffff !important;  /* Button Text Color */
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
            border-radius: 40px;
        }
        .stMarkdown p {
            font-weight: bold;
            font-size: 18px;
        }
        .password-box {
            background: #2c3e50;
            padding: 15px;
            border-radius: 8px;
            color: white;
        }
     
    </style>
    """,
    unsafe_allow_html=True
)

# st.title("🔒 Password Strength Meter")
st.markdown(
    "<h1 style='color:#FFF7D1; text-align:center;  font-size : 32px'>🔒 Password Strength Meter</h1>", 
    unsafe_allow_html=True
)

# password = st.text_input("Enter your password:", type="password" )
password = st.text_input("Enter your password:", type="password", placeholder="Enter your password")

if st.button("Check Strength", key="check"):
    if password:
        result, color, suggestions = check_password_strength(password)
        st.markdown(f"<p style='color:{color}; font-size:20px; font-weight:bold;'>{result}</p>", unsafe_allow_html=True)
        
        if suggestions:
            st.write("### Suggestions:")
            for suggestion in suggestions:
                st.markdown(f"<p style='color:red;'>{suggestion}</p>", unsafe_allow_html=True)
            # ffcc00
            st.write("### 🔹 Suggested Strong Password:")
            strong_password = generate_strong_password()
            st.markdown(f"<div class='password-box'>{strong_password}</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Please enter a password!")

















# import re
# import random
# import streamlit as st

# def check_password_strength(password):
#     score = 0
#     suggestions = []
    
#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append("❌ Password should be at least 8 characters long.")
    
#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append("❌ Include both uppercase and lowercase letters.")
    
#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         suggestions.append("❌ Add at least one number (0-9).")
    
#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         suggestions.append("❌ Include at least one special character (!@#$%^&*).")
    
#     # Strength Rating
#     if score == 4:
#         return "✅ Strong Password!", "green", suggestions
#     elif score == 3:
#         return "⚠️ Moderate Password - Consider adding more security features.", "orange", suggestions
#     else:
#         return "❌ Weak Password - Improve it using the suggestions below.", "red", suggestions

# # def generate_strong_password():
# #     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
# #     return ''.join(random.choice(characters) for _ in range(12))



# def generate_strong_password():
#     lower = random.choice("abcdefghijklmnopqrstuvwxyz")  # At least one lowercase
#     upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # At least one uppercase
#     digit = random.choice("0123456789")  # At least one digit
#     special = random.choice("!@#$%^&*")  # At least one special character
    
#     # Remaining characters randomly select karo
#     remaining_chars = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*") for _ in range(8))
    
#     # In sabko shuffle kar do taake predictable pattern na ho
#     password = list(lower + upper + digit + special + remaining_chars)
#     random.shuffle(password)
    
#     return ''.join(password)  # Final password return


# # Streamlit UI
# st.title("🔒 Password Strength Meter")
# password = st.text_input("Enter your password:", type="password")


# if st.button("Check Strength"):
#     if password:
#         result, color, suggestions = check_password_strength(password)
#         st.markdown(f"<p style='color:{color}; font-size:18px;'>{result}</p>", unsafe_allow_html=True)
        
#         if suggestions:
#             st.write("### Suggestions:")
#             for suggestion in suggestions:
#                 st.write(f"- {suggestion}")
            
#             st.write("### 🔹 Suggested Strong Password:")
#             st.code(generate_strong_password())
#     else:
#         st.error("⚠️ Please enter a password!")





















# import streamlit as st
# import random
# import  string  # ya hama specific letters provide karta hai ya capital , small kisi bhi form ma ho sakta hai


# def generate_password(length , use_digits , use_special):

#     character = string.ascii_letters # add upparcase and lowercase latter 

#     if use_digits:
#         character += string.digits # Add numbers (0-9)  if selected

#     if use_special:
#         character += string.punctuation  # Adds  special character (!,@,#,$,%,&,^)  if selected


#     return "".join(random.choice(character) for _ in range(length))


# st.title("Password Generator")

# length = st.slider("Select Password  Length" , min_value = 6 , max_value = 32 , value = 12)

# use_digits = st.checkbox("Include Digits")

# use_special = st.checkbox("Include special character")

# if st.button("Generate Password"):
#     password = generate_password(length , use_digits , use_special)
#     st.write(f"Generated Password :      {password}")


# # st.write("------------------------------------------------------")

# st.write("Made With ❤ by Tehreem Asghar")