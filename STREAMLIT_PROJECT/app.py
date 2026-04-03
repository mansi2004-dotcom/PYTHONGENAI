import streamlit as st
st.title("My Streamlit App")
st.write("Welcome to my streamlit")
st.header("Header")
st.subheader("Subheader")
st.text("This is a text element")
st.markdown("** This is a Markdown element**")

# displaying the data
import pandas as pd
data = {
    "Name": ["Alice","Bob","Charlie"],
    "Age":[2,30,35],
    "City":["New York", "Los Angeles","Chicago"]
}
df=pd.DataFrame(data)

st.title("Dataframe example")
st.write("here is a sample dataframe:")
st.dataframe(df)

# Intractive Widgets

st.title("Interactive Widgets")
name = st.text_input("Enter your Name:")
age = st.number_input("Enter your age: ", min_value=0, max_value=120)
if st.button("Submit"):
    st.write(f"Hello,{name}! You are {age} years old. ")


# Sliders example
st.title("Slider example")
value1 = st.slider("Select a number: ", 10, 100, 50)
value2 = st.slider("Select a range: ",min_value=0, max_value=100, value=(20,80))
st.write(f"you selected: {value1}")
st.write(f"you selected: {value2}")

# SideBar Example
st.title("SideBar Example")
age = st.sidebar.number_input("Enter your Age: ",min_value=0, max_value=120)
st.sidebar.write(f"You Entered: {age}")
mode = st.sidebar.selectbox("Select a Mode: ",["Light", "Dark"])
st.sidebar.write(f"You selected: {mode}")
features = st.sidebar.multiselect("Select features: ",["Feature A","Feature B","Feature C"])
st.sidebar.write(f"You selected: {features}")
st.title("Chart Example")
import numpy as numpy
import pandas as pd
data = pd.DataFrame(np.random.randn(100,3),
columns =["A","B","C"])
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
st.title("Uploading the Data")
file = st.file_uploader("Upload a CSV file",type =["csv"])
if file is not None:
    import pandas as pd

    df = pd.read_csv(file)
    st.write("DataFrame: ")
    st.dataframe(df)


