import nltk
import PyPDF2
from nltk.corpus import stopwords
import math


# nltk.download('punkt')


def extract_text_from_cv(cv_file):
    pdf = PyPDF2.PdfReader(cv_file)  # Read the PDF file
    text = ''
    for page in pdf.pages:
        text += page.extract_text()  # Extract the text from each page

    return text


def preprocess_text(text):
    tokens = nltk.word_tokenize(text)  # Tokenize the text
    stop_words = set(stopwords.words('english'))  # Get a set of English stop words
    filtered_tokens = [token for token in tokens if
                       token.lower() not in stop_words and token.isalnum()]  # Remove stop words and non
    # alphanumeric tokens
    return filtered_tokens


def calculate_match_percentage(job_seeker, job_description):
    # code for calculating the match percentage
    cv_text = extract_text_from_cv(job_seeker)  # Extract text from CV
    job_description_text = job_description  # Extract text from the job description
    cv_tokens = preprocess_text(cv_text)  # Tokenize the CV text
    job_description_tokens = preprocess_text(job_description_text)
    cv_fd = nltk.FreqDist(cv_tokens)  # Calculate the frequency distribution of the CV tokens
    job_description_fd = nltk.FreqDist(
        job_description_tokens)  # Calculate the frequency distribution of the job description
    common_words = set(cv_fd).intersection(
        set(job_description_fd))  # Find the common words between the frequency distributions
    match_percentage = math.ceil((len(common_words) / len(job_description_fd))*100) # Calculate the match, Rounded Up
    # to the nearest whole number
    return match_percentage
