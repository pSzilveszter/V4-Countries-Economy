import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")
df = pd.read_excel("v4_analytical_database.xlsx")

# Filter for Hungary and the period between 1995 and 2023
df_hu = df[(df['Country Name'] == 'Hungary') & (df['Year'] >= 1995) & (df['Year'] <= 2023)].copy()

# Define the exact column names required for the analysis
gdp_growth_col = 'GDP growth (annual %)'
inflation_col = 'Inflation, consumer prices (annual %)'

# --- VISUALIZATION SETUP ---
fig, ax1 = plt.subplots(figsize=(14, 7))

# Axis 1: GDP Growth (Bar chart)
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontweight='bold', fontsize=12)
ax1.set_ylabel('GDP Growth (Annual %)', color=color1, fontweight='bold', fontsize=12)
bar = ax1.bar(df_hu['Year'], df_hu[gdp_growth_col], color=color1, alpha=0.6, label='GDP Growth')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_xticks(range(1995, 2024, 2))
ax1.axhline(0, color='black', linewidth=1) # Baseline at zero

# Axis 2: Inflation (Line chart, sharing the same x-axis)
ax2 = ax1.twinx()  
color2 = 'tab:red'
ax2.set_ylabel('Inflation (Consumer Prices %)', color=color2, fontweight='bold', fontsize=12)
line = ax2.plot(df_hu['Year'], df_hu[inflation_col], color=color2, linewidth=3, marker='o', label='Inflation')
ax2.tick_params(axis='y', labelcolor=color2)

# Title and combined legend
plt.title('Hungary: Economic Growth vs. Inflation (1995 - 2023)', fontsize=18, fontweight='bold', pad=20)
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.85), fontsize=11)

# Save the image for GitHub
output_image = 'hungary_gdp_vs_inflation.png'
plt.tight_layout()
plt.savefig(output_image, dpi=300)

print(f"\nSuccess! The dual-axis chart has been saved as: {output_image}")
plt.show()
