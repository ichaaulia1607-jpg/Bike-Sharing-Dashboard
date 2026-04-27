# Proyek Analisis Data: Bike Sharing Dataset 🚲

## Identitas
* **Nama**: Icha Aulia Putri
* **Email**: ichaaulia1607@gmail.com
* **ID Dicoding**: cdcc220d6x2697

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda guna memahami pola penggunaan berdasarkan kondisi cuaca dan tren waktu. Hasil analisis ini disajikan dalam dashboard interaktif yang dibangun menggunakan library Streamlit.

## Struktur Folder
```text
.
├── dashboard/
│   ├── dashboard.py       # File utama aplikasi Streamlit
│   └── main_data.csv      # Data hasil pembersihan untuk dashboard
├── data/
│   ├── day.csv            # Dataset harian asli
│   └── hour.csv           # Dataset per jam asli
├── notebook.ipynb         # Dokumentasi proses analisis data (Notebook)
├── README.md              # Dokumentasi proyek
├── requirements.txt       # Daftar library Python yang dibutuhkan
└── url.txt                # Tautan dashboard (jika sudah di-deploy)
```

# Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

# Setup Environment - Terminal/Command Prompt
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
# Cara Menjalankan Dashboard
```bash
streamlit run dashboard/dashboard.py
```
## Fitur Interaktif
Dashboard ini memiliki filter **Rentang Waktu** di sidebar yang akan merubah tampilan grafik secara dinamis.
