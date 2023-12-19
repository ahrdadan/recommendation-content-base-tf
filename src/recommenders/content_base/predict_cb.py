import pandas as pd
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
# df = pd.read_csv('../../datasets/Lomba_dataset.csv', encoding='latin1')
df = pd.read_csv('datasets/Lomba_dataset.csv', encoding='latin1')

# input colom
df['all_words'] = df['title'] + ' ' + df['category_id'] + ' ' +  df['organizer_id'] + ' ' + df['description']

# encode to utf-8
def encode_text(text):
    return text.encode('utf-8')
df['all_words'] = df['all_words'].apply(encode_text)


# change to vector 
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['all_words'])

#load model
# loaded_model = tf.keras.models.load_model('../../save_models/cb_model.h5')
loaded_model = tf.keras.models.load_model('save_models/cb_model.h5')

# Getting recommendations using the trained model
predictions = loaded_model.predict(tfidf_matrix.toarray())

# Function to get lomba recommendations based on title
def get_lomba_recommendations(id, top_n=5):
    lomba_index = df.index[df['id'] == id].tolist()[0]
    similarities = cosine_similarity([predictions[lomba_index]], predictions)
    related_indices = similarities.argsort()[0][::-1][1:]  # Exclude self-similarity
    top_n_recommendations = related_indices[:top_n]  # Get top N recommendations
    recommended_lombas = df.iloc[top_n_recommendations][['id', 'title', 'organizer_id', 'poster','category_id']]
    data = recommended_lombas.to_dict(orient='records')
    return data


# Example: Get top 3 recommendations for 'The Shawshank Redemption'
# recommendations = get_lomba_recommendations('Turnamen Dota 2 - Meister Tarkam Solo Mid', top_n=3)
# print("Top 3 Recommendations:")
# print(recommendations)
