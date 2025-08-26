A content-based movie recommendation system built with Python and deployed as a Streamlit web app on Render.
This project suggests movies similar to a selected movie based on their textual features (genres, overview, keywords, etc.).

🚀 Features

        📌 Recommends movies similar to a given movie.
        
        📊 Uses TF-IDF / Count Vectorization for text vectorization.
        
        🧠 Powered by scikit-learn for similarity computation.
        
        📂 Stores preprocessed data using pickle for fast loading.
        
        🌐 Interactive web application built with Streamlit.
        
        ☁️ Deployed live using Render.
        
        🛠️ Tech Stack

Python

        Pandas, NumPy – Data manipulation
        
        Scikit-learn – Text vectorization & similarity
        
        NLTK – Natural Language Processing
        
        Pickle – Model/data serialization
        
        Streamlit – Web framework
        
        Render – Cloud deployment
        


Installation & Setup

Clone this repository:

    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system

Install dependencies:

    pip install -r requirements.txt

Run the app locally:

    streamlit run app.py

📂 Project Structure

movie-recommendation-system/
│── app.py                 # Streamlit app
│── movies.pkl             # Preprocessed movies data
│── similarity.pkl         # Precomputed similarity matrix
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

🌍 Deployment
The app is deployed using Render:
https://popcornpicks-ap8j.onrender.com check my movie rec sys 

Screenshots: 
<img width="1488" height="618" alt="Screenshot 2025-08-25 at 3 50 51 PM" src="https://github.com/user-attachments/assets/65b408f4-f68a-4753-9836-6fa15710b5b2" />

<img width="1433" height="782" alt="Screenshot 2025-08-26 at 9 48 32 AM" src="https://github.com/user-attachments/assets/817f0d07-0173-4a35-b283-bf33038469a8" />


