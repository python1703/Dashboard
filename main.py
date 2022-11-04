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
    # graph = {0: "Line Chart", 1:"Bar Chart"}
    # opt = ""
    opt = st.radio("Select to ",graph)
    # for i in graph:
      #  opt = st.checkbox(i)
    return opt

def sidebar():
    global df, filename, option, opt, columnList
    df = None
    allowedExtension =['csv', 'xlsx']
    # linegraph = ""
    with st.sidebar:
                df = pd.read_csv("country_wise_latest.csv")     # Can be used wherever a "file-like" object is accepted:
                columnList = df.columns.values.tolist()     # to get list of columns
                option = st.selectbox("Select Column", columnList)
                st.subheader("Filters ")
                opt = showGraphList()

def getIndexes(columnName, value):
    # st.write(df[columnName])
    # st.write(value)
    count = -1
    for i in df[columnName]:
        count += 1
        # print(i, value)
        if i == value:
            # print(count)
            # print(True, value, "index = ",  count)
            # st.write(count)
            return count



def mainContent():
    st.header("Coronavirus world-wide analysis")
    if df is not None:
        st.write(df)
        # graph = ["Line Chart", "Bar Chart"]
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
            # st.write(df[option][5])
            # st.write(columnList[0])


            selectOption = []
            # data = []
            for i in df[columnList[0]]:
                selectOption.append(i)
            selectedData = st.multiselect(f"Choose {columnList[0]} to see", selectOption)

            dataToVisualize = []
            for i in selectedData:
                # st.write(getIndexes(columnList[0], i))
                index = getIndexes(columnList[0], i)
                # st.write(df[option][index])
                dataToVisualize.append(df[option][index])

            x = np.array(dataToVisualize, 'f')
            # st.write(x)
            fig = plt.figure()
            plt.pie(x, labels = selectedData, autopct='%0.f%%')  # %).f%% means no of digit show after decimal

            st.balloons()
            # st.write(option)
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
        # else:
        #     st.write("Loading data")
    else:
        st.write("There is nothing to show!!")




if __name__ == "__main__":
    sidebar()
    mainContent()
