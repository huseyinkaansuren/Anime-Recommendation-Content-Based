from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
pd.set_option('display.max_columns', None)


df = pd.read_csv("data.csv")

def calculate_cosune_sim(dataframe):
    df["Overview"] = df["Overview"].fillna("")
    tfidf = TfidfVectorizer(stop_words="english")
    dataframe["Overview"] = dataframe["Overview"].fillna("")
    tfidf_matrix = tfidf.fit_transform(dataframe["Overview"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = calculate_cosune_sim(df)

def content_based_recommender(title, cosine_sim, dataframe):
    #index'leri oluşturma
    indices = pd.Series(dataframe.index, index = dataframe["Name"])

    #title' ın index' ini yakalama
    movie_index = indices[title]

    #title' a göre benzerlik skorlarını hesaplama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])

    #kendisi hariç ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index

    return dataframe["Name"].iloc[movie_indices]

#content_based_recommender("Naruto", cosine_sim, df)













