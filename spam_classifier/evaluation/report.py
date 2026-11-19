def dataset_stats(emails: list) -> dict:
    """Return a dict with num_emails, num_spam, num_not_spam and num_empty_messages."""
    raise NotImplementedError


def top_words(counts: dict, k: int = 20) -> list:
    """Return the k words with the highest counts, as (word, count) pairs."""
    raise NotImplementedError


def results_table(results: dict) -> list:
    """Turn {detector name: metrics dict} into a list of rows, one dict per detector."""
    raise NotImplementedError
