from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

translation_mapping = {
    "lbSoftwareName": {
        "vi": "KOS SOFTWARE",
        "en": "KOS SOFTWARE",
        "zh": "KOS SOFTWARE"
    },
    "btnCurrentMenu": {
        "vi": "CÀI ĐẶT",
        "en": "SETTINGS",
        "zh": "设置"
    },
    "btntAccount": {
        "vi": "TÀI KHOẢN",
        "en": "Account",
        "zh": "账户"
    },
    "btnProxy": {
        "vi": "PROXY",
        "en": "PROXY",
        "zh": "SOCKS端口"
    },
    "btnStart": {
        "vi": "BẮT ĐẦU",
        "en": "START",
        "zh": "开始"
    },
    "btnStop": {
        "vi": "DỪNG",
        "en": "STOP",
        "zh": "停止"
    },
    "checkBoxProxyList": {
        "vi": "Proxy list",
        "en": "Proxy list",
        "zh": "代理列表"
    },
    "checkBoxProxyKey": {
        "vi": "Proxy Key(khuyên dùng)",
        "en": "Proxy Key(recommended)",
        "zh": "代理密钥（推荐）"
    },
    "btnShop": {
        "vi": "Shop Tài Khoản",
        "en": "shop account",
        "zh": "商店"
    },
    "btnSettings": {
        "vi": "CÀI ĐẶT",
        "en": "Settings",
        "zh": "设置"
    },
    "btnCheckAccount": {
        "vi": "Check Tài Khoản",
        "en": "Check account",
        "zh": "检查账户"
    },
    "btnFilterMembers": {
        "vi": "Lọc Thành Viên",
        "en": "Filter members",
        "zh": "筛选成员"
    },
    
    "txtFilterMembersLinkGroupNeedFilter": {
        "vi": "link nhóm cần lọc",
        "en": "Filter members link group",
        "zh": "需要筛选的链接"
    },
    
    "btnFilterData": {
        "vi": "Lọc Data SĐT",
        "en": "Filter data",
        "zh": "筛选电话号码"
    },
    "btnAddMembers": {
        "vi": "Thêm Thành Viên",
        "en": "Add Member",
        "zh": "添加成员"
    },
    "btnSpamMessage": {
        "vi": "Gửi Tin Nhắn",
        "en": "Spam message",
        "zh": "发送消息"
    },
    
    "btnSeeding": {
        "vi": "Seeding Kịch Bản",
        "en": "Seeding",
        "zh": "对话剧本"
    },
    "btnJoinGroupChannel": {
        "vi": "Tham Gia Nhóm/kênh",
        "en": "Join group/channel",
        "zh": "加入群组/频道"
    },
    "btnLeaveGroupChannel": {
        "vi": "Rời Nhóm/kênh",
        "en": "Leave group/channel",
        "zh": "加入群"
    },
    "btnBuffEmotions": {
        "vi": "Buff Cảm Xúc Bài Viết",
        "en": "buff Emotions",
        "zh": "退出聊天室"
    },
    "btnPostViews": {
        "vi": "Tăng Mắt Bài Viết",
        "en": "Post Views",
        "zh": "增加文章的阅读量"
    },
    "btnChangeAccountInfor": {
        "vi": "Đổi Thông Tin TK",
        "en": "Change account infor",
        "zh": "更改账户信息"
    },
    "btnSettingsToogle": {
        "vi": "CÀI ĐẶT",
        "en": "Settings",
        "zh": "设置"
    },
    "btnCheckAccountToggle": {
        "vi": "Check Tài Khoản",
        "en": "Check account",
        "zh": "检查账户"
    },
    "lbCheckBoxCheckSpam": {
        "vi": "CHECK LIVE",
        "en": "CHECK LIVE",
        "zh": "检查账户"
    },
    "lbcheckBoxCheckLive": {
        "vi": "CHECK SPAM",
        "en": "CHECK SPAM",
        "zh": "检查好坏"
    },
    "btnFilterMembersToggle": {
        "vi": "Lọc Thành Viên",
        "en": "Filter Member",
        "zh": "筛选成员"
    },
    "checkBoxFilterGroupHideMember": {
        "vi": "Lọc Nhóm ẩn Member",
        "en": "Filter Hidden Member Groups",
        "zh": "筛选隐藏成员"
    },
    "checkBoxFilterGroupHideMemberViet": {
        "vi": "Lọc Lấy Member Việt",
        "en": "Filter Get Vietnamese Members",
        "zh": "中国大陆会员"
    },
    "checkBoxMemberOnline": {
        "vi": "Member Online",
        "en": "Online Members",
        "zh": "网上会员"
    },
    "lbNumberDateNeedFilter": {
        "vi": "Số Ngày Cần Lọc",
        "en": "Number of Days to Filter",
        "zh": "需要筛选的天数"
    },
    "btnSaveFileMember": {
        "vi": "Lưu File Member",
        "en": "Save Member File",
        "zh": "保存成员文件"
    },
    "btnFilterDataToggle": {
        "vi": "Lọc Data SĐT",
        "en": "Filter data",
        "zh": "筛选电话号码数据"
    },
    "btnFileDataSDT": {
        "vi": "Tệp DATA SDT",
        "en": "Phone Data File",
        "zh": "筛选电话号码"
    },
    "checkBoxFilterDataDataExists": {
        "vi": "data Tồn Tại",
        "en": "Existing data",
        "zh": "用户已注册帐户"
    },
    "checkBoxFilterDatDoingOnline": {
        "vi": "data đang online",
        "en": "data is online",
        "zh": "用户在线"
    },
    "checkBoxFilterDatDataOnlineOneWeek": {
        "vi": "data online 1 tuần",
        "en": "data online 1 week",
        "zh": "用户 1 周前在线"
    },
    "checkBoxFilterDatDataOnlineOneMonth": {
        "vi": "data online 1 tháng",
        "en": "data online 1 month",
        "zh": "用户1个月前在线"
    },
    "checkBoxFilterDatDataOnlinePerHour": {
        "vi": "data online theo  giờ",
        "en": "data online by hour",
        "zh": "用户按小时筛选选项"
    },
    "lbFilterDataHour": {
        "vi": "Giờ",
        "en": "Hour",
        "zh": "小时"
    },
    "lbQuantityPhoneNumberNeedFilter": {
        "vi": "Số lượng SDT  cần lọc trên mỗi tài khoản Telgram",
        "en": "Number of phone numbers to filter per Telegram account",
        "zh": "每个用户帐户要过滤的用户数"
    },
    "lbPhoneAccount": {
        "vi": "SDT/tài khoản",
        "en": "Phone number/account",
        "zh": "电话号码/账户"
    },
    "btnSaveFileHadFilter": {
        "vi": "Lưu File Đã lọc",
        "en": "Save Filtered File",
        "zh": "保存已筛选文件"
    },
    "btnAddMemberToggle": {
        "vi": "Thêm Thành Viên",
        "en": "Add Member",
        "zh": "添加成员"
    },
    "btnMemberFile": {
        "vi": "Tệp Thành Viên",
        "en": "Member File",
        "zh": "成员文件"
    },
    "txtAddMemberInputLinkGroup": {
        "vi": "Điền Link nhóm",
        "en": "Enter group link",
        "zh": "请输入小组链接"
    },
    "lbChooseType": {
        "vi": "Vui lòng chọn Type",
        "en": "Please select Type",
        "zh": "选项类型"
    },
    "checkBoxAddMemberUsername": {
        "vi": "Username",
        "en": "Username",
        "zh": "用户名"
    },
    "checkBoxAddMemberDataSDT": {
        "vi": "Data SDT",
        "en": "Phone Data",
        "zh": "电话号码"
    },
    "lbQuantiyAccount": {
        "vi": "Số Lượng /Tài khoản",
        "en": "Quantity /Account",
        "zh": "数量/账户"
    },
    "lbAddMemberQuantityAccount": {
        "vi": "Member",
        "en": "Member",
        "zh": "用户"
    },
    "lbAddMemberTimeSleepPerAdd": {
        "vi": "Thời gian nghỉ/lần add",
        "en": "Sleep time/add",
        "zh": "每次成功添加之间的休息时间"
    },
    "lbAddMemberTimeSleepSecond": {
        "vi": "giây",
        "en": "second",
        "zh": "秒"
    },
    "lbSettingsMemberData": {
        "vi": "Cài Đặt kéo mem data nếu chưa lọc data online",
        "en": "Settings to get member data if not filtered online",
        "zh": "如果未筛选在线数据，则获取成员数据设置"
    },
    "checkBoxAddMemberMemOnlineOneDay": {
        "vi": "mem online 1 ngày",
        "en": "members online 1 day",
        "zh": "会员在线 1 天"
    },
    "checkBoxAddMemberMemOnlineThreeDay": {
        "vi": "mem online 3 ngày",
        "en": "members online 3 day",
        "zh": "会员在线 3 天"
    },
    "checkBoxAddMemberMemOnlineOneWeek": {
        "vi": "mem online 1 tuần",
        "en": "members online 1 week",
        "zh": "会员在线 1 周"
    },
    "checkBoxAddMemberMemOnlineOneMonth": {
        "vi": "mem online 1 tháng",
        "en": "members online 1 month",
        "zh": "会员在线 1 个月"
    },
    "btnSpamMessageToggle": {
        "vi": "Gửi Tin Nhắn",
        "en": "Spam Message",
        "zh": "发送消息"
    },
    "lbSpamMessageChooseType": {
        "vi": "Vui lòng chọn Type",
        "en": "Please select Type",
        "zh": "选项类型"
    },
    "checkBoxSpamMessageUsername": {
        "vi": "Username",
        "en": "Username",
        "zh": "用户名"
    },
    "checkBoxSpamMessageGroup": {
        "vi": "Các Hội Nhóm",
        "en": "Groups",
        "zh": "发送到群聊"
    },
    "checkBoxSpamMessageDataSDT": {
        "vi": "DATA SDT",
        "en": "Phone Data",
        "zh": "电话号码"
    },
    "btnFileDataLinkUserName": {
        "vi": "Tệp data/link/username",
        "en": "Data/link/username file",
        "zh": "成员/链接文件"
    },
    "btnImageToSpam": {
        "vi": "Hình ảnh khi Spam",
        "en": "Data/link/username file",
        "zh": "成员/链接文件"
    },
    "lbSpamMessageSetupExtra": {
        "vi": "SETUP PHỤ",
        "en": "EXTRA SETUP",
        "zh": "附加设置"
    },
    "checkBoxSpamMessageRandomContent": {
        "vi": "Random Nội Dung",
        "en": "Random Content",
        "zh": "随机内容"
    },
    "checkBoxSpamMessageForwardMessage": {
        "vi": "Forward Tin Nhắn",
        "en": "Forward Message",
        "zh": "转发消息"
    },
    "lbTimeSleepPerMessage": {
        "vi": "Thời gian nghỉ/mỗi tin",
        "en": "Sleep time/message",
        "zh": "每条消息的休息时间"
    },
    "lbQuantityMessageSecond": {
        "vi": "giây",
        "en": "second",
        "zh": "秒"
    },
    "lbQuantityMessagePerAccount": {
        "vi": "số lượng tin nhắn gửi trên 1 tài khoản",
        "en": "number of messages sent per account",
        "zh": "一个账户发送的消息数量"
    },
    "btnFileScriptMessage": {
        "vi": "File Kịch bản Tin nhắn",
        "en": "Message Script File",
        "zh": "消息脚本文件"
    },
    "lbSpamMessageNote": {
        "vi": "lưu ý: File kịch bản/link bài \nviết  mỗi nội dung cách nhau \n1 dòng",
        "en": "note: script/post link file each content separated by 1 line",
        "zh": "注：脚本文件/文章链接中，各内容以1行分隔"
    },
    "btnSededingToggle": {
        "vi": "Seeding Kịch Bản",
        "en": "Seeding Script",
        "zh": "对话剧本"
    },
    "txtLinkGroupNeedSeeding": {
        "vi": "Link Nhóm cần seeding",
        "en": "Group link needs seeding",
        "zh": "群组链接"
    },
    "lbSeedingChooseType": {
        "vi": "VUI LÒNG CHỌN TYPE",
        "en": "PLEASE SELECT TYPE",
        "zh": "选项类型"
    },
    "checkBoxSeedingWithFile": {
        "vi": "Seeding bằng file",
        "en": "Seeding with file",
        "zh": "使用现有的文件"
    },
    "btnFileSeeding": {
        "vi": "File Seeding",
        "en": "Seeding File",
        "zh": "文件"
    },
    "checkBoxSeedingCopyGroupEnemy": {
        "vi": "Seeding Bằng Copy\nGroup Đối Thủ",
        "en": "Seeding by Copying Competitor Groups",
        "zh": "从群聊复制内容"
    },
    "txtLinkGroupEnemy": {
        "vi": "Link nhóm của đối thủ",
        "en": "Competitor Group Link",
        "zh": "想要复制的群组链接"
    },

    "lbInputID": {
        "vi": "Copy Chát Từ Nội dung có\nID Chát Trên nhóm",
        "en": "Copy Chat From Content with Chat ID on Group",
        "zh": "从具有内容的ID开始复制内容"
    },
    "txtInputID": {
        "vi": "ĐIỀN ID",
        "en": "Enter ID",
        "zh": "聊天ID"
    },
    "lbSeedingSetupExtra": {
        "vi": "SETUP PHỤ",
        "en": "EXTRA SETUP",
        "zh": "聊天ID"
    },
    "checkBoxSeedingRandom": {
        "vi": "Seeding Ngẫu Nhiên",
        "en": "Random Seeding",
        "zh": "附加设置"
    },
    "checkBoxSeedingOrder": {
        "vi": "Seeding Theo thứ tự",
        "en": "Ordered Seeding",
        "zh": "从列表生成随机脚本"
    },
    "lbtTextSleepFrom": {
        "vi": "Nghỉ Từ",
        "en": "Sleep From",
        "zh": "休息"
    },
    "lbSleepFromSecond": {
        "vi": "Giây",
        "en": "Second",
        "zh": "秒"
    },
    "lbTextSleepTo": {
        "vi": "ĐẾN",
        "en": "TO",
        "zh": "到"
    },
    "lbSleepToSecond": {
        "vi": "Giây",
        "en": "Second",
        "zh": "秒"
    },
    "btnJoinGroupChannelToggle": {
        "vi": "Tham Gia Nhóm/kênh",
        "en": "Join Group/Channel",
        "zh": "加入群组/频道"
    },
    "lbJoinLinkGroupChannel": {
        "vi": "Điền Link nhóm/kênh",
        "en": "Enter Group/Channel Link",
        "zh": "填写频道/群聊链接"
    },
    "txtJoinLinkGroupChannel": {
        "vi": "Link Kênh/Nhóm",
        "en": "Channel/Group Link",
        "zh": "频道/群组链接"
    },
    "btnLeaveGroupChannelToggle": {
        "vi": "Rời Nhóm/kênh",
        "en": "Leave Group/Channel",
        "zh": "退出聊天室"
    },
    "lbLeaveLinkGroupChannel": {
        "vi": "Link Kênh/Nhóm",
        "en": "Channel/Group Link",
        "zh": "填写频道/群聊链接"
    },
    "txtLeaveLinkGroupChannel": {
        "vi": "Điền Link  nhóm/kênh",
        "en": "Enter Group/Channel Link",
        "zh": "填写频道/群聊链接"
    },
    "lbLeaveLinkGroupChannelChooseType": {
        "vi": "VUI LÒNG CHỌN TYPE",
        "en": "Please select type",
        "zh": "请选择类型"
    },
    "checkBoxLeaveLinkGroupChannelAll": {
        "vi": "Rời tất cả Nhóm/Kênh",
        "en": "Leave all Groups/Channels",
        "zh": "退出所有群组/频道"
    },
    "checkBoxLeaveLinkGroupChannelFollowList": {
        "vi": "Rời theo danh sách nhóm kênh",
        "en": "Leave Groups/Channels by list",
        "zh": "按列表退出群组/频道"
    },
    "checkBoxLeaveLinkGroupChannelFollowQuantity": {
        "vi": "Rời nhóm/kênh theo số lượng",
        "en": "Leave Groups/Channels by quantity",
        "zh": "按数量退出群组/频道"
    },
    "lbLeaveLinkGroupChannelGroupChannel": {
        "vi": "nhóm/kênh",
        "en": "Group/Channel",
        "zh": "群组/频道"
    },
    "btnBuffEmotionsToggle": {
        "vi": "Buff Cảm Xúc Bài Viết",
        "en": "Buff Emotions",
        "zh": "给文章点赞"
    },
    "lbBuffEmotionsLinkPost": {
        "vi": "LINK BÀI VIẾT",
        "en": "POST LINK",
        "zh": "填写频道/群聊链接"
    },
        "lbBuffEmotionsLinkGroup": {
        "vi": "LINK NHÓM",
        "en": "GROUP LINK",
        "zh": "群链接"
    },
    "txtBuffEmotionsLinkGroup": {
        "vi": "link nhóm kín cần tham gia",
        "en": "Link to private group to join",
        "zh": "需要加入的私密群链接"
    },
    "txtLinkPostNeedEmotion": {
        "vi": "link bài viết cần thả cảm xúc",
        "en": "Post Link Requiring Emotion",
        "zh": "文章链接需要释放情绪"
    },
    "lbBuffEmotionsNote": {
        "vi": "LƯU Ý: Tích chọn các cảm xúc và hệ thống sẽ thả cảm xúc random cho bài viết",
        "en": "NOTE: Check the emotions and the system will randomly add emotions to the post",
        "zh": "注意：勾选情感，系统将随机为文章添加情感表情"
    },
    "btnPostViewsToggle": {
        "vi": "Tăng Mắt Bài Viết",
        "en": "Increase Post Views",
        "zh": "增加文章的阅读量"
    },
    "lbPostViewsLinkGroupChannel": {
        "vi": "Link Kênh/Nhóm",
        "en": "Channel/Group Link",
        "zh": "填写频道/群聊链接"
    },
    "lbPostViewsLinkPost": {
        "vi": "LINK BÀI VIẾT",
        "en": "Post Link",
        "zh": "文章链接"
    },

    "txtPostViewsLinkGroupChannel": {
        "vi": "Link kênh nhóm cần tham gia",
        "en": "Enter Channel/Group Link",
        "zh": "填写频道/群聊链接"
    },
    "lbPostViewsLinkPostChannel": {
        "vi": "Điền link bài viết",
        "en": "Enter Post Link",
        "zh": "填写文章链接"
    }
    ,
    "btnChangeAccountInforToggle": {
        "vi": "Đổi Thông Tin TK",
        "en": "Change Account Info",
        "zh": "更改帐户信息"
    },
    "checkBoxChangeUserName": {
        "vi": "Đổi Username\n (random)",
        "en": "Change Username (random)",
        "zh": "更改 Username (random)"
    },
    "checkBoxChangeName": {
        "vi": "Đổi  Tên",
        "en": "Change Name",
        "zh": "更改用户名"
    },
    "btnChangeName": {
        "vi": "Tệp Tên",
        "en": "Name File",
        "zh": "更改头像"
    },
    "checkBoxSetAvatar": {
        "vi": "Set Ảnh Đại Diện",
        "en": "Set Avatar",
        "zh": "更改头像"
    },
    "btnSetAvatar": {
        "vi": "thư mục chứa ảnh",
        "en": "folder containing images",
        "zh": "包含图像的文件夹"
    },
    "lbVersion": {
        "vi": "BY KOS SOFTWARE V1.1",
        "en": "BY KOS SOFTWARE V1.1",
        "zh": "KOS 软件 V1.1"
    },
    "lbKeyText": {
        "vi": "KEY",
        "en": "KEY",
        "zh": "KEY"
    },
    "lbKey": {
        "vi": "ASKDBJKASDNLANKL KLASLDKNASKLD",
        "en": "ASKDBJKASDNLANKL KLASLDKNASKLD",
        "zh": "ASKDBJKASDNLANKL KLASLDKNASKLD"
    },
    "lbTextExpiration": {
        "vi": "  Ngày hết hạn:",
        "en": "  Expiration Date:",
        "zh": "  保质期:"
    },
    "lbExpirationDate": {
        "vi": "  01.01.2025",
        "en": "  01.01.2025",
        "zh": "  01.01.2025"
    },
    "TÀI KHOẢN":{
        "vi": "TÀI KHOẢN",
        "en": "ACCOUNT",
        "zh": "账户"
    },
    "PROXY":{
      "vi": "PROXY",
       "en": "PROXY",
        "zh": "SOCKS端口"
    },
     "KẾT QUẢ":{
       "vi":"KẾT QUẢ",
       "en":"RESULT",
        "zh":"结果"
    },
     "STATUS":{
       "vi":"STATUS",
       "en":"STATUS",
        "zh":"状态"
    },
    "New Row":{
        "vi":"New Row",
        "en":"New Row",
        "zh":"新行"
    }
}

