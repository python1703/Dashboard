import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np



PAGE_CONFIG = {"page_title":"Data Visualization","page_icon":"chart_with_upwards_trend:", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def showGraphList():
    """This function will return all the graph available"""
    graph = ["Line Chart", "Bar Chart", "Pie Chart", "Scatter Plot"]
    opt = st.radio("Select to ",graph)
    return opt

def sidebar():
    global df, filename, option, opt, columnList
    df = None
    allowedExtension =['csv', 'xlsx']
    with st.sidebar:
                df = pd.read_csv("country_wise_latest.csv")     
                columnList = df.columns.values.tolist()    
                option = st.selectbox("Select Column", columnList)
                st.subheader("Filters ")
                opt = showGraphList()

def getIndexes(columnName, value):
    count = -1
    for i in df[columnName]:
        count += 1
        if i == value:
            return count



def mainContent():
    st.header("Coronavirus world-wide analysis")
    if df is not None:
        st.write(df)
        if opt == "Line Chart":
            label = "Line Chart for country wise data"
            st.header(label)
            st.line_chart(df[option])
            st.balloons()
        elif opt == "Bar Chart":
            label = "Bar Chart for country wise data"
            st.header(label)
            st.bar_chart(df[option])
            st.balloons()
        elif opt == "Pie Chart":
            label = "Pie Chart for country wise data"
            st.header(label)


            selectOption = []
            for i in df[columnList[0]]:
                selectOption.append(i)
            selectedData = st.multiselect(f"Choose {columnList[0]} to see", selectOption)

            dataToVisualize = []
            for i in selectedData:
                index = getIndexes(columnList[0], i)
                dataToVisualize.append(df[option][index])

            x = np.array(dataToVisualize, 'f')
            fig = plt.figure()
            plt.pie(x, labels = selectedData, autopct='%0.f%%')  

            st.balloons()
           
            plt.legend(title = option)
            st.pyplot(fig)

        elif opt == "Scatter Plot":
            label = "Scatter Plot for country wise data"
            st.header(label)
            x_values = st.sidebar.selectbox('X axis', options=columnList)
            y_values = st.sidebar.selectbox('Y axis', options=columnList)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values)
            st.plotly_chart(plot)
            st.balloons()

    else:
        st.write("There is nothing to show!!")




if __name__ == "__main__":
    sidebar()
    mainContent()
