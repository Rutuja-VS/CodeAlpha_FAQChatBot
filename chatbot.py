import pandas as pd
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stopwords.words("english")]
    return " ".join(filtered_words)


data = pd.read_csv("placement_career_faqs.csv")
data["processed_question"] = data["Question"].apply(preprocess_text)

vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
question_vectors = vectorizer.fit_transform(data["processed_question"])


# Chatbot function
def get_response(user_input):
    career_keywords = [
        "placement","placements","resume","cv","interview", "interviews","career","job","jobs","company",
        "companies", "aptitude", "technical","hr","salary", "internship", "campus", "fresher", "skills", "engineering",
        "linkedin", "offer", "offer letter", "recruitment", "communication", "higher studies", "masters", "mtech", "mba", "data science",
        "software engineer", "developer", "coding", "dsa",  "study", "preparation","placement drive", "career growth", "work", "role",
        "industry","consulting","product based","service based"
    ]

    if not any(word in user_input.lower() for word in career_keywords):
        return "Please ask career or placement related questions."
    processed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([processed_input])
    similarity = cosine_similarity(input_vector, question_vectors)
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    if best_score < 0.3:
        return "Sorry, I couldn't find a relevant answer. Please ask placement, interview, resume, or career related questions."

    response = data.iloc[best_match_index]["Answer"]

    return response