class Translation:
    def __init__(self, uic):
        self.uic = uic

    def translate_ui(self, language):
        _translate = QCoreApplication.translate
        #self.setWindowTitle(_translate("FormMain", self.translate_text("FormMain", language)))

        for attr_name in dir(self.uic):
            if not attr_name.startswith("_"): 
                attr = getattr(self.uic, attr_name)
                if isinstance(attr, (QLabel, QPushButton, QCheckBox, QRadioButton, QAbstractButton)):
                    translated_text = self.translate_text(attr_name, language)
                    if translated_text:
                        attr.setText(_translate("FormMain", translated_text))
                elif isinstance(attr, QLineEdit) or isinstance(attr, QTextEdit):
                    translated_placeholder = self.translate_text(attr_name, language)
                    if translated_placeholder:
                        attr.setPlaceholderText(_translate("FormMain", translated_placeholder))
                        

        self.translate_table_headers(language)

    def translate_text(self, object_name, language_code):
        if object_name in translation_mapping:
            if language_code in translation_mapping[object_name]:
                return translation_mapping[object_name][language_code]
            else:
                return translation_mapping[object_name]["en"]
        return ""

    def translate_table_headers(self, language):
        _translate = QCoreApplication.translate
        # for i in range(19):
        #     item = self.uic.tableWidget.verticalHeaderItem(i)
        #     item.setText(_translate("FormMain", self.translate_text("New Row", language)))

        columns = ["TÀI KHOẢN", "PROXY", "KẾT QUẢ", "STATUS"]
        for i, col in enumerate(columns):
            item = self.uic.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("FormMain", self.translate_text(col, language)))