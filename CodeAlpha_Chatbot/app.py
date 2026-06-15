import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Database
faqs = {
    "What is AI?": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",

    "What is Machine Learning?": "Machine Learning is a branch of AI that allows computers to learn from data.",

    "What is Deep Learning?": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",

    "What is NLP?": "NLP stands for Natural Language Processing. It helps computers understand human language.",

    "What is Python?": "Python is a popular programming language used in AI, Machine Learning, and Data Science.",

    "What is Data Science?": "Data Science involves extracting insights and knowledge from data.",

    "What is Computer Vision?": "Computer Vision enables computers to understand and process images and videos.",

    "What is a Chatbot?": "A chatbot is a software application that simulates conversation with users.",

    "What is Streamlit?": "Streamlit is a Python framework used to create web applications quickly.",

    "What is TensorFlow?": "TensorFlow is an open-source deep learning framework developed by Google.",

    "What is PyTorch?": "PyTorch is an open-source machine learning framework developed by Meta.",

    "What is a Neural Network?": "A neural network is a computational model inspired by the human brain.",

    "What is Supervised Learning?": "Supervised Learning uses labeled data to train models.",

    "What is Unsupervised Learning?": "Unsupervised Learning finds patterns in unlabeled data.",

    "What is Reinforcement Learning?": "Reinforcement Learning trains agents through rewards and penalties.",

    "What is Overfitting?": "Overfitting occurs when a model performs well on training data but poorly on new data.",

    "What is Underfitting?": "Underfitting occurs when a model fails to learn patterns from the data.",

    "What is a Dataset?": "A dataset is a collection of related data used for analysis and training models.",

    "What is Big Data?": "Big Data refers to extremely large datasets that require advanced tools for processing.",

    "What is Data Mining?": "Data Mining is the process of discovering useful patterns from large datasets.",

    "What is Feature Engineering?": "Feature Engineering involves creating useful input variables for machine learning models.",

    "What is Classification?": "Classification predicts categories or labels for data.",

    "What is Regression?": "Regression predicts continuous numerical values.",

    "What is Clustering?": "Clustering groups similar data points together.",

    "What is Accuracy?": "Accuracy measures how often a model makes correct predictions.",

    "What is Precision?": "Precision measures the proportion of positive predictions that are correct.",

    "What is Recall?": "Recall measures the proportion of actual positives identified correctly.",

    "What is F1 Score?": "F1 Score combines Precision and Recall into a single metric.",

    "What is Generative AI?": "Generative AI creates new content such as text, images, audio, and videos.",

    "What is ChatGPT?": "ChatGPT is an AI chatbot developed by OpenAI that generates human-like text responses.",

    "What is OpenAI?": "OpenAI is an AI research and deployment company.",

    "What is a Large Language Model?": "A Large Language Model is an AI model trained on vast amounts of text data.",

    "What is Prompt Engineering?": "Prompt Engineering is the practice of designing effective inputs for AI models.",

    "What is Cloud Computing?": "Cloud Computing provides computing resources over the internet.",

    "What is SQL?": "SQL is a language used to manage and query databases.",

    "What is a Database?": "A database is an organized collection of data stored electronically.",

    "What is Automation?": "Automation uses technology to perform tasks with minimal human intervention.",

    "What is Robotics?": "Robotics is the field that deals with designing and operating robots.",

    "What is Edge Computing?": "Edge Computing processes data closer to where it is generated.",

    "What is the Internet of Things?": "The Internet of Things connects physical devices to the internet for communication and data exchange."
}

questions = list(faqs.keys())

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI FAQ Chatbot")
st.write("Ask AI-related questions.")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_question = st.chat_input("Type your question here...")

if user_question:

    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        questions + [user_question]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score < 0.2:
        answer = "❌ Sorry, I don't know the answer to that question."
    else:
        answer = faqs[questions[best_match]]

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])