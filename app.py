import streamlit as st
import pandas as pd

st.title("Sales Revenue Tracker")

st.markdown("#### :blue[Sales 📊 and Revenue 💵 Between 2001-2024]")

data=pd.DataFrame(
    {
        "year":[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],

        "sales":[11206,386530,482126,248822,456021,140370,170816,454035,345743,262306,216055,476151,389004,996992,482323,336451,116138,464098,25215,72450,246868,397959,403078,306759],

        "revenue":[778982,545777,781509,84987,132693,619916,462684,112065,668051,741125,605715,534506,707077,380734,449808,495057,119265,622198,752153,144714,428139,506811,729702,580525]
    }
)

# Table Format

st.data_editor(
    data,
    num_rows="static",
    hide_index=True,
    column_config={
        "year":st.column_config.NumberColumn(
            "Year",
            help="2001-2024",
            width="medium",
            format="%d"
        ),
        "sales":st.column_config.Column(
            "Sales",
            help="Sales Between 2001 and 2024",
            width="medium"
        ),
        "revenue":st.column_config.Column(
            "Revenue",
            help="Revenue Between 2001 and 2024",
            width="medium"
        )
    }
)

sales=pd.DataFrame(
        [11206,386530,482126,248822,456021,140370,170816,454035,345743,262306,216055,476151,389004,996992,482323,336451,116138,464098,25215,72450,246868,397959,403078,306759]
)

revenue=pd.DataFrame(
       [778982,545777,781509,84987,132693,619916,462684,112065,668051,741125,605715,534506,707077,380734,449808,495057,119265,622198,752153,144714,428139,506811,729702,580525]
)

# Sales
st.markdown("# :orange[Sales]")
st.line_chart(sales)

# Revenue
st.markdown("# :green[Revenue]")
st.line_chart(revenue)
