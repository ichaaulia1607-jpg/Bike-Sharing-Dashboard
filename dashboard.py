import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style agar dashboard terlihat profesional
sns.set(style='whitegrid')

@st.cache_data
def load_data():
    try:
        
        day_df = pd.read_csv("main_data.csv")
        hour_df = pd.read_csv("hour.csv") 
        
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        return day_df, hour_df
    except FileNotFoundError:
        # Antisipasi jika file berada di dalam folder dashboard/
        try:
            day_df = pd.read_csv("dashboard/main_data.csv")
            hour_df = pd.read_csv("dashboard/hour.csv")
            day_df['dteday'] = pd.to_datetime(day_df['dteday'])
            hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
            return day_df, hour_df
        except Exception as e:
            st.error(f"Gagal memuat data: {e}")
            return None, None

day_df, hour_df = load_data()

# Pastikan data ada sebelum lanjut
if day_df is not None and hour_df is not None:
    
    # --- 2. Sidebar (Identitas & Filter) ---
    with st.sidebar:
        st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
        st.write("### Informasi Mahasiswa")
        st.write("**Nama:** Icha Aulia Putri")
        st.write("**ID Dicoding:** CDCC220D6X2697")
        
        # Filter Rentang Waktu
        min_date = day_df["dteday"].min()
        max_date = day_df["dteday"].max()
        
        st.write("---")
        date_range = st.date_input(
            label='Pilih Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )

    # Logika Filter Tanggal
    if len(date_range) == 2:
        start_date, end_date = date_range
        main_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                             (day_df["dteday"] <= pd.to_datetime(end_date))]
        main_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                               (hour_df["dteday"] <= pd.to_datetime(end_date))]
    else:
        main_day_df = day_df
        main_hour_df = hour_df

    # --- 3. Main Dashboard ---
    st.header('Bike Sharing Analytics Dashboard 🚲')

    # Visualisasi 1: Kondisi Cuaca 
    st.subheader('Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
    weather_rentals = main_day_df.groupby(by="weathersit").cnt.mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))

    # Reviewer Note: Warna seragam
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
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    st.pyplot(fig)

    # Insight Visualisasi 1 (Kriteria Opsional 4)
    with st.expander("Lihat Insight Kondisi Cuaca"):
        st.write("Berdasarkan grafik, terlihat bahwa rata-rata penyewaan tertinggi terjadi pada kondisi cuaca cerah (1). "
                 "Hal ini ditunjukkan oleh batang berwarna biru yang berfungsi sebagai penanda visual utama.")

    # Visualisasi 2: Tren per Jam 
    st.subheader('Tren Penyewaan oleh Pengguna Terdaftar per Jam (Hari Kerja)')
    
    # Filter hari kerja dari data yang sudah terfilter tanggal
    workingday_df = main_hour_df[main_hour_df["workingday"] == 1]
    hourly_registered = workingday_df.groupby(by="hr").registered.mean().reset_index()

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        x='hr', 
        y='registered', 
        data=hourly_registered, 
        marker='o', 
        linewidth=2, 
        color='#72BCD4',
        ax=ax2
    )

    # Mengubah angka menjadi format jam (contoh: 08:00)
    hours_label = [f"{int(x):02d}:00" for x in range(0, 24)]
    ax2.set_xticks(range(0, 24))
    ax2.set_xticklabels(hours_label, rotation=45)
    
    ax2.set_xlabel('Jam')
    ax2.set_ylabel('Rata-rata Jumlah Pengguna Terdaftar')
    ax2.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig2)

    # Insight Visualisasi 2
    with st.expander("Lihat Insight Tren Jam"):
        st.write("Pada hari kerja, terjadi lonjakan penyewaan oleh pengguna terdaftar pada jam berangkat kantor (08:00) "
                 "dan jam pulang kantor (17:00-18:00).")

    st.caption('Copyright (c) Icha Aulia Putri 2026')