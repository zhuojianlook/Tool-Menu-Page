import streamlit as st

def main():
    st.title("ZJ's Lab Tools")

    # Define your links, icons, and descriptions
    links_info = [
        {"name": "Cornea Donor Information Scraper", "url": "https://corneainfo.streamlit.app/", "icon": "🌐", "desc": "For Saving Sight Corneas"},
        {"name": "Heatmap Bar Chart", "url": "https://xyanalysis.streamlit.app/", "icon": "📚", "desc": "Demo Tool"},
        {"name": "Heatmap Bar Chart", "url": "https://zhuojianlook-multipanelfigure-multipanelfigure-no8tmp.streamlit.app/", "icon": "📚", "desc": "Multi-Panel Figure Generator"},

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
