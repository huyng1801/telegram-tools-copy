import sys
import inspect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import Ui_FormMain
from start import Ui_start
from payment import Ui_payment
from chat import Ui_ChatForm
from login import Ui_LoginForm
from register import Ui_RegisterForm

from translation import Translation
from icons_mapping import emoji_mapping
from chat_client import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.uic = Ui_FormMain()
        self.uic.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.uic_2 = Ui_start()
        self.main_win_2 = QWidget()
        self.uic_2.setupUi(self.main_win_2)

        self.uic_3 = Ui_payment()
        self.main_win_3 = QWidget()
        self.uic_3.setupUi(self.main_win_3)

        self.uic_4 = Ui_LoginForm()
        self.main_win_4 = QWidget()
        self.uic_4.setupUi(self.main_win_4)
        self.main_win_4.setWindowFlags(Qt.FramelessWindowHint)
        self.main_win_4.setAttribute(Qt.WA_TranslucentBackground)
        shadow_effect_4 = QGraphicsDropShadowEffect()
        shadow_effect_4.setBlurRadius(20)  
        shadow_effect_4.setXOffset(5)   
        shadow_effect_4.setYOffset(5)    
        shadow_effect_4.setColor(QColor(0, 0, 0, 150))  
        self.uic_4.wtForm.setGraphicsEffect(shadow_effect_4)
       
        self.uic_5 = Ui_ChatForm()
        self.main_win_5 = QWidget()
        self.uic_5.setupUi(self.main_win_5)
        
        self.uic_6 = Ui_RegisterForm()
        self.main_win_6 = QWidget()
        self.uic_6.setupUi(self.main_win_6)
        self.main_win_6.setWindowFlags(Qt.FramelessWindowHint)
        self.main_win_6.setAttribute(Qt.WA_TranslucentBackground)

        shadow_effect_6 = QGraphicsDropShadowEffect()
        shadow_effect_6.setBlurRadius(20)  
        shadow_effect_6.setXOffset(5)   
        shadow_effect_6.setYOffset(5)    
        shadow_effect_6.setColor(QColor(0, 0, 0, 150))  
        self.uic_6.wtForm.setGraphicsEffect(shadow_effect_6)
  
        self.translation = Translation(self.uic)
        self.emoji_mapping = emoji_mapping
        self.checkboxes = {}
        
        self.oldPosition = None
        self.is_resizing = False
        self.resize_direction = None
        self.can_drag = False

        self.change_stack_index(1)

        # Connect buttons to respective actions
        self._connect_buttons()

        self.uic.btnStart.setVisible(False)
        self.uic.btnStop.setVisible(False)

        # Language selection buttons
        self.uic.btnVietnamese.clicked.connect(lambda: self.translation.translate_ui("vi"))
        self.uic.btnChina.clicked.connect(lambda: self.translation.translate_ui("zh"))
        self.uic.btnEnglish.clicked.connect(lambda: self.translation.translate_ui("en"))
        
        # Button Account, Proxy, Start, Stop
        
        self.uic.btnAccount.clicked.connect(lambda: self.handle_account_button())
        self.uic.btnProxy.clicked.connect(lambda: self.handle_proxy_button())
        self.uic.btnStart.clicked.connect(lambda: self.handle_start_button())
        self.uic.btnStop.clicked.connect(lambda: self.handle_stop_button())
        
        # Button Shop
        self.uic.btnShop.clicked.connect(lambda: self.handle_shop_button())
        
        # Event Page 
        self.uic.btnSaveFileMember.clicked.connect(lambda: self.handle_save_file_member())
        self.uic.btnFileDataSDT.clicked.connect(lambda: self.handle_file_data_sdt())
        self.uic.btnSaveFileHadFilter.clicked.connect(lambda: self.handle_save_file_had_filter())

        # Checkbox Username

        # Connect signals for toggle events
        self.uic.checkBoxProxyList.toggled.connect(lambda: self.toggle_proxy_checkboxes())
        self.uic.checkBoxProxyKey.toggled.connect(lambda: self.toggle_proxy_checkboxes())

        # Initialize HTTP and SOCK checkboxes as hidden
        self.uic.checkBoxHTTP.setVisible(False)
        self.uic.checkBoxSOCK.setVisible(False)
        
        self.uic_4.btnLogin.clicked.connect(lambda: self.handle_login())
        self.uic_4.btnExit.clicked.connect(lambda: self.main_win_4.close())
        self.uic_4.btnRegister.clicked.connect(lambda: self.show_register())
        
        
        self.uic_5.btnSendMessage.clicked.connect(lambda: self.handle_send_message())
        self.uic_5.btnChatRoom.clicked.connect(lambda: self.handle_get_rooms())
        self.uic_5.btnUser.clicked.connect(lambda: self.handle_get_users())
        self.uic_5.lstContact.itemClicked.connect(lambda: self.handle_contact_clicked())
        
        self.uic_6.btnLogin.clicked.connect(lambda: self.show_login())
        self.uic_6.btnRegister.clicked.connect(lambda: self.handle_register())
        self.uic_6.btnExit.clicked.connect(lambda: self.main_win_6.close())
        
        self.handle_get_rooms()
        
    def show_login(self):
        self.main_win_6.close()
        self.main_win_4.show()
            
    def show_register(self):
        self.main_win_4.close()
        self.main_win_6.show()
        
    def handle_register(self):
        name = self.uic_6.txtUsername.text()
        email = self.uic_6.txtEmail.text()
        password = self.uic_6.txtPassword.text()
        confirm_password = self.uic_6.txtConfirmPassword.text()

        if not name or not email or not password or not confirm_password:
            QMessageBox.warning(self.main_win_6, "Lỗi Đăng Ký", "Vui lòng nhập đầy đủ thông tin.")
            return

        if password != confirm_password:
            QMessageBox.warning(self.main_win_6, "Lỗi Đăng Ký", "Mật khẩu xác nhận không khớp.")
            return

        success = register_user(name, email, password)

        if success:
            QMessageBox.information(self.main_win_6, "Đăng Ký Thành Công", "Bạn đã đăng ký thành công! Hãy đăng nhập.")
            self.show_login()
        else:
            QMessageBox.critical(self.main_win_6, "Đăng Ký Thất Bại", "Email đã được sử dụng hoặc có lỗi xảy ra.")
        
    def handle_login(self):
        email = self.uic_4.txtEmail.text()
        password = self.uic_4.txtPassword.text()

        if not email or not password:
            QMessageBox.warning(self.main_win_4, "Lỗi Đăng Nhập", "Vui lòng nhập email và mật khẩu.")
            return

        user_token = login_user(email, password)
        
        if user_token:
            QMessageBox.information(self.main_win_4, "Đăng Nhập Thành Công", "Bạn đã đăng nhập thành công!")
            self.main_win_4.hide()
            self.main_win_5.show()
        else:
            QMessageBox.critical(self.main_win_4, "Đăng Nhập Thất Bại", "Thông tin đăng nhập không hợp lệ. Vui lòng thử lại.")
            
    def handle_send_message(self):
        message = self.uic_5.txtInputMessage.text().strip()
        if not message:
            print("Tin nhắn không được để trống.")
            return

        selected_item = self.uic_5.lstContact.currentItem()
        if not selected_item:
            return  # No item selected

        contact_name = selected_item.text()
        
        # Check if the contact is a room or a private user
        rooms = get_rooms()
        users = get_users()

        selected_room = next((room for room in rooms if room["name"] == contact_name), None)
        selected_user = next((user for user in users if user["username"] == contact_name), None)

        # Send message to the selected contact (user or room)
        if selected_user:  # If a user is selected, send a direct message
            user_id = selected_user["id"]  # Assuming the user ID is stored in the user object
            send_direct_message(user_id, message)
            print(f"Tin nhắn đã gửi đến người dùng: {user_id}")
        elif selected_room:  # If a room is selected, send the message to the room
            room_id = selected_room["id"]
            send_message(room_id, message)
            print(f"Tin nhắn đã gửi đến phòng chat: {selected_room['name']}")
        else:
            print("Không tìm thấy người dùng hoặc phòng chat.")

        # Clear the message input field after sending
        self.uic_5.txtInputMessage.clear()

        # Reload the messages for the selected contact (room or user)
        self.handle_contact_clicked()  # This will reload the conversation
    
    def create_message_widget(self, sender_name, content, created_at, is_own_message):
        """Tạo một widget hiển thị tin nhắn theo phong cách chat Zalo (bên trái/bên phải)"""
        widget = QWidget()
        layout = QHBoxLayout()

        # Widget con chứa nội dung tin nhắn
        message_container = QWidget()
        message_layout = QVBoxLayout()

        # Hiển thị tên người gửi nếu không phải tin nhắn của mình
        if not is_own_message:
            sender_label = QLabel(sender_name)
            sender_label.setStyleSheet("font-weight: bold; color: #1677ff;")
            message_layout.addWidget(sender_label)

        # Nội dung tin nhắn
        message_label = QLabel(content)
        message_label.setWordWrap(True)  # Cho phép xuống dòng
        message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Tự động mở rộng
        message_label.setMinimumHeight(30)  # Đặt chiều cao tối thiểu để tránh cắt chữ
        
        # Thêm thời gian gửi
        timestamp_label = QLabel(created_at)
        timestamp_label.setStyleSheet("font-size: 10px; color: gray; margin-top: 4px;")

        # Áp dụng style cho tin nhắn (nền khác nhau)
        if is_own_message:
            message_label.setStyleSheet("""
                background-color: #e6f4ff;
                padding: 8px;
                border-radius: 12px;
                color: black;
            """)
        else:
            message_label.setStyleSheet("""
                background-color: white;
                padding: 8px;
                border-radius: 12px;
                color: black;
            """)

        message_layout.addWidget(message_label)
        message_layout.addWidget(timestamp_label, alignment=Qt.AlignRight)  # Canh thời gian về góc phải

        # Giảm margin để tránh bị che chữ
        message_layout.setContentsMargins(0, 0, 0, 0)
        message_container.setLayout(message_layout)

        # Sử dụng QSpacerItem để đẩy tin nhắn về bên phải hoặc bên trái
        if is_own_message:
            layout.addStretch()  # Đẩy tin nhắn về bên phải
            layout.addWidget(message_container)
        else:
            layout.addWidget(message_container)
            layout.addStretch()  # Đẩy tin nhắn về bên trái

        widget.setLayout(layout)
        return widget

    def handle_contact_clicked(self):
        """Xử lý khi người dùng click vào danh bạ và load tin nhắn"""
        selected_item = self.uic_5.lstContact.currentItem()
        if not selected_item:
            return  

        contact_name = selected_item.text()

        rooms = get_rooms()
        users = get_users()

        selected_room = next((room for room in rooms if room["name"] == contact_name), None)
        selected_user = next((user for user in users if user["username"] == contact_name), None)

        self.uic_5.lstMessage.clear()  # Xóa tin nhắn cũ

        if selected_room:
            room_id = selected_room["id"]
            messages = get_room_messages(room_id)
        elif selected_user:
            user_id = selected_user["id"]
            messages = get_direct_messages(user_id)
        else:
            print("Unknown contact selected")
            return

        messages = messages.get('messages', [])
        current_user = get_current_user_id()  

        if isinstance(messages, list):
            for msg in messages:
                if isinstance(msg, dict):  
                    sender_id = msg.get("sender_id")
                    sender_name = msg.get("sender_name", "Unknown")
                    created_at = msg.get("created_at", "Unknown")
                    content = msg.get("content", "")

                    is_own_message = sender_id == current_user
                    message_widget = self.create_message_widget(sender_name, content, created_at, is_own_message)

                    item = QListWidgetItem()
                    item.setSizeHint(message_widget.sizeHint())  # Điều chỉnh kích thước

                    self.uic_5.lstMessage.addItem(item)
                    self.uic_5.lstMessage.setItemWidget(item, message_widget)
        else:
            print("Unexpected response format:", messages)



    def handle_get_rooms(self):
        """Lấy danh sách phòng và hiển thị lên lstContact"""
        rooms = get_rooms()
        self.uic_5.lstContact.clear()  
        for room in rooms:
            self.uic_5.lstContact.addItem(f"{room['name']}")  


    def handle_get_users(self):
        """Lấy danh sách người dùng và hiển thị lên lstContact"""
        users = get_users()  
        self.uic_5.lstContact.clear()  
        for user in users:
            self.uic_5.lstContact.addItem(f"{user['username']}")  
   
    # Handle event 

                
    def handle_save_file_member(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Save File Member")
        
    def handle_member_file(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Member File")
        
    def handle_image_spam(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Image Spam")        
        
    def handle_file_data_sdt(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: File Data SDT")

    def handle_save_file_had_filter(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Save File Had Filter")

    def handle_file_data_link_username(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: File Data Link Username")

    def handle_file_script_message(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: File Script Message")

    def handle_file_seeding(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: File Seeding")

    def handle_change_name(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Change Name")

    def handle_set_avatar(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Button text: Set Avatar")
    
    def handle_cell_click(self, row, column):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Cell clicked at row: {row}, column: {column}")
        
        if self.uic.tableWidget.item(row, column) != None:
            clicked_data = self.uic.tableWidget.item(row, column).text()
            print(f"Data in clicked cell: {clicked_data}")

    def get_checked_emojis(self):
        checked_emojis = [f"{name}: {symbol}" for name, symbol in self.emoji_mapping.items() if self.checkboxes[symbol].isChecked()]
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Data Emojis: {checked_emojis}")
        return checked_emojis
    
    def handle_account_button(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line} Event: Account button clicked!")
        
    def handle_proxy_button(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line} Event: Proxy button clicked!!")

    def handle_start_button(self):
        self.get_current_stack_page_name()
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line} Event: Start button clicked!")

    def handle_stop_button(self):
        self.get_current_stack_page_name()
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line} Event: Stop button clicked!!")
    def handle_shop_button(self):
        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Data: Shop button clicked!")
        
        google_url = "https://www.google.com"
        QDesktopServices.openUrl(QUrl(google_url))

    def _connect_buttons(self):
        # Main buttons with indices
        button_actions = [
            (self.uic.btnSettings, 1), (self.uic.btnCheckAccount, 2), 
            (self.uic.btnFilterMembers, 3), (self.uic.btnFilterData, 4),

        ]
        for button, index in button_actions:
            button.clicked.connect(lambda _, idx=index: self.change_stack_index(idx))

        # Toggle buttons
        toggle_buttons = [
            self.uic.btnSettingsToogle, self.uic.btnCheckAccountToggle,
            self.uic.btnFilterMembersToggle, self.uic.btnFilterDataToggle,
            self.uic.btnSettingsToogle, self.uic.btnSettingsToogleDropdown, self.uic.btnCheckAccountToggleDropdown,
            self.uic.btnFilterMembersToggleDropdown, self.uic.btnFilterDataToggleDropdown,
        ]
        for toggle_button in toggle_buttons:
            toggle_button.clicked.connect(lambda _: self.change_stack_index(0))

        self.uic.btnCurrentMenu.clicked.connect(lambda _: self.change_stack_index(0))

        # Close and minimize actions
        self.uic.btnClose.clicked.connect(lambda: self.close())
        self.uic.btnMinimize.clicked.connect(lambda: self.showMinimized())
        self.uic.btnMaximized.clicked.connect(lambda: self.toggleMaximized())

        # Event for cell
        self.uic.tableWidget.cellClicked.connect(lambda row, column: self.handle_cell_click(row, column))
    

    # Toggle visibility of HTTP and SOCK checkboxes based on ProxyList or ProxyKey
    def toggle_proxy_checkboxes(self):
        checked = self.uic.checkBoxProxyList.isChecked()
        self.uic.checkBoxHTTP.setVisible(checked)
        self.uic.checkBoxSOCK.setVisible(checked)
        
    def toggleMaximized(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def show_payment_window(self):
        self.main_win_2.close()
        self.main_win_3.show()            

                      
    def get_current_stack_page_name(self):

        current_index = self.uic.stackedWidget.currentIndex()
        page_names = {
            0: "Home",
            1: "Settings",
            2: "Account Check",
            3: "Filter Members",
            4: "Filter Data",
            5: "Add Members",
            6: "Spam Message",
            7: "Seeding",
            8: "Join Group Channel",
            9: "Leave Group Channel",
            10: "Buff Emotions",
            11: "Post Views",
            12: "Change Account Info"
        }

        current_line = inspect.currentframe().f_lineno
        print(f"Current line: {current_line}, Current Page: {page_names.get(current_index, 'Unknown Page')}")
        
        return page_names.get(current_index, "Unknown Page")
    
    def change_stack_index(self, index):
        self.uic.stackedWidget.setCurrentIndex(index)
        self.set_icon_based_on_index(index)
        self.update_current_menu_text(index)
        self.update_button(index)

    def set_icon_based_on_index(self, index):
        icons = {
            0: ":/images/icons/sidebar/icons8-home-50.png",
            1: ":/images/icons/sidebar/icons8-home-50.png",
            2: ":/images/icons/sidebar/icons8-check-50.png",
            3: ":/images/icons/sidebar/icons8-scan-50.png",
            4: ":/images/icons/sidebar/icons8-phone-50.png",
            5: ":/images/icons/sidebar/icons8-add-user-50.png",
            6: ":/images/icons/sidebar/icons8-send-50.png",
            7: ":/images/icons/sidebar/icons8-clone-50.png",
            8: ":/images/icons/sidebar/icons8-member-50.png",
            9: ":/images/icons/sidebar/icons8-exit-50.png",
            10: ":/images/icons/sidebar/icons8-emotion-50.png",
            11: ":/images/icons/sidebar/icons8-eye-50.png",
            12: ":/images/icons/sidebar/icons8-change-user-50.png"
        }

        if index in icons:
            self.uic.btnCurrentMenu.setIcon(QIcon(icons[index]))
            self.uic.btnCurrentMenu.setIconSize(QSize(30, 30))

    def update_current_menu_text(self, index):
        if self.sender() is not None and index not in [0, 1]:
            self.uic.btnCurrentMenu.setText(self.sender().text())
        else:
            self.uic.btnCurrentMenu.setText("CÀI ĐẶT")

    def update_button(self, index):
        if index not in [0, 1]:
            self.uic.btnStart.setVisible(True)
            self.uic.btnStop.setVisible(True)
            self.uic.btnStop.setEnabled(False)
            self.uic.btnAccount.setVisible(False)
            self.uic.btnProxy.setVisible(False)
        else:
            self.uic.btnAccount.setVisible(True)
            self.uic.btnProxy.setVisible(True)
            self.uic.btnStart.setVisible(False)
            self.uic.btnStop.setVisible(False)
        


    def mousePressEvent(self, event: QMouseEvent):
        """Called when the mouse is pressed."""
        try:
            self.oldPosition = event.globalPos()
            if event.button() == Qt.LeftButton:
                self.is_resizing = False
                self.resize_direction = None
                rect = self.rect()
                self.can_drag = False 

                if abs(event.pos().x() - rect.right()) < 20 and abs(event.pos().y() - rect.bottom()) < 20 :
                    self.resize_direction = 'bottom_right'
                    self.setCursor(Qt.SizeFDiagCursor)
                elif abs(event.pos().x() - rect.right()) < 20: 
                    self.resize_direction = 'right'
                    self.setCursor(Qt.SizeHorCursor)
                elif abs(event.pos().y() - rect.bottom()) < 20: 
                    self.resize_direction = 'bottom'
                    self.setCursor(Qt.SizeVerCursor)
                else:
                    self.setCursor(Qt.ArrowCursor)
                if self.resize_direction:
                    self.is_resizing = True
                elif event.pos().y() <= 100:
                    self.can_drag = True 
        except Exception as e:
            print(f"Error in mousePressEvent: {e}")


    def mouseMoveEvent(self, event: QMouseEvent):
        """Called when the mouse is moved."""
        try:
            if self.is_resizing:
                rect = self.rect()
                if self.resize_direction == 'bottom_right':
                     new_width = event.x() - rect.left()
                     new_height = event.y() - rect.top()
                     self.resize(new_width, new_height)
                elif self.resize_direction == 'right':
                    new_width = event.x() - rect.left()
                    self.resize(new_width, rect.height())
                elif self.resize_direction == 'bottom':
                    new_height = event.y() - rect.top()
                    self.resize(rect.width(), new_height)
            elif self.can_drag: 
                delta = event.globalPos() - self.oldPosition
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPosition = event.globalPos()

                rect = self.rect()
                if abs(event.pos().x() - rect.right()) < 20 and abs(event.pos().y() - rect.bottom()) < 20:
                     self.setCursor(Qt.SizeFDiagCursor)  
                elif abs(event.pos().x() - rect.right()) < 20:
                    self.setCursor(Qt.SizeHorCursor)  
                elif abs(event.pos().y() - rect.bottom()) < 20:
                    self.setCursor(Qt.SizeVerCursor)  
                else:
                    self.setCursor(Qt.ArrowCursor)  
        except Exception as e:
            print(f"Error in mouseMoveEvent: {e}")


    def mouseReleaseEvent(self, event: QMouseEvent):
        """Called when the mouse button is released."""
        try:
            if event.button() == Qt.LeftButton:
                self.is_resizing = False
                self.resize_direction = None
                self.can_drag = False
        except Exception as e:
            print(f"Error in mouseReleaseEvent: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    # main_win.main_win_2.show()
    #main_win.main_win_4.show()
    sys.exit(app.exec())
