import joblib
import os

def load_system():
    # Load the saved model and vectorizer
    try:
        model = joblib.load('models/spam_model.pkl')
        tfidf = joblib.load('models/tfidf_vectorizer.pkl')
        return model, tfidf
    except FileNotFoundError:
        print("Error: Trained model files not found. Run 'spam_classifier.py' first!")
        return None, None

def start_interactive_menu():
    model, tfidf = load_system()
    if not model: return

    print("\n" + "="*50)
    print("      EMAIL SPAM CLASSIFICATION SYSTEM")
    print("="*50)
    print("Type 'exit' to close the program.")

    while True:
        user_input = input("\nEnter email text to classify: ").strip()

        if user_input.lower() == 'exit':
            print("Shutting down... Goodbye!")
            break
        
        if not user_input:
            continue

        # Convert user text into numbers
        transformed_input = tfidf.transform([user_input])

        # Get Prediction and Probabilities
        prediction = model.predict(transformed_input)[0]
        probabilities = model.predict_proba(transformed_input)[0]
        
        # In Scikit-Learn, usually index 0 is 'ham' and index 1 is 'spam'
        # but it depends on your dataset labels alphabet order.
        classes = model.classes_
        ham_idx = 0 if classes[0] == 'ham' else 1
        spam_idx = 1 if classes[1] == 'spam' else 0

        ham_prob = probabilities[ham_idx] * 100
        spam_prob = probabilities[spam_idx] * 100

        # Display Results
        print("\n" + "-"*30)
        print(f"CLASSIFICATION: {prediction.upper()}")
        print(f"Ham Confidence: {ham_prob:.2f}%")
        print(f"Spam Confidence: {spam_prob:.2f}%")
        
        if prediction == 'spam':
            print("🚨 ALERT: This email looks like SPAM!")
        else:
            print("✅ This email seems safe (HAM).")
        print("-"*30)

if __name__ == "__main__":
    start_interactive_menu()