def load_emails(path: str) -> list:
    """Read a CSV file and return a list of Email objects.

    Treat an empty message as "". Drop duplicate emails.
    """
    raise NotImplementedError


def save_emails(emails: list, path: str):
    """Write emails to a CSV file that load_emails can read."""
    raise NotImplementedError


def split_emails(emails: list, test_ratio: float = 0.2, seed: int = 42) -> tuple:
    """Shuffle with the seed, then return (train_emails, test_emails).

    The same seed always gives the same split.
    """
    raise NotImplementedError

