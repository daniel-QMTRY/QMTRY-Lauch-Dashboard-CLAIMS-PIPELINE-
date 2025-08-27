
import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="QMTRY Launch Dashboard", layout="wide")
st.markdown("# 🚀 QMTRY — Launch Dashboard (Claims Pipeline)")
st.caption("Dark theme • Synthetic demo data • HIPAA-safe")

@st.cache_data
def load_data():
    path = os.path.join("data","sample","claims_demo.csv")
    return pd.read_csv(path, parse_dates=["service_date"])

df = load_data()
df["month"] = df["service_date"].dt.to_period("M").dt.to_timestamp()

payers = sorted(df["payer"].unique())
sel = st.sidebar.multiselect("Filter payers", payers, default=payers)
f = df[df["payer"].isin(sel)]

m = f.groupby("month")["claim_id"].count().reset_index()
st.plotly_chart(px.line(m, x="month", y="claim_id", title="Claims Volume by Month", template="plotly_dark"), use_container_width=True)
drp = f.groupby("payer")["status"].apply(lambda s: (s=="Denied").mean()).reset_index()
drp.columns = ["payer","denial_rate"]
st.plotly_chart(px.bar(drp.sort_values("denial_rate", ascending=False), x="payer", y="denial_rate", title="Denial Rate by Payer", template="plotly_dark"), use_container_width=True)

queue = f[f["status"]=="Denied"][["claim_id","member_id","provider_id","payer","service_date","billed_amount","allowed_amount","denial_reason"]]
st.subheader("📤 Export Outreach Queue")
st.download_button("Download CSV", queue.to_csv(index=False).encode("utf-8"), "outreach_queue.csv", "text/csv")
