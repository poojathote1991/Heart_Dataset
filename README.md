# Heart_Dataset@@ -1 +1,42 @@
# Heart-Disease
# Heart-Disease Analysis and Prediction

## About the dataset:

This data set dates from 1988 and consists of four databases: `Cleveland`, `Hungary`, `Switzerland`, and `Long Beach V`. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The **`target`** field refers to the presence of heart disease in the patient. 
```
 0 = doesn't have heart disease
 1 = has heart disease
  ```

## Repository Analysis:

*`data`* -> Contains the dataset of this project.

*`notebooks`* -> Contains two notebooks. One is for analysis another is for model evaluation.

*`src`* -> Contains all python files.

## My approch:

The dataset was pretty straight forward. Didn't need much preprocessing. `Feature Engineeing`, `Feature Selection`, `Feature Scaling` lead to *overfitting*. So, I avoided those steps. Dataset was divided into `train` and `dev` set. Trained the model on train set and check overfitting on dev set. 

`Random Forest` algorithm has *`highest`* score.
