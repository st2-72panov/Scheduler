import datetime
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QTimer
from copy import deepcopy


todatetime = lambda _qdate: datetime.datetime(_qdate.year(), _qdate.month(), _qdate.day())

def tableSort(data):
    data.sort(key=lambda task: (task[0][1], task[1], task[0][0]))


class CheckBoxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def paint(self, painter, option, index):
        if index.data()[0] != 3:
            priority = '_pr' + str(index.data()[0] + 1)
        else:
            priority = ''

        if int(index.data()[1]) == 0:
            pixmap_ = QtGui.QPixmap(u":/icons/images/icons/icon_unchecked%s.png" % priority)
        else:
            pixmap_ = QtGui.QPixmap(u":/icons/images/icons/icon_checked%s.png" % priority)
        self.drawDecoration(painter, option, option.rect, pixmap_)

    def editorEvent(self, event, model, option, index):
        if event.type() == QtCore.QEvent.Type.MouseButtonRelease:
            model.setData(index, 1 if int(index.data()[1]) == 0 else 0, QtCore.Qt.ItemDataRole.EditRole)
            return True
        return False


class MainTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, rowHeaders, window):
        super(MainTableModel, self).__init__()
        tableSort(data)
        if data[0][0][1] == 1:
            for i, task in enumerate(data):
                data[i] = [deepcopy(task[0])] + deepcopy(task[2:5])
        self._data = data
        self.rowHeaders = rowHeaders
        self.window = window

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime.datetime):
                return value.strftime("%d.%m.%Y")

            return value

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            task = self._data[index.row()]
            task[0][1] = value
            tableSort(self._data)
            self.window.redefineTasks(self, task)
            self.layoutChanged.emit()
        return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0]) if self._data[0][0][1] == 0 else 4

    def headerData(self, section, orientation, role):
        # section - это номер column/row (в зависимости от orientation).
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return str(self.rowHeaders[section])


class DeadlinesTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, rowHeaders, window):
        super().__init__()
        tableSort(data)
        self._data = data
        self.rowHeaders = rowHeaders
        self.window = window

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime.datetime):
                return value.strftime("%d.%m.%Y")
            return value

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            task = self._data[index.row()]
            task[0][1] = value
            tableSort(self._data)
            for curTask in self.window.unfinished:
                if curTask[-2] == task[-2]:
                    curDate = self.window.current_date
                    curTask[1] = datetime.datetime(curDate.year, curDate.month, curDate.day)
            self.layoutChanged.emit()
        return task[0][1]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return str(self.rowHeaders[section])


class HabitsTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(HabitsTableModel, self).__init__()
        if data:
            for i, habit in enumerate(data):
                data[i] = [deepcopy(habit[4]), deepcopy(habit[5]), deepcopy(habit[2])]
        else:
            data = [['', '', 'Здесь могла быть ваша привычка'], ['', '', 'Здесь могла быть ваша привычка']]
        self._data = sorted(data, key=lambda habit: habit[-1])
        self.rowHeaders = ['Выполняется дней подряд', 'Лучший счёт']

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 2

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.rowHeaders[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self._data[section][-1])


class PlanTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, window):
        super().__init__()
        if not data:
            data = [['', '', '', 'Здесь могла быть ваша задача'], ['', '', '', 'Здесь могла быть ваша задача']]
        else:
            for task in data:
                if len(task) == 4:
                    task.append('')
                task[0] = [task[0][0], [task[-1], task[-1]]]
        self.rowHeaders = ['', 'Дедлайн', 'Задача', 'Заметка']
        self.window = window
        self._data = data
        self.sort_ = lambda data: data.sort(key=lambda task: task[1])
        self.sort_(self._data)
        self.curDate = todatetime(self.window.ui.pp_dateEdit.date())

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime.datetime):
                return value.strftime("%d.%m.%Y")
            return value

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            task = self._data[index.row()]
            task[0][1][0] = self.curDate if value else task[0][1][1]
            self.layoutChanged.emit()
        return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 4

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return str(self.rowHeaders[section])


class PlanCheckBoxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, window):
        QtWidgets.QItemDelegate.__init__(self)
        self.window = window

    def paint(self, painter, option, index):
        priority = '_pr' + str(index.data()[0] + 1)
        if self.window.pp_tasksModel._data[index.row()][0][1][0] == todatetime(self.window.ui.pp_dateEdit.date()):
            pixmap_ = QtGui.QPixmap(u":/icons/images/icons/icon_checked%s.png" % priority)
        else:
            pixmap_ = QtGui.QPixmap(u":/icons/images/icons/icon_unchecked%s.png" % priority)
        self.drawDecoration(painter, option, option.rect, pixmap_)

    def editorEvent(self, event, model, option, index):
        if event.type() == QtCore.QEvent.Type.MouseButtonRelease:
            model.setData(index, 1 if self.window.pp_tasksModel.curDate == index.data()[1][0] else 0,
                          QtCore.Qt.ItemDataRole.EditRole)
            return True
        return False
