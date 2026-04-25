import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# --- 1. Load Data ---
# Pastikan path file sesuai dengan folder di VS Code kamu
try:
    day_df = pd.read_csv("dashboard/main_data.csv")
    # Jika kamu punya file hour.csv terpisah, pastikan ada di folder dashboard
    hour_df = pd.read_csv("data/hour.csv") 
except:
    # Backup jika path di atas tidak terbaca (misal saat deploy)
    day_df = pd.read_csv("main_data.csv")
    hour_df = pd.read_csv("hour.csv")

# Header Dashboard
st.header('Bike Sharing Analytics Dashboard 🚲')

# Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.write("### Proyek Analisis Data")
    st.write("Nama: Icha Aulia Putri")

# --- Visualisasi 1: Kondisi Cuaca ---
st.subheader('☁️ Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
fig1, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(
    x='weathersit',
    y='cnt',
    data=day_df,
    palette='viridis',
    ax=ax1
)

ax1.set_title('Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca', fontsize=15)
ax1.set_xlabel('Kondisi Cuaca', fontsize=12)
ax1.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
st.pyplot(fig1)


# --- Visualisasi 2: Tren per Jam (Hari Kerja) ---
st.subheader('⏰ Tren Penyewaan Pengguna Terdaftar per Jam (Hari Kerja)')

# Menghitung rata-rata penyewaan per jam untuk hari kerja
workingday_hourly_df = hour_df[hour_df["workingday"] == 1].groupby("hr").registered.mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(
    x='hr',
    y='registered',
    data=workingday_hourly_df,
    marker='o',
    color='tab:blue',
    ax=ax2
)

ax2.set_title('Tren Penyewaan Sepeda oleh Pengguna Terdaftar per Jam (Hari Kerja)', fontsize=15)
ax2.set_xlabel('Jam (0-23)', fontsize=12)
ax2.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
ax2.set_xticks(range(0, 24))
ax2.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig2)

st.caption('Copyright (c) Icha Aulia Putri 2026')