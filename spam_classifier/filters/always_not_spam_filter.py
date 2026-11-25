class AlwaysNotSpamFilter:
    """Detector 0: the baseline every other detector must beat.

    Like every detector, it has fit(emails) and predict(email).
    """

    def fit(self, emails: list):
        """Nothing to learn."""
        pass

    def predict(self, email) -> bool:
        """Always return False (not spam)."""
        return False
