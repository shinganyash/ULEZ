import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ULEZ Penalties & Income Inequality in London",
    layout="wide"
)

# ── Header ────────────────────────────────────────────────────
st.title("Who Pays for Clean Air?")
st.subheader("ULEZ Penalty Charge Notices and Income Inequality Across London Boroughs")
st.markdown("""
*By Ava, Dori, Greg & Yash · Spring 2026 · Applied Quantitative Research and Journalistic Practice*

---
""")

# ── Introduction ──────────────────────────────────────────────
st.markdown("""
London's Ultra Low Emission Zone (ULEZ) charges drivers of older, more polluting vehicles 
a daily fee — and issues Penalty Charge Notices (PCNs) to those who don't pay. 
But who is actually receiving these penalties?

This investigation finds a strong negative correlation (**r ≈ −0.76, p < 0.001**) between 
borough median weekly earnings and annual ULEZ PCN counts — suggesting that the flat-fee 
structure of emissions penalties falls disproportionately on lower-income communities.
""")

# ── Section 1: Maps ───────────────────────────────────────────
st.markdown("---")
st.header("📍 The Geography of Penalties and Income")

col1, col2 = st.columns(2)
with col1:
    st.image("images/london_choropleth_maps_wide1.png", 
             caption="ULEZ PCNs by borough (2024)", use_container_width=True)
with col2:
    st.image("images/london_choropleth_maps_wide1.png",
             caption="Weekly household income by borough (2024)", use_container_width=True)

st.markdown("""
The maps reveal a clear spatial pattern: outer boroughs in the north and east — 
areas with lower median incomes — receive far more penalty notices than their 
wealthier counterparts in inner south and west London.
""")

# ── Section 4: Income groups ──────────────────────────────────
st.markdown("---")
st.header("⚖️ Low vs. High Income Boroughs")

st.image("images/london_income_groups_pcn_per_vehicle_bar.png",
         caption="PCNs per 1,000 vehicles: 10 lowest vs. 10 highest income boroughs (2024)",
         use_container_width=True)

st.markdown("""
The contrast is stark. The 10 lowest-income boroughs average around **46,000 PCNs** 
compared to just **14,000** in the 10 highest-income boroughs — a 3.3× gap. 
Normalised by vehicle counts, the difference remains close to **2×**, 
at approximately 397 vs 205 PCNs per 1,000 vehicles.
""")

# ── Methodology ───────────────────────────────────────────────
st.markdown("---")
st.header("🔬 Methodology")
st.markdown("""
- **PCN data**: Transport for London ULEZ Penalty Charge Notices, 2024  
- **Income data**: ONS Annual Survey of Hours and Earnings (ASHE), median weekly pay by borough, 2024  
- **Vehicle data**: DVLA/DfT licensed vehicles by borough, 2024  
- **Statistical method**: OLS regression with borough-level observations; 
  Pearson correlation coefficient reported  
- City of London excluded from income analysis (earnings data suppressed by ONS)  
- All analysis conducted in R using `sf`, `ggplot2`, and `ggrepel`
""")

# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.caption("Data sources: TfL, ONS ASHE, DVLA/DfT · Visualisations produced in R · © 2026")
