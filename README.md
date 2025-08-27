# 🚀 QMTRY — Launch Dashboard (Claims Pipeline)

> **Dark‑theme Streamlit app** that proves automated claims pipelines can **cut denials, shrink days‑to‑pay, and reduce cost‑to‑collect**. Synthetic, HIPAA‑safe data. Ready to demo fast — then swap in your Synthea CSVs or real feeds.

<p align="center">
  <img src="assets/claims_volume.png" alt="Claims volume by month" width="48%"/>
  <img src="assets/denial_rate_by_payer.png" alt="Denial rate by payer" width="48%"/>
  <br/>
  <img src="assets/top_denials.png" alt="Top denial reasons" width="48%"/>
  <img src="assets/cost_to_collect_trend.png" alt="Cost to collect trend" width="48%"/>
</p>

## One‑path Quickstart (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Use provided demo data (already in data/sample)
streamlit run app/streamlit_app.py
```

### Swap in your Synthea CSVs (optional later)
```powershell
python scripts/build_claims_from_synthea.py --input "Y:\Synthea\csv" --out data\claims_canonical
# Then point the app to data\claims_canonical\claims_demo.csv
```
