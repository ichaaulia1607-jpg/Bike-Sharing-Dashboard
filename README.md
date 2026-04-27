# Proyek Analisis Data: Bike Sharing Dataset 🚲

## Identitas
* **Nama**: Icha Aulia Putri
* **Email**: ichaaulia1607@gmail.com
* **ID Dicoding**: CDCC220D6X2697

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda guna memahami pola penggunaan berdasarkan kondisi cuaca dan tren waktu. Hasil analisis ini disajikan dalam dashboard interaktif yang dibangun menggunakan library Streamlit.

## Struktur Folder
```text
.
├── data/
│   ├── day.csv
│   └── hour.csv
├── dashboard.py       # File utama Streamlit
├── main_data.csv      # Data untuk dashboard
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
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
streamlit run dashboard.py
```
## Fitur Interaktif
Dashboard ini memiliki filter **Rentang Waktu** di sidebar yang akan merubah tampilan grafik secara dinamis.
