import streamlit as st

@st.cache_resource
def load_detectors() -> tuple:
    """Return (word_filter, bayes_filter): the cleaned WordScoreFilter and NaiveBayesFilter.

    Load the CSV, split it like run_experiments, and fit both on the train emails.
    """
    raise NotImplementedError


def show_demo(word_filter, bayes_filter):
    """Let the user paste a subject and an email body, then show:

    - each detector's verdict (spam / not spam) and its confidence
    - the email's top spam words, from word_filter.top_spam_words

    Confidence is the spam score (word_filter.score or bayes_filter.spam_probability)
    for a spam verdict, and 1 minus that score for a not-spam verdict.
    """
    raise NotImplementedError


def show_report():
    """Run the experiments, then show dataset stats, top words, confusion matrix and the results table."""
    raise NotImplementedError


st.title("Spam Classifier")

# TODO: call show_demo(*load_detectors()) and show_report() once implemented.
