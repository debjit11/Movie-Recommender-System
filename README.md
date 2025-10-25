# Movie Recommender System 🎬

**A simple, easy-to-run movie recommendation system built using the TMDB 5000 Movies dataset.**

---

## Table of Contents

* [About](#about)
* [Features](#features)
* [Repository Structure](#repository-structure)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Dataset](#dataset)
* [Run / Usage](#run--usage)
* [How the Recommender Works (high level)](#how-the-recommender-works-high-level)
* [Retrain / Rebuild](#retrain--rebuild)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [Acknowledgements](#acknowledgements)

---

## About

This repository contains a movie recommender system built using the **TMDB 5000 Movies dataset**. It includes a Jupyter notebook with the full pipeline (data load → preprocess → feature engineering → model/similarity creation) and a lightweight `app.py` to demo the model as an interactive app.

> Quick note: a preprocessed file `movies.pkl` is included so you can run the demo without downloading or preprocessing the full dataset.

## Features

* Content-based / hybrid-style recommender (metadata + text features).
* Jupyter notebook walkthrough (`main.ipynb`) showing preprocessing and similarity computations step-by-step.
* Lightweight demo application (`app.py`) so non-technical users can try the recommender.
* `movies.pkl` — preprocessed dataset for quick start.

## Repository Structure

```
Movie-Recommender-System/
├─ .gitignore
├─ app.py              # Demo app (Flask/Streamlit/Script — run with `python app.py`)
├─ main.ipynb          # Notebook: full data processing & model building
├─ movies.pkl          # Preprocessed DataFrame used by the app
├─ requirements.txt    # Python dependencies
```

## Prerequisites

* Python 3.8+ recommended
* Git
* (Optional) Jupyter / JupyterLab for running the notebook interactively

## Installation

Follow these commands to clone and set up the project locally.

```bash
# 1. Clone the repo
git clone https://github.com/debjit11/Movie-Recommender-System.git
cd Movie-Recommender-System

# 2. Create and activate a virtual environment (recommended)
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Dataset

This project was built using the **TMDB 5000 Movies** dataset (commonly available on Kaggle). Two options:

1. **Quick start:** Use the included `movies.pkl` (already preprocessed) — nothing else needed.
2. **Full reproduction:** Download the TMDB 5000 dataset (CSV) from Kaggle or your source, place the CSV files in a `data/` folder, and run the preprocessing cells in `main.ipynb` to regenerate `movies.pkl`.

**Notes**:

* If you re-generate `movies.pkl`, the demo will automatically use the new file the next time you run `app.py`.
* When downloading from Kaggle, you may need a Kaggle account and to accept dataset rules.

## Run / Usage

### 1) Run the Jupyter Notebook (explore & retrain)

```bash
jupyter notebook main.ipynb
# or jupyter lab
```

Open the notebook and run cells in order. The notebook contains clear sections for:

* Loading raw CSVs
* Cleaning and extracting relevant fields (cast, crew, keywords, genres)
* Vectorizing text features
* Computing similarity matrix
* Saving `movies.pkl`

### 2) Run the demo app

There are multiple ways the app might be executed depending on how `app.py` is implemented. Try these in order:

```bash

# the app is a Streamlit app
streamlit run app.py

```

Open the printed URL in your browser ([http://localhost:8501](http://localhost:8501) for Streamlit).

## How the Recommender Works (high level)

* The notebook builds a combined textual feature for each movie (e.g. `genres`, `keywords`, `cast`, `crew`).
* Text features are vectorized (CountVectorizer / TF-IDF) and similarities are computed (usually cosine similarity).
* Given a movie input, the system finds the nearest neighbours in the similarity space and returns those titles as recommendations.
* `movies.pkl` typically contains the processed DataFrame and any helper mappings (title → index, etc.).

## Retrain / Rebuild

If you want to rebuild everything from scratch (recommended when you change preprocessing):

1. Place original TMDB CSV files into `data/` (or edit the `main.ipynb` paths).
2. Open and run the notebook from top to bottom.
3. When the notebook finishes, it will save a fresh `movies.pkl`.
4. Restart the demo app so it picks up the new `movies.pkl`.

## Troubleshooting

* **Missing packages / import errors**: Make sure the virtualenv is activated and `pip install -r requirements.txt` completed without errors.
* **`movies.pkl` not found**: Ensure the file exists in repo root or run the preprocessing in `main.ipynb` to create it.
* **App won’t start**: Check the console for stack traces. Common problems: port already in use, missing environment variables, or mismatched dependency versions.

## Contributing

Contributions are welcome! Suggested workflow:

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make changes and add tests / documentation
4. Open a pull request


## Acknowledgements

* TMDB 5000 Movies dataset (used for training / features)
* Any blog posts, tutorials, or libraries used (Scikit-learn, Pandas, Streamlit/Flask etc.)

---


