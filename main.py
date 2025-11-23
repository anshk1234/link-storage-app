import streamlit as st
import json
import os

# File to store links
FILE_PATH = "links.json"

# Load existing links from file
def load_links():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

# Save links to file
def save_links(links):
    with open(FILE_PATH, "w") as file:
        json.dump(links, file, indent=4)

st.set_page_config(page_title="My Link Manager", layout="centered")
st.title("🔗 My Link Storage App")

links = load_links()

# Add New Link
st.subheader("➕ Add a New Link")
title = st.text_input("Link Name")
url = st.text_input("Link URL (https://...)")
add_btn = st.button("Save Link")

if add_btn:
    if title and url:
        new_link = {"title": title, "url": url}
        links.append(new_link)
        save_links(links)
        st.success("Link saved successfully!")
    else:
        st.warning("Please enter both title and URL!")

# Display Saved Links
st.subheader("📚 Saved Links")

if len(links) > 0:
    for i, link in enumerate(links):
        col1, col2, col3 = st.columns([4, 4, 1])
        col1.markdown(f"**{link['title']}**")
        col2.markdown(f"[Open Link]({link['url']})")

        
else:
    st.info("No links saved yet! Add some 😊")

