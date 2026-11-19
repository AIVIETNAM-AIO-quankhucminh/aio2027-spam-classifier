class NaiveBayesFilter:
    """Detector 3: the same word counts, combined as probabilities."""

    def __init__(self, preprocessor, min_count: int = 1):
        """Words seen fewer than min_count times in training are ignored."""
        raise NotImplementedError

    def fit(self, emails: list):
        """Count each word in spam and in normal training emails, and count the emails.

        Store the word counts in two dicts: self.spam_counts and self.normal_counts.
        """
        raise NotImplementedError

    def log_odds(self, email) -> float:
        """Return the spam log score minus the normal log score, using +1 smoothing.

        Skip words seen in neither class.
        """
        raise NotImplementedError

    def predict(self, email) -> bool:
        """Return True (spam) when log_odds(email) > 0."""
        raise NotImplementedError

    def spam_probability(self, email) -> float:
        """Return how likely the email is spam, from 0.0 to 1.0: 1 / (1 + e^(-log_odds))."""
        raise NotImplementedError
