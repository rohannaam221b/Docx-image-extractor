import os
import datetime

# Project title (you can make this dynamic if needed)
PROJECT_NAME = "Docx Image Extractor"

# Auto-detect folders
folders = [f for f in os.listdir() if os.path.isdir(f) and not f.startswith(".")]

# Current date
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# README content
readme_content = f"""# 🖼️ {PROJECT_NAME}

# Automatically extracts **screenshots and images** from `.docx` files and organizes them into folders.  
# This README was auto-generated on **{date_str}**.




"""