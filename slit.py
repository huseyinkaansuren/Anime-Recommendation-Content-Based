import streamlit as st
import time
from PIL import Image
import pandas as pd
import recomme as rc


st.set_page_config(layout="wide")

df = pd.read_csv("data.csv")
df.head()
df.drop("Unnamed: 0", axis = 1, inplace=True)
# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src = "https://templates.simplified.co/thumb/74f9312c-7b3e-47ef-8d7c-52d5955c930b.jpg" alt="banner">
</div>
<style>
    .banner {
        width: %100;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        height: 150px;
        object-fit: cover;
    }
</style>
"""

st.components.v1.html(custom_html)


st.markdown("""<h1 style='color: #3498db; text-align: center;'>Anime Recommendation System</h1>""",unsafe_allow_html=True)

#image = Image.open('banner.jpeg')
#st.image(image, use_column_width=True)

st.write("In this project we are recommending similar animes that you watched. With this you can easily enjoy the next show. In this data only contains 1000 anime.")

anime_title = st.text_input("Enter Anime Name")

if anime_title != "":
    selected_name = st.selectbox("Select a Name", df.loc[df["Name"].str.contains(anime_title.capitalize())])
    if selected_name != "":
        cosine_sim = rc.calculate_cosune_sim(df)
        recommended_animes = rc.content_based_recommender(selected_name, cosine_sim, df)
        st.write(recommended_animes)
else:
    st.warning("Write Name")





#st.dataframe(df.loc[df["Name"].str.contains(anime_title.capitalize())])



#st.write(anime_title, "Selected")

# Using object notation
#rec_type = st.sidebar.selectbox(
#    "Which Type of Recommendation?",
#    ("Content-Based", "Item-Based")
#)
#if rec_type == "Content-Based":
#    st.write("Content-Based Selected!!")
#
#elif rec_type == "Item-Based":
#    st.write("Item-Based Selected!!")

# Using "with" notation
#with st.sidebar:
#    add_radio = st.radio(
#        "Which Type of Recommendation?",
#        ("Content-Based", "Item-Based")
#    )
#    if add_radio == "Content-Based":
#        text = st.write("Selected Content")
#
#    elif add_radio != "Content-Based":
#        st.write("")


#with st.sidebar:
    #st.write("Bu kod buraya printlenecek")

    #with st.spinner("Loading..."):
        #time.sleep(1)
        #st.success("Done!")