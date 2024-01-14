# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout, QSpacerItem,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpinBox, QStackedWidget,
    QTabWidget, QTableView, QTextEdit,
    QVBoxLayout, QWidget, QAbstractScrollArea)

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheets = QWidget(MainWindow)
        self.styleSheets.setObjectName(u"styleSheets")
        font = QFont()
        font.setPointSize(10)
        self.styleSheets.setFont(font)
        self.styleSheets.setCursor(QCursor(Qt.ArrowCursor))
        self.styleSheets.setStyleSheet(u"/*/////////////////////////////////////////////////////////////////////////////////////////////////////////////\n"
"    Layouts   */\n"
"\n"
"#bgApp {	 background-color: #f8f9fa }\n"
"#bottomBar { background-color: #dee5ef }\n"
"\n"
" /*//////////////*/\n"
"/*Top Header*/\n"
"#topHeader { background-color: #7EAFE7 }\n"
"\n"
" /*//////////*/\n"
"/*Content*/\n"
"#pageContainer { background-color: #f8f9fa }\n"
"\n"
"QToolTip {\n"
"    color: #2f2f2f;\n"
"    background-color: #fff;\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 3px solid #d7dee7;\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px\n"
"}\n"
"\n"
"/*/////////////////////////////////////////////////////////////////////////////////////////////////////////////\n"
"    Menus    */\n"
"\n"
" /*////////////////*/\n"
"/* Top Buttons */\n"
"#topButtons { background-color: #f8f9fa; border: 2px solid #72A5DC;  border-radius: 5px; }\n"
"\n"
"#topButtons .QPushButton { border: none;  border-radius: 5px; }\n"
"#topButtons .QPushButton:hover { background-color: #dde4e6; border-style: solid; border-radius: 4px; }\n"
"#topButtons .QPushButton:pressed { background-color: #cdd7da; border-style: solid; border-radius: 4px; }\n"
"\n"
" /*////////////////*"
                        "/\n"
"/* Left Buttons */\n"
"\n"
"#leftMenuBox0 { background-color: #7EAFE7 }\n"
"#leftMenuBox { \n"
"	background-color: #f8f9fa; \n"
"	border-top: 2px solid #72A5DC; \n"
"	border-bottom: 2px solid #72A5DC\n"
"}\n"
"#leftMenuBox .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 16px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#leftMenuBox .QPushButton:hover { background-color: #dde4e6 }\n"
"#leftMenuBox .QPushButton:pressed { background-color: #cdd7da }\n"
"\n"
"#mmHomeBtn { background-image: url(:/images/images/icons/home.png) }\n"
"#mmDLBtn { background-image: url(:/images/images/icons/deadline.png) }\n"

"#mmPlanBtn { background-image: url(:/images/images/icons/plan.png) }\n"
"#mmStatisticsBtn { background-image: url(:/images/images/icons/statistics.png) }\n"
"\n"
"/*/////////////////////////////////////////////////////////////////////////////////////////////////////////////\n"
"    Page Container    */\n"
"\n"
"#pageContainer .QLabel { color: #1F1F1F; font-size: 10pt }\n"
"#pageContainer .QTableView, QTableWidget { border: 2px solid #7EAFE7; border-radius: 5px }\n"
"QScrollArea, QLineEdit, QTextEdit { border: none }\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget:pane {\n"
"	border: 2px solid #cad0d9;\n"
"	border-radius: 5px;\n"
"	padding: 7px;\n"
"	padding-top: 11px;\n"
"	padding-bottom: 11px\n"
"}\n"
"QTabWidget::tab-bar { left: 6px }\n"
"QTabBar::tab { \n"
"	border: 2px solid #cad0d9;\n"
"	border-bottom: none;\n"
"	padding: 4px\n"
"}\n"
"\n"
"QTabBar::tab:first { border-top-left-radius: 4px }\n"
"QTabBar::tab:last { border-top-right-radius: 4px }\n"
"QTabBar::tab:!first:!last { margin-left: -1px; margin-right: -1px }\n"
"QTabBar::tab:!selected { margin-top: 4px }\n"
"QTabBar::tab"
                        ":first { margin-right: -1px }\n"
"QTabBar::tab:last { margin-left: -1px }\n"
"QTabBar::tab:selected {\n"
"	border: 2px solid #b5bac1;\n"
"	border-bottom: none;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"/*QSpinBox*/\n"
"QDateEdit, QSpinBox {\n"
"	border: 2px solid #cad0d9;\n"
"	border-radius: 4px;\n"
"	padding: 2px;\n"
"	font-size: 10pt\n"
"}\n"
"QDateEdit::up-button, QDateEdit::down-button,\n"
"QSpinBox::up-button, QSpinBox::down-button {	\n"
"	background-color: #fff;\n"
"	border: 2px solid #b6bbc3;\n"
"	margin: -2px;\n"
"	width: 10px\n"
"}\n"
"QDateEdit::up-button, QSpinBox::up-button { margin-bottom: -1px; border-top-right-radius: 4px }\n"
"QDateEdit::down-button, QSpinBox::down-button { margin-top: -1px; border-bottom-right-radius: 4px }\n"
"QDateEdit::up-arrow, QSpinBox::up-arrow { image: url(:/icons/images/icons/icon_arrow-up.png); }\n"
"QDateEdit::down-arrow, QSpinBox::down-arrow { image: url(:/icons/images/icons/icon_arrow-down.png); }\n"
"\n"
"/*QCheckBox*/\n"
"QCheckBox::indicator:unchecked { image: url(:/icons/images/icons/icon_unchecked.png) }\n"
"QCheckBox::indicator:checked { image: url(:/icons/images/icons/icon_checked.png) }\n"
"\n"
"/*QScrollBar*/\n"
"QScrollBar:horizontal {height: 0}"
"QScrollBar:vertical {\n"
"	border: 2px solid #7EAFE7;\n"
"	border-radius: 5px;\n"
"	background: #ddd;\n"
"	width: 12px;\n"
"	margin: 17px 0 17px 0;\n"
" }\n"
"QScrollBar::handle:vertical {\n"
"	background: #fff;\n"
"	border: 1px solid #dee5ef;\n"
"	min-height: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"	border: 2px solid #cad0d9;\n"
"	background: #fff;\n"
"	height: 7px;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical { subcontrol-position: bottom }\n"
"QScrollBar::sub-line:vertical { subcontrol-position: top }\n"
"\n"
"QScrollBar::up-arrow:vertical { image: url(:/icons/images/icons/icon_arrow-up.png) }\n"
"QScrollBar::down-arrow:vertical { image: url(:/icons/images/icons/icon_arrow-down.png) }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"

"\n"
"#ph_mainlabelBorder, #pd_mainlabelBorder, #pg_mainlabelBorder,\n"
"#pp_mainlabelBorder, #ps_mainlabelBorder { border-top: 2px solid #dee5ef }\n"
"#ph_mainLabel, #pd_mainLabel, #pg_mainLabel,\n"
"#pp_mainLabel, #ps_mainLabel { margin-left: 5px; margin-right: 5px }\n"
"\n"
" /*//////////////*/\n"
"/*Home Page*/\n"
"#page_Home { background-color: #D9E9F5 }\n"
"#page_Home_Layout { background-color: #f8f9fa }\n"
"\n"
"#ph_border {\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-top: 2px dashed #dee5ef\n"
"}\n"
"\n"
"#ph_label_1 { margin-left: 3px }\n"
"#ph_label_2 { margin-left: 3px }\n"
"\n"
"#ph_tabWidget .QLabel { margin-left: 3px }\n"
"#ph_todayWidget, #ph_weekWidget, #ph_monthWidget { background-color: #fff }\n"
"\n"
" /*//////////////////*/\n"
"/*Deadlines Page*/\n"
"#page_Deadlines { background-color: #D9E9F5 }\n"
"#page_Deadlines_Layout { background-color: #f8f9fa }\n"
"#page_Deadlines_Layout .QLabel { margin-left: 3px }\n"
"\n"
" /*////////////*/\n"
"/*Plan Page*/\n"
"#page_Plan { background-color: #D9E9F5 }\n"
"#page_Plan_mainLayout { background-color: #f8f9fa }\n"
"#pp_border {\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-top: 2px dashed #dee5ef\n"
"}\n"
"\n"
"#pp_createTaskBtn, #pp_editTaskBtn {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	image-position: left;\n"
"	text-align: right;\n"
"}\n"
"#pp_createTaskBtn { image: url(:/icons/images/icons/icon_plus.png) }\n"
"#pp_createTaskBtn:hover { image: url(:/icons/images/icons/icon_plus_hov.png); color: #313131 }\n"
"#pp_editTaskBtn { image: url(:/icons/images/icons/icon_edit.png) }\n"
"#pp_editTaskBtn:hover { image: url(:/icons/images/icons/icon_edit_hov.png); color: #313131 }\n"
"\n"
"/*TaskEditFrame*/\n"
""
                        "#pp_te_habitLabel { margin-left: 5px }\n"
"#pp_te_dateFrame { border: 2px dashed #dee5ef }\n"
"#pp_te_datesFrame { border-top: 2px dashed #dee5ef }\n"
"#pp_te_DoW_Frame { border-right: 2px dashed #dee5ef; border-radius: 0px }\n"
"\n"
"#pp_te_habitFrame {\n"
"	border-left: 2px solid #dee5ef;\n"
"	border-radius: 0px;\n"
"	background-color: #fff\n"
"}\n"
"\n"
"#pp_te_cancelBtn, #pp_te_doneBtn {\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"}\n"
"#pp_te_doneBtn:hover, #pp_te_cancelBtn:hover { background-color: #dde4e6 }\n"
"\n"
"#pp_te_rBtn_1,\n"
"#pp_te_rBtn_2,\n"
"#pp_te_rBtn_3 { margin-right: -5px }\n"
"#pp_te_rBtn_1::indicator::unchecked { image: url(:/icons/images/icons/icon_ucRadio_pr1.png) }\n"
"#pp_te_rBtn_2::indicator::unchecked { image: url(:/icons/images/icons/icon_ucRadio_pr2.png) }\n"
"#pp_te_rBtn_3::indicator::unchecked { image: url(:/icons/images/icons/icon_ucRadio_pr3.png) }\n"
"#pp_te_rBtn_1::indicator::checked { image: url(:/icons/images/icons/icon_cRadio_pr1.png) }"
                        "\n"
