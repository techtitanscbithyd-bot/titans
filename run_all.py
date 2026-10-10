"""
ONE command to rebuild everything:   python run_all.py

Right now it does:  1) generate data  2) make plots
Later steps will add: 3) train models  4) launch the Streamlit app
"""
from src.plots import make_all_plots
from src.simulate import generate_all

if __name__ == "__main__":
    homes, sales, truth = generate_all()          # fixed seed 42 inside simulate.py
    print(f"[1/2] Data ready: {len(homes)} homes, {len(sales)} sales")
    for p in make_all_plots():
        print("[2/2] Plot saved:", p)
    print("Done. (Model training and the dashboard are added in later steps.)")
