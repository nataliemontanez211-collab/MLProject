# FINTECH 540: Machine Learning Project

This repository contains the work for the Fall 2025 FINTECH 540 Machine Learning project.

---

## Dataset

The dataset includes several key volatility measures calculated at both 1-minute and 5-minute frequencies. For this project, we are focusing on the **5-minute data**. Key variables include:

* **Realized Variance (RV):** The total daily price variation.
* **Good & Bad Variance:** Volatility components from positive and negative intraday returns, respectively.
* **Bipower Variation (BPV):** A measure of the continuous part of the price process.
* **Realized Quarticity (RQ):** The volatility of volatility.

---

## Repository Structure

This repository is organized to facilitate collaboration and maintain a clean workflow:

* **/data**: Contains the raw dataset (`RV_March2024.xlsx`).
* **/notebooks**: Houses Jupyter Notebooks for analysis, experimentation, and visualization.
* **/scripts**: Contains reusable Python scripts for tasks like data loading (`data_loader.py`) and feature engineering.
* **/Checkpoint**: Contains checkpoint slides.
* **/Guidelines**: Project guidelines and other relevant documents from the course.

---

## How to Get Started

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/samfan-27/mlproject.git](https://github.com/samfan-27/mlproject.git)
    cd mlproject
    ```

2. **Set up the environment:**
    This project uses a Python virtual environment to manage dependencies. Ensure you have Python 3.10+ installed.

    ```bash
    # Create and activate the virtual environment
    python3 -m venv .venv
    source .venv/bin/activate

    # Install required packages
    pip install -r requirements.txt
    ```

---

## Team Members

* Natalie Montanez
* Sam Fan
* Gavin Pang
* Jiaxi Lin
* Xi Zuo
