import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('delivered_orders.csv')

# Memastikan kolom 'customer_delivery_date' bertipe data datetime dan mengambil tanggalnya saja.
df['customer_delivery_date'] = pd.to_datetime(df['customer_delivery_date'], errors='coerce').dt.date

# Judul pada dashboard
st.title("Dashboard Jumlah Pesanan Berdasarkan Tanggal")

# Menampilkan DataFrame
st.subheader("Data Pesanan")
st.dataframe(df)

# Menghitung jumlah pesanan per tanggal pengiriman
# Setiap baris mewakili satu pesanan, jadi  menghitung berapa banyak pesanan pada setiap tanggal
df_count = df.groupby('customer_delivery_date').size().reset_index(name='jumlah_pesanan')

# Memfilter berdasarkan rentang tanggal
st.subheader("Filter Rentang Tanggal")
start_date = st.date_input("Tanggal Mulai", df['customer_delivery_date'].min())
end_date = st.date_input("Tanggal Akhir", df['customer_delivery_date'].max())

# Merubah start_date dan end_date ke datetime agar bisa digunakan untuk perbandingan dengan data.
start_date = pd.to_datetime(start_date).date()
end_date = pd.to_datetime(end_date).date()

# Memfilter data berdasarkan rentang tanggal yang dipilih
filtered_df = df[(df['customer_delivery_date'] >= start_date) & 
                 (df['customer_delivery_date'] <= end_date)]

# Menghitung jumlah pesanan per tanggal yang difilter
filtered_df_count = filtered_df.groupby('customer_delivery_date').size().reset_index(name='jumlah_pesanan')

# Menampilkan data yang telah difilter
st.subheader("Data Pesanan yang Difilter")
st.dataframe(filtered_df_count)

# Menampilkan grafik berdasarkan data yang difilter
st.subheader("Grafik Jumlah Pesanan per Tanggal (Filtered)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df_count['customer_delivery_date'], filtered_df_count['jumlah_pesanan'], marker='o', color='g', label="Jumlah Pesanan")
ax.set_xlabel("Tanggal Pengiriman")
ax.set_ylabel("Jumlah Pesanan")
ax.set_title("Tren Jumlah Pesanan Berdasarkan Tanggal Pengiriman (Filtered)")
ax.legend()

fig.autofmt_xdate()
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
st.pyplot(fig)
