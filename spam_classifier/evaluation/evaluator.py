class Evaluator:
    """Scores every detector on the same labelled test emails."""

    def __init__(self, test_emails: list):
        raise NotImplementedError

    def evaluate(self, spam_filter) -> dict:
        """Run spam_filter.predict on every test email and return compute_metrics(...)."""
        raise NotImplementedError

    def compute_metrics(self, actual: list, predicted: list) -> dict:
        """Return a dict with accuracy, precision, recall, f1, tp, fp, fn and tn.

        Spam (True) is the positive class. If a division would be by 0, use 0.0.
        """
        raise NotImplementedError
