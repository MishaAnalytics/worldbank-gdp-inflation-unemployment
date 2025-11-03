import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # стиль графіків

# directory to save generated images; create it if it doesn't exist
images_dir = os.path.join(os.getcwd(), "images")
os.makedirs(images_dir, exist_ok=True)


df = pd.read_csv('merged_data_with_avg.csv')


countries = ['Ukraine', 'Netherlands', 'Average']
data = df[df['Country'].isin(countries)]


plt.figure(figsize=(10,5))
sns.lineplot(data=data, x='Year', y='GDP', hue='Country', linewidth=2.2)
plt.title('GDP Trends (1970–2024)')
plt.xlabel('Year')
plt.ylabel('GDP (current US$)')
plt.legend(title='Country')
plt.tight_layout()
path = os.path.join(images_dir, "gdp_trends.png")
plt.savefig(path, dpi=300)
plt.show()


plt.figure(figsize=(10,5))
sns.lineplot(data=data, x='Year', y='Inflation', hue='Country', linewidth=2.2)
plt.title('Inflation Trends (1970–2024)')
plt.xlabel('Year')
plt.ylabel('Inflation (%)')
plt.legend(title='Country')
plt.tight_layout()
path = os.path.join(images_dir, "inflation_trends.png")
plt.savefig(path, dpi=300)
plt.show()



plt.figure(figsize=(10,5))
sns.lineplot(data=data, x='Year', y='Unemployment', hue='Country', linewidth=2.2)
plt.title('Unemployment Trends (1970–2024)')
plt.xlabel('Year')
plt.ylabel('Unemployment (%)')
plt.legend(title='Country')
plt.tight_layout()
path = os.path.join(images_dir, "unemployment_trends.png")
plt.savefig(path, dpi=300)
plt.show()


plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x='GDP', y='Unemployment', hue='Country', style='Country', s=60)
sns.regplot(data=data, x='GDP', y='Unemployment', scatter=False, color='gray', ci=None)
plt.title('Relationship between GDP and Unemployment')
plt.xlabel('GDP (current US$)')
plt.ylabel('Unemployment (%)')
plt.tight_layout()
path = os.path.join(images_dir, "gdp_unemployment_scatter.png")
plt.savefig(path, dpi=300)
plt.show()

print("I have created and saved the plots of Ukraine, Netherlands and average data across all countries in categories, such as GDP, Inflation, and Unemployment.")