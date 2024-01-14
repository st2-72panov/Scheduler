from mainUi import *
from loadingBar import *
from QModels import *
import datetime, json


class DataReceiverClass(QThread):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

    def code_decode(self, fun, habits, dones, unfinished, undefined):
        for element in habits:
            if element[1][0] == 1:
                element[1][1][0] = fun(element[1][1][0])
            element[-1][0] = fun(element[-1][0])
            element[-1][1] = fun(element[-1][1])

        for db in (unfinished, dones):
            for element in db:
                element[1] = fun(element[1])
                element[2] = fun(element[2])

        for element in undefined:
            element[1] = fun(element[1])

    def run(self):
        data = dict()
        dateToList = lambda date: [date.year, date.month, date.day]
        habits = deepcopy(self.mainWindow.habits)
        dones = deepcopy(self.mainWindow.dones)
        unfinished = deepcopy(self.mainWindow.unfinished)
        undefined = deepcopy(self.mainWindow.undefined)
        self.code_decode(dateToList, habits, dones, unfinished, undefined)

        data['habits'] = habits
        data['dones'] = dones
        data['unfinished'] = unfinished
        data['undefined'] = undefined
        with open('saved_data.json', 'w') as sD:
            json.dump(data, sD)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init values
        self.dateDefining()
        self.dateDefineTimer = QTimer()
        self.dateDefineTimer.timeout.connect(self.dateDefining)
        self.dateDefineTimer.start(1000 * 60 * 5)

        self.dataReceiver = DataReceiverClass(self)

        # USER INTERFACE
        # /////////////////////////////////////////////////////////////////////////////////

        # Безрамочный режим
        self.maximized = False

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.topHeader.mouseMoveEvent = self.moveWindow
        self.ui.leftMenuBox0.mouseMoveEvent = self.moveWindow
        self.ui.topHeader.mouseDoubleClickEvent = self.dobleClickMaximizeRestore
        self.ui.leftMenuBox0.mouseDoubleClickEvent = self.dobleClickMaximizeRestore

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # Resize window
        self.sizegrip = QSizeGrip(self.ui.frameSizeGrip)
        self.sizegrip.setStyleSheet('width: 20px; height: 20px; margin 0px; padding: 0px;')

        # Смена курсора на tabBar
        self.ui.ph_tabWidget.tabBar().setCursor(Qt.PointingHandCursor)

        # BUTTONS CONNECTION
        # /////////////////////////////////////////////////////////////////////////////////

        # Main Menu
        self.ui.mmHomeBtn.clicked.connect(lambda: self.select_page(0))
        self.ui.mmDLBtn.clicked.connect(lambda: self.select_page(1))
        self.ui.mmPlanBtn.clicked.connect(lambda: self.select_page(2))
        self.ui.mmStatisticsBtn.clicked.connect(lambda: self.select_page(3))

        # Top Buttons
        self.ui.minimizeAppBtn.clicked.connect(self.showMinimized)
        self.ui.maximizeAppBtn.clicked.connect(self.maximize_restore)
        self.ui.closeAppBtn.clicked.connect(self.close)

        # Done Buttons
        self.ui.pp_te_doneBtn.clicked.connect(self.defineTask)
        self.ui.pp_te_cancelBtn.clicked.connect(
            lambda: self.createDialog('Создание задачи', 'Удалить?', self.cancelTask)
        )

        # Остальные кнопки

        self.ui.pp_te_isHabit_cBox.clicked.connect(self.reHide_Frame)
        self.ui.pp_createTaskBtn.clicked.connect(lambda: self.ui.pp_taskEditFrame.show())

        self.ui.ph_tabWidget.currentChanged.connect(lambda: self.resizeTables(0))

        # PLAN PAGE
        # /////////////////////////////////////////////////////////////////////////////////

        self.ui.pp_te_habitFrame.hide()
        self.ui.pp_taskEditFrame.hide()

    # USER INTERFACE AND AUXILIARY FUNCTIONS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def creatingError(self, text):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Осторожно!')
        dlg.setText(text)
        button = dlg.exec()

    def createDialog(self, title, text, ifYes):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(text)
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            ifYes()

    def setTableHeight(self, table):
        tableSpaceHeight = table.height() - 16
        modelDataHeight = table.rowHeight(0) * (table.model().rowCount(0) + 1)
        if tableSpaceHeight > modelDataHeight:
            table.setFixedHeight(modelDataHeight + 2)

    def findDelta(self, page_itself, k, tables):
        delta = page_itself.height() - k
        if type(tables) == tuple:
            for table in tables:
                delta -= (table.rowHeight(0) + 1) * (table.model().rowCount(0) + 1)
                self.setTableHeight(table)
        else:
            delta -= tables.rowHeight(0) * (tables.model().rowCount(0) + 1)
            self.setTableHeight(tables)
        return max(delta - 6, 0)

    def resizeTables(self, current_page):
        page_itself = self.ui.stackedWidget.widget(current_page)

        if current_page == 0:
            current_table_page = self.ui.ph_tabWidget.currentIndex()

            if current_table_page == 0:
                tableSize = self.ui.ph_mainTableToday.width() - 126
                self.ui.ph_mainTableToday.setColumnWidth(2, tableSize - tableSize // 2)
                self.ui.ph_mainTableToday.setColumnWidth(3, tableSize // 2)

                tableSize -= 75
                self.ui.ph_addTable.setColumnWidth(3, tableSize - tableSize // 2)
                self.ui.ph_addTable.setColumnWidth(4, tableSize // 2)

                delta = self.findDelta(page_itself, 206, (self.ui.ph_mainTableToday, self.ui.ph_addTable))
                self.ui.ph_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)

            elif current_table_page == 1:
                tableSize = self.ui.ph_mainTableWeek.width() - 126 - 75
                self.ui.ph_mainTableWeek.setColumnWidth(3, tableSize - tableSize // 2)
                self.ui.ph_mainTableWeek.setColumnWidth(4, tableSize // 2)

                delta = self.findDelta(page_itself, 438 - 322, self.ui.ph_mainTableWeek)
                self.ui.ph_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)

            elif current_table_page == 2:
                tableSize = self.ui.ph_mainTableMonth.width() - 126 - 75
                self.ui.ph_mainTableMonth.setColumnWidth(3, tableSize - tableSize // 2)
                self.ui.ph_mainTableMonth.setColumnWidth(4, tableSize // 2)

                delta = self.findDelta(page_itself, 438 - 322, self.ui.ph_mainTableMonth)
                self.ui.ph_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ui.verticalLayout_3.invalidate()

        elif current_page == 1:
            tableSize = self.ui.deadlines_tasks.width() - 126
            self.ui.deadlines_tasks.setColumnWidth(2, tableSize - tableSize // 2)
            self.ui.deadlines_tasks.setColumnWidth(3, tableSize // 2)

            delta = self.findDelta(page_itself, 458 - 329 + 16, self.ui.deadlines_tasks)
            self.ui.pd_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ui.verticalLayout_23.invalidate()

        elif current_page == 2:
            tableSize = self.ui.pp_tableView.width() - 126
            self.ui.pp_tableView.setColumnWidth(2, tableSize - tableSize // 2)
            self.ui.pp_tableView.setColumnWidth(3, tableSize // 2)

            k = 630
            if self.ui.pp_te_isHabit_cBox.isChecked():
                k -= 112
            else:
                k -= 200

            delta = page_itself.height() - k
            modelPaddingWidth = self.ui.pp_tableView.rowHeight(0) * (self.pp_tasksModel.rowCount(0) + 1)
            modelPaddingWidth = max(modelPaddingWidth, self.ui.pp_deadlineFrame.height() - 16)
            if modelPaddingWidth > self.ui.pp_deadlineFrame.height():
                delta = max(delta - (modelPaddingWidth + 6), 0)
            self.setTableHeight(self.ui.pp_tableView)
            self.ui.pp_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ui.verticalLayout_28.invalidate()

        elif current_page == 3:
            tableSize = self.ui.ps_habitsTable.width() - 5 - self.ui.ps_habitsTable.verticalHeader().width()
            self.ui.ps_habitsTable.setColumnWidth(0, tableSize // 2)
            self.ui.ps_habitsTable.setColumnWidth(1, tableSize // 2)

            tableSize = self.ui.ps_archiveTable.width() - 124
            self.ui.ps_archiveTable.setColumnWidth(2, tableSize - tableSize // 2)
            self.ui.ps_archiveTable.setColumnWidth(3, tableSize // 2)

            delta = (self.findDelta(page_itself, 458 - 275, (self.ui.ps_habitsTable, self.ui.ps_archiveTable)))
            self.ui.ps_verticalSpacer.changeSize(20, delta, QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ui.verticalLayout_22.invalidate()

    # QT OVERRIDEN UI METHODS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def resizeEvent(self, event):
        super().resizeEvent(event)
        current_page = self.ui.stackedWidget.currentIndex()
        self.resizeTables(current_page)

    def maximize_restore(self):
        if self.maximized:
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeAppBtn.setToolTip('Развернуть')
            self.ui.maximizeAppBtn.setIcon(QIcon(u':/icons/images/icons/icon_maximize.png'))
        else:
            self.showMaximized()
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeAppBtn.setToolTip('Восстановить')
            self.ui.maximizeAppBtn.setIcon(QIcon(u':/icons/images/icons/icon_restore.png'))
        self.maximized = not self.maximized

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        if self.maximized:
            self.maximize_restore()
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def dobleClickMaximizeRestore(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(100, lambda: self.maximize_restore())

    # BUTTONS CONNECTION
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def select_page(self, page):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidget.widget(page))
        self.resizeTables(page)

    def reHide_Frame(self):
        if self.ui.pp_te_isHabit_cBox.isChecked():
            self.ui.pp_te_habitFrame.show()
            self.ui.pp_te_priorityFrame.hide()
            self.ui.pp_te_deadlineFrame.hide()
        else:
            self.ui.pp_te_habitFrame.hide()
            self.ui.pp_te_priorityFrame.show()
            self.ui.pp_te_deadlineFrame.show()

    # MAIN SCRIPTS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def dateDefining(self):
        self.current_date = datetime.date.today()
        for dateEdit in (self.ui.pp_dateEdit, self.ui.pp_te_dateEdit):
            readDate = dateEdit.date()
            readDate = datetime.datetime(readDate.year(), readDate.month(), readDate.day())
            maxDate = readDate
            if readDate.year < self.current_date.year:
                maxDate = self.current_date
            elif readDate.month < self.current_date.month:
                maxDate = self.current_date
            elif readDate.day < self.current_date.day:
                maxDate = self.current_date
            dateEdit.setDate(maxDate)
            dateEdit.setMinimumDate(QDate(self.current_date.year, self.current_date.month, self.current_date.day))

    def code_decode(self, fun, habits, dones, unfinished, undefined):
        for element in habits:
            if element[1][0] == 1:
                element[1][1][0] = fun(element[1][1][0])
            element[-1][0] = fun(element[-1][0])
            element[-1][1] = fun(element[-1][1])

        for db in (unfinished, dones):
            for element in db:
                element[1] = fun(element[1])
                element[2] = fun(element[2])

        for element in undefined:
            element[1] = fun(element[1])

    def saveData(self):
        data = dict()
        dateToList = lambda date: [date.year, date.month, date.day]
        habits = deepcopy(self.habits)
        dones = deepcopy(self.dones)
        unfinished = deepcopy(self.unfinished)
        undefined = deepcopy(self.undefined)
        self.code_decode(dateToList, habits, dones, unfinished, undefined)

        data['habits'] = habits
        data['dones'] = dones
        data['unfinished'] = unfinished
        data['undefined'] = undefined
        with open('saved_data.json', 'w') as sD:
            json.dump(data, sD)

    def receiveData(self):
        """
        listToDate = lambda lst: datetime.datetime(lst[0], lst[1], lst[2])
        with open('saved_data.json', 'r') as rD:
            dataBase = json.load(rD)

        self.habits = dataBase['habits']
        self.dones = dataBase['dones']
        self.unfinished = dataBase['unfinished']
        self.undefined = dataBase['undefined']
        self.code_decode(listToDate, self.habits, self.dones, self.unfinished, self.undefined)

        for db in (self.habits, self.dones, self.unfinished, self.undefined):
            db.sort(key=lambda row: row[1])
        """
        self.habits = [
            [
                [3, 0], [0, [6, 7]], 'Привычка 2',
                'Пояснение', 1, 10, [datetime.datetime(2022, 4, 20), datetime.datetime(2022, 4, 20)]
            ],
            [
                [3, 0], [1, [datetime.datetime(2022, 4, 10), 2]], 'Привычка 1',
                'Пояснение', 1, 10, [datetime.datetime(2022, 4, 20), datetime.datetime(2022, 4, 20)]
            ]
        ]

        self.dones = sorted([
            [[1, 1], datetime.datetime(2022, 5, 10), datetime.datetime(2022, 4, 17),  'Задача 1', 'Пояснение'],
            [[2, 1], datetime.datetime(2022, 6, 11), datetime.datetime(2022, 4, 18),  'Задача 2', 'Пояснение']
            ], key=lambda row: row[1])

        self.unfinished = sorted([
            [[0, 0], datetime.datetime(2022, 4, 16), datetime.datetime(2022, 12, 23),  'Задача 3', 'Пояснение'],
            [[1, 0], datetime.datetime(2022, 4, 26), datetime.datetime(2022, 4, 19), 'Задача 4', 'Пояснение']
            ], key=lambda row: row[1])

        self.undefined = sorted([
            [[0, 0],  datetime.datetime(2022, 4, 17), 'Задача 5', 'Пояснение'],
            [[1, 0],  datetime.datetime(2022, 7, 23), 'Задача 6', 'Пояснение']
        ], key=lambda row: row[1])
        splashScreen.clock(self, 35, 1)

    def setData(self):

        todayTasks = list()
        otherData = list()
        weekTasks = list()
        monthTasks = list()
        tasksDeadlines = list()
        planTasks = deepcopy(self.undefined)

        current_week = self.current_date.isocalendar()[1]
        current_month = self.current_date.month

        unfinished = deepcopy(self.unfinished)
        for task in unfinished:
            if task[1].date() == self.current_date:
                task_today = deepcopy(task)
                del task_today[1]
                todayTasks.append(task)
            else:
                otherData.append(task)

            if task[1].isocalendar()[1] == current_week:
                weekTasks.append(task)

            if task[1].month == current_month:
                monthTasks.append(task)

            tasksDeadlines.append([task[0]] + task[2:])
            planTasks.append([task[0]] + task[2:] + [task[1]])

        habits = list()
        for habit in self.habits:
            status = False  # Попадает ли привычка на сегодня
            habit = deepcopy(habit[:-1])
            if habit[1][0] == 0:  # Дни недели
                if self.current_date.weekday() + 1 in habit[1][1]:
                    status = True
            elif int((self.current_date - habit[1][1][0].date()).days) % (habit[1][1][1] + 1) == 0:  # Через x дней
                status = True

            if status:
                habits.append([habit[0], datetime.datetime(
                    self.current_date.year, self.current_date.month, self.current_date.day
                ), habit[2], habit[3]])

        # Установка данных в таблицы
        tasksRowLabels = ['', 'Сделать', 'Дедлайн', 'Задача', 'Заметка']
        taskTemplate = [[[-1, 0], '', '', '', 'Здесь могла быть ваша задача']]

        # HOME PAGE
        tasksDoneLabel = tasksRowLabels_Today = ['', 'Дедлайн', 'Задача', 'Заметка']
        if todayTasks:
            for i, task in enumerate(todayTasks):
                todayTasks[i] = task[:2] + task[3:]
        if habits:
            todayTasks += habits
        if not todayTasks:
            todayTasks = [[[-1, 0], '', '', 'Здесь могла быть ваша задача']]
        self.ph_todayModel = MainTableModel(todayTasks, tasksRowLabels_Today, self)
        self.ui.ph_mainTableToday.setModel(self.ph_todayModel)

        if not otherData:
            otherData = taskTemplate
        self.ph_addModel = MainTableModel(otherData, tasksRowLabels, self)
        self.ui.ph_addTable.setModel(self.ph_addModel)

        if not weekTasks:
            weekTasks = taskTemplate
        self.ph_weekModel = MainTableModel(weekTasks, tasksRowLabels, self)
        self.ui.ph_mainTableWeek.setModel(self.ph_weekModel)

        if not monthTasks:
            monthTasks = taskTemplate
        self.ph_monthModel = MainTableModel(monthTasks, tasksRowLabels, self)
        self.ui.ph_mainTableMonth.setModel(self.ph_monthModel)

        # DEADLINES PAGE
        if not tasksDeadlines:
            tasksDeadlines = taskTemplate
        self.pd_tasksModel = DeadlinesTableModel(deepcopy(tasksDeadlines), tasksRowLabels, self)
        self.ui.deadlines_tasks.setModel(self.pd_tasksModel)

        # PLAN PAGE
        self.pp_tasksModel = PlanTableModel(planTasks, self)
        self.ui.pp_tableView.setModel(self.pp_tasksModel)

        # STATISTICS PAGE
        self.habitsModel = HabitsTableModel(deepcopy(self.habits))
        self.ui.ps_habitsTable.setModel(self.habitsModel)

        self.archiveModel = MainTableModel(deepcopy(self.dones), tasksDoneLabel, self)
        self.ui.ps_archiveTable.setModel(self.archiveModel)

        splashScreen.clock(self, 45, 2)

        # TABLE CONFIGURATING
        # /////////////////////////////////////////////////////////////////////////////////

        for table in (self.ui.ph_mainTableToday, self.ui.ps_archiveTable):
            tableSize = 822 - 120
            delegate = CheckBoxDelegate()
            self.ui.ph_mainTableToday.setItemDelegateForColumn(0, delegate)
            self.ui.ph_mainTableToday.setColumnWidth(0, 35)
            self.ui.ph_mainTableToday.setColumnWidth(1, 75)
            self.ui.ph_mainTableToday.setColumnWidth(2, tableSize - tableSize // 2)
            self.ui.ph_mainTableToday.setColumnWidth(3, tableSize // 2)

        for table in (
                self.ui.ph_mainTableWeek, self.ui.ph_mainTableMonth,
                self.ui.ph_addTable, self.ui.deadlines_tasks,
                self.ui.ps_archiveTable
        ):
            delegate = CheckBoxDelegate()
            table.setItemDelegateForColumn(0, delegate)
            table.setColumnWidth(0, 35)
            table.setColumnWidth(1, 75)
            table.setColumnWidth(2, 75)

        table = self.ui.pp_tableView
        delegate = PlanCheckBoxDelegate(self)
        table.setItemDelegateForColumn(0, delegate)
        table.setColumnWidth(0, 35)
        table.setColumnWidth(1, 75)
        table.setColumnWidth(2, 75)

    # TASK MANIPULATING FUNCTIONS
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def defineTask(self):
        task = [[0, 0], 0, 0, 0]
        task[2] = self.ui.pp_te_taskEdit.text()

        if not task[2]:
            self.creatingError('Вы не указали саму задачу')
            return

        task[3] = self.ui.pp_te_noteEdit.toPlainText()
        isHabit = self.ui.pp_te_isHabit_cBox.isChecked()

        # Привычка
        if isHabit:
            task[0][0] = 3

            # По дням недели
            if self.ui.DoW_rBtn.isChecked():
                if not (self.ui.ppte_mon.isChecked() or self.ui.ppte_tue.isChecked() or
                        self.ui.ppte_wen.isChecked() or self.ui.ppte_thu.isChecked() or
                        self.ui.ppte_fri.isChecked() or self.ui.ppte_sat.isChecked() or self.ui.ppte_sun.isChecked()):
                    self.creatingError('Вы не указали частоту привычки')
                    return

                days = list()
                for day, state in enumerate((self.ui.ppte_mon.isChecked(), self.ui.ppte_tue.isChecked(),
                        self.ui.ppte_wen.isChecked(), self.ui.ppte_thu.isChecked(),
                        self.ui.ppte_fri.isChecked(), self.ui.ppte_sat.isChecked(), self.ui.ppte_sun.isChecked())):
                    if state: days.append(day + 1)
                task[1] = (0, tuple(days))

            # Через x дней
            elif self.ui.daysInRow_rBtn.isChecked():
                task[1] = (1, self.ui.pp_te_spinBox.value())
            else:
                self.creatingError('Вы не указали частоту привычки')
                return

        # Задача
        else:
            # Приоритет
            if not (self.ui.pp_te_rBtn_1.isChecked() or self.ui.pp_te_rBtn_2.isChecked()
                    or self.ui.pp_te_rBtn_3.isChecked()):
                self.creatingError('Вы не указали приоритет задачи')
                return
            if self.ui.pp_te_rBtn_1.isChecked():
                task[0][0] = 0
            elif self.ui.pp_te_rBtn_2.isChecked():
                task[0][0] = 1
            else:
                task[0][0] = 2

            # Дедлайн
            date = self.ui.pp_te_dateEdit.date()
            if self.ui.pp_te_isDLless.isChecked():
                task[1] = 'Бессрочно'
            else:
                task[1] = todatetime(date)

        # Создание задачи
        self.createDialog('Создание задачи', 'Создать задачу?', lambda: self.createTask(task))

    def createTask(self, task):
        # Привычка
        if task[0][0] == 3:
            todayDate = datetime.datetime(
                self.current_date.year, self.current_date.month, self.current_date.day
            )
            habit = [[3, 1], task[-3], task[-2], task[-1], 0, 0, [todayDate, todayDate]]
            self.habits.append(habit)

        # Задача
        else:
            self.undefined.append(task)
            self.pd_tasksModel._data.append(task[:2] + [''] + task[2:])

        self.cancelTask()

    def cancelTask(self):
        # Сброс кнопок
        for button in (
            self.ui.pp_te_isHabit_cBox,
            self.ui.ppte_mon, self.ui.ppte_tue, self.ui.ppte_wen,
            self.ui.ppte_thu, self.ui.ppte_fri, self.ui.ppte_sat,
            self.ui.ppte_sun, self.ui.pp_te_isDLless
        ):
            button.setChecked(False)

        for button in (
             self.ui.pp_te_rBtn_1, self.ui.pp_te_rBtn_2, self.ui.pp_te_rBtn_3,
             self.ui.DoW_rBtn, self.ui.daysInRow_rBtn
        ):
            if button.isChecked():
                button.setAutoExclusive(False)
                button.setChecked(False)
                button.setAutoExclusive(True)
                break

        for button in (
             self.ui.DoW_rBtn, self.ui.daysInRow_rBtn
        ):
            if button.isChecked():
                button.setAutoExclusive(False)
                button.setChecked(False)
                button.setAutoExclusive(True)
                break

        # Сброс Линий ввода
        self.ui.pp_te_taskEdit.setText('')
        self.ui.pp_te_noteEdit.setText('')
        self.ui.pp_te_dateEdit.setDate(self.current_date)
        self.ui.pp_te_spinBox.setValue(1)

        self.reHide_Frame()
        self.ui.pp_taskEditFrame.hide()

    def redefineTasks(self, model, task):
        if task[0][0] == 3:
            for habit in self.habits:
                if habit[2] == task[2]:
                    # Выполнена
                    if task[0][1] == 1:
                        # Привычка в self.habits
                        if habit[-3] == habit[-2]:
                            habit[-2] += 1
                        habit[-3] += 1
                        habit[-1][0] = datetime.datetime(
                            self.current_date.year, self.current_date.month, self.current_date.day)

                    # Отмена
                    else:
                        if habit[-1][1].date() == self.current_date and habit[-3] == task[-2]:
                            habit[-2] -= 1
                        habit[-3] -= 1

                    break

            # Установка изменений в self.habitsModel
            for habit_ in self.habitsModel._data:
                if habit_[-1] == task[2]:
                    habit_[0] = habit[-3]
                    habit_[1] = habit[-2]
                    self.habitsModel.layoutChanged.emit()
                    break

        # Задача
        else:
            if task[0][0] == -1: return
            if task[0][1] == 1:
                # Удаление из всех таблиц
                taskModels = [
                    self.ph_todayModel, self.ph_addModel, self.ph_weekModel,
                    self.ph_monthModel, self.pd_tasksModel, self.pp_tasksModel
                ]
                for element in task:
                    if isinstance(element, str):
                        taskItself = element
                        break
                for curModel in taskModels:
                    for i, curTask in enumerate(curModel._data):
                        if taskItself in curTask:
                            del curModel._data[i]
                            if not curModel._data:
                                if curModel is self.ph_todayModel:
                                    curModel._data = [[[-1, 0], '', '', 'Здесь могла быть ваша задача']]
                                elif curModel in (self.ph_addModel, self.ph_weekModel,
                                                  self.ph_monthModel, self.pd_tasksModel):
                                    curModel._data = [[[-1, 0], '', '', '', 'Здесь могла быть ваша задача']]
                            curModel.layoutChanged.emit()

                    # Добавление в архив
                if len(task) == 4:
                    taskItself = task[2]
                    for curTask in self.unfinished:
                        if taskItself in curTask:
                            task = [[curTask[0][0], 1]] + curTask[1:]
                self.dones.append(task)
                del self.unfinished[self.unfinished.index([[task[0][0], 0]] + task[1:])]
                task = task[0:2] + task[3:]
                self.archiveModel._data.append(task)
                self.archiveModel.layoutChanged.emit()

            # Из архива в таблицы
            else:
                # Удаление из архива и сделанных, добавление в несделанные
                curIndex = self.archiveModel._data.index(task)
                taskItself = self.archiveModel._data[curIndex][2]
                del self.archiveModel._data[curIndex]

                for i, curTask in enumerate(self.dones):
                    if taskItself in curTask:
                        task = deepcopy(self.dones[i])
                        del self.dones[i]
                        break
                task = [[task[0][0], 0]] + task[1:]
                self.unfinished.append(task)

                # Добавление в таблицы
                if task[1].date() == self.current_date:
                    self.ph_todayModel._data.append(deepcopy(task))
                    tableSort(self.ph_todayModel._data)
                    self.ph_todayModel.layoutChanged.emit()
                else:
                    self.ph_addModel._data.append(deepcopy(task))
                    tableSort(self.ph_addModel._data)
                    self.ph_addModel.layoutChanged.emit()

                if task[1].isocalendar()[1] == self.current_date.isocalendar()[1]:
                    self.ph_weekModel._data.append(deepcopy(task))
                    tableSort(self.ph_weekModel._data)
                    self.ph_weekModel.layoutChanged.emit()
                if task[1].month == self.current_date.month:
                    self.ph_monthModel._data.append(deepcopy(task))
                    tableSort(self.ph_monthModel._data)
                    self.ph_monthModel.layoutChanged.emit()

                self.pd_tasksModel._data.append(deepcopy([task[0]]) + deepcopy(task[2:]))
                tableSort(self.pd_tasksModel._data)
                self.pd_tasksModel.layoutChanged.emit()

                task = deepcopy([task[0]]) + deepcopy(task[2:]) + deepcopy([task[1]])
                task[0] = [task[0][0], [task[-1], task[-1]]]
                self.pp_tasksModel._data.append(task)
                self.pp_tasksModel.layoutChanged.emit()

        self.dataReceiver.run()
        if model in (self.ph_todayModel, self.ph_addModel, self.ph_weekModel, self.ph_monthModel):
            index = 0
        elif model is self.pd_tasksModel:
            index = 1
        elif model is self.archiveModel:
            index = 3
        else: return
        self.resizeTables(index)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    splashScreen = Bar()
    window = MainWindow()
    splashScreen.clock(window, 20, 0)
    sys.exit(app.exec())
