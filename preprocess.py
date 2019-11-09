import re
import string
dict = [["ship", "vận chuyển"], ["shop", "cửa hàng"], ["m", "mình"], ["mik", "mình"], ["ko", "không"], ["k", "không"],
        ["kh", "không"], ["khong", "không"], ["kg", "không"], ["khg", "không"], ["tl", "trả lời"],
        ["rep", "trả lời"], ["r", "rồi"], ["fb", "facebook"], ["face", "faceook"], ["thanks", "cảm ơn"],
        ["thank", "cảm ơn"], ["tks", "cảm ơn"], ["tk", "cảm ơn"], ["ok\n", "tốt\n"], ["oki", "tốt"], ["okie", "tốt"],
        ["sp", "sản phẩm"], ['nhg', 'nhưng'],
        ["dc", "được"], ["vs", "với"], ["đt", "điện thoại"], ["thjk", "thích"], ["thik", "thích"], ["qá", "quá"],
        ["trể", "trễ"], ["bgjo", "bao giờ"], ["h", "giờ"], ["qa", "quá"], ["dep", "đẹp"], ["xau", "xấu"],
        ["ib", "nhắn tin"],
        ["cute", 'dễ thương'], ["sz", "size"], ["good", "tốt"], ["god", "tốt"], ["bt", "bình thường"],
        ["ks", "khách sạn"], ['deluxe', 'sang trọng'], ['seeview ', 'see view'], ['superior', 'cao cấp'],
        ["comment", "bình luận"], ["comments", "bình luận"], ["twin", "phòng đôi"], ['WC', 'nhà vệ sinh'],
        ['toilet', 'nhà vệ '
                   'sinh'],
        ['Toilet', 'nhà vệ sinh'], ['feedback', 'phản hồi'], ['Danh gia', 'Đánh giá'],
        ['b&atildei', 'bãi'], ['&nbspsẽ', ' sẽ'], ['r&atildei', 'rãi'],
        ["good", "tốt"], ["Resort", "Khu nghỉ dưỡng"], ["Ks", "khách sạn"], ["KS", "khách sạn"], ["ko", "không"],
        ["View", "cảnh"],
        ["kg", "không"], ["ok", "tốt"], ["ks", "khách sạn"], ["Ko", "không"], ["kO", "không"],
        ["k", "không"], ["Nice view", "cảnh đẹp"],
        ["Relax", "thư giãn"],
        ["NV", "nhân viên"],
        ["book", "đặt"], ['co so', 'cơ sở'], ['vat chat', 'vật chất'], ['xuong cap', 'xuống cấp'],
        ['thai do', 'thái độ'],
        ['tich cuc', 'tích cực'], ['VN', 'Việt Nam'], ['our', 'chúng tôi'], ['stay', 'ở'],
        ['was not long enough', 'không đủ lâu'], ['everything', 'mọi thứ'], ['tudo', 'tất cả'],
        ['otimo', 'tuyệt vời'], ['Le petit déjeuner', 'ăn sáng'], ['homestay', 'nhà trọ'], ['tp', 'thành phố'],
        ['k', 'không'], ['match', 'giống'], ['ok', 'ổn'], ['. ,', '. '], ['. .', '. '], ['ks', 'khách sạn'],
        ['DN', 'Đà Nẵng'], ['money', 'tiền'], ['thoai mai', 'thoải mái'], ['toilet', 'nha vệ sinh'],
        ['improve', 'cải thiện'], ['clean', 'sạch sẽ'], ['room', 'phòng'], ['mind', 'suy nghĩ'], ['very', 'rất'],
        ['every', 'mọi thứ'], ['perfect', 'tuyệt vời'], ['bad', 'tệ'], ['nice', 'tốt'], ['staffs', 'nhân viên'],
        ['staff', 'nhân viên'], ['breakfast', 'bữa sáng'], ['phuc vu', 'phuc vu'], ['do an', 'đồ ăn'],
        ['be boi', 'bể bơi'], ['nha hang', 'nhà hàng'], ['ho boi', 'hồ bơi'], ['hop ly', 'hợp lý'],
        ['cung duoc', 'cũng được'], ['khach san', 'khách sạn'], ['gđ', 'gia đình'], ['cam giac', 'cảm giác'],
        ['sach se', 'sạch sẽ'], ['xinh xan', 'xinh xắn'], ['cam giac', 'cảm giác'], ['dep', 'đẹp'],
        ['thuc an', 'thức ăn'], ['comfortable', 'thoải mái'], ['trung tam', 'trung tâm'], ['toi let', 'nhà vệ sinh'],
        ['moi nguoi', 'mọi người'], ['tam duoc', 'tạm được'], ['tieu chuan', 'tiêu chuẩn'], ['bai tam', 'bãi tắm'],
        ['niem no', 'niềm nở'], ['tot', 'tốt'], ['view', 'tầm nhìn'], ['yen tinh', 'yên tĩnh'],
        ['bai bien', 'bãi biển'], ['nghi ngoi', 'nghỉ ngơi'], ['than thien', 'thân thiện'], ['dang ky', 'đăng ký'],
        ['du lich', 'du lịch'], ['thuyet phuc', 'thuyết phục'], ['dieu hoa', 'điều hòa'],
        ['thuong xuyen', 'thường xuyên'], ['tuyet voi', 'tuyệt vời'], ['nha ve sinh', 'nhà vệ sinh'],
        ['su dung', 'sử dụng'], ['lang man', 'lãng mạn'], ['vui ve', 'vui vẻ'], ['lich su', 'lịch sự'],
        ['khung canh', 'khung cảnh'], ['ly tuong', 'lý tưởng'], ['hai long', 'hài lòng'], ['lua chon', 'lựa chọn'],
        ['nang cap', 'nâng cấp'], ['bo ho', 'bờ hồ'], ['thuan tien', 'thuận tiện'], ['di lai', 'đi lại'],
        ['mua sam', 'mua sắm'], ['nhiet tinh', 'nhiệt tình'], ['yeu cau', 'yêu cầu'], ['cung cap', 'cung cấp'],
        ['hoa don', 'hóa đơn'], ['Tout est parfait', 'Mọi thứ đều hoàn hảo'], ['free', 'miễn phí'],
        ['Ben thanh', 'Bến Thành'], ['Nothing', 'không có gì'], ['Location', 'vị trí'], ['vi tri', 'vị trí'],
        ['thuan loi', 'thuận lợi'], ['tien nghi', 'tiện nghi'], ['and', 'và'], ['helpful', 'hữu ích'], ['tot', 'tốt'],
        ['ok', 'tốt'], ['toilet', 'phòng vệ sinh'], ['K', 'Không'], ['deluxe', 'sang trọng'], ['okay', 'tốt'],
        ['ks', 'khách sạn'], ['thanks', 'cảm ơn'], ['view', 'tầm nhìn'], ['or', 'hoặc'], ['kg', 'không'],['k\n','không\n'],
        ['TPHCM', 'Thành phố Hồ Chí Minh'], ['book', 'đặt'], ['be boi', 'bể bơi'], ['an sang', 'ăn sáng'],
        ['ksan', 'khách sạn'], ['than thien', 'thân thiện'], ['nhiet tinh', 'nhiệt tình'], ['thoai mai', 'thoải mái'],
        ['vui ve', 'vui vẻ'], ['de chiu', 'dễ chịu'], ['mua sam', 'mua sắm'], ['thuan tien', 'thuận tiện'],
        ['hanh lang', 'hành lang'], ['nhan vien', 'nhân viên'], ['hai long', 'hài lòng'], ['dich vu', 'dịch vụ'],
        ['tot', 'tốt'], ['tuong doi', 'tương đối'], ['he thong', 'hệ thống'], ['niem no', 'niềm nở'],
        ['chuyen nghiep', 'chuyên nghiệp'], ['booking', 'đặt'], ['tien nghi', 'tiện nghi'], ['hanh ly', 'hành lý'],
        ['resort', 'khu nghỉ dưỡng'], ['ko', 'không'], ['danh gia', 'đánh giá'], ['chung toi', 'chúng tôi'],
        ['don tiep', 'đón tiếp'], ['than thien', 'thân thiện'], ['quay lai', 'quay lại'], ['dieu kien', 'điều kiện'],
        ['cong vien', 'công viên'], ['phien phuc', 'phiền phức'], ['may lanh', 'máy lạnh'], ['rat', 'rất'],
        ['chu y', 'chú ý'], ['dao tao', 'đào tạo'], ['binh dan', 'bình dân'], ['tan tinh', 'tận tình'],
        ['de thuong', 'dễ thương'], ['phong ve sinh', 'phòng vệ sinh'], ['gon gang', 'gọn gàng'],
        ['trang tri', 'trang trí'], ['phong', 'phòng'], ['gia dinh', 'gia đình'], ['con nho', 'con nhỏ'],
        ['chu đao', 'chu đáo'], ['sang trong', 'sang trọng'], ['vi tri', 'vị trí'], ['sai gon', 'Sài Gòn'],
        ['hoan toan', 'hoàn toàn'], ['thoang mat', 'thoáng mát'], ['dieu hoa', 'điều hòa'], ['di chuyen', 'di chuyển'],
        ['de dang', 'dễ dàng'], ['day du', 'đầy đủ'], ['rong', 'rộng'], ['dep', 'đẹp'], ['thai do', 'thái độ'],
        ['thich hop', 'thích hợp'], ['ky nghi', 'kỳ nghỉ'], ['dac biet', 'đặc biệt'], ['du lich', 'du lịch'],
        ['phu hop', 'phù hợp'], ['gia ca', 'giá cả'], ['lam viec', 'làm việc'], ['khach hang', 'khách hàng'],
        ['khach', 'khách'], ['nen', 'nên'], ['cancel', 'hủy'], ['hoi an', 'Hội An'], ['pho co', 'phố cổ'],
        ['ve sinh', 'vệ sinh'], ['gan', 'gần'], ['oc', 'ốc'], ['tuyet voi', 'tuyệt vời'], ['nha hang', 'nhà hàng'],
        ['cua hang', 'cửa hàng'], ['va', 'và'], ['and', 'và'], ['duoc', 'được'], ['khu vuc', 'khu vực'],
        ['chac chan', 'chắc chắn'], ['tre em', 'trẻ em'], ['an toan', 'an toàn'], ['on ao', 'ồn ào'], ['voi', 'với'],
        ['lang man', 'lãng mạn'], ['sach', 'sạch'], ['kha', 'khá'], ['yeu cau', 'yêu cầu'], ['dia diem', 'địa điểm'],
        ['cac', 'các'], ['wc', 'phòng vệ sinh'], ['hop ly', 'hợp lý'], ['thoi gian', 'thời gian'],
        ['vui choi', 'vui chơi'], ['khuyet diem', 'khuyết điểm'], ['tieng on', 'tiếng ồn'], ['lan sau', 'lần sau'],
        ['tiep tuc', 'tiếp tục'], ['bo tri', 'bố trí'], ['khung canh', 'khung cảnh'], ['yen tinh', 'yên tĩnh'],
        ['an tuong', 'ấn tượng'], ['ho boi', 'hồ bơi'], ['tre con', 'trẻ con'], ['hut thuoc', 'hút thuốc'],
        ['room', 'phòng'], ['ly tuong', 'lý tưởng'], ['se', 'sẽ'], ['o', 'ở'], ['moi thu', 'mọi thứ'],
        ['duy nhat', 'duy nhất'], ['bao ve', 'bảo vệ'], ['noi tieng', 'nổi tiếng'], ['hcm', 'Hồ Chí Minh'],
        ['HN', 'Hà Nội'], ['SG', 'Sài Gòn'], ['cung nhu', 'cũng như'], ['che bien', 'chế biến'],
        ['trinh bay', 'trình bày'], ['internet', 'mạng internet'], ['toc do', 'tốc độ'], ['bao gio', 'bao giờ'],
        ['di lai', 'đi lại'], ['tro lai', 'trở lại'], ['qua te', 'quá tệ'], ['may tinh', 'máy tính'],
        ['su dung', 'sử dụng'], ['tiet kiem', 'tiết kiệm'], ['thuan loi', 'thuận lợi'],
        ['cho ben thanh', 'cho Ben Thanh'], ['vua', 'vừa'], ['le tan', 'lễ tân'], ['tuy nhien', 'tuy nhiên'],
        ['that su', 'thật sự'], ['cmnd', 'chứng minh nhân dân'], ['sieu thi', 'siêu thị'], ['nhu cau', 'nhu cầu'],
        ['dap ung', 'đáp ứng'], ['lua chon', 'lựa chọn'], ['Da lat', 'Đà Lạt'], ['cong cong', 'công cộng'],
        ['bat tien', 'bất tiện'], ['quy dinh', 'quy định'], ['thuc an', 'thức ăn'], ['of', 'của'],
        ['Da Nang', 'Đà Nẵng'], ['cua so', 'cửa số'], ['Breakfast', 'bữa sáng'], ['kho chiu', 'khó chịu'],
        ['phu thu', 'phụ thu'], ['gia re', 'giá rẻ'], ['ho xuan huong', 'Hồ Xuân Hương'], ['vuon hoa', 'vườn hoa'],
        ['nhe nhang', 'nhẹ nhàng'], ['dang yeu', 'đáng yêu'], ['tan huong', 'tận hưởng'], ['noi nay', 'nơi này'],
        ['hotel', 'khách sạn'], ['huy chuyen', 'hủy chuyến'], ['cty', 'công ty'], ['nguyen trai', 'nguyễn trãi'],
        ['xinh xan', 'xinh xắn'], ['am cung', 'ấm cúng'], ['lich su', 'lịch sự'], ['tu te', 'tử tế'],
        ['tiep dai', 'tiếp đãi'], ['thu tuc', 'thủ tục'], ['good', 'tốt'], ['doi ngu', 'đội ngũ'],
        ['tien loi', 'tiện lợi'], ['dia chi', 'địa chỉ'], ['nghi duong', 'nghỉ dưỡng'],
        ['very', 'rất'],['de men', 'dễ mến'], ['good', 'tốt'], ['khong gian', 'không gian'], ['phu hop', 'phù hợp'],
        ['thiet ke', 'thiết kế'], ['phong cach', 'phong cách'], ['gia dinh', 'gia đình'], ['dia diem', 'địa điểm'],
        ['tin hieu', 'tín hiệu'], ['hanh ly', 'hành lý'], ['khach', 'khách'], ['thuc don', 'thực đơn'],
        ['an sang', 'ăn sáng'], ['cuoi tuan', 'cuối tuần'], ['dong nghiep van phong', 'đồng nghiệp văn phòng'],
        ['ra bien', 'ra biển'], ['tre em', 'trẻ em'], ['uu diem', 'ưu điểm'], ['phong canh', 'phong cảnh'],
        ['thoang mat', 'thoáng mát'], ['nv', 'nhân viên'], ['tro lai', 'trở lại'], ['tiep tuc', 'tiếp tục'],
        ['resort', 'khu nghỉ dưỡng'], ['mon an', 'món ăn'], ['viet nam', 'Việt Nam'], ['phan thiet', 'Phan Thiết'],
        ['bua sang', 'bữa sáng'], ['khong', 'không'], ['thich hop', 'thích hợp'], ['da dang', 'đa dạng'],
        ['tam nang', 'tắm nắng'], ['tre nho', 'trẻ nhỏ'], ['rong rai', 'rộng rãi'], ['tien loi', 'tiện lợi'],
        ['ki nghi', 'kỳ nghỉ'], ['quay lai', 'quay lại'], ['ko', 'không'], ['k/s', 'khách sạn'], ['k', 'không'],
        ['o', 'ở'], ['nghi duong', 'nghỉ dưỡng'], ['chung toi', 'chúng tôi'], ['ky nghi', 'kỳ nghỉ'],['upgraded','nâng cấp'],
        ['gia phong', 'giá phòng'], ['may man', 'may mắn'], ['quang cao', 'quảng cáo'],['upgrade','nâng cấp']
        ]


