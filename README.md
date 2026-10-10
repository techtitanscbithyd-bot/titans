# Green Home Score and Retrofit Recommendation Engine

Lloyds – Megathon X Problem Statement 2. Calculates a Green Home Score, recommends retrofits, and
estimates energy, carbon and property-value impact. **Models calculate; the LLM only explains.**
All outputs are estimates, not guarantees.

## Folder map
- `data/` – generated CSVs (homes, sales, truth)
- `src/` – simulator, physics model, schema, plots (calculation code lives here)
- `app/` – Streamlit dashboard (built in a later step)
- `docs/` – `DATA_README.md` explains every formula and assumption
- `tests/` – automatic checks
- `outputs/` – plots and results

## Run it (any computer, Replit or Google Colab)
```
pip install -r requirements.txt
python run_all.py          # regenerates data + plots (seed 42, identical every time)
python -m pytest -q        # optional: run the checks
streamlit run app/app.py   # dashboard (placeholder for now)
```

## Status
- [x] Step 1 project setup
- [x] Step 2 synthetic data + physics simulator
- [ ] Step 3 Green Home Score, retrofits, savings, carbon, value (same functions for both app modes)
- [ ] Step 4 dashboard + LLM explanations
