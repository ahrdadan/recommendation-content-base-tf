import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
lomba_df = pd.read_csv('../../datasets/Lomba_dataset.csv', encoding='latin1')

# input colom
lomba_df['all_words'] = lomba_df['title'] + ' ' + lomba_df['category_id'] + ' ' +  lomba_df['organizer_id'] + ' ' + lomba_df['description']

# encode to utf-8
def encode_text(text):
    return text.encode('utf-8')
lomba_df['all_words'] = lomba_df['all_words'].apply(encode_text)

# change to vector 
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(lomba_df['all_words'])

# Model dan layers
input_dim = tfidf_matrix.shape[1]
input_layer = Input(shape=(input_dim,))
dense_layer_1 = Dense(128, activation='relu')(input_layer)
dense_layer_2 = Dense(64, activation='relu')(dense_layer_1)
output_layer = Dense(input_dim, activation='linear')(dense_layer_2)

model = Model(inputs=input_layer, outputs=output_layer)
model.compile(optimizer='adam', loss='mse')

# Training the model
model.fit(x=tfidf_matrix.toarray(), y=tfidf_matrix.toarray(), epochs=10, batch_size=32)

# save model and data
model.save('../../save_models/cb_model.h5')