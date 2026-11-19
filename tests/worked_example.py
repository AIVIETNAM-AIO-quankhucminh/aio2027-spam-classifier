"""The worked example from the proposal."""

from spam_classifier.dataset.email_message import Email


def make_train_emails():
    return [
        Email("", "win free money now", True),
        Email("", "free prize win", True),
        Email("", "claim your free money", True),
        Email("", "meeting at noon", False),
        Email("", "send the report now", False),
        Email("", "your meeting notes", False),
    ]


def make_new_email():
    return Email("", "free money for your meeting")
