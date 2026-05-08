# Nayla - AI Sales Chatbot Hexxamind

Chatbot AI spesialis penjualan jasa pengembangan aplikasi digital. Dibuat untuk **Hexxamind** — perusahaan milik **Sunarno**.

Ditenagai oleh **Google Gemini AI**, chatbot ini bertindak sebagai sales profesional bernama **Nayla** yang siap membantu calon klien mulai dari konsultasi hingga closing.

## Fitur

-  Bertindak sebagai sales profesional (Nayla) dengan strategi penjualan terstruktur
-  Menjual 5 layanan: **Website**, **Android**, **iOS**, **Desktop**, dan **Custom App**
-  Harga produk sudah ditentukan dalam IDR
-  Quick replies untuk respons cepat
-  Typing indicator animasi
-  Multi-session (banyak pengguna bisa chat bersamaan)
-  Dark theme UI yang modern dan responsif
-  API key aman via `.env` (tidak terekspos ke GitHub)
-  Footer dengan kontak WA & email

## Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| Backend  | Python + FastAPI |
| AI       | Google Gemini 1.5 Flash |
| Frontend | HTML, CSS, JavaScript (Vanilla) |
| Server   | Uvicorn |

## Cara Instalasi

### Prasyarat

- Python 3.10+
- Pip (Python package manager)
- API key Gemini ([dapatkan gratis di sini](https://makersuite.google.com/app/apikey))

### Langkah-langkah

1. **Clone repositori**

```bash
git clone https://github.com/sunarno85/chatbot_sales.git
cd chatbot_sales
```

2. **Buat file environment**

```bash
copy .env.example .env
```

3. **Isi API key** di file `.env`

```
GEMINI_API_KEY=api_key_kamu_disini
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Jalankan aplikasi**

```bash
python main.py
```

6. **Buka di browser**

```
http://localhost:8000
```

## Cara Penggunaan

1. Buka `http://localhost:8000` di browser
2. Chat dengan **Nayla** seperti biasa
3. Gunakan **quick replies** untuk pilihan cepat:
   -  `Saya mau buat website`
   -  `Saya mau buat aplikasi Android`
   -  `Saya mau buat aplikasi iOS`
   -  `Saya mau buat aplikasi Desktop`
   -  `Saya mau konsultasi dulu`
4. Nayla akan merespon dengan ramah dan membantu sesuai kebutuhan Anda

## API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET    | `/`      | Menampilkan halaman chat |
| POST   | `/api/chat` | Kirim pesan ke chatbot |
| POST   | `/api/reset` | Reset session chat |

### Contoh Request Chat

```json
POST /api/chat
{
  "session_id": "user123",
  "message": "Halo, saya ingin buat website toko online"
}
```

### Contoh Response

```json
{
  "reply": "Halo! Senang bertemu dengan Anda...",
  "session_id": "user123"
}
```

## Struktur Proyek

```
chatbot_sales/
├── main.py              # Backend FastAPI + integrasi Gemini
├── requirements.txt     # Dependencies Python
├── .env                 # API key (tidak di-commit)
├── .env.example         # Template .env untuk developer
├── .gitignore           # File yang diabaikan git
├── README.md            # Dokumentasi ini
└── static/
    └── index.html       # Frontend chat UI
```

## Keamanan

- API key disimpan di `.env` yang sudah masuk `.gitignore`
- File `.env.example` aman di-commit sebagai template
- Tidak ada data sensitif yang terekspos ke publik

## Harga & Spesifikasi Layanan

### Website Development
| Paket | Harga | Fitur |
|-------|-------|-------|
| Landing Page | Rp 2.500.000 | 1 halaman, responsif, form kontak, hosting 1 thn, domain, SSL |
| Company Profile | Rp 5.000.000 | 5-10 halaman, profil, galeri, admin dashboard, hosting 1 thn, domain, SSL |
| E-commerce | Rp 10.000.000 | Manajemen produk, keranjang, checkout, payment gateway, dashboard admin |
| Portal/Sistem | Rp 15.000.000+ | Database, multi-user, role management, API integration |

### Mobile Development (Android & iOS)
| Paket | Harga | Platform |
|-------|-------|----------|
| Aplikasi Sederhana | Rp 15.000.000+ | Android (Play Store) & iOS (App Store) |
| Aplikasi Menengah | Rp 25.000.000+ | Native (Kotlin/Swift) atau Hybrid (Flutter/React Native) |
| Aplikasi Kompleks | Rp 40.000.000+ | Fitur advance, offline mode, custom UI/UX, admin panel |

### Desktop Development
| Paket | Harga | Platform |
|-------|-------|----------|
| Aplikasi Sederhana | Rp 12.000.000+ | Windows / Cross-platform (Electron/Flutter) |
| Aplikasi Menengah | Rp 20.000.000+ | Multi-user, import/export, cetak laporan |
| Aplikasi Enterprise | Rp 35.000.000+ | Client-server, realtime sync, role management |

### Custom Application
| Layanan | Harga |
|---------|-------|
| Konsultasi & Analisis | **GRATIS** |
| Pengembangan Custom | Mulai Rp 20.000.000 |
| Integrasi Sistem | Mulai Rp 8.000.000 |
| Migrasi Data | Mulai Rp 5.000.000 |
| Maintenance & Support | Rp 500.000 - 2.000.000/bulan |

## Kontak

- **WhatsApp:** [085729158209](https://wa.me/6285729158209)
- **Email:** v1ck4zy@gmail.com
- **Copyright:** © 2026 Hexxamind by Sunarno

## Lisensi

Hak cipta dilindungi. Hexxamind — Sunarno.
