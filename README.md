
# Flask REST API Blog

REST API Blog ini dibangun menggunakan Python dengan framework Flask dan menggunakan database MySQL. API ini menyediakan berbagai endpoint untuk mengelola data penulis, kategori, postingan, dan komentar pada blog.

## Fitur
- CRUD untuk **Authors** (Penulis)
- CRUD untuk **Categories** (Kategori)
- CRUD untuk **Posts** (Postingan)
- CRUD untuk **Comments** (Komentar)

## Teknologi yang Digunakan
- **Python 3.x**
- **Flask**
- **SQLAlchemy (ORM)**
- **MySQL/MariaDB**
- **Postman** (Untuk pengujian API)

## Demo

Aplikasi API Blog ini sudah dideploy dan dapat diakses melalui URL berikut:

[Demo Flask REST API Blog](https://flask-blog-api-aimdev.vercel.app/)


## Instalasi

### 1. Clone Repository
Clone repository ini ke dalam direktori lokal:

```bash
git clone https://github.com/username/repository.git
```

### 2. Membuat Virtual Environment
Buat virtual environment dan aktifkan dalam direktori lokal:

```bash
python -m venv venv
# Untuk Windows
venv\Scripts\activate
# Untuk MacOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
Instal semua dependencies yang diperlukan dengan pip:
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Database

1. Buat database MySQL dengan nama sesuai yang Anda inginkan (misalnya `db_blog_api`).

2. Buat file `.env` di root direktori proyek dan isi dengan konfigurasi database Anda:

```env
DB_USERNAME=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=db_blog_api
```

3. Konfigurasi database di file `config.py` menggunakan environment variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USERNAME')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)
```

4. Pastikan file `.env` sudah ditambahkan ke dalam `.gitignore` untuk keamanan:

```
# .gitignore
.env
venv/
__pycache__/
```

### 5. Menjalankan Aplikasi

Untuk menjalankan aplikasi, gunakan perintah berikut:

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`.



## Endpoint API

### 1. Authors
- **GET** `/api/authors`: Mendapatkan semua penulis.
- **GET** `/api/authors/<id>`: Mendapatkan data penulis berdasarkan ID.
- **POST** `/api/authors`: Menambahkan penulis baru.
- **PUT** `/api/authors/<id>`: Memperbarui data penulis berdasarkan ID.
- **DELETE** `/api/authors/<id>`: Menghapus penulis berdasarkan ID.

### 2. Categories
- **GET** `/api/categories`: Mendapatkan semua kategori.
- **POST** `/api/categories`: Menambahkan kategori baru.
- **DELETE** `/api/categories/<id>`: Menghapus kategori berdasarkan ID.

### 3. Posts
- **GET** `/api/posts`: Mendapatkan semua postingan.
- **GET** `/api/posts/<id>`: Mendapatkan data postingan berdasarkan ID.
- **POST** `/api/posts`: Menambahkan postingan baru.
- **PUT** `/api/posts/<id>`: Memperbarui postingan berdasarkan ID.
- **DELETE** `/api/posts/<id>`: Menghapus postingan berdasarkan ID.

### 4. Comments
- **GET** `/api/comments`: Mendapatkan semua komentar.
- **POST** `/api/comments`: Menambahkan komentar baru.
- **DELETE** `/api/comments/<id>`: Menghapus komentar berdasarkan ID.


## Pengujian API

Untuk pengujian API, Anda dapat menggunakan alat seperti **Postman** untuk melakukan permintaan HTTP ke endpoint yang telah disediakan.

## Struktur Proyek
```
Flask Blog API/
├── venv/                       # Virtual environment
├── models/                     # Menyimpan definisi model ORM SQLAlchemy untuk tabel-tabel (authors, categories, posts, comments)
|   ├── AuthorModel.py          # Model untuk tabel authors (penulis)
|   ├── CategoryModel.py        # Model untuk tabel categories (kategori)
|   ├── PostModel.py            # Model untuk tabel posts (postingan)
|   └── CommentModel.py         # Model untuk tabel comments (komentar)
|
├── controllers/                # Mengelola logika API, seperti validasi data dan interaksi antara model dan rute
|   ├── AuthorController.py     # Kontroler untuk menangani logika terkait author
|   ├── CategoryController.py   # Kontroler untuk menangani logika terkait kategori
|   ├── PostController.py       # Kontroler untuk menangani logika terkait postingan
|   └── CommentController.py    # Kontroler untuk menangani logika terkait komentar
|
├── routes/                     # Menyimpan definisi rute dan endpoint API
|   ├── AuthorRoute.py          # Rute untuk menangani permintaan terkait authors
|   ├── CategoryRoute.py        # Rute untuk menangani permintaan terkait categories
|   ├── PostRoute.py            # Rute untuk menangani permintaan terkait posts
|   └── CommentRoute.py         # Rute untuk menangani permintaan terkait comments
|
├── README.md                   # Dokumentasi proyek
├── .env                        # File konfigurasi untuk menyimpan variabel lingkungan (misalnya, konfigurasi database)
├── .gitignore                  # Daftar file dan folder yang harus diabaikan oleh git
├── vercel.json                 # File konfigurasi untuk deploy ke Vercel
├── requirements.txt            # Daftar dependensi aplikasi (misal: Flask, SQLAlchemy, dll)
├── config.py                   # File konfigurasi untuk pengaturan aplikasi, termasuk konfigurasi database
└── app.py                      # File utama yang menjalankan aplikasi Flask
```

## Authors

Proyek ini dikembangkan oleh [@grimaimm](https://www.github.com/grimaimm). Untuk informasi lebih lanjut atau pertanyaan, Anda dapat menghubungi saya melalui GitHub [@grimaimm](https://www.github.com/grimaimm).

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

