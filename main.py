import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title("Iris Flower Classification")
st.write("Thank you for using the Iris Flower Classification app!")
st.write("Enter values to predict the Iris flower type.")

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length", 1.0, 7.0, 2.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

user_input = pd.DataFrame(
    {
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width],
    }
)

iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(X, y)

prediction = clf.predict(user_input)

target_names = iris.target_names

st.write("Prediction:")
st.write(f"The Iris flower type is {target_names[prediction[0]]}.")