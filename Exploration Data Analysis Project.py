import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.io as pio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Define the directory for saving figures
figures_dir = r"C:\Desktop\EDA\figures"
os.makedirs(figures_dir, exist_ok=True)

# Load dataset
path = r"C:\Desktop\EDA\billionaires.csv"
df = pd.read_csv(path)

# Display basic info
print(df.shape)
print(df.columns)
print(df.head())
print(df.describe().T)

# Identify and remove outliers using IQR
Q1 = df['wealth.worth in billions'].quantile(0.25)
Q3 = df['wealth.worth in billions'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['wealth.worth in billions'] < (Q1 - 1.5 * IQR)) | 
          (df['wealth.worth in billions'] > (Q3 + 1.5 * IQR)))]

# Impute missing values
df['demographics.age'] = df['demographics.age'].fillna(df['demographics.age'].median())
df['wealth.how.industry'] = df['wealth.how.industry'].fillna('Unknown')

# Convert 'year' to datetime
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Convert categorical column
df['wealth.how.industry'] = df['wealth.how.industry'].astype('category')

# ---- PLOTTING FIGURES ----

# Wealth Distribution
plt.figure(figsize=(15, 10))
sns.histplot(df['wealth.worth in billions'], kde=False)
plt.xscale('log')
plt.title("Wealth Distribution of Billionaires")
plt.savefig(f"{figures_dir}/wealth_distribution.png")

# Age Distribution
df = df[df['demographics.age'] > 0]  # Remove invalid ages
plt.figure(figsize=(15, 10))
sns.histplot(df['demographics.age'], bins=15, kde=False)
plt.title("Age Distribution of Billionaires")
plt.savefig(f"{figures_dir}/age_distribution.png")

# Age Distribution by Industry
plt.figure(figsize=(15, 10))
g = sns.FacetGrid(data=df, hue='wealth.how.industry', aspect=3, height=4)
g.map(sns.kdeplot, 'demographics.age', fill=True)
g.add_legend(title='Industry')
plt.savefig(f"{figures_dir}/age_by_industry.png")

# Industry Count
industry_counts = df['wealth.how.industry'].value_counts(ascending=False)
df_industry = df[['wealth.how.industry']].copy()
df_industry['count'] = 1
grouped_industry = df_industry.groupby('wealth.how.industry', as_index=False, observed=True).sum()
grouped_industry = grouped_industry.sort_values('count', ascending=False)

plt.figure(figsize=(15, 8))
sns.barplot(data=grouped_industry, x='count', y='wealth.how.industry')
plt.title('Industries of Billionaires')
plt.savefig(f"{figures_dir}/industry_counts.png")

# Gender Distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='demographics.gender')
plt.title('Gender Distribution')
plt.savefig(f"{figures_dir}/gender_distribution.png")

# Billionaires by Country (Plotly)
column = 'location.citizenship'
fig = go.Figure(data=[
    go.Pie(
        values=df[column].value_counts().values.tolist(),
        labels=df[column].value_counts().keys().tolist(),
        name=column,
        marker=dict(line=dict(width=2, color='rgb(243,243,243)')),
        hole=0.3
    )],
    layout=dict(title=dict(text="Billionaire Countries"))
)
fig.update_traces(textposition='inside', textinfo='percent+label')

# Save Plotly figure as an HTML file
pio.write_html(fig, f"{figures_dir}/billionaire_countries.html")

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the HTML file in the browser
driver.get("file://" + os.path.abspath(f"{figures_dir}/billionaire_countries.html"))
time.sleep(2)  # Wait for chart to load

# Take a screenshot
driver.save_screenshot(f"{figures_dir}/billionaire_countries.png")
driver.quit()

print("✅ All figures saved successfully in the 'figures' folder!")
