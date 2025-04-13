# yacht_hydrodynamics_prediction

## Project Overview
This project aims to predict the residuary resistance (RR) of a yacht based on various hydrodynamic features of its design. The prediction is carried out using different machine learning models to evaluate which provides the most accurate prediction.

## Technologies Used
- **Programming Language**: Python 3.x
- **Libraries**: 
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - xgboost
  - lightgbm

## Machine Learning Models Used
- **Linear Regression**: Simple model for understanding linear relationships.
- **Decision Tree Regressor**: Captures non-linearities in the data.
- **Random Forest Regressor**: Ensemble model that reduces overfitting.
- **Gradient Boosting**: Boosted model to improve prediction accuracy.
- **Support Vector Regressor (SVR)**: Model that performs well for non-linear data using RBF kernel.

Each model is evaluated using:
- **Root Mean Squared Error (RMSE)**
- **R² Score**

## Dataset Description
The dataset consists of various hydrodynamic features related to the yacht's design and its corresponding residuary resistance (RR). The columns are:

| Column     | Description                                             |
|------------|---------------------------------------------------------|
| **LC**     | Longitudinal position of the center of buoyancy         |
| **PC**     | Prismatic coefficient                                   |
| **L/D**    | Length-displacement ratio                               |
| **B/Dr**   | Beam-draught ratio                                      |
| **L/B**    | Length-beam ratio                                       |
| **Fr**     | Froude number                                           |
| **RR**     | Residuary resistance (target variable)                  |

## Results and Insights
- **Best Performing Model**: Based on RMSE and R² score, **Gradient Boosting** is the best performing model.
- **Feature Importance**: 
  - The **Froude number (Fr)** and **Prismatic coefficient (PC)** are identified as the most influential features for predicting the residuary resistance.

## Future Work
- Implement more advanced models like **XGBoost** and **LightGBM**.
- Explore **Deep Learning models** such as **Neural Networks** for higher accuracy.
- Incorporate **real-time predictions** for dynamic yacht design adjustments.

## Conclusion
This project provides insights into the importance of hydrodynamic design features for predicting yacht performance, and explores different machine learning models to optimize prediction accuracy.
