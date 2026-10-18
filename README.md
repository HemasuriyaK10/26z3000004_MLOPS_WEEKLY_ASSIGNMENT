# WEEK 2 ASSIGNMENT

This repository contains the Week 2 assignment for MLOps, demonstrating **Data Version Control (DVC)** integration with Git and Google Cloud Storage (GCS).  

---

## 📌 Assignment Tasks

### Task 1: Initialize DVC
- DVC initialized in the repository (`dvc init`).
- Configuration files committed to Git.

### Task 2: Configure Google Cloud Storage as DVC Remote
- A GCS bucket was created and set as the default DVC remote.
- Verified `dvc push` and `dvc pull` operations.

### Task 3: Version Data and Models Across Iterations
- Augmented the dataset to simulate new data.
- Trained models across multiple iterations.
- Tracked datasets and model artifacts using DVC.

### Task 4: Switch Between Data and Model Versions
- Used Git history and `dvc checkout` to revert to previous versions.
- Verified reproducibility by switching between `v1.0` and `v2.0`.

### Task 5: Push All Relevant Files
- Pushed all configs, pointer files, `.gitignore` updates, and training scripts.
- Repository is fully reproducible.

---

