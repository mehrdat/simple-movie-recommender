# Movie Recommendation System

This project is a **simple movie recommendation system** developed in Python. It allows users to get movie recommendations based on their preferences, utilizing a minimal yet effective approach. The application is built using **Streamlit** to provide an intuitive web interface.

The Streamlit app address: 
https://simplemoviereco.streamlit.app/

## Features
- Recommends movies based on the user's input
- Lightweight and easy to use
- Interactive and fast interface with Streamlit

## Libraries Used
The main libraries used for the project are:
- **Streamlit**: For building the web interface.
- **Pandas**: To handle and manipulate the data.
- **Scikit-learn**: For implementing the recommendation logic.
- **Fuzzywuzzy**: To improve matching of user inputs.
- **Seaborn & Matplotlib**: For visualizations.

You can find the full list of required packages in the `requirements.txt` file.

- **`app.py`**: This is the entry point of the application, where the Streamlit interface is created, and recommendations are displayed.
- **`data.py`**: Handles data loading, cleaning, and any preprocessing needed.
- **`utils.py`**: Contains helper functions for the recommendation algorithm, such as filtering and calculating similarity scores.

## Screenshot
<div style="text-align: center;">
    <img src="/img/app.jpg" alt="App Image" style="width: 50%; height: auto;">
    <img src="/img/app2.jpg" alt="App Image" style="width: 50%; height: auto;">
</div>

## How to Run

1. Install the required dependencies:

```bash
pip install -r requirements.txt


streamlit run app.py

```

## Code Structure
```plaintext
movie-recommendation/
│
├── app.py           # Main script to run the Streamlit app
├── data.py          # Script for handling movie dataset
├── utils.py         # Helper functions used for recommendation logic
├── requirements.txt # Required Python libraries
└── README.md        # Project documentation