"#pp_te_rBtn_2::indicator::checked { image: url(:/icons/images/icons/icon_cRadio_pr2.png) }\n"
"#pp_te_rBtn_3::indicator::checked { image: url(:/icons/images/icons/icon_cRadio_pr3.png) }\n"
"\n"
"#pp_te_deadlineFrame, #pp_te_endFrame, #pp_te_priorityFrame {\n"
"	border-left: 2px solid #dee5ef;\n"
"	border-radius: 0px;\n"
"	background-color: #fff\n"
"}\n"
"\n"
"#pp_te_taskEdit, #pp_te_noteEdit { border-bottom: 2px solid #dee5ef }\n"
"\n"
"\n"
" /*//////////////////*/\n"
"/*Statistics Page*/\n"
"#page_Statistics { background-color: #D9E9F5 }\n"
"#ps_mainLayout { background-color: #f8f9fa }\n"
"#ps_border_1, #ps_border_2 {\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	border-top: 2px dashed #dee5ef\n"
"}\n"
"#ps_archiveBg { background-color: #fff }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheets)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheets)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QVBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.topHeader = QFrame(self.bgApp)
        self.topHeader.setObjectName(u"topHeader")
        self.topHeader.setMinimumSize(QSize(0, 50))
        self.topHeader.setMaximumSize(QSize(16777215, 50))
        self.topHeader.setCursor(QCursor(Qt.ArrowCursor))
        self.topHeader.setFrameShadow(QFrame.Raised)
        self.headerLayout = QHBoxLayout(self.topHeader)
        self.headerLayout.setSpacing(0)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(0, 0, 10, 0)
        self.topLogo = QFrame(self.topHeader)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(50, 50))
        self.topLogo.setMaximumSize(QSize(16777215, 50))
        self.topLogo.setFrameShape(QFrame.StyledPanel)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.topLogo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(5, 5, 42, 42))
        self.logo.setStyleSheet(u"background-image: url(:/images/images/logo/spiral.png);")

        self.headerLayout.addWidget(self.topLogo)

        self.topLeftBox = QFrame(self.topHeader)
        self.topLeftBox.setObjectName(u"topLeftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLeftBox.sizePolicy().hasHeightForWidth())
        self.topLeftBox.setSizePolicy(sizePolicy)
        self.topLeftBox.setFont(font)
        self.topLeftBox.setCursor(QCursor(Qt.ArrowCursor))
        self.topLeftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topLeftBox)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.headerInfo = QLabel(self.topLeftBox)
        self.headerInfo.setObjectName(u"headerInfo")
        self.headerInfo.setMaximumSize(QSize(16777215, 45))
        self.headerInfo.setFont(font)
        self.headerInfo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.headerInfo)


        self.headerLayout.addWidget(self.topLeftBox)

        self.topButtons = QFrame(self.topHeader)
        self.topButtons.setObjectName(u"topButtons")
        self.topButtons.setMinimumSize(QSize(0, 32))
        self.topButtons.setMaximumSize(QSize(16777215, 32))
        self.topButtons.setCursor(QCursor(Qt.ArrowCursor))
        self.topButtons.setFrameShadow(QFrame.Raised)
        self.frameLayout = QHBoxLayout(self.topButtons)
        self.frameLayout.setSpacing(5)
        self.frameLayout.setObjectName(u"frameLayout")
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.topButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setFont(font)
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.frameLayout.addWidget(self.minimizeAppBtn)

        self.maximizeAppBtn = QPushButton(self.topButtons)
        self.maximizeAppBtn.setObjectName(u"maximizeAppBtn")
        self.maximizeAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeAppBtn.setFont(font)
        self.maximizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeAppBtn.setIcon(icon1)
        self.maximizeAppBtn.setIconSize(QSize(20, 20))

        self.frameLayout.addWidget(self.maximizeAppBtn)

        self.closeAppBtn = QPushButton(self.topButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setFont(font)
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.frameLayout.addWidget(self.closeAppBtn)


        self.headerLayout.addWidget(self.topButtons)


        self.appLayout.addWidget(self.topHeader)

        self.mainContent = QFrame(self.bgApp)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_5 = QHBoxLayout(self.mainContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBox0 = QFrame(self.mainContent)
        self.leftMenuBox0.setObjectName(u"leftMenuBox0")
        self.leftMenuBox0.setMinimumSize(QSize(50, 0))
        self.leftMenuBox0.setMaximumSize(QSize(50, 16777215))
        self.leftMenuBox0.setFont(font)
        self.leftMenuBox0.setCursor(QCursor(Qt.ArrowCursor))
        self.leftMenuBox0.setLayoutDirection(Qt.LeftToRight)
        self.leftMenuBox0.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuBox0)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalMenuLayout.setContentsMargins(0, 10, 0, 0)
        self.leftMenuBox = QFrame(self.leftMenuBox0)
        self.leftMenuBox.setObjectName(u"leftMenuBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuBox.sizePolicy().hasHeightForWidth())
        self.leftMenuBox.setSizePolicy(sizePolicy1)
        self.leftMenuBox.setMinimumSize(QSize(0, 0))
        self.leftMenuBox.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuBox.setFont(font)
        self.leftMenuBox.setCursor(QCursor(Qt.ArrowCursor))
        self.leftMenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.leftMenuBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mmHomeBtn = QPushButton(self.leftMenuBox)
        self.mmHomeBtn.setObjectName(u"mmHomeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mmHomeBtn.sizePolicy().hasHeightForWidth())
        self.mmHomeBtn.setSizePolicy(sizePolicy2)
        self.mmHomeBtn.setMinimumSize(QSize(0, 45))
        self.mmHomeBtn.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.mmHomeBtn.setFont(font1)
        self.mmHomeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.mmHomeBtn.setIconSize(QSize(45, 45))

        self.verticalLayout.addWidget(self.mmHomeBtn)

        self.mmDLBtn = QPushButton(self.leftMenuBox)
        self.mmDLBtn.setObjectName(u"mmDLBtn")
        sizePolicy2.setHeightForWidth(self.mmDLBtn.sizePolicy().hasHeightForWidth())
        self.mmDLBtn.setSizePolicy(sizePolicy2)
        self.mmDLBtn.setMinimumSize(QSize(0, 45))
        self.mmDLBtn.setFont(font)
        self.mmDLBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.mmDLBtn)

        self.mmPlanBtn = QPushButton(self.leftMenuBox)
        self.mmPlanBtn.setObjectName(u"mmPlanBtn")
        self.mmPlanBtn.setMinimumSize(QSize(0, 45))
        self.mmPlanBtn.setMaximumSize(QSize(16777215, 16777215))
        self.mmPlanBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.mmPlanBtn)

        self.mmStatisticsBtn = QPushButton(self.leftMenuBox)
        self.mmStatisticsBtn.setObjectName(u"mmStatisticsBtn")
        sizePolicy2.setHeightForWidth(self.mmStatisticsBtn.sizePolicy().hasHeightForWidth())
        self.mmStatisticsBtn.setSizePolicy(sizePolicy2)
        self.mmStatisticsBtn.setMinimumSize(QSize(0, 45))
        self.mmStatisticsBtn.setFont(font)
        self.mmStatisticsBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.mmStatisticsBtn)


        self.verticalMenuLayout.addWidget(self.leftMenuBox, 0, Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.leftMenuBox0)

        self.contentBox = QFrame(self.mainContent)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFont(font)
        self.contentBox.setCursor(QCursor(Qt.ArrowCursor))
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBox)
        self.content.setObjectName(u"content")
        self.content.setFont(font)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.content)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pageContainer = QFrame(self.content)
        self.pageContainer.setObjectName(u"pageContainer")
        sizePolicy.setHeightForWidth(self.pageContainer.sizePolicy().hasHeightForWidth())
        self.pageContainer.setSizePolicy(sizePolicy)
        self.pageContainer.setFont(font)
        self.pageContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.pageContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.pageContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font1)
        self.page_Home = QWidget()
        self.page_Home.setObjectName(u"page_Home")
        self.page_Home.setFont(font)
        self.page_Home.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.page_Home)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.page_Home_Layout = QFrame(self.page_Home)
        self.page_Home_Layout.setObjectName(u"page_Home_Layout")
        self.page_Home_Layout.setMaximumSize(QSize(1000, 16777215))
        self.page_Home_Layout.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_19 = QVBoxLayout(self.page_Home_Layout)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.ph_mainBg = QFrame(self.page_Home_Layout)
        self.ph_mainBg.setObjectName(u"ph_mainBg")
        self.ph_mainBg.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.ph_mainBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ph_mainlabelFrame = QFrame(self.ph_mainBg)
        self.ph_mainlabelFrame.setObjectName(u"ph_mainlabelFrame")
        self.ph_mainlabelFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_6 = QVBoxLayout(self.ph_mainlabelFrame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.ph_mainLabel = QLabel(self.ph_mainlabelFrame)
        self.ph_mainLabel.setObjectName(u"ph_mainLabel")
        self.ph_mainLabel.setFont(font)
        self.ph_mainLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.ph_mainLabel.setStyleSheet(u"color: rgb(101, 103, 107);")

        self.verticalLayout_6.addWidget(self.ph_mainLabel)

        self.ph_mainlabelBorder = QFrame(self.ph_mainlabelFrame)
        self.ph_mainlabelBorder.setObjectName(u"ph_mainlabelBorder")
        self.ph_mainlabelBorder.setMinimumSize(QSize(0, 2))
        self.ph_mainlabelBorder.setMaximumSize(QSize(16777215, 2))
        self.ph_mainlabelBorder.setFrameShape(QFrame.StyledPanel)
        self.ph_mainlabelBorder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.ph_mainlabelBorder)


        self.verticalLayout_3.addWidget(self.ph_mainlabelFrame, 0, Qt.AlignHCenter)

        self.ph_tabWidget = QTabWidget(self.ph_mainBg)
        self.ph_tabWidget.setObjectName(u"ph_tabWidget")
        self.ph_tabWidget.setFont(font)
        self.ph_todayWidget = QWidget()
        self.ph_todayWidget.setObjectName(u"ph_todayWidget")
        self.verticalLayout_9 = QVBoxLayout(self.ph_todayWidget)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ph_todayMainFrame = QFrame(self.ph_todayWidget)
        self.ph_todayMainFrame.setObjectName(u"ph_todayMainFrame")
        self.ph_todayMainFrame.setMinimumSize(QSize(0, 100))
        self.ph_todayMainFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_25 = QVBoxLayout(self.ph_todayMainFrame)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 9)
        self.ph_tabLabel_1 = QLabel(self.ph_todayMainFrame)
        self.ph_tabLabel_1.setObjectName(u"ph_tabLabel_1")

        self.verticalLayout_25.addWidget(self.ph_tabLabel_1)

        self.ph_mainTableToday = QTableView(self.ph_todayMainFrame)
        self.ph_mainTableToday.setObjectName(u"ph_mainTableToday")
        self.ph_mainTableToday.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_25.addWidget(self.ph_mainTableToday)


        self.verticalLayout_9.addWidget(self.ph_todayMainFrame)

        self.ph_border = QFrame(self.ph_todayWidget)
        self.ph_border.setObjectName(u"ph_border")
        self.ph_border.setMinimumSize(QSize(0, 2))
        self.ph_border.setMaximumSize(QSize(16777215, 2))
        self.ph_border.setFrameShape(QFrame.StyledPanel)
        self.ph_border.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.ph_border)

        self.ph_todayAddFrame = QFrame(self.ph_todayWidget)
        self.ph_todayAddFrame.setObjectName(u"ph_todayAddFrame")
        self.verticalLayout_7 = QVBoxLayout(self.ph_todayAddFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.ph_label_2 = QLabel(self.ph_todayAddFrame)
        self.ph_label_2.setObjectName(u"ph_label_2")
        self.ph_label_2.setMaximumSize(QSize(16777215, 16777215))
        self.ph_label_2.setFont(font)

        self.verticalLayout_7.addWidget(self.ph_label_2)

        self.ph_addTable = QTableView(self.ph_todayAddFrame)
        self.ph_addTable.setObjectName(u"ph_addTable")

        self.verticalLayout_7.addWidget(self.ph_addTable)


        self.verticalLayout_9.addWidget(self.ph_todayAddFrame)

        self.ph_tabWidget.addTab(self.ph_todayWidget, "")
        self.ph_weekWidget = QWidget()
        self.ph_weekWidget.setObjectName(u"ph_weekWidget")
        self.verticalLayout_20 = QVBoxLayout(self.ph_weekWidget)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.ph_tabLabel_2 = QLabel(self.ph_weekWidget)
        self.ph_tabLabel_2.setObjectName(u"ph_tabLabel_2")

        self.verticalLayout_20.addWidget(self.ph_tabLabel_2)

        self.ph_mainTableWeek = QTableView(self.ph_weekWidget)
        self.ph_mainTableWeek.setObjectName(u"ph_mainTableWeek")

        self.verticalLayout_20.addWidget(self.ph_mainTableWeek)

        self.ph_tabWidget.addTab(self.ph_weekWidget, "")
        self.ph_monthWidget = QWidget()
        self.ph_monthWidget.setObjectName(u"ph_monthWidget")
        self.verticalLayout_24 = QVBoxLayout(self.ph_monthWidget)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.ph_tabLabel_3 = QLabel(self.ph_monthWidget)
        self.ph_tabLabel_3.setObjectName(u"ph_tabLabel_3")

        self.verticalLayout_24.addWidget(self.ph_tabLabel_3)

        self.ph_mainTableMonth = QTableView(self.ph_monthWidget)
        self.ph_mainTableMonth.setObjectName(u"ph_mainTableMonth")

        self.verticalLayout_24.addWidget(self.ph_mainTableMonth)

        self.ph_tabWidget.addTab(self.ph_monthWidget, "")

        self.verticalLayout_3.addWidget(self.ph_tabWidget)

        self.verticalLayout_19.addWidget(self.ph_mainBg)

        self.ph_verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(self.ph_verticalSpacer)

        self.horizontalLayout_11.addWidget(self.page_Home_Layout)
        self.stackedWidget.addWidget(self.page_Home)


        self.page_Deadlines = QWidget()
        self.page_Deadlines.setObjectName(u"page_Deadlines")
        self.horizontalLayout_10 = QHBoxLayout(self.page_Deadlines)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.page_Deadlines_Layout = QFrame(self.page_Deadlines)
        self.page_Deadlines_Layout.setObjectName(u"page_Deadlines_Layout")
        self.page_Deadlines_Layout.setMaximumSize(QSize(1000, 16777215))

        self.verticalLayout_23 = QVBoxLayout(self.page_Deadlines_Layout)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 10, 0, 0)

        self.pd_mainlabelFrame = QFrame(self.page_Deadlines_Layout)
        self.pd_mainlabelFrame.setObjectName(u"pd_mainlabelFrame")
        self.verticalLayout_29 = QVBoxLayout(self.pd_mainlabelFrame)
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 5)
        self.pd_mainLabel = QLabel(self.pd_mainlabelFrame)
        self.pd_mainLabel.setObjectName(u"pd_mainLabel")
        self.pd_mainLabel.setStyleSheet(u"color: rgb(101, 103, 107);")

        self.verticalLayout_29.addWidget(self.pd_mainLabel)

        self.pd_mainlabelBorder = QFrame(self.pd_mainlabelFrame)
        self.pd_mainlabelBorder.setObjectName(u"pd_mainlabelBorder")
        self.pd_mainlabelBorder.setMinimumSize(QSize(0, 2))
        self.pd_mainlabelBorder.setMaximumSize(QSize(16777215, 2))
        self.pd_mainlabelBorder.setFrameShape(QFrame.StyledPanel)
        self.pd_mainlabelBorder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.pd_mainlabelBorder)


        self.verticalLayout_23.addWidget(self.pd_mainlabelFrame, 0, Qt.AlignHCenter)

        self.pd_tasks = QFrame(self.page_Deadlines_Layout)
        self.pd_tasks.setObjectName(u"pd_tasks")
        self.pd_tasks.setMinimumSize(QSize(0, 200))
        self.verticalLayout_15 = QVBoxLayout(self.pd_tasks)
        self.verticalLayout_15.setSpacing(12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 13, 10, 12)
        self.pd_tasksLabel_1 = QLabel(self.pd_tasks)
        self.pd_tasksLabel_1.setObjectName(u"pd_tasksLabel_1")
        self.pd_tasksLabel_1.setMinimumSize(QSize(0, 0))
        self.pd_tasksLabel_1.setFont(font)

        self.verticalLayout_15.addWidget(self.pd_tasksLabel_1)

        self.deadlines_tasks = QTableView(self.pd_tasks)
        self.deadlines_tasks.setObjectName(u"deadlines_tasks")

        self.verticalLayout_15.addWidget(self.deadlines_tasks)

        self.pd_tasksLabel_2 = QLabel(self.pd_tasks)
        self.pd_tasksLabel_2.setObjectName(u"pd_tasksLabel_2")
        self.pd_tasksLabel_2.setMinimumSize(QSize(0, 0))

        self.verticalLayout_15.addWidget(self.pd_tasksLabel_2)


        self.verticalLayout_23.addWidget(self.pd_tasks)

        self.pd_verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(self.pd_verticalSpacer)

        self.horizontalLayout_10.addWidget(self.page_Deadlines_Layout)

        self.stackedWidget.addWidget(self.page_Deadlines)

        self.page_Plan = QWidget()
        self.page_Plan.setObjectName(u"page_Plan")
        self.horizontalLayout_2 = QHBoxLayout(self.page_Plan)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_Plan)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(1000, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.pg_scrollAreaWidget = QWidget()
        self.pg_scrollAreaWidget.setObjectName(u"pg_scrollAreaWidget")
        self.pg_scrollAreaWidget.setGeometry(QRect(0, 0, 848, 696))
        self.horizontalLayout_22 = QHBoxLayout(self.pg_scrollAreaWidget)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.page_Plan_mainLayout = QFrame(self.pg_scrollAreaWidget)
        self.page_Plan_mainLayout.setObjectName(u"page_Plan_mainLayout")
        self.verticalLayout_28 = QVBoxLayout(self.page_Plan_mainLayout)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pp_mainlabelFrame = QFrame(self.page_Plan_mainLayout)
        self.pp_mainlabelFrame.setObjectName(u"pp_mainlabelFrame")
        self.verticalLayout_37 = QVBoxLayout(self.pp_mainlabelFrame)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 5)
        self.pp_mainLabel = QLabel(self.pp_mainlabelFrame)
        self.pp_mainLabel.setObjectName(u"pp_mainLabel")
        self.pp_mainLabel.setFont(font)
        self.pp_mainLabel.setStyleSheet(u"color: rgb(101, 103, 107);")

        self.verticalLayout_37.addWidget(self.pp_mainLabel)

        self.pp_mainlabelBorder = QFrame(self.pp_mainlabelFrame)
        self.pp_mainlabelBorder.setObjectName(u"pp_mainlabelBorder")
        self.pp_mainlabelBorder.setMinimumSize(QSize(0, 2))
        self.pp_mainlabelBorder.setMaximumSize(QSize(16777215, 2))
        self.pp_mainlabelBorder.setFrameShape(QFrame.StyledPanel)
        self.pp_mainlabelBorder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_37.addWidget(self.pp_mainlabelBorder)


        self.verticalLayout_28.addWidget(self.pp_mainlabelFrame, 0, Qt.AlignHCenter)

        self.pp_mainFrame = QFrame(self.page_Plan_mainLayout)
        self.pp_mainFrame.setObjectName(u"pp_mainFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pp_mainFrame.sizePolicy().hasHeightForWidth())
        self.pp_mainFrame.setSizePolicy(sizePolicy5)
        self.horizontalLayout_19 = QHBoxLayout(self.pp_mainFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pp_deadlineFrame = QFrame(self.pp_mainFrame)
        self.pp_deadlineFrame.setObjectName(u"pp_deadlineFrame")
        self.verticalLayout_31 = QVBoxLayout(self.pp_deadlineFrame)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.pp_dateLabel = QLabel(self.pp_deadlineFrame)
        self.pp_dateLabel.setObjectName(u"pp_dateLabel")

        self.verticalLayout_31.addWidget(self.pp_dateLabel)

        self.pp_dateEdit = QDateEdit(self.pp_deadlineFrame)
        self.pp_dateEdit.setObjectName(u"pp_dateEdit")
        self.pp_dateEdit.setFont(font)
        self.pp_dateEdit.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.pp_dateEdit.setMinimumDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.pp_dateEdit.setDate(QDate(2022, 1, 1))

        self.verticalLayout_31.addWidget(self.pp_dateEdit)

        self.pp_infoLable = QLabel(self.pp_deadlineFrame)
        self.pp_infoLable.setObjectName(u"pp_infoLable")
        self.pp_infoLable.setStyleSheet(u"color: rgb(101, 103, 107);")

        self.verticalLayout_31.addWidget(self.pp_infoLable)

        self.horizontalLayout_19.addWidget(self.pp_deadlineFrame, 0, Qt.AlignTop)

        self.pp_tableView = QTableView(self.pp_mainFrame)
        self.pp_tableView.setObjectName(u"pp_tableView")

        self.horizontalLayout_19.addWidget(self.pp_tableView, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.pp_mainFrame)

        self.pp_border = QFrame(self.page_Plan_mainLayout)
        self.pp_border.setObjectName(u"pp_border")
        self.pp_border.setMinimumSize(QSize(0, 2))
        self.pp_border.setMaximumSize(QSize(16777215, 2))
        self.pp_border.setFrameShape(QFrame.StyledPanel)
        self.pp_border.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28.addWidget(self.pp_border)

        self.pp_taskEditBtnsFrame = QFrame(self.page_Plan_mainLayout)
        self.pp_taskEditBtnsFrame.setObjectName(u"pp_taskEditBtnsFrame")
        self.pp_taskEditBtnsFrame.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_18 = QHBoxLayout(self.pp_taskEditBtnsFrame)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pp_createTaskBtn = QPushButton(self.pp_taskEditBtnsFrame)
        self.pp_createTaskBtn.setObjectName(u"pp_createTaskBtn")
        self.pp_createTaskBtn.setMinimumSize(QSize(109, 0))
        self.pp_createTaskBtn.setFont(font)
        self.pp_createTaskBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.pp_createTaskBtn)

        self.pp_editTaskBtn = QPushButton(self.pp_taskEditBtnsFrame)
        self.pp_editTaskBtn.setObjectName(u"pp_editTaskBtn")
        self.pp_editTaskBtn.setMinimumSize(QSize(152, 0))
        self.pp_editTaskBtn.setFont(font)
        self.pp_editTaskBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_18.addWidget(self.pp_editTaskBtn)


        self.verticalLayout_28.addWidget(self.pp_taskEditBtnsFrame, 0, Qt.AlignHCenter)

        self.pp_taskEditFrame = QFrame(self.page_Plan_mainLayout)
        self.pp_taskEditFrame.setObjectName(u"pp_taskEditFrame")
        self.verticalLayout_30 = QVBoxLayout(self.pp_taskEditFrame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.pp_te_taskEdit = QLineEdit(self.pp_taskEditFrame)
        self.pp_te_taskEdit.setObjectName(u"pp_te_taskEdit")

        self.verticalLayout_30.addWidget(self.pp_te_taskEdit)

        self.pp_te_noteEdit = QTextEdit(self.pp_taskEditFrame)
        self.pp_te_noteEdit.setObjectName(u"pp_te_noteEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pp_te_noteEdit.sizePolicy().hasHeightForWidth())
        self.pp_te_noteEdit.setSizePolicy(sizePolicy6)
        self.pp_te_noteEdit.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_30.addWidget(self.pp_te_noteEdit)

        self.pp_te_isHabit_cBox = QCheckBox(self.pp_taskEditFrame)
        self.pp_te_isHabit_cBox.setObjectName(u"pp_te_isHabit_cBox")
        self.pp_te_isHabit_cBox.setFont(font)
        self.pp_te_isHabit_cBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_30.addWidget(self.pp_te_isHabit_cBox, 0, Qt.AlignLeft)

        self.pp_te_habitFrame = QFrame(self.pp_taskEditFrame)
        self.pp_te_habitFrame.setObjectName(u"pp_te_habitFrame")
        self.verticalLayout_32 = QVBoxLayout(self.pp_te_habitFrame)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 5, 0, 0)
        self.pp_te_habitLabel = QLabel(self.pp_te_habitFrame)
        self.pp_te_habitLabel.setObjectName(u"pp_te_habitLabel")

        self.verticalLayout_32.addWidget(self.pp_te_habitLabel, 0, Qt.AlignLeft)

        self.pp_te_dateFrame = QFrame(self.pp_te_habitFrame)
        self.pp_te_dateFrame.setObjectName(u"pp_te_dateFrame")
        self.pp_te_dateFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_33 = QVBoxLayout(self.pp_te_dateFrame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.pp_te_dateRBtns = QFrame(self.pp_te_dateFrame)
        self.pp_te_dateRBtns.setObjectName(u"pp_te_dateRBtns")
        self.horizontalLayout_24 = QHBoxLayout(self.pp_te_dateRBtns)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, 2, 10, 2)
        self.DoW_rBtn = QRadioButton(self.pp_te_dateRBtns)
        self.DoW_rBtn.setObjectName(u"DoW_rBtn")
        self.DoW_rBtn.setFont(font)
        self.DoW_rBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.DoW_rBtn)

        self.daysInRow_rBtn = QRadioButton(self.pp_te_dateRBtns)
        self.daysInRow_rBtn.setObjectName(u"daysInRow_rBtn")
        self.daysInRow_rBtn.setFont(font)
        self.daysInRow_rBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_24.addWidget(self.daysInRow_rBtn)


        self.verticalLayout_33.addWidget(self.pp_te_dateRBtns, 0, Qt.AlignLeft)

        self.pp_te_datesFrame = QFrame(self.pp_te_dateFrame)
        self.pp_te_datesFrame.setObjectName(u"pp_te_datesFrame")
        self.horizontalLayout_23 = QHBoxLayout(self.pp_te_datesFrame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pp_te_DoW_Frame = QFrame(self.pp_te_datesFrame)
        self.pp_te_DoW_Frame.setObjectName(u"pp_te_DoW_Frame")
        self.verticalLayout_34 = QVBoxLayout(self.pp_te_DoW_Frame)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(5, 5, 2, 5)
        self.ppte_mon = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_mon.setObjectName(u"ppte_mon")
        font2 = QFont()
        font2.setPointSize(9)
        self.ppte_mon.setFont(font2)
        self.ppte_mon.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_mon, 0, Qt.AlignLeft)

        self.ppte_tue = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_tue.setObjectName(u"ppte_tue")
        self.ppte_tue.setFont(font2)
        self.ppte_tue.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_tue, 0, Qt.AlignLeft)

        self.ppte_wen = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_wen.setObjectName(u"ppte_wen")
        self.ppte_wen.setFont(font2)
        self.ppte_wen.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_wen, 0, Qt.AlignLeft)

        self.ppte_thu = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_thu.setObjectName(u"ppte_thu")
        self.ppte_thu.setFont(font2)
        self.ppte_thu.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_thu, 0, Qt.AlignLeft)

        self.ppte_fri = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_fri.setObjectName(u"ppte_fri")
        self.ppte_fri.setFont(font2)
        self.ppte_fri.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_fri, 0, Qt.AlignLeft)

        self.ppte_sat = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_sat.setObjectName(u"ppte_sat")
        self.ppte_sat.setFont(font2)
        self.ppte_sat.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_sat, 0, Qt.AlignLeft)

        self.ppte_sun = QCheckBox(self.pp_te_DoW_Frame)
        self.ppte_sun.setObjectName(u"ppte_sun")
        self.ppte_sun.setFont(font2)
        self.ppte_sun.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.ppte_sun, 0, Qt.AlignLeft)


        self.horizontalLayout_23.addWidget(self.pp_te_DoW_Frame)

        self.pp_te_daysInRow_Frame = QFrame(self.pp_te_datesFrame)
        self.pp_te_daysInRow_Frame.setObjectName(u"pp_te_daysInRow_Frame")
        self.pp_te_daysInRow_Frame.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_25 = QHBoxLayout(self.pp_te_daysInRow_Frame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pp_te_spinBox = QSpinBox(self.pp_te_daysInRow_Frame)
        self.pp_te_spinBox.setObjectName(u"pp_te_spinBox")
        self.pp_te_spinBox.setMinimum(1)
        self.pp_te_spinBox.setMaximum(64)
        self.pp_te_spinBox.setValue(1)

        self.horizontalLayout_25.addWidget(self.pp_te_spinBox, 0, Qt.AlignTop)


        self.horizontalLayout_23.addWidget(self.pp_te_daysInRow_Frame)


        self.verticalLayout_33.addWidget(self.pp_te_datesFrame)


        self.verticalLayout_32.addWidget(self.pp_te_dateFrame, 0, Qt.AlignLeft)


        self.verticalLayout_30.addWidget(self.pp_te_habitFrame)

        self.pp_te_priorityFrame = QFrame(self.pp_taskEditFrame)
        self.pp_te_priorityFrame.setObjectName(u"pp_te_priorityFrame")
        self.horizontalLayout_26 = QHBoxLayout(self.pp_te_priorityFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(9, 9, 9, 9)
        self.pp_te_label = QLabel(self.pp_te_priorityFrame)
        self.pp_te_label.setObjectName(u"pp_te_label")

        self.horizontalLayout_26.addWidget(self.pp_te_label)

        self.pp_te_rBtn_1 = QRadioButton(self.pp_te_priorityFrame)
        self.pp_te_rBtn_1.setObjectName(u"pp_te_rBtn_1")
        self.pp_te_rBtn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.pp_te_rBtn_1)

        self.pp_te_rBtn_2 = QRadioButton(self.pp_te_priorityFrame)
        self.pp_te_rBtn_2.setObjectName(u"pp_te_rBtn_2")
        self.pp_te_rBtn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.pp_te_rBtn_2)

        self.pp_te_rBtn_3 = QRadioButton(self.pp_te_priorityFrame)
        self.pp_te_rBtn_3.setObjectName(u"pp_te_rBtn_3")
        self.pp_te_rBtn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.pp_te_rBtn_3)


        self.verticalLayout_30.addWidget(self.pp_te_priorityFrame, 0, Qt.AlignLeft)

        self.pp_te_deadlineFrame = QFrame(self.pp_taskEditFrame)
        self.pp_te_deadlineFrame.setObjectName(u"pp_te_deadlineFrame")
        self.pp_te_deadlineFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_35 = QVBoxLayout(self.pp_te_deadlineFrame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(9, 9, 9, 9)
        self.pp_te_DLLabel = QLabel(self.pp_te_deadlineFrame)
        self.pp_te_DLLabel.setObjectName(u"pp_te_DLLabel")

        self.verticalLayout_35.addWidget(self.pp_te_DLLabel)

        self.pp_te_changeDateFrame = QFrame(self.pp_te_deadlineFrame)
        self.pp_te_changeDateFrame.setObjectName(u"pp_te_changeDateFrame")
        self.pp_te_changeDateFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalLayout_20 = QHBoxLayout(self.pp_te_changeDateFrame)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pp_te_dateEdit = QDateEdit(self.pp_te_changeDateFrame)
        self.pp_te_dateEdit.setObjectName(u"pp_te_dateEdit")
        self.pp_te_dateEdit.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.pp_te_dateEdit.setMinimumDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.pp_te_dateEdit.setDate(QDate(2022, 1, 1))

        self.horizontalLayout_20.addWidget(self.pp_te_dateEdit)

        self.pp_te_isDLless = QCheckBox(self.pp_te_changeDateFrame)
        self.pp_te_isDLless.setObjectName(u"pp_te_isDLless")
        self.pp_te_isDLless.setFont(font)
        self.pp_te_isDLless.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.pp_te_isDLless)


        self.verticalLayout_35.addWidget(self.pp_te_changeDateFrame, 0, Qt.AlignLeft)


        self.verticalLayout_30.addWidget(self.pp_te_deadlineFrame)

        self.pp_te_endFrame = QFrame(self.pp_taskEditFrame)
        self.pp_te_endFrame.setObjectName(u"pp_te_endFrame")
        self.horizontalLayout_27 = QHBoxLayout(self.pp_te_endFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.pp_te_doneBtn = QPushButton(self.pp_te_endFrame)
        self.pp_te_doneBtn.setObjectName(u"pp_te_doneBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_done.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pp_te_doneBtn.setIcon(icon4)
        self.pp_te_doneBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_27.addWidget(self.pp_te_doneBtn)

        self.pp_te_cancelBtn = QPushButton(self.pp_te_endFrame)
        self.pp_te_cancelBtn.setObjectName(u"pp_te_cancelBtn")
        self.pp_te_cancelBtn.setIcon(icon2)
        self.pp_te_cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_27.addWidget(self.pp_te_cancelBtn)


        self.verticalLayout_30.addWidget(self.pp_te_endFrame, 0, Qt.AlignLeft)


        self.verticalLayout_28.addWidget(self.pp_taskEditFrame)

        self.pp_verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayout_28.addItem(self.pp_verticalSpacer)

        self.horizontalLayout_22.addWidget(self.page_Plan_mainLayout)

        self.scrollArea.setWidget(self.pg_scrollAreaWidget)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_Plan)
        self.page_Statistics = QWidget()
        self.page_Statistics.setObjectName(u"page_Statistics")
        self.horizontalLayout_8 = QHBoxLayout(self.page_Statistics)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ps_mainLayout = QFrame(self.page_Statistics)
        self.ps_mainLayout.setObjectName(u"ps_mainLayout")
        self.ps_mainLayout.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.ps_mainLayout)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.ps_mainlabelFrame = QFrame(self.ps_mainLayout)
        self.ps_mainlabelFrame.setObjectName(u"ps_mainlabelFrame")
        self.verticalLayout_4 = QVBoxLayout(self.ps_mainlabelFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.ps_mainLabel = QLabel(self.ps_mainlabelFrame)
        self.ps_mainLabel.setObjectName(u"ps_mainLabel")
        self.ps_mainLabel.setStyleSheet(u"color: rgb(101, 103, 107);")

        self.verticalLayout_4.addWidget(self.ps_mainLabel)

        self.ps_mainlabelBorder = QFrame(self.ps_mainlabelFrame)
        self.ps_mainlabelBorder.setObjectName(u"ps_mainlabelBorder")
        self.ps_mainlabelBorder.setMinimumSize(QSize(0, 2))
        self.ps_mainlabelBorder.setMaximumSize(QSize(16777215, 2))
        self.ps_mainlabelBorder.setFrameShape(QFrame.StyledPanel)
        self.ps_mainlabelBorder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.ps_mainlabelBorder)


        self.verticalLayout_22.addWidget(self.ps_mainlabelFrame, 0, Qt.AlignHCenter)

        self.ps_habitsFrame = QFrame(self.ps_mainLayout)
        self.ps_habitsFrame.setObjectName(u"ps_habitsFrame")
        self.ps_habitsFrame.setMinimumSize(QSize(0, 100))
        self.verticalLayout_17 = QVBoxLayout(self.ps_habitsFrame)
        self.verticalLayout_17.setSpacing(12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 0, 10, 12)
        self.ps_habitsLabel = QLabel(self.ps_habitsFrame)
        self.ps_habitsLabel.setObjectName(u"ps_habitsLabel")
        self.ps_habitsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.ps_habitsLabel)

        self.ps_habitsTable = QTableView(self.ps_habitsFrame)
        self.ps_habitsTable.setObjectName(u"ps_habitsTable")

        self.verticalLayout_17.addWidget(self.ps_habitsTable)


        self.verticalLayout_22.addWidget(self.ps_habitsFrame)

        self.ps_border_2 = QFrame(self.ps_mainLayout)
        self.ps_border_2.setObjectName(u"ps_border_2")
        self.ps_border_2.setMinimumSize(QSize(0, 2))
        self.ps_border_2.setMaximumSize(QSize(16777215, 2))
        self.ps_border_2.setFrameShape(QFrame.StyledPanel)
        self.ps_border_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.ps_border_2)

        self.ps_archiveFrame = QFrame(self.ps_mainLayout)
        self.ps_archiveFrame.setObjectName(u"ps_archiveFrame")
        self.verticalLayout_12 = QVBoxLayout(self.ps_archiveFrame)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 13, 10, 12)
        self.ps_archiveLabel = QLabel(self.ps_archiveFrame)
        self.ps_archiveLabel.setObjectName(u"ps_archiveLabel")
        self.ps_archiveLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.ps_archiveLabel)

        self.ps_archiveTable = QTableView(self.ps_archiveFrame)
        self.ps_archiveTable.setObjectName(u"ps_archiveTable")

        self.verticalLayout_12.addWidget(self.ps_archiveTable)


        self.verticalLayout_22.addWidget(self.ps_archiveFrame)

        self.ps_verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(self.ps_verticalSpacer)

        self.horizontalLayout_8.addWidget(self.ps_mainLayout)

        self.stackedWidget.addWidget(self.page_Statistics)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_14.addWidget(self.pageContainer)


        self.verticalLayout_2.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBox)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFont(font)
        self.bottomBar.setCursor(QCursor(Qt.ArrowCursor))
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setStyleSheet(u"color: rgb(152, 137, 122);")

        self.horizontalLayout_17.addWidget(self.creditsLabel)

        self.frameSizeGrip = QFrame(self.bottomBar)
        self.frameSizeGrip.setObjectName(u"frameSizeGrip")
        self.frameSizeGrip.setMinimumSize(QSize(22, 0))
        self.frameSizeGrip.setMaximumSize(QSize(22, 16777215))
        self.frameSizeGrip.setFont(font)
        self.frameSizeGrip.setFrameShape(QFrame.NoFrame)
        self.frameSizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frameSizeGrip)


        self.verticalLayout_2.addWidget(self.bottomBar)


        self.horizontalLayout_5.addWidget(self.contentBox)


        self.appLayout.addWidget(self.mainContent)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheets)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.ph_tabWidget.setCurrentIndex(0)

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # Tooltips

        self.minimizeAppBtn.setToolTip('Свернуть')
        self.maximizeAppBtn.setToolTip('Развернуть')
        self.closeAppBtn.setToolTip('Закрыть приложение')

        self.mmHomeBtn.setToolTip('Домашняя страница')
        self.mmDLBtn.setToolTip('Страница Дедлайны')
        self.mmPlanBtn.setToolTip('Страница Планирование')
        self.mmStatisticsBtn.setToolTip('Страница Статистика')

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.logo.setText("")
        self.headerInfo.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.mmHomeBtn.setText("")
        self.mmDLBtn.setText("")
        self.mmPlanBtn.setText("")
        self.mmStatisticsBtn.setText("")
        self.ph_mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430</span></p></body></html>", None))
        self.ph_tabLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e x \u0434\u0435\u043b (\u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 y \u0441\u0434\u0435\u043b\u0430\u043d\u043e)", None))
        self.ph_label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0435\u043b\u0430:", None))
        self.ph_tabWidget.setTabText(self.ph_tabWidget.indexOf(self.ph_todayWidget), QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.ph_tabLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u044d\u0442\u0443 \u043d\u0435\u0434\u0435\u043b\u044e \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 \u0434\u0435\u043b\u0430:", None))
        self.ph_tabWidget.setTabText(self.ph_tabWidget.indexOf(self.ph_weekWidget), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043d\u0435\u0434\u0435\u043b\u044f", None))
        self.ph_tabLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u044d\u0442\u043e\u0442 \u043c\u0435\u0441\u044f\u0446 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 \u0434\u0435\u043b\u0430:", None))
        self.ph_tabWidget.setTabText(self.ph_tabWidget.indexOf(self.ph_monthWidget), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.pd_mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0414\u0435\u0434\u043b\u0430\u0439\u043d\u044b</span></p></body></html>", None))
        self.pd_tasksLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u044b \u0441\u0440\u043e\u043a\u0438 \u0432\u0441\u0435\u0445 \u0432\u0430\u0448\u0438\u0445 \u0437\u0430\u0434\u0430\u0447:", None))
        self.pd_tasksLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u0423 \u0432\u0430\u0441 x \u0441\u0440\u043e\u0447\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447. \u0423\u0434\u0430\u0447\u0438 \u0432 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438!", None))

        self.pp_mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.pp_dateLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0430\u0442\u0443\n"
"\u0434\u043b\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pp_infoLable.setText(QCoreApplication.translate("MainWindow", u"\n"
" \u0417\u0434\u0435\u0441\u044c \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0443\u043a\u0430\u0437\u0430\u0442\u044c,\n"
" \u043a\u043e\u0433\u0434\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u0442\u0435\n"
" \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pp_createTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pp_editTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.pp_te_isHabit_cBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0432\u044b\u0447\u043a\u0430", None))
        self.pp_te_habitLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435, \u0441 \u043a\u0430\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u043e\u0442\u043e\u0439 \u043e\u043d\u0430 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0442\u044c\u0441\u044f", None))
        self.DoW_rBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u043d\u044f\u043c \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.daysInRow_rBtn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0436\u0434\u044b\u0435 x \u0434\u043d\u0435\u0439", None))
        self.ppte_mon.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None))
        self.ppte_tue.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None))
        self.ppte_wen.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u0430", None))
        self.ppte_thu.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None))
        self.ppte_fri.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None))
        self.ppte_sat.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0431\u0431\u043e\u0442\u0430", None))
        self.ppte_sun.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435", None))
        self.pp_te_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442:", None))
        self.pp_te_rBtn_1.setText("")
        self.pp_te_rBtn_2.setText("")
        self.pp_te_rBtn_3.setText("")
        self.pp_te_DLLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d:", None))
        self.pp_te_isDLless.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0441\u0441\u0440\u043e\u0447\u043d\u043e", None))
        self.pp_te_doneBtn.setText("")
        self.pp_te_cancelBtn.setText("")
        self.ps_mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430</span></p></body></html>", None))
        self.ps_habitsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0432\u044b\u0447\u043a\u0438\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043e\u0431\u0440\u0430\u043d\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0432\u0430\u0448\u0438\u043c \u043f\u0440\u0438\u0432\u044b\u0447\u043a\u0430\u043c", None))
        self.ps_archiveLabel.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043e\u0431\u0440\u0430\u043d\u044b \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 \u0437\u0430 5 \u043f\u0440\u043e\u0448\u043b\u044b\u0445 \u0434\u043d\u0435\u0439", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Stepanov Viktor", None))
    # retranslateUi

