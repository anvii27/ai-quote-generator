import streamlit as st
import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data.get("content", "No quote found")
        author = data.get("author", "Unknown")
        return f'"{quote}" — {author}'
    else:
        return "Failed to retrieve quote."

st.title("Inspirational Quote Generator")

if st.button("Get Quote"):
    quote = get_random_quote()
    st.write(quote)
else:
    st.write("Click the button to get an inspirational quote.")
