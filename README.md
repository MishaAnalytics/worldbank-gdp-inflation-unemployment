# 🌍worldbank-gdp-inflation-unemployment
Analysis of global economic indicators (GDP, inflation, unemployment) using World Bank data.

---

## 📊 Overview

This project:
- Merges datasets on **GDP**, **Inflation**, and **Unemployment**  
- Calculates **average global values** for comparison  
- Visualizes trends for **Ukraine**, **Netherlands**, and the **global average**  
- Demonstrates the correlation between GDP and Unemployment
- In  the `outputs/` forlder you can find demonstrations of running this code.

---

## 🧠 What I Learned

- Handling real-world macroeconomic data from the **World Bank**  
- Data reshaping, cleaning, and aggregation with **pandas**  
- Creating analytical visualizations using **matplotlib** and **seaborn**  
- Structuring a reproducible data analysis workflow  

---

## 🌱 Personal Growth Note

This project reflects my journey into **data science and economic analytics**.  
It helped me connect global economic concepts with real data, improving both my technical and analytical thinking.  
I’m continuously learning to transform data into insight - a skill I aim to deepen through my university studies.

---

## ⚙️ How to Run

You can reproduce the analysis locally in just a few steps:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Prepare the merged dataset
python prepare_data.py

# 3. Generate and save visualizations
python visualize_data.py

```
Note: All charts are generated automatically and saved in the `images/` folder when you run `visualize_data.py`.
