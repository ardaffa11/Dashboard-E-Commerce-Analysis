import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  

# Load the data
top_5_products = pd.read_csv('top_5_products.csv')  # Ganti path sesuai file Anda
top_10_states = pd.read_csv('top_10_states.csv')  # Ganti path sesuai file Anda

# Set title of the dashboard
st.title("Dashboard E-Commerce Analysis")

# Top 5 Produk Paling Banyak Terjual
st.subheader("Top 5 Produk Paling Banyak Terjual")
st.write("Berikut adalah 5 produk terlaris berdasarkan jumlah penjualan:")
st.dataframe(top_5_products)

# Visualisasi Top 5 Produk
fig1, ax1 = plt.subplots()
ax1.bar(top_5_products['product_id'], top_5_products['sales'], color='skyblue')
ax1.set_xlabel('Product ID')
ax1.set_ylabel('Sales')
ax1.set_title('Top 5 Produk Paling Banyak Terjual')
plt.xticks(rotation=90)
st.pyplot(fig1)

# Top 10 State dengan Pembelian Terbanyak
st.subheader("Top 10 State dengan Pembelian Terbanyak")
st.write("Berikut adalah 10 state dengan jumlah pembelian terbanyak:")
st.dataframe(top_10_states)

# Visualisasi Top 10 State
fig2, ax2 = plt.subplots()
ax2.bar(top_10_states['state'], top_10_states['total_products_sold'], color='orange')
ax2.set_xlabel('State')
ax2.set_ylabel('Total Products Sold')
ax2.set_title('Top 10 State dengan Pembelian Terbanyak')
plt.xticks(rotation=90)
st.pyplot(fig2)
