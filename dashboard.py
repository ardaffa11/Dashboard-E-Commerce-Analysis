import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged_data = pd.read_csv('merged_data2.csv')
merged_data_product = pd.read_csv('merged_data_product.csv')

# Memastikan kolom 'customer_delivery_date' bertipe data datetime
merged_data['customer_delivery_date'] = pd.to_datetime(merged_data['customer_delivery_date'])
merged_data_product['customer_delivery_date'] = pd.to_datetime(merged_data_product['customer_delivery_date'])

# Dashboard 
st.title('Sales Dashboard')

# Filter berdasarkan Rentang Tanggal
st.sidebar.title("Filter Options")

# Memilih rentang tanggal untuk filter
start_date = st.sidebar.date_input('Start Date', merged_data['customer_delivery_date'].min())
end_date = st.sidebar.date_input('End Date', merged_data['customer_delivery_date'].max())

# Melakukan filtering data berdasarkan rentang tanggal
filtered_data = merged_data[(merged_data['customer_delivery_date'] >= pd.to_datetime(start_date)) & 
                             (merged_data['customer_delivery_date'] <= pd.to_datetime(end_date))]

filtered_data2 = merged_data_product[(merged_data_product['customer_delivery_date'] >= pd.to_datetime(start_date)) & 
                                    (merged_data_product['customer_delivery_date'] <= pd.to_datetime(end_date))]


# Bagian 1: Top 5 Produk Terlaris
# Menghitung jumlah penjualan per produk
product_sales = filtered_data2.groupby(['product_id']).size().reset_index(name='sales')

# Mengurutkan berdasarkan jumlah penjualan terbanyak
top_5_products = product_sales.sort_values(by='sales', ascending=False).head(5)

# Visualisasi Bar Chart untuk Top 5 Products
st.subheader('Top 5 Products by Sales')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_5_products, x='product_id', y='sales', palette='viridis', ax=ax)
ax.set_title('Top 5 Products by Sales')
ax.set_xlabel('Product ID')
ax.set_ylabel('Sales')
plt.xticks(rotation=90)
st.pyplot(fig)



# Bagian 2: Top 10 States by Total Products Sold
# Menghitung jumlah produk yang terjual di setiap state
sales_per_state = filtered_data.groupby('state').size().reset_index(name='total_products_sold')

# Mengurutkan berdasarkan jumlah produk terjual dan ambil 10 teratas
top_10_states = sales_per_state.sort_values(by='total_products_sold', ascending=False).head(10)

# Visualisasi Bar Chart untuk Top 10 States
st.subheader('Top 10 States by Total Products Sold')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_10_states, x='state', y='total_products_sold', palette='viridis', ax=ax2)
ax2.set_title('Top 10 States by Total Products Sold')
ax2.set_xlabel('State')
ax2.set_ylabel('Total Products Sold')
plt.xticks(rotation=90)
st.pyplot(fig2)


# Sidebar info
st.sidebar.write(f"Data filtered from {start_date} to {end_date}")
