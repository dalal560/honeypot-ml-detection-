# Honeypot Machine Learning Detection

This project presents a simple honeypot system powered by a trained **XGBoost** model to classify incoming network connections as **Benign** or **Attack**. It demonstrates how machine learning can be integrated into cybersecurity tools for real-time threat simulation and detection.

## Project Structure

| File/Folder                          | Description                                                   |
|-------------------------------------|---------------------------------------------------------------|
| `training_model.ipynb`              | Jupyter Notebook used to preprocess the dataset and train the XGBoost model. |
| `xgboost_model.pkl`                 | Trained XGBoost model saved for inference.                    |
| `honeypot_with_model_v2_Attack.py`  | Honeypot script that simulates and classifies an **attack** connection. |
| `honeypot_with_modelBenign.py`      | Honeypot script that simulates and classifies a **benign** connection. |
| `honeypot_simulation_screenshots/`  | Folder containing screenshots of honeypot behavior in both scenarios. |

## Screenshots

- `honeypot_simulation_screenshots1.png`: Simulation result for a benign (normal) connection.
- `honeypot_simulation_screenshots.png`: Simulation result for a malicious (attack) connection.

These screenshots show how the honeypot detects and logs different types of incoming traffic using the ML model.

## Technologies Used

- **Python 3**
- **XGBoost**
- **Scikit-learn**
- **Socket Programming**
- **Google Colab** (for training and preprocessing)
- **Logging** (to store connection logs)
- **Matplotlib & Seaborn** (for evaluation)

## Usage Notes

- The honeypot listens on port `8080`.
- Extracted features used in prediction are simulated for demonstration purposes.
- All connections are logged into a file named `honeypot_ml.log`.
- For full functionality, real-time network feature extraction should replace manual input.

## Disclaimer

This project is intended for academic and demonstration purposes only. Do not deploy in production environments without proper safeguards.

## Authors

- **Dalal Alwadei** — Master's Student in Computer Science  
- **Razan Bajam’an** — Master's Student in Computer Science
