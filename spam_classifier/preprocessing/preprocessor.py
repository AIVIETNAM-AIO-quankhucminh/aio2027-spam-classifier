class Preprocessor:
    """Turns an email into the list of words a filter sees."""

    def __init__(self, removed_words: list):
        """removed_words: words to drop, such as STOPWORDS. Pass [] to keep every word."""
        raise NotImplementedError

    def tokenize(self, email) -> list:
        """Lowercase the email's text, split it into words, and drop removed words."""
        raise NotImplementedError
