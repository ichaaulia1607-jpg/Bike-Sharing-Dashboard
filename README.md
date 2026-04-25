# Proyek Analisis Data: Bike Sharing Dataset 🚲

## Deskripsi
Proyek ini merupakan hasil analisis data pada "Bike Sharing Dataset" yang berfokus pada pemahaman pola penyewaan sepeda berdasarkan kondisi cuaca dan tren waktu. Proyek ini mencakup seluruh siklus analisis data, mulai dari pengumpulan data (*Data Wrangling*), pembersihan data (*Cleaning*), eksplorasi (*EDA*), hingga pembuatan dashboard interaktif menggunakan Streamlit.

## Pertanyaan Bisnis
1. Bagaimana pengaruh kondisi cuaca (*weathersit*) terhadap rata-rata jumlah penyewaan sepeda harian?
2. Bagaimana tren penyewaan sepeda oleh pengguna terdaftar (*registered*) pada setiap jam di hari kerja (*working day*)?

## Struktur Folder
```text
.
├── dashboard/
│   ├── dashboard.py       # File utama aplikasi Streamlit
│   └── main_data.csv      # Data yang telah dibersihkan untuk dashboard
├── data/
│   ├── day.csv            # Dataset harian asli
│   └── hour.csv           # Dataset per jam asli
├── notebook.ipynb         # Dokumentasi proses analisis data (Notebook)
├── README.md              # Dokumentasi proyek
├── requirements.txt       # Daftar pustaka (library) Python yang dibutuhkan
└── url.txt                # Tautan dashboard (jika sudah di-deploy)
```

# Membuat environment baru
conda create --name main-ds python=3.9

# Mengaktifkan environment
conda activate main-ds

# Instalasi library yang dibutuhkan
pip install -r requirements.txt

# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment
# Windows:
venv\Scripts\activate

# Instalasi library
pip install -r requirements.txt
