class WordScoreFilter:
    """Detectors 1 and 2: learned word scores.

    The preprocessor and min_count decide which detector this is.
    """

    def __init__(self, preprocessor, min_count: int = 1):
        """Words seen fewer than min_count times in training are ignored."""
        raise NotImplementedError

    def fit(self, emails: list):
        """Count each word in spam and in normal training emails.

        Store the counts in two dicts: self.spam_counts and self.normal_counts.
        """
        raise NotImplementedError

    def score(self, email) -> float:
        """Return the average word score. Skip unknown words. Return 0.0 if none are known."""
        raise NotImplementedError

    def predict(self, email) -> bool:
        """Return True (spam) when score(email) > 0.5."""
        raise NotImplementedError


    def top_spam_words(self, email, k: int = 5) -> list:
        """Return the email's k known words with the highest scores, as (word, score) pairs."""
        raise NotImplementedError