class util():
    def remove(self, text):  # remove cac ky tu keo dai vd: "cai ao nay dep quaaaaaa" : "cai ao nay dep qua"

        text = ''.join([i for i in text if not i.isdigit()])
        return text

    def A_cvt_a(self, text):  # chuyen cac ky tu viet hoa ve cac ky tu viet thuong
        text = text.lower()
        return text

    def utils_data(self, text):
        list_text = text.split(" ")
        for i in range(len(list_text)):
            for j in range(len(dict)):
                if (list_text[i] == dict[j][0]):
                    list_text[i] = dict[j][1]
        text = " ".join(list_text)


        return text
    def remove_html(self,text):
        text = str(text)
        if '&nbsp' in text:
                text = text.replace('&nbsp', " ")
        if '. ' in text:
                text = text.replace('. ', ' . ')
        if ' .' in text:
                text = text.replace(' .', ' . ')
        return text
    def removepuctual (self,text):
        text = str(text)
        new_string = text.translate(text.maketrans(string.punctuation, '                                '))
        pattern = re.compile(r'\s+')
        new_string = re.sub(pattern, ' ', new_string)
        return new_string
    def text_util_final(self, text):
        # text = self.remove(text)
        # text = self.removepuctual(text)
        # text = self.remove_html(text)
        # text = self.A_cvt_a(text)
        text = self.utils_data(text)
        return text
