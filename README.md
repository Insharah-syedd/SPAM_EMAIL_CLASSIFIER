## Email Detector Pro
Enterprise-Grade Email Security Analysis Dashboard
Email Detector Pro is an advanced, AI-driven security tool designed to classify electronic communications into Spam or Ham (Safe) with high precision. Built using a robust Machine Learning pipeline and a cutting-edge "Cyber-Aura" dashboard, it provides real-time threat intelligence for communication safety.

## LIVE DEMO  https://spamemaildetectorinsharah.streamlit.app/
## Key Features
Pattern Recognition Engine: Leverages a Multinomial Naive Bayes algorithm optimized for high-dimensional text data.

High-Fidelity UI: An ultra-responsive, dark-mode dashboard featuring glassmorphism and neon-glow status indicators.

Probability Metrics: Delivers granular insights via "Threat Level" and "Trust Score" metrics.

Asynchronous Processing: Integrated visual feedback (spinners) to simulate deep-engine neural analysis.

Responsive Architecture: Fully adapted for desktop and professional monitoring screens.

## Technical Stack
Language: Python 3.x

Framework: Streamlit (Advanced Web UI)

Machine Learning: Scikit-Learn

Data Persistence: Joblib (Model Serialization)

Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency)

Styling: Custom CSS3 with Google Font "Plus Jakarta Sans"

## Repository Structure
```Plaintext
├── models/
│   ├── spam_model.pkl        # Pre-trained Classification Model
│   └── tfidf_vectorizer.pkl  # Fitted Feature Extraction Object
├── app.py                    # Main Application Entry Point
├── requirements.txt          # Production Dependency Manifest
└── README.md                 # Project Documentation
```
## Installation & Usage
Follow these steps to deploy the system locally:

Clone the Repository

```Bash
git clone https://github.com/your-username/Email-Detector-Pro.git
cd Email-Detector-Pro
```
Initialize Virtual Environment (Optional but Recommended)

```Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
```
```Bash
pip install -r requirements.txt
```
Launch the Application

```...Bash
streamlit run app.py
```

⚙️ How It Works
The system operates through a three-stage pipeline:

Feature Extraction: Raw email text is processed through a TF-IDF vectorizer to calculate the importance of specific keywords.

Inference Engine: The vectorized input is fed into the Naive Bayes model to calculate the log-probability of classes.

Visual Reporting: Results are rendered via a custom CSS dashboard, displaying the malicious risk probability versus secure integrity score.

🛡️ License
Distributed under the MIT License. See LICENSE for more information.


Developed with precision by INSHARAH SYED

