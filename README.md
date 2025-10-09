# 📚 Books Recommender System

A collaborative filtering-based book recommendation system built with Python and Streamlit. This application uses K-Nearest Neighbors (KNN) algorithm to suggest books similar to a user's selection based on user ratings data.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange.svg)

## 🎯 Features

- **Collaborative Filtering**: Recommendations based on user rating patterns
- **Interactive UI**: Clean and intuitive Streamlit interface
- **Visual Recommendations**: Displays book covers for recommended titles
- **Real-time Suggestions**: Get 5 book recommendations instantly
- **Large Dataset**: Trained on Book-Crossing dataset with thousands of books and ratings

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** - Web application framework
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning (KNN algorithm)
- **Pickle** - Model serialization

## 📁 Project Structure

```
Books Recommender Project/
│
├── app.py                      # Main Streamlit application
├── research.ipynb              # Jupyter notebook for EDA and model training
├── requirements.txt            # Project dependencies
│
├── artifacts/                  # Serialized models and data
│   ├── model.pkl              # Trained KNN model
│   ├── book_names.pkl         # List of book titles
│   ├── book_pivot.pkl         # Pivot table of user-book ratings
│   └── final_rating.pkl       # Processed ratings with metadata
│
├── Datasets/                   # Raw datasets (Book-Crossing)
│   ├── BX-Books.csv           # Book information
│   ├── BX-Users.csv           # User information
│   └── BX-Book-Ratings.csv    # User ratings
│
└── env/                        # Virtual environment (not tracked in git)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Books Recommender Project"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   # source env/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure artifacts folder exists**
   Make sure the `artifacts/` folder contains all the required pickle files:
   - `model.pkl`
   - `book_names.pkl`
   - `book_pivot.pkl`
   - `final_rating.pkl`

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   The application will automatically open in your default browser at `http://localhost:8501`

3. **Use the application**
   - Select a book from the dropdown menu
   - Click "Show Recommendation"
   - View 5 similar book recommendations with cover images

## 📊 How It Works

### Collaborative Filtering Approach

1. **Data Preprocessing**: 
   - Loads Book-Crossing dataset containing books, users, and ratings
   - Filters users with significant rating history
   - Filters popular books with sufficient ratings
   - Creates a user-book rating matrix

2. **Model Training**:
   - Uses K-Nearest Neighbors (KNN) algorithm
   - Calculates similarity between books based on user rating patterns
   - Books rated similarly by the same users are considered similar

3. **Recommendation Generation**:
   - Takes a selected book as input
   - Finds the 6 nearest neighbors (including the input book)
   - Returns 5 most similar books with cover images

### Algorithm Details

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Similarity Metric**: Cosine similarity / Euclidean distance
- **Number of Neighbors**: 6 (returns 5 recommendations)
- **Approach**: User-Item Collaborative Filtering

## 📈 Dataset

The project uses the **Book-Crossing Dataset**, which contains:
- **Books**: 271,360 books with metadata (ISBN, title, author, publisher, etc.)
- **Users**: 278,858 users (anonymized)
- **Ratings**: 1,149,780 ratings (scale 0-10)

**Dataset Source**: [Book Recommendation Dataset on Kaggle](https://www.kaggle.com/datasets/ra4u12/bookrecommendation)

*Original Source: Book-Crossing dataset collected by Cai-Nicolas Ziegler*

## 🔧 Model Training

To retrain the model or explore the data analysis process:

1. Open `research.ipynb` in Jupyter Notebook or VS Code
2. Run all cells sequentially
3. The notebook will:
   - Load and explore the datasets
   - Perform data cleaning and preprocessing
   - Create the user-item matrix
   - Train the KNN model
   - Save artifacts to the `artifacts/` folder

## 📝 Key Functions

### `recommend_book(book_name)`
- **Input**: Book title (string)
- **Output**: List of recommended books and their poster URLs
- **Process**: Finds nearest neighbors using KNN model

### `fetch_poster(suggestion)`
- **Input**: Book indices from KNN suggestions
- **Output**: List of poster/cover image URLs
- **Process**: Maps book indices to image URLs from dataset

## 🎨 User Interface

The Streamlit interface includes:
- Clean header with emoji icon
- Descriptive subtitle and methodology info
- Searchable dropdown for book selection
- Recommendation button
- 5-column grid layout for displaying results
- Book titles and cover images for each recommendation
- Error handling with user-friendly messages

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:
- Report bugs and issues
- Suggest new features or improvements
- Improve documentation
- Add new recommendation algorithms
- Enhance the UI/UX

## 📄 License

This project is open-source and available for educational purposes.

## 🙏 Acknowledgments

- **Book-Crossing Dataset** - For providing the comprehensive books and ratings data
- **Streamlit** - For the excellent web framework
- **Scikit-learn** - For machine learning tools

## � Author

**Vineet Patel**
- �📧 Email: vineetpatel468@gmail.com
- 💻 GitHub: [@vineet416](https://github.com/vineet416)
- 🔗 LinkedIn: [@vineet416](https://www.linkedin.com/in/vineet416/)

## 📧 Contact

For questions or feedback, please open an issue in the repository or reach out via email.

---

**Note**: Make sure to have all pickle files generated before running the app. Run the `research.ipynb` notebook first to generate these files if they don't exist.

---

⭐ If you found this project helpful, please give it a star!