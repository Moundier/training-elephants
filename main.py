import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample user-item matrix (replace this with your data)
user_item_matrix = pd.DataFrame({
    'User1': [5, 4, 0, 0, 1],
    'User2': [0, 5, 4, 0, 2],
    'User3': [2, 0, 0, 5, 4],
    'User4': [0, 2, 3, 4, 5],
}, index=['Item1', 'Item2', 'Item3', 'Item4', 'Item5'])

# Sample movie data with genres (replace this with your data)
movies_data = pd.DataFrame({
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genres': ['Action, Adventure', 'Comedy, Romance', 'Action, Sci-Fi', 'Drama', 'Comedy, Drama'],
})

# Create a TF-IDF Vectorizer for genres
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
genres_matrix = tfidf_vectorizer.fit_transform(movies_data['Genres'])

def user_based_recommendation(user_item_matrix, target_user):
    similarities = cosine_similarity(user_item_matrix.T)
    target_user_index = user_item_matrix.columns.get_loc(target_user)
    user_similarities = similarities[target_user_index]
    similar_users = user_similarities.argsort()[:-1][::-1]
    recommendations = user_item_matrix.iloc[:, similar_users].mean(axis=1)
    recommendations = recommendations.sort_values(ascending=False)
    return recommendations

def item_based_recommendation(user_item_matrix, target_user):
    item_similarities = cosine_similarity(user_item_matrix.T)  # Transpose here
    target_user_index = user_item_matrix.columns.get_loc(target_user)
    item_scores = item_similarities[:, target_user_index]
    similar_items = item_scores.argsort()[:-1][::-1]
    recommendations = user_item_matrix.iloc[similar_items, user_item_matrix.columns.get_loc(target_user)]
    recommendations = recommendations.sort_values(ascending=False)
    return recommendations

def content_based_recommendation(movies_data, target_movie):
    cosine_similarities = linear_kernel(genres_matrix)  # Pass only one instance of genres_matrix
    target_movie_index = movies_data[movies_data['Title'] == target_movie].index[0]
    movie_similarities = cosine_similarities[target_movie_index]
    similar_movies = movie_similarities.argsort()[:-1][::-1]
    recommendations = movies_data.iloc[similar_movies]['Title']
    return recommendations

# Example usage
target_user = 'User1'
target_movie = 'Movie A'

user_based_results = user_based_recommendation(user_item_matrix, target_user)
item_based_results = item_based_recommendation(user_item_matrix, target_user)
content_based_results = content_based_recommendation(movies_data, target_movie)

print("User-based Recommendations:")
print(user_based_results)

print("\nItem-based Recommendations:")
print(item_based_results)

print("\nContent-based Recommendations:")
print(content_based_results)

# The [:-1] slice operation is used to remove the last element (which is the index of the movie itself) 
# The [::-1] is used to reverse the array, so the most similar movies come first.