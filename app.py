import pickle
import streamlit as st
import numpy as np

# Load the saved pickle files from artifacts folder
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))


def fetch_poster(suggestion):
    """
    Fetch poster URLs for recommended books
    """
    book_name = []
    ids_index = []
    poster_url = []
    
    # Get book names from suggestions
    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    
    # Get indices in final_rating dataframe
    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)
    
    # Get image URLs
    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)
    
    return poster_url


def recommend_book(book_name):
    """
    Recommend books based on the selected book using KNN model
    """
    books_list = []
    
    # Find the book ID in book_pivot
    book_id = np.where(book_pivot.index == book_name)[0][0]
    
    # Get nearest neighbors (6 books including the selected one)
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    
    # Fetch poster URLs
    poster_url = fetch_poster(suggestion)
    
    # Get book names from suggestions
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    
    return books_list, poster_url


# Streamlit App Interface
st.header('📚 Books Recommender System')
st.markdown("### Discover your next favorite book!")
st.text("This is a collaborative filtering based recommendation system.")
st.markdown("---")

# Book selection dropdown
selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

# Show Recommendation button
if st.button('Show Recommendation'):
    try:
        recommended_books, poster_url = recommend_book(selected_books)
        
        st.success(f"Books similar to '{selected_books}':")
        st.markdown("---")
        
        # Display recommendations in 5 columns (skipping the first one as it's the selected book)
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.text(recommended_books[1])
            st.image(poster_url[1])
        
        with col2:
            st.text(recommended_books[2])
            st.image(poster_url[2])
        
        with col3:
            st.text(recommended_books[3])
            st.image(poster_url[3])
        
        with col4:
            st.text(recommended_books[4])
            st.image(poster_url[4])
        
        with col5:
            st.text(recommended_books[5])
            st.image(poster_url[5])
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please make sure all pickle files are present in the 'artifacts' folder.")