import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")
# Load the clean analytical dataset
df = pd.read_excel("v4_analytical_database.xlsx")

# Define the exact name of the GDP column we want to analyze
gdp_column = 'GDP per capita (constant 2015 US$)'

# Filter data for the years 1995 to 2023 for a clear historical view
df_filtered = df[(df['Year'] >= 1995) & (df['Year'] <= 2023)].copy()

print("Generating the line chart...")
# --- VISUALIZATION SETUP ---
# Set the visual style using seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 8))

# Create the line plot
sns.lineplot(
    data=df_filtered, 
    x='Year', 
    y=gdp_column, 
    hue='Country Name',
    linewidth=2.5,
    marker='o',          # Adds dots to data points
    markersize=6,
    palette='tab10'      # Uses a distinct color palette
)

# --- ADDING HISTORICAL MILESTONES (THE "PRO" TOUCH) ---

# Milestone 1: 2004 EU Accession
plt.axvline(x=2004, color='green', linestyle='--', linewidth=1.5, alpha=0.7)
plt.text(2004.2, df_filtered[gdp_column].min(), '2004: EU Accession\n(V4 joined)', 
         color='green', fontsize=10, verticalalignment='bottom')

# Milestone 2: 2008 Global Financial Crisis
plt.axvline(x=2008, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
plt.text(2008.2, df_filtered[gdp_column].min(), '2008: Global\nFinancial Crisis', 
         color='red', fontsize=10, verticalalignment='bottom')

# Milestone 3: 2020 COVID-19 Pandemic
plt.axvline(x=2020, color='purple', linestyle='--', linewidth=1.5, alpha=0.7)
plt.text(2020.2, df_filtered[gdp_column].min(), '2020: COVID-19\nPandemic', 
         color='purple', fontsize=10, verticalalignment='bottom')

# --- FORMATTING AND LABELS ---
plt.title('GDP per Capita Growth in V4 Countries (1995 - 2023)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('GDP per capita (Constant 2015 US$)', fontsize=12, fontweight='bold')

# Customize the legend
plt.legend(title='Country', title_fontsize='13', fontsize='11', loc='upper left')

# Adjust x-axis ticks to show every 2 years
plt.xticks(range(1995, 2024, 2))

# Save the image for GitHub
output_image = 'v4_gdp_growth_milestones.png'
plt.tight_layout()
plt.savefig(output_image, dpi=300)

print(f"\nSuccess! The line chart has been saved as: {output_image}")

# Display the chart
plt.show()
