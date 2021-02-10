import streamlit as st 
import numpy as np 
import pandas as pd
import matplotlib.pyplot  as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("data.csv")
x=np.array(data['YearsExperience']).reshape(-1,1)
y=np.array(data['Salary'])
lr=LinearRegression()
lr.fit(x,y)


st.title("Salary Predictor")

nav=st.sidebar.radio("Navigation",['Home',"Prediction","Contribute"])

if nav=="Home":
    if st.checkbox("Show Table"):
        st.table(data)

    val=st.slider("Filter data using years",0,20)
    data=data.loc[data['YearsExperience']>=val]
    plt.figure(figsize=(10,5))
    plt.scatter(data['YearsExperience'],data["Salary"])
    plt.ylim(0)
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.tight_layout()
    st.pyplot(plt)


elif nav=="Prediction":
    st.header("Know your salary")
    val=st.number_input("Enter Your Exp",0.00,20.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    pred=lr.predict(val)[0]
    if st.button("Predict"):
        st.success(f"Your Predicted Salary is {round(pred)}")

else:
    st.write("Contribute")

