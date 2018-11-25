import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

df = pd.read_csv("datos.csv")

plt.figure(figsize=(18,10))
plt.tick_params(labelsize=16)
plt.title("Tipo de galletita por paquete - Surtido Bagley", fontsize=22)
df.boxplot()
plt.figtext(0.99, 0.01, 'fuente de los datos: https://www.reddit.com/r/argentina/comments/9iv9jp/an%C3%A1lisis_de_un_paquete_surtido_bagley/', horizontalalignment='right')
plt.savefig("bagley")