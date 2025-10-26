# 📚 Premium PDF Merger

A visually modern and user-friendly desktop application built in **Python + PyQt5** that allows users to easily merge multiple PDF files with thumbnail previews. Designed for simplicity, speed, and a professional UI experience.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| ✅ Professional GUI | Built using PyQt5 with clean and modern layout |
| ✅ Thumbnail Previews | Automatically generates previews of the first page |
| ✅ Reorder & Edit List | Add or remove PDFs as needed |
| ✅ Quick Merging | Simple process for combining multiple PDFs |
| ✅ No Internet Required | Fully offline desktop application |

---

## 🚀 Demo Overview

1. Click **Add PDFs**
2. Select multiple PDF files to merge
3. Preview appears with thumbnails + filenames
4. Remove if needed
5. Click **Merge PDFs**
6. Save your merged file anywhere

---

## 📦 Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/narendrasyadav/pdf-merger.git
cd premium-pdf-merger
```

### 2️⃣ Install Dependencies
```sh
pip install PyQt5 PyPDF2 pdf2image
```

**Windows users only**  
Install Poppler to enable thumbnail previews:  
https://github.com/oschwartz10612/poppler-windows/releases  
Add the `/bin` folder to PATH.

---

## ▶️ Usage

Run the application:
```sh
python main.py
```

---

## 🖼 UI Screenshot (Optional – you can add an image later)

| Preview |
|--------|
<img width="598" height="490" alt="image" src="https://github.com/user-attachments/assets/1606d9fd-a1fb-4ec1-b7f5-426c065e944d" />
 

---

## 🧩 Code Structure

```
📁 pdf-merger
│
├── merger.py              # Application entry point
├── README.md            # Project documentation
```

---

## 🔮 Future Enhancements

Planned upcoming improvements:

- Dark mode support
- Drag-and-drop PDF reordering
- Full page gallery view
- Progress indicator during merging
- `.exe` Windows build for installation

---

## 🤝 Contributing

Contributions are welcome. Fork the repository and submit a pull request for review.

---

## 📝 License

This project is licensed under the **MIT License**, which allows free personal and commercial use.

---

## ❤️ Acknowledgments

- Powered by **PyQt5** for UI
- Uses **PyPDF2** for merging logic
- Thanks to **pdf2image** and Poppler for PDF thumbnails
