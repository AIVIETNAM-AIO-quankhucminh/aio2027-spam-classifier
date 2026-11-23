import datetime
class Email:
    """One email: a subject, a message and a spam label.

    For an email pasted into the demo the label is unknown, so leave is_spam as False.
    """

    def __init__(self, subject: str, message: str, is_spam: bool = False, date: str = ""):
        self.subject = subject
        self.message = message
        self.is_spam = is_spam
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d") if date else None

    def get_text(self) -> str:
        """Return the subject and message joined by a space."""
        return f"{self.subject} {self.message}"
