import math
import unittest

from spam_classifier.filters.naive_bayes_filter import NaiveBayesFilter
from spam_classifier.preprocessing.preprocessor import Preprocessor
from worked_example import make_new_email, make_train_emails


class NaiveBayesFilterTest(unittest.TestCase):
    def test_worked_example(self):
        spam_filter = NaiveBayesFilter(Preprocessor([]))
        spam_filter.fit(make_train_emails())

        # P(word | class) for: free, money, your, meeting ("for" is skipped).
        spam = (4 / 25) * (3 / 25) * (2 / 25) * (1 / 25)
        normal = (1 / 24) * (1 / 24) * (2 / 24) * (3 / 24)
        self.assertAlmostEqual(spam_filter.log_odds(make_new_email()), math.log(spam / normal))
        self.assertTrue(spam_filter.predict(make_new_email()))

    def test_spam_probability(self):
        spam_filter = NaiveBayesFilter(Preprocessor([]))
        spam_filter.fit(make_train_emails())

        # P(spam) = P(normal) = 0.5, so the priors cancel out (about 77%).
        spam = (4 / 25) * (3 / 25) * (2 / 25) * (1 / 25)
        normal = (1 / 24) * (1 / 24) * (2 / 24) * (3 / 24)
        self.assertAlmostEqual(
            spam_filter.spam_probability(make_new_email()), spam / (spam + normal)
        )
