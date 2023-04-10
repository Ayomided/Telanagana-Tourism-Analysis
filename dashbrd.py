import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

domestic_stuff = pd.read_csv('domestic_yearly_sum.csv')

dom = pd.read_csv('total_2016.csv')
forr = pd.read_csv('total_2019.csv')
cagr = pd.read_csv('cagr_m.csv')

# year = pd.DataFrame([2016, 2017, 2018, 2019], dtype='int')

# district = st.multiselect('Select District', options=dom['district'], default=None)
year_o = 2016
year_f = 2019

six_sum = dom['visitors'].sum()
nin_sum = forr['visitors'].sum()
proj_sum = round(cagr['Visitors 2025'].sum())

cagr_val = cagr['CAGR'].sum()
visitdelta = int(nin_sum - six_sum)
projdelta = round(int(proj_sum - nin_sum), 1)
projrev = int(cagr['Projected Revenue Domestic'].sum() +
              cagr['Projected Revenue Foreign'].sum())

st.subheader('Metrics')
col1, col2 = st.columns(2)
col1.metric("Visitors Change (2016-2019)", nin_sum, 
          delta=visitdelta, delta_color="normal")
col2.metric("Visitors Projected Change (2019-2025)", proj_sum,
          delta=projdelta, delta_color="normal")

col1, col2 = st.columns(2)
col1.metric('CAGR', cagr_val)
col2.metric('Projected Revenue', projrev)

st.subheader('District by District Data')
def plot():
    domestic_stuff = pd.read_csv('domestic_yearly_sum.csv')
    domestic_stuff = domestic_stuff.dropna()

    clist = domestic_stuff["district"].unique().astype('str').tolist()  

    districts = st.multiselect("Select year", clist)
    # st.write("You selected: {}".format(", ".join(districts)))

    dfs = {
        year: domestic_stuff[domestic_stuff["district"] == year] for year in districts}

    fig = go.Figure()
    for districts, domestic_stuff in dfs.items():
        fig = fig.add_trace(go.Scatter(
            x=domestic_stuff["year"], y=domestic_stuff["visitors"], name=districts))

    st.plotly_chart(fig)

plot()

# st.line_chart(domestic_stuff, x='district', y='visitors')












# if len(district) > 0:
#     dom = dom[dom['district'].isin(district)]

# st.write(district)
# st.line_chart(data=dom)
# fig = px.line(dom, x='district', y='visitors', color='year')
# st.plotly_chart(fig)
