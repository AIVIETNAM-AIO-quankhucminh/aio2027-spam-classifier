from .filters import WordScoreFilter, AlwaysNotSpamFilter, NaiveBayesFilter
from .preprocessing import Preprocessor, STOPWORDS, FILLER_WORDS
from .dataset import Email,load_emails, split_emails
from .evaluation import Evaluator
import pandas as pd

"""Run with: uv run python -m spam_classifier.run_experiments"""

EMAIL_DATA_PATH = "data/raw/enron_spam_data.csv"

def build_filters() -> dict:
    """Return {name: detector} for the results table, changing one thing at a time:

    always_not_spam, word_scores, no_stopwords, no_filler_words,
    no_rare_words, word_scores_cleaned, naive_bayes_cleaned.
    """
    preprocessor_keep_all = Preprocessor([])
    preprocessor_no_stopwords = Preprocessor(STOPWORDS)
    preprocessor_no_filler_words = Preprocessor(FILLER_WORDS)
    preprocessor_cleaned = Preprocessor([STOPWORDS, FILLER_WORDS])

    always_not_spam = AlwaysNotSpamFilter()
    word_scores_keep_all = WordScoreFilter(preprocessor_keep_all,0)
    word_scores_no_stopwords = WordScoreFilter(preprocessor_no_stopwords,0)
    word_scores_no_filler_words = WordScoreFilter(preprocessor_no_filler_words,0)
    word_scores_no_rare_words = WordScoreFilter(preprocessor_keep_all, 5)
    word_scores_cleaned = WordScoreFilter(preprocessor_cleaned, 5)
    naive_bayes_cleaned = NaiveBayesFilter(preprocessor_cleaned, 5)

    return {
        "always_not_spam": always_not_spam,
        "word_scores": word_scores_keep_all,
        "no_stopwords": word_scores_no_stopwords,
        "no_filler_words": word_scores_no_filler_words,
        "no_rare_words": word_scores_no_rare_words,
        "word_scores_cleaned": word_scores_cleaned,
        "naive_bayes_cleaned": naive_bayes_cleaned
    }

def run_experiments(filters: dict, train_emails: list, test_emails: list) -> dict:
    """Fit every detector on train_emails and return {name: metrics dict} on test_emails."""
    evaluator = Evaluator(test_emails)
    results = {}
    for name, filter in filters.items():
        filter.fit(train_emails)
        results[name] = evaluator.evaluate(filter)
    return results


def main():
    """Load the emails, split them, run the experiments and print the results table."""
    train_emails, test_emails = split_emails(load_emails(EMAIL_DATA_PATH))
    filters = build_filters()
    results = run_experiments(filters, train_emails, test_emails)
    for name, metrics in results.items():
        print(f"{name}: {metrics}")
