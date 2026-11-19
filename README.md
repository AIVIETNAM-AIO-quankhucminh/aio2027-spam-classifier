# AIO2027 Spam Classifier

## Setup

```bash
uv sync
```

## Data

Download the
[Enron-Spam CSV](https://www.kaggle.com/datasets/marcelwiechmann/enron-spam-data/data)
and save it as `data/raw/enron_spam_data.csv`. Git ignores `data/raw/`.
The experiments and the Streamlit demo both read this file.

## Run

```bash
uv run streamlit run app.py
uv run python -m spam_classifier.run_experiments
```

## Test

```bash
uv run python -m unittest discover -s tests
```
