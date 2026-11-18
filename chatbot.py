import json
import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQ_PATH = Path(__file__).parent / "data" / "faqs.json"

with FAQ_PATH.open(encoding="utf-8") as file:
    FAQS = json.load(file)

# Each FAQ entry has several example questions. We compare a user's
# question with these examples using TF-IDF and cosine similarity.
examples = []
answers = []

for item in FAQS:
    for question in item["questions"]:
        examples.append(question)
        answers.append(item["answer"])

vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True)
faq_matrix = vectorizer.fit_transform(examples)

def clean_text(text):
    """Basic text normalization; NLTK can be added for richer NLP."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return re.sub(r"\s+", " ", text)

def get_response(user_message):
    message = clean_text(user_message)

    if not message:
        return "Please type a question so I can help."

    greetings = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}
    if message in greetings:
        return "Hello! I'm ChatMate AI. Ask me about our services, account, payments, or support."

    if message in {"bye", "goodbye", "see you"}:
        return "Goodbye! Thanks for chatting with ChatMate AI."

    user_vector = vectorizer.transform([message])
    scores = cosine_similarity(user_vector, faq_matrix)[0]
    best_index = scores.argmax()
    best_score = float(scores[best_index])

    # A conservative threshold avoids confidently returning unrelated answers.
    if best_score < 0.18:
        return (
            "I'm not fully sure I understood that. Could you rephrase your question? "
            "You can ask about account help, payments, services, or contacting support."
        )

    return answers[best_index]
