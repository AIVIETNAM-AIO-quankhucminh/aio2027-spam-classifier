from spam_classifier.dataset.email_message import Email
from spam_classifier.filters.always_not_spam_filter import AlwaysNotSpamFilter
from spam_classifier.filters.word_score_filter import WordScoreFilter
from spam_classifier.filters.naive_bayes_filter import NaiveBayesFilter
import numpy as np

class Evaluator:
    """Scores every detector on the same labelled test emails."""

    def __init__(self, test_emails: list[Email]):
        self.test_emails = test_emails
        # Extract the actual labels (True for spam, False for not spam)
        self.actual = np.array([e.is_spam for e in test_emails], dtype=bool)

    def evaluate(self, spam_filter) -> dict:
        """Run spam_filter.predict on every test email and return compute_metrics(...)."""
        # Check if the spam_filter is not empty and is an instance of the expected classes
        if spam_filter is None:
            raise ValueError("spam_filter cannot be None")
        if not isinstance(spam_filter, (AlwaysNotSpamFilter, WordScoreFilter, NaiveBayesFilter)):
            raise ValueError("Invalid spam filter for evaluation")

        # Get predictions from the spam filter
        predicted = np.array([spam_filter.predict(email) for email in self.test_emails], dtype=bool)
        # Compute and return the evaluation metrics
        return self.compute_metrics(self.actual, predicted)

    def compute_metrics(self, actual: np.ndarray, predicted: np.ndarray) -> dict:
        """Return a dict with accuracy, precision, recall, f1, tp, fp, fn and tn.

        Spam (True) is the positive class. If a division would be by 0, use 0.0.
        """
        # Calculate true positives, false positives, false negatives, and true negatives
        tp = np.sum(actual & predicted)
        fp = np.sum(~actual & predicted)
        fn = np.sum(actual & ~predicted)
        tn = np.sum(~actual & ~predicted)

        # Calculate precision, recall, accuracy, and F1 score with checks to avoid division by zero
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0.0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "tn": tn
        }
