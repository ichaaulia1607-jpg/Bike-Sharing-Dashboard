import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# --- 1. Load Data ---
# Memastikan path sesuai dengan struktur yang diminta Dicoding
# --- 1. Load Data ---
def load_data():
    # Mencoba membaca file main_data.csv
    try:
        # Jika dijalankan dari folder utama (root)
        day_df = pd.read_csv("dashboard/main_data.csv")
    except FileNotFoundError:
        # Jika dijalankan dari dalam folder dashboard
        day_df = pd.read_csv("main_data.csv")
    
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    
    # Mencoba membaca file hour.csv
    try:
        hour_df = pd.read_csv("data/hour.csv")
    except FileNotFoundError:
        try:
            hour_df = pd.read_csv("hour.csv")
        except FileNotFoundError:
            # Jika file hour tidak ditemukan sama sekali, kita buat data kosong agar tidak crash
            st.error("File hour.csv tidak ditemukan di folder data!")
            hour_df = pd.DataFrame()
        
    return day_df, hour_df

day_df, hour_df = load_data()

# --- 2. Sidebar (Fitur Interaktif & ID Dicoding) ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Filter Rentang Waktu (Kriteria Wajib Interaktif)
    min_date = day_df["dteday"].min()
    max_date = day_df["dteday"].max()
    
    st.write("### Filter Dashboard")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    st.write("---")
    # Menambahkan ID Dicoding sesuai instruksi reviewer
    st.write("**Nama:** Icha Aulia Putri")
    st.write("**ID Dicoding:** cdcc220d6x2697")

# Menghubungkan Filter Tanggal ke Data
main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                 (day_df["dteday"] <= str(end_date))]

# --- 3. Main Page ---
st.header('Bike Sharing Analytics Dashboard 🚲')

# Visualisasi 1: Kondisi Cuaca (Menggunakan Codingan Icha)
st.subheader('Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    x='weathersit',
    y='cnt',
    data=main_df, # Data ini sudah terpengaruh filter tanggal di sidebar
    palette='viridis',
    ax=ax
)

ax.set_title('Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca', fontsize=15)
ax.set_xlabel('Kondisi Cuaca', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Penyewaan', fontsize=12)
st.pyplot(fig)


# Visualisasi 2: Tren per Jam (Menggunakan Codingan Icha)
st.subheader('Tren Penyewaan Sepeda oleh Pengguna Terdaftar per Jam (Hari Kerja)')

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