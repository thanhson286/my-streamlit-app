import pdfplumber
import pandas as pd
from docx import Document

# Đọc PDF
def read_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc tệp PDF: {e}")

# Đọc Excel
def read_excel(file):
    try:
        # Kiểm tra loại tệp (xls hoặc xlsx)
        file_name = file.name.lower()
        if file_name.endswith(".xls"):
            return pd.read_excel(file, engine="xlrd").to_string()
        elif file_name.endswith(".xlsx"):
            return pd.read_excel(file, engine="openpyxl").to_string()
        else:
            raise ValueError("Định dạng Excel không được hỗ trợ.")
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc tệp Excel: {e}")

# Đọc Word
def read_word(file):
    try:
        doc = Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
        return text
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc tệp Word: {e}")

# Đọc TXT
def read_txt(file):
    try:
        return file.read().decode("utf-8")
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc tệp TXT: {e}")

# Đọc CSV
def read_csv(file):
    try:
        df = pd.read_csv(file)
        return df.to_string()
    except Exception as e:
        raise ValueError(f"Lỗi khi đọc tệp CSV: {e}")

# Xử lý tệp tải lên
def process_uploaded_file(uploaded_file):
    try:
        # MIME types cho các loại tệp
        if uploaded_file.type == "application/pdf":
            return read_pdf(uploaded_file)
        elif uploaded_file.type in ["application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
            return read_excel(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return read_word(uploaded_file)
        elif uploaded_file.type == "text/plain":
            return read_txt(uploaded_file)
        elif uploaded_file.type == "text/csv":
            return read_csv(uploaded_file)
        else:
            raise ValueError("Định dạng tệp không được hỗ trợ.")
    except Exception as e:
        raise ValueError(f"Lỗi khi xử lý tệp tải lên: {e}")
