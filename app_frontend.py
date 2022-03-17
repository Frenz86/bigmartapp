#Run "streamlit run streamlit_app.py"
# This works on POST
import streamlit as st
import requests

url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict?")


def main():
    st.title("FANTASTICAPI - POST-GET Debugger")
    input1 = st.text_input("Please write the CRIM",2.0)
    input2 = st.text_input("Please write the ZN",1.4)
    input3 = st.text_input("Please write the INDUS",3.0)
    input4 = st.text_input("Please write the CHAS",3.0)
    input5 = st.text_input("Please write the NOX",3.0)
    input6 = st.text_input("Please write the RM",3.0)
    input7 = st.text_input("Please write the AGE",3.0)
    input8 = st.text_input("Please write the DIS",3.0)
    input9 = st.text_input("Please write the RAD",3.0)
    input10 = st.text_input("Please write the TAX",3.0)
    input11 = st.text_input("Please write the PTRATIO",3.0)
    input12 = st.text_input("Please write the B",3.0)
    input13 = st.text_input("Please write the LSTAT",3.0)

    #VERY IMP!! IMPOSTARE GLI STESSI NOMI DELLE STRINGE INPUT IN FASTAPI
    data = { 
            "CRIM": input1, # key must be the named the same as the api BASEMODEL
            "ZN": input2, # key must be the named the same as the api BASEMODEL
            "INDUS": input3, # key must be the named the same as the api BASEMODEL
            "CHAS": input4, # key must be the named the same as the api BASEMODEL
            "NOX": input5, # key must be the named the same as the api BASEMODEL
            "RM": input6, # key must be the named the same as the api BASEMODEL
            "AGE": input7, # key must be the named the same as the api BASEMODEL
            "DIS": input8, # key must be the named the same as the api BASEMODEL
            "RAD": input9, # key must be the named the same as the api BASEMODEL
            "TAX": input10, # key must be the named the same as the api BASEMODEL
            "PTRATIO": input11, # key must be the named the same as the api BASEMODEL
            "B": input12, # key must be the named the same as the api BASEMODEL
            "LSTAT": input13, # key must be the named the same as the api BASEMODEL
            }

    if st.button("Predict with GET"):
        url = url_API
        data_keys = data.keys()
        data_values = data.values()
        url2 ="&".join("{0}={1}".format(x,y) for x,y in zip(data_keys,data_values))
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        prediction =response.json()
        prediction = prediction['prediction']
        st.success(f"The final prediction is: {prediction}")

    if st.button("Predict with POST"):
        url = url_API
        data_keys = data.keys()
        data_values = data.values()
        url2 ="&".join("{0}={1}".format(x,y) for x,y in zip(data_keys,data_values))
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.post(link)
        prediction =response.json()
        prediction = prediction['prediction']
        st.success(f"The final prediction is: {prediction}")

#by default it will main at 8501 port
if __name__ == '__main__':
    main()
