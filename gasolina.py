import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# código de geração do gráfico 
df =pd.read_csv('gasolina.csv')
sns.set_style('darkgrid')
plt.figure(figsize=(8,6))
sns.lineplot(x='dia',y='venda',data=df, marker='d')
plt.title('Preço da gasolina', fontsize=14)
plt.xlabel('Dias', fontsize=12)
plt.ylabel('Preço(R$)', fontsize=12)

plt.tight_layout()

#código para mostrar o gráfico
plt.savefig('gasolina.png')
plt.show()
    