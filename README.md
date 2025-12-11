🎬 Movie Recommendation System — Streamlit Web Application

A production-ready Movie Recommendation System built using Machine Learning, Python, and a modern Netflix-style Streamlit UI.
This application recommends movies based on similarity scores using content-based filtering and displays high-quality posters using the TMDB API.

🚀 Project Overview

This project recommends movies based on similarity between movie metadata such as genres, cast, crew, keywords, and overview.
Using CountVectorizer + Cosine Similarity, the model identifies movies that are closest to the user's selected title and displays them in a clean, UI-rich Netflix-like interface.

🛠 Tech Stack

| Category     | Technologies                                  |
| ------------ | --------------------------------------------- |
| Language     | Python                                        |
| Framework    | Streamlit                                     |
| ML Libraries | scikit-learn, pandas, numpy                   |
| Model Assets | CountVectorizer, Cosine Similarity            |
| Deployment   | Streamlit Cloud / Render / HuggingFace Spaces |
| UI Theme     | Custom Netflix-style interface                |

📂 Project Structure

📦 Movie_Recommendation_System
│
├── app.py                     
├── Model_files/
│   ├── movies_list.pkl        
│   └── similarity.pkl         
│
├── requirements.txt           
├── README.md                  

🔧 Installation & Setup

1️⃣ Clone the Repository

2️⃣ Create Virtual Environment

conda create -n mrenv python=3.10
conda activate mrenv

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

📬 Contact

Sivaranjan g
📧 Email: sivaranjanguna@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/sivaranjang
