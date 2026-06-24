# XÂY DỰNG ỨNG DỤNG TÍNH RA CON GIÁP CỦA NĂM
## UI gồm có 3 phần: Giới thiệu đây là ứng dụng gì/ Nhập số năm muốn tính/ Trả lại kết quả ra con giáp và ý nghĩa của nó
## Người dùng có thể là người nước ngoài cần tìm hiểu về văn hoá Á Đông.
## Khi người dùng lựa chọn ngôn ngữ, toàn bộ kịch bản sẽ tự động dịch sang ngôn ngữ của người dùng.


# 1. IMPORT STREAMLIT VÀ DEEP_TRANSLATOR
import streamlit as st
st.set_page_config(layout="wide")
from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    if target_lang == "vi":
        return text
    try:
        translated = GoogleTranslator(source='vi', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"[Translation Error] {text}"
    

# 2. NHẬP KỊCH BẢN GỐC BẰNG TIẾNG VIỆT
## 2.1. Phần giới thiệu
KICH_BAN = {
    "title": "Ứng Dụng Tính Con Giáp Theo Năm",
    "intro_title": "🎎Chào mừng bạn đến với hành trình khám phá văn hóa Á Đông!🏮",
    "intro_text": "Văn hoá Á Đông - nơi thời gian không trôi đi theo một đường thẳng mà vận hành theo những vòng tuần hoàn kỳ diệu! Người xưa khi quan sát bầu trời đã nhận ra chu kỳ 12 năm tương ứng với hành trình của Sao Mộc và 12 lần Trăng tròn trong một năm, từ đó kết hợp cùng triết lý Âm Dương để chia dòng chảy vũ trụ thành 12 cột mốc định hình. Để biến những phép tính thiên văn trừu tượng ấy trở nên gần gũi và sống động trong đời sống thường nhật, cha ông chúng tôi đã khéo léo chọn ra 12 con vật thân thuộc làm biểu tượng đại diện. Mỗi con giáp không chỉ là một cột mốc thời gian, mà còn mang theo một cặp tính cách đối lập nhưng bù trừ hoàn hảo — như sự cần cù của Trâu đi đôi với cái trí của Chuột — tạo nên một bài học sâu sắc về sự cân bằng và hòa hợp giữa con người với tự nhiên.",
    "input_label": "Nhập năm bạn muốn tính (Ví dụ: 1995, 2026):",
    "button_text": "Tính con giáp",
    "result_text": "Năm {} thuộc tuổi con giáp: **{}**",
    "error_year": "Vui lòng nhập một năm hợp lệ lớn hơn 0."
}
## 2.2. Phần các con giáp: Khi trả ra kết quả các con giáp, sẽ tương ứng từng con có hình ảnh và ý nghĩa
THU_VIEN_CON_GIAP = {
    0: {"name": "Thân (Khỉ)", "img": "Than.jpg", "mean": "Thân: Nhanh nhẹn, sáng tạo và tài trí."},
    1: {"name": "Dậu (Gà)", "img": "Dau.jpg", "mean": "Dậu: Trách nhiệm, chính trực và đón nhận hào quang."},
    2: {"name": "Tuất (Chó)", "img": "Tuat.jpg", "mean": "Tuất: Trung thành, tin cậy và bảo vệ vẹn toàn."},
    3: {"name": "Hợi (Heo)", "img": "Hoi.jpg", "mean": "Hợi: An nhàn, sung túc và hạnh phúc tự tại."},
    4: {"name": "Tý (Chuột)", "img": "Tý (chuot).jpg", "mean": "Tý: Khởi đầu may mắn, nhạy bén và thịnh vượng."},
    5: {"name": "Sửu (Trâu)", "img": "Suu.jpg", "mean": "Sửu: Kiên trì, bền bỉ và nền tảng vững chắc."},
    6: {"name": "Dần (Hổ)", "img": "Dan.jpg", "mean": "Dần: Dũng cảm, uy quyền và ý chí kiên cường."},
    7: {"name": "Mão (Mèo/Thỏ)", "img": "Mao.jpg", "mean": "Mão: Tinh tế, hòa nhã và bình an."},
    8: {"name": "Thìn (Rồng)", "img": "Thin.jpg", "mean": "Thìn: Quyền lực, vận may và khát vọng lớn."},
    9: {"name": "Tỵ (Rắn)", "img": "Ti (ran).jpg", "mean": "Tỵ: Sâu sắc, nhạy bén và bí ẩn cuốn hút."},
    10: {"name": "Ngọ (Ngựa)", "img": "Horse.jpg", "mean": "Ngọ: Tự do, trung thành và không ngừng tiến bước."},
    11: {"name": "Mùi (Dê)", "img": "Mui.jpg", "mean": "Mùi: Nhân hậu, hòa thuận và nghệ thuật."}
}

# 3. THAO TÁC CỦA NGƯỜI DÙNG
# 3.1. Nút lựa chọn ngôn ngữ và tự động dịch
selected_lang_label = st.selectbox(
    "Chọn ngôn ngữ / Select Language / 选择语言:", 
    ["Tiếng Việt", "English (Tiếng Anh)", "Chinese (Tiếng Trung)"]
)

# Ánh xạ lựa chọn giao diện sang mã ngôn ngữ tiêu chuẩn của NLP
lang_map = {
    "Tiếng Việt": "vi",
    "English (Tiếng Anh)": "en",
    "Chinese (Tiếng Trung)": "zh-CN"
}
target_lang = lang_map[selected_lang_label]

# Tự động dịch tiêu đề và giới thiệu của App
app_title = translate_text(KICH_BAN["title"], target_lang)
intro_title = translate_text(KICH_BAN["intro_title"], target_lang)
intro_text = translate_text(KICH_BAN["intro_text"], target_lang)

st.title(app_title)
st.subheader(intro_title)

# Chia bố cục 2 bên cho đẹp mắt: 1 bên là phần giới thiệu nguồn gốc 12 con giáp, bên kia là kết quả tính
col1, col2 = st.columns(2)
with col1:
    st.write(intro_text)
    st.write("---")

# 3.2. Tính ra con giáp và trả về kết quả
## Tạo nút để nhập số năm:
with col2:
    input_label = translate_text(KICH_BAN["input_label"], target_lang)
    button_text = translate_text(KICH_BAN["button_text"], target_lang)

    year = st.number_input(input_label, min_value=1, max_value=9999, value=2026, step=1)

    if st.button(button_text):
        if year > 0:
            remainder = year % 12
            
            # Lấy tên con giáp gốc (Tiếng Việt) và link ảnh
            zodiac_vi_name = THU_VIEN_CON_GIAP[remainder]["name"]
            zodiac_img = THU_VIEN_CON_GIAP[remainder]["img"]
            zodiac_vi_mean = THU_VIEN_CON_GIAP[remainder]["mean"]
        
            # NLP tự động dịch tên con giáp sang ngôn ngữ đích
            zodiac_translated_name = translate_text(zodiac_vi_name, target_lang)
            zodiac_translated_mean = translate_text(zodiac_vi_mean, target_lang)
            # Dịch câu thông báo kết quả
            result_template = translate_text(KICH_BAN["result_text"], target_lang)
        
            # Hiển thị kết quả văn bản và ảnh
            # Lưu ý: result_template lúc này có dạng "Year {} belongs to..." hoặc "{} 年属于...", ta dùng .format() để chèn dữ liệu vào
            st.success(result_template.format(year, zodiac_translated_name))
            st.image(zodiac_img, caption=zodiac_translated_name, width=150)
            st.write(zodiac_translated_mean)
        
        else:
            error_year = translate_text(KICH_BAN["error_year"], target_lang)
            st.error(error_year)