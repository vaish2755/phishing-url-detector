# 🛡️ Phishing URL Detection using Machine Learning

A machine learning-based cybersecurity application that analyzes URL characteristics and classifies URLs as **potentially phishing** or **legitimate**.

The system uses lexical and structural features extracted from URLs and a Random Forest classifier to identify patterns associated with phishing URLs.

> **Note:** This application analyzes the URL string only. It does not visit, open, or crawl the submitted website.

---

## 📌 Overview

Phishing attacks often use deceptive URLs to trick users into visiting malicious websites or revealing sensitive information.

This project explores how machine learning can identify suspicious URL patterns without accessing the actual website.

The application:

1. Accepts a URL from the user
2. Extracts URL-based features
3. Passes the features to a trained machine learning model
4. Predicts whether the URL resembles phishing or legitimate URLs
5. Displays the prediction and phishing probability

---

## 🎯 Objectives

- Detect suspicious URL patterns using machine learning
- Extract meaningful lexical features from URLs
- Compare multiple classification algorithms
- Evaluate models using classification metrics
- Build a real-time web interface for URL analysis
- Demonstrate an end-to-end machine learning cybersecurity workflow

---

## 🏗️ System Architecture

```text
                    User
                     │
                     ▼
                 Enter URL
                     │
                     ▼
              Web Interface
             HTML / CSS / JS
                     │
                     ▼
                  FastAPI
                     │
                     ▼
           Feature Extraction
                     │
                     ▼
             Random Forest
                  Model
                     │
                     ▼
        Prediction + Probability
                     │
                     ▼
              Web Interface.\venv\Scripts\Activate.ps1