import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")
df = pd.read_excel("v4_analytical_database.xlsx")

# Szûrés egy stabil közelmúltbeli évre (pl. 2021, ahol a legtöbb adat már teljes)
target_year = 2021
df_year = df[df['Year'] == target_year].copy()

# Szükséges oszlopok
gdp_col = 'GDP per capita (constant 2015 US$)'
life_exp_col = 'Life expectancy at birth, total (years)'
pop_col = 'Population, total'

# --- VIZUALIZÁCIÓ BEÁLLÍTÁSA ---
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# Buborékdiagram rajzolása (A scatterplot méret paraméterével)
bubble = sns.scatterplot(
    data=df_year, 
    x=gdp_col, 
    y=life_exp_col, 
    size=pop_col, 
    sizes=(500, 3000),  # Buborékok mérettartománya
    hue='Country Name', # Országok szerinti színezés
    palette='Set2', 
    alpha=0.8, 
    edgecolor='black'
)

# Egyedi feliratok hozzáadása a buborékok mellé
for i in range(df_year.shape[0]):
    plt.text(df_year[gdp_col].iloc[i], 
             df_year[life_exp_col].iloc[i] + 0.2, # Kicsit eltoljuk felfelé a szöveget
             df_year['Country Name'].iloc[i], 
             horizontalalignment='center', size='medium', color='black', weight='semibold')

# Cím és formázás
plt.title(f'V4 Wealth vs. Health Overview ({target_year})\nBubble size represents Total Population', 
          fontsize=16, fontweight='bold', pad=15)
plt.xlabel('GDP per capita (Constant 2015 US$)', fontsize=12, fontweight='bold')
plt.ylabel('Life Expectancy at Birth (Years)', fontsize=12, fontweight='bold')

# Eltávolítjuk az alapértelmezett, csúnya legendát
bubble.legend_.remove()

output_image = 'v4_health_wealth_bubble.png'
plt.tight_layout()
plt.savefig(output_image, dpi=300)

print(f"\nSuccess! The bubble chart has been saved as: {output_image}")
plt.show()
