This project automatically extracts **screenshots and images** from `.docx` files and saves them into organized folders.  
It is especially useful for AI/ML workflows, documentation cleanup, or preparing datasets.

---

## ✨ Features
- Works with **any `.docx` file**
- Extracts all embedded images (PNG, JPG, etc.)
- Organizes images into **folders named after the document**
- Automatically generates a **ZIP file** per document
- Batch processing: handles multiple `.docx` files at once

---

## 📂 Folder Structure
docx-image-extractor/
│── input_docs/ # Put your .docx files here
│── output_images/ # Images will be saved here
│── extract_images.py # Main extraction script
│── README.md # Project documentation

---

## ⚙️ Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/docx-image-extractor.git
   cd docx-image-extractor
Create & activate a virtual environment:
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
Install dependencies:
pip install python-docx
🚀 Usage
Place one or more .docx files into the input_docs/ folder.
Run the script:
python extract_images.py
Extracted images will appear in:
output_images/<document_name>/
Each folder will also contain a .zip file for easy download/share.
🧾 Example
Input:
input_docs/
   ├── Contract1.docx
   ├── Report.docx
Output:
output_images/
   ├── Contract1/
   │    ├── image_1.png
   │    ├── image_2.png
   │    └── Contract1.zip
   ├── Report/
        ├── image_1.jpg
        ├── image_2.png
        └── Report.zip
🛠 Tech Stack
Python 3.8+
python-docx
🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.
