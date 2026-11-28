import re
from spam_classifier.dataset.email_message import Email

class Preprocessor:
    """Turns an email into the list of words a filter sees."""

    def __init__(self, removed_words: list[str]):
        """removed_words: words to drop, such as STOPWORDS. Pass [] to keep every word."""
        self.removed_words = set(removed_words)


    def tokenize(self, email: Email) -> list[str]:
        """Return lowercase tokens, excluding removed words.

        A token is a maximal run of ASCII letters a-z, digits 0-9,
        or straight apostrophes. Numbers are kept. Email addresses
        split at punctuation such as @ and dots. Order and repeated
        tokens are preserved.
        """
        text = email.get_text().lower()
        words = re.findall(r"[a-z0-9']+", text)
        result = []
        for word in words:
            if word not in self.removed_words:
                result.append(word)
        return result

