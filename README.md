# Heart Disease Prediction Using Machine Learning ❤️‍🩹 🩺

# Introduction
This project focuses on predicting heart disease using a comprehensive dataset containing patient information. The goal is to build machine learning models that can predict the presence of heart disease based on various health parameters. The dataset has been used to test multiple algorithms, and the best-performing model was selected based on accuracy, confusion matrix, and classification report.

![c1_2144995_210707170149](https://github.com/user-attachments/assets/38e097ed-ed65-453d-8d44-9c995d45fd99)



# Dataset



The dataset consists of various health-related features that are indicative of heart conditions. Below is a description of the columns in the dataset:



• age: Age of the patient.


• sex: Gender of the patient (1 = male; 0 = female).


• chest pain type: Type of chest pain experienced (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 4 = asymptomatic).


• resting bp s: Resting blood pressure in mm Hg.


• cholesterol: Serum cholesterol level in mg/dl.


• fasting blood sugar: Whether fasting blood sugar is greater than 120 mg/dl (1 = true; 0 = false).


• resting ecg: Resting electrocardiographic results (0 = normal; 1 = having ST-T wave abnormality; 2 = showing probable or definite left ventricular hypertrophy).


• max heart rate: Maximum heart rate achieved during exercise.


• exercise angina: Exercise-induced angina (1 = yes; 0 = no).


• oldpeak: ST depression induced by exercise relative to rest.


• ST slope: The slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping).


• target: Whether the patient has heart disease (1 = yes; 0 = no).




# Algorithms Used

A wide variety of machine learning algorithms were applied to the dataset to evaluate their performance in predicting heart disease:

• RandomForestClassifier


• GradientBoostingClassifier (Best Performing Model)

• GaussianNBModel


• LogisticRegressionModel


• SGDClassifierModel


• DecisionTreeClassifierModel


• KNNClassifierModel


• ExtraTreesClassifier


• AdaBoostClassifier


• HistGradientBoostingClassifier


• XGBClassifier


• CatBoostClassifier


• LGBMClassifier


• MLPClassifier


• SVCModel


# Best Model: Gradient Boosting Classifier


After evaluating all the models, the Gradient Boosting Classifier was found to be the most accurate in predicting heart disease. Below are the key performance metrics for this model:

• Accuracy: Achieved the highest accuracy compared to other models.

• Confusion Matrix: Used to evaluate the performance of the classification model by showing the true positives, true negatives, false positives, and false negatives.

• Classification Report: Generated to provide a detailed analysis of precision, recall, F1-score, and support for each class.


# GUI Implementation

The project also includes a user-friendly graphical interface built using Streamlit. This GUI allows users to input patient data and get real-time predictions of heart disease based on the Gradient Boosting Classifier. The interface provides a simple and interactive way to explore the model's predictions and insights.

