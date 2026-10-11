import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Khởi tạo dữ liệu
data = {
   'STT': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   'Họ và tên': ['An', 'Tiến', 'Tiền', 'Hào', 'Dũng', 'Đô', 'Tuấn', 'Thành', 'Thư', 'Thành Trung'],
    'Chuyên cần': [8, 9, 3, 10, 8, 6, 9, 8, 7, 10],
    'Giữa kỳ': [7, 8, 6, 3, 7, 5, 8, 7, 7, 9],
    'Cuối kỳ': [8, 8, 3, 6, 7, 6, 8, 6, 8, 9]
}
df = pd.DataFrame(data)
df.set_index('STT', inplace=True)

# 2. Xử lý tính toán (Điểm tổng kết & Xếp loại)
# Điểm tổng kết = 20% × Chuyên cần + 30% × Giữa kỳ + 50% × Cuối kỳ[cite: 1]
df['Tong_ket'] = df['Chuyên cần']*0.2 + df['Giữa kỳ']*0.3 + df['Cuối kỳ']*0.5

# Xếp loại sinh viên theo quy định[cite: 1]
def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'
df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 3. Xây dựng giao diện Web App bằng Streamlit
# Hiển thị tiêu đề Web App[cite: 1]
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# Hiển thị bảng điểm của 10 sinh viên[cite: 1]
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(df)

# Hiển thị các thông tin thống kê[cite: 1]
st.subheader("2. Thống kê")
dtb_lop = df['Tong_ket'].mean()
sv_cao_nhat = df[df['Tong_ket'] == df['Tong_ket'].max()]['Họ và tên'].tolist()
sv_thap_nhat = df[df['Tong_ket'] == df['Tong_ket'].min()]['Họ và tên'].tolist()
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {', '.join(sv_cao_nhat)}")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {', '.join(sv_thap_nhat)}")
st.write(f"- **Số sinh viên đạt:** {so_sv_dat}")

# Tạo danh sách xổ xuống (Selectbox) để chọn sinh viên và hiển thị chi tiết[cite: 1]
st.subheader("3. Tra cứu điểm sinh viên")
selected_student = st.selectbox("Chọn một sinh viên:", df['Họ và tên'])
student_info = df[df['Họ và tên'] == selected_student].iloc[0]

st.info(f"""
**Họ và tên:** {student_info['Họ và tên']}  
**Chuyên cần:** {student_info['Chuyên cần']} | **Giữa kỳ:** {student_info['Giữa kỳ']} | **Cuối kỳ:** {student_info['Cuối kỳ']}  
**Điểm tổng kết:** {student_info['Tong_ket']} | **Xếp loại:** {student_info['Xep_loai']}
""")

# Hiển thị biểu đồ cột điểm tổng kết[cite: 1]
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(df['Họ và tên'], df['Tong_ket'], color='#5D9CEB')
ax.set_title('Điểm tổng kết của 10 sinh viên')
ax.set_xlabel('Điểm')
ax.set_ylabel('Sinh viên')
ax.invert_yaxis()
st.pyplot(fig)

# Hiển thị họ tên và MSSV ở cuối trang Web App, kích thước chữ nhỏ[cite: 1]
st.markdown("---")
# LƯU Ý: Vui lòng thay đổi thông tin Tên và MSSV của bạn ở dòng dưới trước khi nộp bài
st.markdown("<p style='text-align: center; font-size: 12px;'>Người tạo: [Nguyễn Ngọc Nguyên] - MSSV: [060208009198]</p>", unsafe_allow_html=True)