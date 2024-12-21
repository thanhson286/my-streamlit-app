import streamlit as st
from file_processing import process_uploaded_file
from gpt_analysis import analyze_content

st.title("Trợ lý phân tích tài chính GPT-4")

# Upload tệp
uploaded_file = st.file_uploader("Tải lên báo cáo tài chính (PDF, Excel, Word, TXT, CSV)", type=["pdf", "xlsx", "xls", "docx", "txt", "csv"])

if uploaded_file is not None:
    try:
        # Xử lý nội dung từ tệp
        content = process_uploaded_file(uploaded_file)
        st.text_area("Nội dung tệp đã tải lên:", content, height=300)

        # Gửi tới GPT-4
        if st.button("Phân tích"):
            st.write("Đang phân tích... Vui lòng chờ.")
            result = analyze_content(content)
            st.text_area("Kết quả phân tích:", result, height=300)

    except ValueError as e:
        st.error(f"Lỗi: {e}")
    except Exception as e:
        st.error(f"Có lỗi xảy ra: {e}")
