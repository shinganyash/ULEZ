import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load London borough GeoJSON
with open("London_Boroughs.geojson", "r") as f:
    boroughs_geojson = json.load(f)

# ULEZ PCN data for 2024
pcn_data = pd.DataFrame({
    "Borough": [
        "Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden",
        "City of London", "Croydon", "Ealing", "Enfield", "Greenwich", "Hackney",
        "Hammersmith and Fulham", "Haringey", "Harrow", "Havering", "Hillingdon",
        "Hounslow", "Islington", "Kensington and Chelsea", "Kingston upon Thames",
        "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge",
        "Richmond upon Thames", "Southwark", "Sutton", "Tower Hamlets",
        "Waltham Forest", "Wandsworth", "Westminster"
    ],
    "PCNs_2024": [
        53517, 35525, 33375, 49078, 27657, 7199,
        525, 52800, 33406, 79938, 37933, 21921,
        9127, 52176, 34896, 38759, 52094,
        31427, 14448, 6999, 15350,
        22141, 28874, 21982, 45117, 47303,
        7717, 16730, 19171, 19460,
        40628, 14125, 13445
    ]
})

# Match GeoJSON borough names if needed
name_map = {
    "Barking & Dagenham": "Barking and Dagenham",
    "Hammersmith & Fulham": "Hammersmith and Fulham",
    "Kensington & Chelsea": "Kensington and Chelsea",
    "Richmond upon Thames": "Richmond upon Thames",
    "Kingston upon Thames": "Kingston upon Thames"
}

pcn_data["Borough"] = pcn_data["Borough"].replace(name_map)

# Choropleth map
fig = px.choropleth_mapbox(
    pcn_data,
    geojson=boroughs_geojson,
    locations="Borough",
    featureidkey="properties.NAME",
    color="PCNs_2024",
    color_continuous_scale=["#fff7bc", "#fec44f", "#fe9929", "#d95f0e", "#993404"],
    range_color=(pcn_data["PCNs_2024"].min(), pcn_data["PCNs_2024"].max()),
    mapbox_style="carto-positron",
    zoom=8.8,
    center={"lat": 51.5074, "lon": -0.1278},
    opacity=0.8,
    hover_name="Borough",
    hover_data={"PCNs_2024": True, "Borough": False}
)

fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>PCNs in 2024: %{z:,}<extra></extra>"
)

fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    coloraxis_colorbar=dict(title="ULEZ PCNs")
)

# Streamlit section
st.markdown("---")
st.header("📍 ULEZ PCNs Across London (2024)")
st.plotly_chart(fig, use_container_width=True)

st.markdown("Hover over each borough to see its name and total ULEZ penalty notices received in 2024.")
