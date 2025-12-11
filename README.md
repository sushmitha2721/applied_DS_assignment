# 🌍 G7 Climate, Population & Energy Indicators — Exploratory Data Analysis (EDA)

This project explores key environmental, population, and energy-related indicators for **G7 countries** using Python.  
The analysis includes line charts, bar graphs, and correlation heatmaps created from World Bank climate and population data.  
The goal is to understand long-term trends and relationships between major sustainability indicators.

---

You may replace this with any World Bank formatted dataset.

---

## 🛠 Tools & Libraries

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 📊 Visualisations Included

### **1️⃣ Line Plots**
Line plots show the change over time (for selected indicators) across all G7 countries:

- Electricity production from natural gas  
- Electricity production from hydroelectric sources  
- Electricity production from renewable sources  

These visualisations highlight long-term energy transition patterns.

---

### **2️⃣ Bar Charts**
Two bar charts focus on trends starting around 2005:

- Urban population growth in G7 countries  
- Total greenhouse gas emissions (kt of CO₂ equivalent)

These charts help compare development and environmental impact across regions.

---

### **3️⃣ Correlation Heatmaps**
Correlation matrices were generated for:

- Urban population  
- Mortality rate (under-5)  
- CO₂ emissions  
- Electric power consumption  
- Electricity production from oil sources  

Countries analysed:

- **Canada**
- **Italy**

The heatmaps reveal relationships between development, pollution, and energy use.

---

## 🧩 Code Structure

### `dataframes_make()`
Processes the dataset, creates two dataframes:  
- Transposed by years  
- Standard format by indicators

### `lines_ploting()`
Creates multi-country line plots for a given indicator.

### `correlations_plotting()`
Generates correlation heatmaps for selected indicators in one G7 country.

### Main Script Tasks:
- Loads and preprocesses dataset  
- Filters the G7 countries  
- Creates bar charts  
- Creates correlation heatmaps  
- Generates energy production line plots  

### Main Script Tasks:
- Loads and preprocesses dataset  
- Filters the G7 countries  
- Creates bar charts  
- Creates correlation heatmaps  
- Generates energy production line plots  




