"""Run with: uv run python -m spam_classifier.run_experiments"""


def build_filters() -> dict:
    """Return {name: detector} for the results table, changing one thing at a time:

    always_not_spam, word_scores, no_stopwords, no_filler_words,
    no_rare_words, word_scores_cleaned, naive_bayes_cleaned.
    """
    raise NotImplementedError


def run_experiments(train_emails: list, test_emails: list) -> dict:
    """Fit every detector on train_emails and return {name: metrics dict} on test_emails."""
    raise NotImplementedError


def main():
    """Load the emails, split them, run the experiments and print the results table."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
