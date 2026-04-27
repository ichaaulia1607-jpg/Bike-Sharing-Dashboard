import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style='whitegrid')

# --- 1. Fungsi Load Data Sederhana ---
@st.cache_data
def load_data():
    try:
        day_df = pd.read_csv("main_data.csv")
        hour_df = pd.read_csv("hour_data.csv")
        
        # Konversi kolom tanggal
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        
        return day_df, hour_df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return None, None

day_df, hour_df = load_data()

if day_df is not None and hour_df is not None:
    
    # --- 2. Sidebar Filter ---
    with st.sidebar:
        st.header("Proyek Analisis Data")
        st.write(f"Nama: Icha Aulia Putri")
        
        # Filter Rentang Tanggal
        min_date = day_df["dteday"].min()
        max_date = day_df["dteday"].max()
      
        date_range = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )

    # Logika filter data
    if len(date_range) == 2:
        start_date, end_date = date_range
        main_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                             (day_df["dteday"] <= pd.to_datetime(end_date))]
    else:
        main_day_df = day_df

    # --- 3. Main Page ---
    st.title('Bike Sharing Analytics Dashboard 🚲')

    # Visualisasi 1: Cuaca 
    st.subheader('Penyewaan Sepeda berdasarkan Kondisi Cuaca')
    weather_rentals = main_day_df.groupby(by="weathersit").cnt.mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Warna seragam kecuali yang tertinggi sebagai PETUNJUK
    colors = ["#D3D3D3"] * len(weather_rentals)
    if not weather_rentals.empty:
        max_idx = weather_rentals['cnt'].idxmax()
        colors[max_idx] = "#72BCD4" 

    sns.barplot(
        x='weathersit', 
        y='cnt', 
        data=weather_rentals, 
        hue='weathersit', 
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_xlabel('Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan)')
    ax.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)
    
    with st.expander("Lihat Insight"):
        st.write("Insight: Cuaca cerah (1) memiliki rata-rata penyewaan tertinggi. Warna biru pada grafik berfungsi sebagai penanda visual utama untuk kategori terbaik.")

    # Visualisasi 2: Tren Jam (Format Jam 00:00)
    st.subheader('Tren Penyewaan per Jam (Hari Kerja)')
    workingday_df = hour_df[hour_df["workingday"] == 1]
    hourly_registered = workingday_df.groupby(by="hr").registered.mean().reset_index()

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hr', y='registered', data=hourly_registered, marker='o', color='#72BCD4', ax=ax2)
  
    # Format Jam
    hours_label = [f"{int(x):02d}:00" for x in range(0, 24)]
    ax2.set_xticks(range(0, 24))
    ax2.set_xticklabels(hours_label, rotation=45)
    
    st.pyplot(fig2)

    st.caption('Copyright (c) Icha Aulia Putri 2026')