from dataclasses import dataclass
@dataclass
class Email:
    subject: str
    message: str
    is_spam: bool

    def get_text(self):
        return self.subject  + ' '+ self.message

email1 = Email(
    "Free Money",
    "Get free money now",
    True
)
print(email1.subject)
print(email1.message)
print(email1.get_text())

import csv

with open(file, encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

