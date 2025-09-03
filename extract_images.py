from docx import Document
import os, mimetypes, shutil

# Folders
input_dir = "input_docs"
output_base = "output_images"

os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_base, exist_ok=True)

# Loop over all .docx files in input folder
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".docx"):
        doc_path = os.path.join(input_dir, filename)
        doc_name = os.path.splitext(filename)[0]  # file name without extension

        # Create output folder for this document
        output_dir = os.path.join(output_base, doc_name)
        os.makedirs(output_dir, exist_ok=True)

        # Load the document
        doc = Document(doc_path)

        # Extract images
        image_count = 0
        for rel in doc.part.rels.values():
            if "image" in rel.reltype:
                image_count += 1
                img_bytes = rel.target_part.blob
                content_type = getattr(rel.target_part, "content_type", None)
                ext = mimetypes.guess_extension(content_type) if content_type else None
                if not ext:
                    ext = ".png"
                filename_out = f"image_{image_count}{ext}"
                with open(os.path.join(output_dir, filename_out), "wb") as f:
                    f.write(img_bytes)

      