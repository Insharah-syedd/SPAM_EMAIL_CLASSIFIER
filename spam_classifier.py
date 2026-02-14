import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Create 'models' folder if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

def train_model():
    print("--- Loading Dataset ---")
    # Load the dataset (ensure spam.csv is in the main folder)
    try:
        df = pd.read_csv('spam.csv', encoding='latin-1')
    except FileNotFoundError:
        print("Error: 'spam.csv' not found. Please place it in the project folder.")
        return

    # Keep only relevant columns and rename them
    df = df[['v1', 'v2']]
    df.columns = ['label', 'text']

    print("--- Preprocessing & Vectorization ---")
    # Convert text to numbers using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    X = tfidf.fit_transform(df['text'])
    y = df['label']

    # Split data: 80% for training, 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("--- Training the Brain (Logistic Regression) ---")
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nDetailed Report:\n", classification_report(y_test, predictions))

    # Save the 'Brain' and 'Translator'
    joblib.dump(model, 'models/spam_model.pkl')
    joblib.dump(tfidf, 'models/tfidf_vectorizer.pkl')
    print("\nDONE! Files saved in the 'models' folder.")

if __name__ == "__main__":
    train_model()