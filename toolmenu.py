import streamlit as st

def main():
    st.title("ZJ's Lab Tools")

    # Define your links, icons, and descriptions
    links_info = [
        {"name": "Google", "url": "https://www.google.com", "icon": "🌐", "desc": "Search the web"},
        {"name": "Wikipedia", "url": "https://www.wikipedia.org", "icon": "📚", "desc": "Free encyclopedia"},
        # Add more links as needed
    ]

    # Setting up a grid layout
    cols_per_row = 3
    for i in range(0, len(links_info), cols_per_row):
        cols = st.columns(cols_per_row)
        for col, link_info in zip(cols, links_info[i:i+cols_per_row]):
            with col:
                # Icon and name centered
                st.markdown(f"<a href='{link_info['url']}' target='_blank' style='text-decoration:none;'><center>{link_info['icon']}<br>{link_info['name']}</center></a>", unsafe_allow_html=True)
                # Description centered
                st.markdown(f"<center>{link_info['desc']}</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
