import unittest

from spam_classifier.dataset.email_message import Email
from spam_classifier.preprocessing.preprocessor import Preprocessor
from spam_classifier.preprocessing.word_lists import FILLER_WORDS, STOPWORDS

class PreprocessorTest(unittest.TestCase):
    def test_lowercase_and_split_separators(self):
        email = Email("HELLO, Team!", "Win money.\nClaim\tNOW?")

        words = Preprocessor([]).tokenize(email)

        self.assertEqual(
            words,
            ["hello", "team", "win", "money", "claim", "now"],
        )

    def test_removed_words_are_dropped(self):
        email = Email("The prize", "is for YOU")

        words = Preprocessor(["the", "is", "for"]).tokenize(email)

        self.assertEqual(words, ["prize", "you"])

    def test_empty_removal_list_keeps_every_word(self):
        email = Email("The prize", "is for you")

        words = Preprocessor([]).tokenize(email)

        self.assertEqual(words, ["the", "prize", "is", "for", "you"])

    def test_empty_email(self):
        email = Email("", "")

        self.assertEqual(Preprocessor([]).tokenize(email), [])

    def test_repeated_words_are_preserved(self):
        email = Email("FREE", "free money money")

        words = Preprocessor([]).tokenize(email)

        self.assertEqual(words, ["free", "free", "money", "money"])

    def test_numbers_apostrophes_and_email_addresses(self):
        email = Email("", "Don't pay 100. Email alice@example.com")

        words = Preprocessor([]).tokenize(email)

        self.assertEqual(
            words,
            ["don't", "pay", "100", "email", "alice", "example", "com"],
        )

    def test_removed_words_are_stored_as_set(self):
        preprocessor = Preprocessor(["the", "and", "the"])

        self.assertIsInstance(preprocessor.removed_words, set)
        self.assertEqual(preprocessor.removed_words, {"the", "and"})

    def test_stopwords_are_unique_lowercase_words(self):
        self.assertTrue(STOPWORDS)
        self.assertEqual(len(STOPWORDS), len(set(STOPWORDS)))

        for word in STOPWORDS:
            self.assertTrue(word.isalpha())
            self.assertEqual(word, word.lower())

        self.assertTrue({"the", "and", "of"}.issubset(set(STOPWORDS)))

    def test_filler_words_stay_empty(self):
        self.assertEqual(FILLER_WORDS, [])



    