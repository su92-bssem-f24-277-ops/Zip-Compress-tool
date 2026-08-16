# Tactical Zip Compress Tool 🗂️⚡

A modern, high-performance web application for compressing single files and archives into clean ZIP packages. Built with **Flask** and Python **`zipfile`**, featuring an eye-catching **Intelligence Dossier-inspired UI design system**, target file size limit validation, real-time status diagnostics, and dynamic in-memory stream processing.

---

## 💼 Key Features

- 🎨 **Tactical Intelligence Dossier UI**: Custom Manila folder aesthetic featuring scanline CRT background effects, agency stamps, and retro mono typography (`Bebas Neue`, `IBM Plex Mono`, `Share Tech Mono`).
- 📂 **Drag & Drop Archive Support**: Drag-and-drop file uploader supporting instant archive selection (`.zip`, `.rar`, `.tar`, `.tgz`, `.tar.gz`, `.tbz2`, `.txz`).
- ⚡ **In-Memory Stream Compression**: Compresses files in RAM using `io.BytesIO` and Python `zipfile` with maximum DEFLATED compression (`level 9`) without writing temporary files to server disk.
- 🎯 **Target Size Validation**: Custom target byte limits (e.g., `100000` bytes) with automated header inspection (`X-Compressed-Bytes` vs `X-Target-Bytes`) and status alerts.
- 🛡️ **Payload Protection & Error Handling**: Accepts file uploads up to **200 MB** with custom Flask payload handling and archive validation.
- 🔗 **Instant Download Generation**: Streams generated ZIP files directly to the user's browser with attachment download triggers.

---

## 📋 Repository Structure

```text
Zip-Compress-tool/
│
├── app.py                  # Main Flask application & ZIP compression engine
├── templates/
│   └── index.html          # Dossier web interface (HTML5 / CSS3 / Vanilla JS)
├── requirements.txt        # Python dependency manifest
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## 🛠️ Technologies Used

- **Backend:** Python 3.8+, Flask, `zipfile`, `rarfile` (optional)
- **Frontend:** HTML5, Modern CSS3 (Custom Variables, Scanlines, Vintage Manila Folder styling), JavaScript (Fetch API & Drag-and-Drop)
- **Typography:** Google Fonts (`Bebas Neue`, `IBM Plex Mono`, `Share Tech Mono`)
- **Stream Processing:** `io.BytesIO`, Python Standard Library `zipfile`

---

## ⚙️ REST API Reference

### Compress File Endpoint

Compresses an uploaded file into a high-density ZIP archive.

- **URL:** `/compress`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`

#### Form Parameters

| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `file_a` | File | The target archive file to compress | **Yes** |
| `target_size` | Integer | Target size limit in bytes (Default: `100000`) | No |

#### Response Headers

| Header | Example Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/zip` | Binary zip payload stream |
| `Content-Disposition` | `attachment; filename="file.zip"` | Triggers browser file download |
| `X-Compressed-Bytes` | `45230` | Final compressed size in bytes |
| `X-Target-Bytes` | `100000` | User requested target size |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your machine.

```bash
python --version
```

### Installation

1. **Create and Activate a Virtual Environment:**

   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   python app.py
   ```

4. **Access the Web Interface:**  
   Open your browser and navigate to `http://127.0.0.1:5002`.

---

## 📄 License

This project is available under the **MIT License**. Free to use, modify, and distribute with proper attribution.

---

## 👨‍💻 Author

**Malik Lateef**  
*Software Engineering Student*  
📍 Lahore, Pakistan  
📧 Email: imaliklateef@gmail.com  

*Developed as part of practical learning to demonstrate web development with Flask, stream processing, and custom UI design.*
