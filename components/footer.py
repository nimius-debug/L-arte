import streamlit as st
def footer():
    ft = """
    <style>
        a:link , a:visited{
            color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
            background-color: transparent;
            text-decoration: none;
        }

        a:hover,  a:active {
            color: #383b3a; /* theme's primary color*/
            background-color: transparent;
            text-decoration: underline;
        }

        #page-container {
            position: relative;
            min-height: 10vh;
        }

        footer{
            visibility:hidden;
        }

        .footer {
            font-size: 1rem; /* equals 14px */
            position: relative;
            left: 0;
            top:230px;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #808080; /* theme's text color hex code at 50 percent brightness*/
            text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
        }
    </style>

    <div id="page-container">
        <div class="footer">
            <p style='font-size: 0.875em;'>Made with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://www.instagram.com/Skinbylauralo/?fbclid=IwAR32AQJ6S3Z_fAUUIYrqHiGi4NCtXOifhGWyHcNX1yqGdxbr3YUlnBTjRQc" target="_blank"> by Skin by Laura Lo</a></p>
        </div>
    </div>
    """
    st.markdown(ft,unsafe_allow_html=True)

    # <div class="footer">
    # <p>Developed with ❤ at <a style='display: block; text-align: center;' href="https://www.instagram.com/Skinbylauralo/?fbclid=IwAR32AQJ6S3Z_fAUUIYrqHiGi4NCtXOifhGWyHcNX1yqGdxbr3YUlnBTjRQc" target="_blank">@ Skin by Laura Lo</a></p>
    # </div>
    # """
    # st.markdown(footer,unsafe_allow_html=True)