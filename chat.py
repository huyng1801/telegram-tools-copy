# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatForm(object):
    def setupUi(self, ChatForm):
        ChatForm.setObjectName("ChatForm")
        ChatForm.resize(1280, 720)
        ChatForm.setStyleSheet("QWidget#wtSidebar QPushButton {\n"
"    background-color: transparent;\n"
"    color: #1677FF;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    border-bottom: 2px solid transparent;\n"
"}\n"
"\n"
"QWidget#wtSidebar QPushButton:hover {\n"
"    border-bottom: 2px solid #1677FF;\n"
"}\n"
"\n"
"#wtSidebarHeader {\n"
"    background-color: white;\n"
"    border-bottom: 1px solid #d9d9d9;\n"
"}\n"
"\n"
"#wtSidebar QListWidget {\n"
"    border: none;\n"
"    background-color: white;\n"
"}\n"
"\n"
"#wtMessage QListWidget {\n"
"    border: none;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"#wtSidebar QListWidget::item {\n"
"    padding: 5px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"\n"
"#wtChatHeader {\n"
"    background: white;\n"
"    border-left: 1px solid #d9d9d9;\n"
"}\n"
"\n"
"#wtChatHeader QLabel {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#wtInput {\n"
"    background: white;\n"
"    border-left: 1px solid #d9d9d9;\n"
"}\n"
"\n"
"#wtInput QLineEdit {\n"
"    background: white;\n"
"    border: 1px solid #d9d9d9;\n"
"    padding: 5px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#wtInput QPushButton {\n"
"    color: white;\n"
"    background: #1677ff;\n"
"    padding: 9px;\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(ChatForm)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wtContainer = QtWidgets.QWidget(ChatForm)
        self.wtContainer.setObjectName("wtContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wtContainer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wtSidebar = QtWidgets.QWidget(self.wtContainer)
        self.wtSidebar.setObjectName("wtSidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wtSidebar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wtSidebarHeader = QtWidgets.QWidget(self.wtSidebar)
        self.wtSidebarHeader.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wtSidebarHeader.setObjectName("wtSidebarHeader")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.wtSidebarHeader)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnChatRoom = QtWidgets.QPushButton(self.wtSidebarHeader)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/chat/icons8-user-groups-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnChatRoom.setIcon(icon)
        self.btnChatRoom.setObjectName("btnChatRoom")
        self.horizontalLayout_3.addWidget(self.btnChatRoom)
        self.btnUser = QtWidgets.QPushButton(self.wtSidebarHeader)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/chat/icons8-user-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUser.setIcon(icon1)
        self.btnUser.setIconSize(QtCore.QSize(15, 15))
        self.btnUser.setObjectName("btnUser")
        self.horizontalLayout_3.addWidget(self.btnUser)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 11)
        self.verticalLayout.addWidget(self.wtSidebarHeader)
        self.widget_2 = QtWidgets.QWidget(self.wtSidebar)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstContact = QtWidgets.QListWidget(self.widget_2)
        self.lstContact.setObjectName("lstContact")
        item = QtWidgets.QListWidgetItem()
        self.lstContact.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstContact.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstContact.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstContact.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lstContact.addItem(item)
        self.verticalLayout_2.addWidget(self.lstContact)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout_2.addWidget(self.wtSidebar)
        self.wtChat = QtWidgets.QWidget(self.wtContainer)
        self.wtChat.setObjectName("wtChat")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wtChat)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wtChatHeader = QtWidgets.QWidget(self.wtChat)
        self.wtChatHeader.setObjectName("wtChatHeader")
        self.labelRoomName = QtWidgets.QLabel(self.wtChatHeader)
        self.labelRoomName.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.labelRoomName.setObjectName("labelRoomName")
        self.verticalLayout_3.addWidget(self.wtChatHeader)
        self.wtMessage = QtWidgets.QWidget(self.wtChat)
        self.wtMessage.setObjectName("wtMessage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.wtMessage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lstMessage = QtWidgets.QListWidget(self.wtMessage)
        self.lstMessage.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lstMessage.setObjectName("lstMessage")
        self.verticalLayout_4.addWidget(self.lstMessage)
        self.verticalLayout_3.addWidget(self.wtMessage)
        self.wtInput = QtWidgets.QWidget(self.wtChat)
        self.wtInput.setObjectName("wtInput")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.wtInput)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtInputMessage = QtWidgets.QLineEdit(self.wtInput)
        self.txtInputMessage.setObjectName("txtInputMessage")
        self.horizontalLayout_4.addWidget(self.txtInputMessage)
        self.btnSendMessage = QtWidgets.QPushButton(self.wtInput)
        self.btnSendMessage.setObjectName("btnSendMessage")
        self.horizontalLayout_4.addWidget(self.btnSendMessage)
        self.verticalLayout_3.addWidget(self.wtInput)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_2.addWidget(self.wtChat)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout.addWidget(self.wtContainer)

        self.retranslateUi(ChatForm)
        QtCore.QMetaObject.connectSlotsByName(ChatForm)

    def retranslateUi(self, ChatForm):
        _translate = QtCore.QCoreApplication.translate
        ChatForm.setWindowTitle(_translate("ChatForm", "Form"))
        self.btnChatRoom.setText(_translate("ChatForm", "Phòng chat"))
        self.btnUser.setText(_translate("ChatForm", "Người dùng"))
        __sortingEnabled = self.lstContact.isSortingEnabled()
        self.lstContact.setSortingEnabled(False)
        item = self.lstContact.item(0)
        item.setText(_translate("ChatForm", "New Item"))
        item = self.lstContact.item(1)
        item.setText(_translate("ChatForm", "New Item"))
        item = self.lstContact.item(2)
        item.setText(_translate("ChatForm", "New Item"))
        item = self.lstContact.item(3)
        item.setText(_translate("ChatForm", "New Item"))
        item = self.lstContact.item(4)
        item.setText(_translate("ChatForm", "New Item"))
        self.lstContact.setSortingEnabled(__sortingEnabled)
        self.labelRoomName.setText(_translate("ChatForm", "Tên"))
        self.btnSendMessage.setText(_translate("ChatForm", "Gửi"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatForm = QtWidgets.QWidget()
    ui = Ui_ChatForm()
    ui.setupUi(ChatForm)
    ChatForm.show()
    sys.exit(app.exec_())
