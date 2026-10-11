# MLOps Weekly Assignment - Week 1

This repository contains the Week 1 assignment for the IITMBS MLOps course.  
It demonstrates setting up a machine learning pipeline on Google Cloud using Vertex AI Workbench and Google Cloud Storage (GCS).

---

## 📌 Tasks Overview

1. **Activate GCP & Setup Vertex AI Workbench**  
   - Enable required APIs:  
     - `storage.googleapis.com`  
     - `aiplatform.googleapis.com`  
     - `compute.googleapis.com`  
     - `notebooks.googleapis.com`  
     - `iam.googleapis.com`  
   - Create a Vertex AI Workbench instance.

2. **Store Training Data in GCS**  
   - Create a regional GCS bucket.  
   - Upload the IRIS dataset.  
   - Split into training and evaluation sets.

3. **Execute the IRIS Training Pipeline**  
   - Train a scikit-learn model (e.g., Decision Tree / Random Forest).  
   - Save artifacts (model, logs) locally in `artifacts/` and upload to GCS.  
   - Organize outputs by timestamp.

4. **Run Inference on Evaluation Set**  
   - Load the
