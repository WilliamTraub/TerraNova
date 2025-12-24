![image](https://github.com/user-attachments/assets/e35e0d3c-243b-460d-97ac-01c5decd31ec)

# TerraNova 
TerraNova is a machine-learning application designed to assist city planners in identifying and classifying brownfield sites. Brownfield sites are previously developed lands that may be contaminated or underutilized, making them potential candidates for redevelopment. This application uses a neural network to classify sites based on various features, helping city planners make informed land use and redevelopment decisions.

A project for the Northeastern University InnovAIte hackathon

## What This Project Does
- Ingests Massachusetts parcel data, cleans missing zoning and location attributes, and engineer features such as haversine distance to Boston city center.
- Converts each parcel into a structured `Land` object and maps categorical zoning descriptions to numeric labels for supervised learning.
- Trains a simple neural network (TensorFlow/Keras) to predict the land use/building type label from three features: distance to city center, county index, and lot size (square feet).
- Visualizes predicted vs. test labels to gauge model performance and spot discrepancies quickly.

## What I Built
- Wrote data prep with pandas and `SimpleImputer` to handle incomplete records and keep the feature set consistent.
- Implemented the `Land` class to encapsulate feature engineering (quantizing counties/zoning and computing haversine distance) and provide clean model inputs.
- Prototyped a compact Keras classifier with an 80/20 train-test split, accuracy reporting, and a quick visualization of prediction vs. truth.
- Wired an end-to-end script (`main.py`) that reads the CSV, cleans it, builds `Land` objects, trains the model, and displays results.

## How I Grew My Python Skills
- Practiced pandas for filtering columns, imputing missing values, and iterating rows into domain objects.
- Learned to structure code with lightweight classes to keep feature engineering reusable and testable.
- Got hands-on with TensorFlow/Keras: defining layers, compiling with appropriate loss/metrics for multiclass classification, and managing train/test splits with NumPy.
- Used matplotlib to create sanity-check plots, reinforcing the habit of validating models visually, not just by metrics.
- Integrated geospatial math (haversine) to turn raw lat/lon into a meaningful distance feature, showing how to mix math utilities with data pipelines.
