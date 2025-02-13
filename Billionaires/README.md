# Billionaire Dataset Exploration

This project performs an exploratory data analysis (EDA) on a dataset of billionaires, analyzing their wealth, age, industry, gender distribution, and geographical spread. Various visualizations are generated to present key insights.

## Dataset
- The dataset contains details about billionaires, including their net worth, industry, country, and demographics.
- Data is cleaned, missing values are handled, and outliers are removed.

## Requirements
To run this project, install the required dependencies:
```bash
pip install pandas matplotlib seaborn plotly selenium webdriver-manager
```

## Analysis and Visualizations

### 1. Wealth Distribution
**Insight:** Billionaire wealth follows a heavily skewed distribution, with most individuals clustered in lower wealth ranges and a few extreme outliers in the upper range. The log scale helps in visualizing the disparities.

![Wealth Distribution](figures/wealth_distribution.png)

### 2. Age Distribution
**Insight:** Most billionaires are between 50 and 70 years old, indicating that significant wealth accumulation takes decades. Younger billionaires are rare, often due to inherited wealth or tech startups.

![Age Distribution](figures/age_distribution.png)

### 3. Age Distribution by Industry
**Insight:** Different industries have varied age distributions. The tech industry has a relatively younger billionaire population, while traditional industries like manufacturing and real estate are dominated by older individuals.

![Age by Industry](figures/age_by_industry.png)

### 4. Industries of Billionaires
**Insight:** Some industries, like finance and tech, dominate billionaire creation. The data shows a clear trend that high-growth and high-margin industries generate the most ultra-wealthy individuals.

![Industry Counts](figures/industry_counts.png)

### 5. Gender Distribution
**Insight:** There is a significant gender imbalance among billionaires, with males vastly outnumbering females. This highlights historical and systemic disparities in wealth accumulation opportunities.

![Gender Distribution](figures/gender_distribution.png)

### 6. Billionaires by Country
**Insight:** The distribution of billionaires is not uniform worldwide. The US and China dominate, reflecting their large economies and business-friendly environments. Other countries have significantly fewer billionaires.

![Billionaire Countries](figures/billionaire_countries.png)

## Key Takeaways
- **Wealth is highly concentrated**, with a small number of ultra-rich individuals driving the global billionaire landscape.
- **Age trends show that building extreme wealth takes time**, but newer industries (like tech) create younger billionaires.
- **Industry matters:** Finance, technology, and real estate dominate billionaire creation.
- **Gender disparity is massive**, indicating structural inequalities in wealth accumulation.
- **Geographical concentration is clear**, with the US and China leading in billionaire numbers.

## How to Run the Script
1. Place the dataset `billionaires.csv` in the `EDA` directory.
2. Run the Python script:
   ```bash
   python Exploration_Data_Analysis_Project.py
   ```
3. The figures will be saved in the `figures` folder.

## Notes
- The script is fully automated and generates visualizations after processing the data.
- It uses Selenium to capture the Plotly visualization as a static image.
- Ensure ChromeDriver is installed and compatible with your browser version.

## Author
Harjot / Iris

---
✅ All figures will be saved inside the `figures` folder after execution.

