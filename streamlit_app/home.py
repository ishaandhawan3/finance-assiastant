import streamlit as st
import requests
import plotly.graph_objects as go

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Finance Assistant", layout="wide")
st.title("🧠 Multi-Agent Finance Assistant")

symbol = st.text_input("Enter Stock Symbol", value="AAPL")
if st.button("Get Latest Price"):
    r = requests.get(f"{API_URL}/price/{symbol}")
    st.write(r.json())

if st.button("Get History"):
    r = requests.get(f"{API_URL}/history/{symbol}")
    data = r.json()
    st.write(data)
    if "close" in data:
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=list(data["close"].values()), mode='lines', name=symbol))
        st.plotly_chart(fig)

url = st.text_input("News URL to Scrape")
if st.button("Scrape News"):
    r = requests.post(f"{API_URL}/scrape", params={"url": url})
    st.write(r.json())

context = st.text_area("Context for Market Brief")
if st.button("Generate Brief"):
    r = requests.post(f"{API_URL}/brief", params={"context": context})
    st.write(r.json()["brief"])
