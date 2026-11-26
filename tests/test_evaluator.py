import unittest

from sklearn import metrics
import numpy as np

from spam_classifier.evaluation.evaluator import Evaluator


class EvaluatorTest(unittest.TestCase):
    def test_metrics_match_sklearn(self):
        actual = [True, True, True, False, False]
        predicted = [True, False, True, True, False]

        result = Evaluator([]).compute_metrics(actual, predicted)

        self.assertEqual(result["tp"], 2)
        self.assertEqual(result["fp"], 1)
        self.assertEqual(result["fn"], 1)
        self.assertEqual(result["tn"], 1)
        self.assertAlmostEqual(result["accuracy"], metrics.accuracy_score(actual, predicted))
        self.assertAlmostEqual(result["precision"], metrics.precision_score(actual, predicted))
        self.assertAlmostEqual(result["recall"], metrics.recall_score(actual, predicted))
        self.assertAlmostEqual(result["f1"], metrics.f1_score(actual, predicted))

    def test_no_spam_predicted_gives_zero_precision(self):
        actual = [True, False, False]
        predicted = [False, False, False]

        result = Evaluator([]).compute_metrics(actual, predicted)

        self.assertEqual(result["precision"], 0.0)
        self.assertEqual(result["recall"], 0.0)
        self.assertEqual(result["f1"], 0.0)
