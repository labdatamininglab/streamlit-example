import altair as alt
import numpy as np
import pandas as pd
import streamlit as st




st.title('Fashion in Action')
st.write('Purchasing Prediction for Loyalty Customers')
user_input = st.text_input('Hello, User!')


# Global variable to keep track of the page number
page_number = 1

# Load your CSV data
@st.cache  # Cache the data for better performance
def load_data1():
    url = "https://github.com/labdatamininglab/Fashion.git/frq_items.csv"
    df = pd.read_csv(url)
    return df

def load_data2():
    url = "https://github.com/labdatamininglab/Fashion.git/recommendation.csv"
    df = pd.read_csv(url)
    return df


def transformations(df):

    df1 = df.drop(columns=['Unnamed: 0', 'support'], inplace=False)

    df1['Item'] = df1['itemsets'].astype(str).str.extract(r"\{(.+?)\}")

    unique_items = [item.strip() for sublist in df1['Item'].str.split(',') for item in sublist]

    unique_items = list(set(unique_items))

    unique_items.sort()

    cleaned_items = [item.strip().strip("'") for item in unique_items]

    list_one = []
    list_two = []
    list_three = []

    # Iterate over each row in the dataframe
    for index, row in df1.iterrows():
        # Split the itemsets by comma and remove the leading and trailing whitespace
        items = [item.strip().strip("'") for item in row['Item'].split(',')]
        # Based on the number of items in the row, append to the respective list
        if len(items) == 1:
            list_one.append(items)
        elif len(items) == 2:
            list_two.append(items)
        elif len(items) == 3:
            list_three.append(items)
            
    return cleaned_items, list_one, list_two, list_three


def main():
    global page_number  # Use the global variable
    
    # Create a button to navigate to different pages
    if st.button("BI Reporting"):
        page_number = 1
    elif st.button("Rules of Purchasing"):
        page_number = 2
    elif st.button("Recommendation"):
        page_number = 3
    elif st.button("Cluster"):
        page_number = 4

    # Display content based on the page number
    if page_number == 1:
        st.write('BI')        
    elif page_number == 2:
        # Load data for "Rules of Purchasing" 
        dfx = load_data1()   
        # cleaned_items, list_one, list_two, list_three = transformations(dfx)     
        st.write('Rules')
    elif page_number == 3:
        dfy = load_data2()
        st.write('Reco')
    elif page_number == 4:
        st.write('Cluster')
        

if __name__ == "__main__":
    main()