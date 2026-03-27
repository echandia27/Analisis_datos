import pandas as pd
import matplotlib.pyplot as plt

#configuracion opcional para ver mas clumnas en consola
pd.set_option("display.max_column",None)
pd.set_option("display.width", 1000)

# 1 cargar dataset
df = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")
print("\n primeras 5 filas")
print(df.head())

print("\n informacion general")
df.info()

print("\n DIMENSIONES DEL DATASET ---")
print(df.shape)

print("\n--- NOMBRES DE COLUMNAS ---")
print(df.columns.tolist())

print("\n--- VALORES NULOS POR COLUMNA ---")
print(df.isnull().sum())

print("\n--- DUPLICADOS ---")
print(df.duplicated().sum())

df.columns = df.columns.str.strip().str.lower()
df['orderdate'] = pd.to_datetime(df['orderdate'])
df.info()
print(df.duplicated().sum())
df = df.drop_duplicates()
df.isnull().sum()

#aqui se muentras el top 10 de los paises 
print("\n top paises\n")
sales_by_country = df.groupby('country')['sales']. sum().sort_values(ascending=False)
print(sales_by_country.head(10))

sales_by_country.head(10).plot(kind='bar')
plt.title("top paises por ingresos")
plt.ylabel("ventas")
plt.show()

#ahora mostraremos producto mas vendido
print("\n top producto \n")
sales_by_product = df.groupby('productline')['sales'].sum().sort_values(ascending=False)
print(sales_by_product)

sales_by_product.plot(kind='bar')
plt.title("ventas por linea de producto")
plt.ylabel("ventas")
plt.show()

#crecimiento atraves de los años 
print("\n crecimiento en años \n")
sales_by_year = df.groupby('year_id')['sales'].sum()
print(sales_by_year)

sales_by_year.plot(marker='o')
plt.title("ventas por año")
plt.ylabel("ventas")
plt.show()

print("\n numero de meses por año \n")
print(df.groupby('year_id')['month_id'].nunique())

#donde debe invertir la empresa
print("\n donde invertir \n")
sales_country_product = df.groupby(['country', 'productline'])['sales'].sum().sort_values(ascending=False)
print(sales_country_product.head(10))