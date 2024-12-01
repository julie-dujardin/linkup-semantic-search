import os

import streamlit as st
import requests

# Input query
query = st.text_input("Search")

# Send query to FastAPI endpoint
if query:
    # local: BACKEND_ENDPOINT=http://127.0.0.1:8888/
    response = requests.get(os.environ["BACKEND_ENDPOINT"], params={"query": query})
    response.raise_for_status()
    results = response.json()

    # Display results
    for result in results:
        st.write(f"Article: {result['title']}")
        st.write(f"Description: {result['description']}")
        st.write(f"Link: {result['url']}")
        st.write(f"Author: {result['creator']}")
        st.write("--")
