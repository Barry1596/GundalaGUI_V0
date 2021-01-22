
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Accesing_Data_Sensor_API import AccesLiveData, AccesHistoryData



class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)
    def compute_initial_figure(self):
        pass

class Update_Plot(Canvas):
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData(ID,N_data,step).AccesLive()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.draw()

class Update_Battery_Plot(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter(self, ID, N_data, step, title):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure(self.ID, self.N_data, self.step, self.title))
        timer.start(12000)

    def update_figure(self, ID, N_data, step, title):
        data = AccesLiveData(ID,N_data,step).AccesLive()
        l = data[2]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Voltage [V]')
        self.axes.set_title(title)
        self.axes.plot(a,l,'r')
        self.draw()

class Static_Plot(Canvas):
    
    def __init__(self, ID):
        Canvas.__init__(self, ID)
        self.ID = ID 

    def ubah_Parameter_Static(self, ID, date_begin, date_end, step, title):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.title = title

        timer = QtCore.QTimer(self)
        timer.timeout.connect(lambda:self.update_figure_static(self.ID, self.date_begin, self.date_end,self.step, self.title))
        timer.start(12000000)
        
    def update_figure_static(self, ID, date_begin, date_end, step, title):
        data = AccesHistoryData(ID, date_begin, date_end, step).AccesHistory()
        l = data[1]
        a = data[0]
        self.axes.cla()
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Temperatur [°C]')
        self.axes.set_title(title)
        self.axes.plot(a,l)
        self.draw()
       
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #==========================================================Setup Configuration Main Window=====================================================================
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1578, 935)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Stgobain_GUI = QtWidgets.QTabWidget(self.centralwidget)
        self.Stgobain_GUI.setGeometry(QtCore.QRect(0, 0, 1847, 1100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Stgobain_GUI.setFont(font)
        self.Stgobain_GUI.setElideMode(QtCore.Qt.ElideNone)
        self.Stgobain_GUI.setDocumentMode(False)
        self.Stgobain_GUI.setMovable(False)
        self.Stgobain_GUI.setObjectName("Stgobain_GUI")
         #==================================================================Live Tab====================================================================================
        self.Live = QtWidgets.QWidget()
        self.Live.setObjectName("Live")
        self.V_line = QtWidgets.QFrame(self.Live)
        self.V_line.setGeometry(QtCore.QRect(160, 10, 16, 760))
        self.V_line.setAutoFillBackground(False)
        self.V_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_line.setObjectName("V_line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Live)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 141, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Thermistor_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Thermistor_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.Thermistor_Label.setObjectName("Thermistor_Label")
        self.verticalLayout_2.addWidget(self.Thermistor_Label)
        #============= Push Button Control ==================
        self.Thermistor_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Thermistor_1.setObjectName("Thermistor 1")
        self.verticalLayout_2.addWidget(self.Thermistor_1)
        self.Thermistor_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Thermistor_2.setObjectName("Thermistor 2")
        self.verticalLayout_2.addWidget(self.Thermistor_2)
        self.Thermistor_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Thermistor_3.setObjectName("Thermistor 3")
        self.verticalLayout_2.addWidget(self.Thermistor_3)
        self.Thermistor_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Thermistor_4.setObjectName("Thermistor 4")
        self.verticalLayout_2.addWidget(self.Thermistor_4)
        self.Display_All = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Display_All.setObjectName("Display All")
        self.verticalLayout_2.addWidget(self.Display_All)
        
        self.Setting = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Setting.setObjectName("Setting")
        self.verticalLayout_2.addWidget(self.Setting)
        #=========List Time Range============================
        self.ListTimeRange = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.ListTimeRange.setEditable(False)
        self.ListTimeRange.setCurrentText("")
        self.ListTimeRange.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.ListTimeRange.setMinimumContentsLength(0)
        self.ListTimeRange.setModelColumn(0)
        self.ListTimeRange.setObjectName("ListTimeRange")
        self.ListTimeRange.setObjectName("ListTimeRange")
        self.ListTimeRange.addItem("Time Range")
        self.ListTimeRange.addItem("1 minute")
        self.ListTimeRange.addItem("5 minute")
        self.ListTimeRange.addItem("15 minute")
        self.ListTimeRange.addItem("30 minute")
        self.ListTimeRange.addItem("1 hour")
        self.ListTimeRange.addItem("4 hours")
        self.ListTimeRange.addItem("12 hours")
        self.ListTimeRange.addItem("1 day")
        self.verticalLayout_2.addWidget(self.ListTimeRange)
        #====================================
        self.SetTimeRange = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SetTimeRange.setObjectName("SetTimeRange")
        self.verticalLayout_2.addWidget(self.SetTimeRange)
        self.H_line = QtWidgets.QFrame(self.Live)
        self.H_line.setGeometry(QtCore.QRect(5, 765, 1850, 16))
        self.H_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_line.setObjectName("H_line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Live)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1000, 780, 811, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MONITORINGIO = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.MONITORINGIO.setObjectName("MONITORINGIO")
        self.horizontalLayout.addWidget(self.MONITORINGIO)
        self.KONTAK = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.KONTAK.setObjectName("KONTAK")
        self.horizontalLayout.addWidget(self.KONTAK)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Live)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(1000, 810, 811, 131))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DESK_MONITORINGIO = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.DESK_MONITORINGIO.setWordWrap(True)
        self.DESK_MONITORINGIO.setObjectName("DESK_MONITORINGIO")
        self.horizontalLayout_4.addWidget(self.DESK_MONITORINGIO)
        self.DES_KONTAK = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_4)
        self.DES_KONTAK.setObjectName("DES_KONTAK")
        self.horizontalLayout_4.addWidget(self.DES_KONTAK)
        self.Logo = QtWidgets.QLabel(self.Live)
        self.Logo.setGeometry(QtCore.QRect(140, 790, 571, 131))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("Logo Gundala1.png"))
        self.Logo.setWordWrap(False)
        self.Logo.setObjectName("Logo")
        #====== Live Plot =============
        self.Live_Plot_Widget = QtWidgets.QWidget(self.Live)
        self.Live_Plot_Widget.setGeometry(QtCore.QRect(170, 10, 1725, 760))
        self.Live_Plot_Widget.setObjectName("Live_Plot_Widget")
        self.Live_Plot_Layout = QtWidgets.QGridLayout(self.Live_Plot_Widget)
        self.Live_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.Live_Plot_Layout.setObjectName("Live_Plot_Layout")
        self.Live_Plot_Layout.addWidget(self.Live_Plot_Widget, 1, 1, 1, 1)
        #=========================================================
        self.MU_Icon = QtWidgets.QLabel(self.Live)
        self.MU_Icon.setGeometry(QtCore.QRect(10, 500, 141, 131))
        self.MU_Icon.setText("")
        self.MU_Icon.setPixmap(QtGui.QPixmap("Mortar Utama.png"))
        self.MU_Icon.setScaledContents(True)
        self.MU_Icon.setWordWrap(False)
        self.MU_Icon.setObjectName("MU_Icon")
        self.Stgobain_GUI.addTab(self.Live, "")
        #=======================================================================Historical Tab==========================================================================
        self.Historical = QtWidgets.QWidget()
        self.Historical.setObjectName("Historical")
        self.V_Line_2 = QtWidgets.QFrame(self.Historical)
        self.V_Line_2.setGeometry(QtCore.QRect(160, 10, 16, 760))
        self.V_Line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_Line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_Line_2.setObjectName("V_Line_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Historical)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Thermistor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Thermistor.setObjectName("Thermistor")
        self.verticalLayout.addWidget(self.Thermistor)
        self.Thermistor1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Thermistor1.setObjectName("Thermistor1")
        self.verticalLayout.addWidget(self.Thermistor1)
        self.Thermistor2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Thermistor2.setObjectName("Thermistor2")
        self.verticalLayout.addWidget(self.Thermistor2)
        self.Thermistor3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Thermistor3.setObjectName("Thermistor3")
        self.verticalLayout.addWidget(self.Thermistor3)
        self.Thermistor4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Thermistor4.setObjectName("Thermistor4")
        self.verticalLayout.addWidget(self.Thermistor4)
        self.Setting_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Setting_2.setObjectName("Setting_2")
        
        self.verticalLayout.addWidget(self.Setting_2)
        self.BeginTime_String = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.BeginTime_String.setObjectName("BeginTime_String")
        self.verticalLayout.addWidget(self.BeginTime_String)

        self.Begin_Date = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.Begin_Date.setObjectName("Begin_Date")
        self.Begin_Date.setDisplayFormat('dd-MM-yyyy')
        self.verticalLayout.addWidget(self.Begin_Date)
        
        self.Begin_Time = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.Begin_Time.setObjectName("BeginTime")
        self.verticalLayout.addWidget(self.Begin_Time)

        self.EndTime_String = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.EndTime_String.setObjectName("EndTime_String")
        self.verticalLayout.addWidget(self.EndTime_String)

        self.End_Date = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.End_Date.setObjectName("End_Date")
        self.End_Date.setDisplayFormat('dd-MM-yyyy')
        self.verticalLayout.addWidget(self.End_Date)

        self.End_Time = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.End_Time.setObjectName("EndTime")
        self.verticalLayout.addWidget(self.End_Time)

        self.SetTimeRange_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SetTimeRange_2.setObjectName("SetTimeRange_2")
        self.verticalLayout.addWidget(self.SetTimeRange_2)
        self.line_4 = QtWidgets.QFrame(self.Historical)
        self.line_4.setGeometry(QtCore.QRect(5, 765, 1850, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.Logo_2 = QtWidgets.QLabel(self.Historical)
        self.Logo_2.setGeometry(QtCore.QRect(140, 790, 571, 131))
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap("Logo Gundala1.png"))
        self.Logo_2.setWordWrap(False)
        self.Logo_2.setObjectName("Logo_2")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.Historical)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(1000, 810, 811, 131))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DESK_MONITORINGIO_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.DESK_MONITORINGIO_2.setWordWrap(True)
        self.DESK_MONITORINGIO_2.setObjectName("DESK_MONITORINGIO_2")
        self.horizontalLayout_5.addWidget(self.DESK_MONITORINGIO_2)
        self.DES_KONTAK_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.DES_KONTAK_2.setObjectName("DES_KONTAK_2")
        self.horizontalLayout_5.addWidget(self.DES_KONTAK_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Historical)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1000, 780, 811, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MONITORINGIO_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.MONITORINGIO_2.setObjectName("MONITORINGIO_2")
        self.horizontalLayout_2.addWidget(self.MONITORINGIO_2)
        self.KONTAK_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.KONTAK_2.setObjectName("KONTAK_2")
        self.horizontalLayout_2.addWidget(self.KONTAK_2)

        #======== Historical Plot =======================
       
        self.History_Plot_Widget = QtWidgets.QWidget(self.Historical)
        self.History_Plot_Widget.setGeometry(QtCore.QRect(170, 10, 1725, 760))
        self.History_Plot_Widget.setObjectName("History1_Widget")
        self.History_Plot_Layout = QtWidgets.QGridLayout(self.History_Plot_Widget)
        self.History_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.History_Plot_Layout.addWidget(self.History_Plot_Widget, 1, 1, 1, 1)
        
        #================================================
        self.MU_ICON_2 = QtWidgets.QLabel(self.Historical)
        self.MU_ICON_2.setGeometry(QtCore.QRect(10, 600, 141, 131))
        self.MU_ICON_2.setText("")
        self.MU_ICON_2.setPixmap(QtGui.QPixmap("Mortar Utama.png"))
        self.MU_ICON_2.setScaledContents(True)
        self.MU_ICON_2.setWordWrap(False)
        self.MU_ICON_2.setObjectName("MU_ICON_2")
        self.Stgobain_GUI.addTab(self.Historical, "")
         #========================================================================Battery Tab==============================================================================

        self.Battery = QtWidgets.QWidget()
        self.Battery.setObjectName("Battery")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Battery)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 141, 400))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BV_Label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.BV_Label.setObjectName("BV_Label")
        self.verticalLayout_3.addWidget(self.BV_Label)
        self.BV_Thermistor1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BV_Thermistor1.setObjectName("BV_Thermistor1")
        self.verticalLayout_3.addWidget(self.BV_Thermistor1)
        self.BV_Thermistor2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BV_Thermistor2.setObjectName("BV_Thermistor2")
        self.verticalLayout_3.addWidget(self.BV_Thermistor2)
        self.BV_Thermistor3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BV_Thermistor3.setObjectName("BV_Thermistor3")
        self.verticalLayout_3.addWidget(self.BV_Thermistor3)
        self.BV_THermistor4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.BV_THermistor4.setObjectName("BV_THermistor4")
        self.verticalLayout_3.addWidget(self.BV_THermistor4)
        self.Display_All_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Display_All_2.setObjectName("Display All_2")
        self.verticalLayout_3.addWidget(self.Display_All_2)

        self.Setting_Label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Setting_Label.setObjectName("Setting_Label")
        self.verticalLayout_3.addWidget(self.Setting_Label)
        # ==== List Time Range ======================
        self.ListTimeRange_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.ListTimeRange_2.setObjectName("ListTimeRange_2")
        self.ListTimeRange_2.addItem("Time Range")
        self.ListTimeRange_2.addItem("1 minute")
        self.ListTimeRange_2.addItem("5 minute")
        self.ListTimeRange_2.addItem("15 minute")
        self.ListTimeRange_2.addItem("30 minute")
        self.ListTimeRange_2.addItem("1 hour")
        self.ListTimeRange_2.addItem("4 hours")
        self.ListTimeRange_2.addItem("12 hours")
        self.ListTimeRange_2.addItem("1 day")
        self.verticalLayout_3.addWidget(self.ListTimeRange_2)
        #============================================
        self.SetTimeRange_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.SetTimeRange_3.setObjectName("SetTimeRange_3")
        self.verticalLayout_3.addWidget(self.SetTimeRange_3)
        self.V_Line = QtWidgets.QFrame(self.Battery)
        self.V_Line.setGeometry(QtCore.QRect(160, 10, 16, 775))
        self.V_Line.setAutoFillBackground(False)
        self.V_Line.setFrameShape(QtWidgets.QFrame.VLine)
        self.V_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.V_Line.setObjectName("V_Line")
        self.H_Line = QtWidgets.QFrame(self.Battery)
        self.H_Line.setGeometry(QtCore.QRect(5, 775, 1840, 16))
        self.H_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.H_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.H_Line.setObjectName("H_Line")
        self.Logo_3 = QtWidgets.QLabel(self.Battery)
        self.Logo_3.setGeometry(QtCore.QRect(140, 790, 571, 131))
        self.Logo_3.setText("")
        self.Logo_3.setPixmap(QtGui.QPixmap("Logo Gundala1.png"))
        self.Logo_3.setWordWrap(False)
        self.Logo_3.setObjectName("Logo_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Battery)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1000, 780, 811, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MONITORINGIO_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.MONITORINGIO_3.setObjectName("MONITORINGIO_3")
        self.horizontalLayout_3.addWidget(self.MONITORINGIO_3)
        self.KONTAK_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.KONTAK_3.setObjectName("KONTAK_3")
        self.horizontalLayout_3.addWidget(self.KONTAK_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.Battery)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(1000, 810, 811, 131))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.DESK_MONITORINGIO_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.DESK_MONITORINGIO_3.setWordWrap(True)
        self.DESK_MONITORINGIO_3.setObjectName("DESK_MONITORINGIO_3")
        self.horizontalLayout_6.addWidget(self.DESK_MONITORINGIO_3)
        self.DES_KONTAK_3 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_6)
        self.DES_KONTAK_3.setObjectName("DES_KONTAK_3")
        self.horizontalLayout_6.addWidget(self.DES_KONTAK_3)


        # ===== Battery Plot ===========================
        self.Battery_Plot_Widget = QtWidgets.QWidget(self.Battery)
        self.Battery_Plot_Widget.setGeometry(QtCore.QRect(170, 10, 1725, 760))
        self.Battery_Plot_Widget.setObjectName("Battery_Widget")
        self.Battery_Plot_Layout = QtWidgets.QGridLayout(self.Battery_Plot_Widget)
        self.Battery_Plot_Layout.setContentsMargins(0, 0, 0, 0)
        self.Battery_Plot_Layout.addWidget(self.Battery_Plot_Widget, 1, 1, 1, 1)
        
       
        # ===============================================
        self.MU_ICON = QtWidgets.QLabel(self.Battery)
        self.MU_ICON.setGeometry(QtCore.QRect(10, 500, 141, 131))
        self.MU_ICON.setText("")
        self.MU_ICON.setPixmap(QtGui.QPixmap("Mortar Utama.png"))
        self.MU_ICON.setScaledContents(True)
        self.MU_ICON.setWordWrap(False)
        self.MU_ICON.setObjectName("MU_ICON")
        self.Stgobain_GUI.addTab(self.Battery, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1578, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Stgobain_GUI.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        #======== Retranslate Live Tab ======================================
        self.Thermistor_Label.setText(_translate("MainWindow", "Sensor"))
        self.Thermistor_1.setText(_translate("MainWindow", "Thermistor 1"))
        self.Thermistor_1.clicked.connect(self.Live_Thermistor_1)
        self.Thermistor_2.setText(_translate("MainWindow", "Thermistor 2"))
        self.Thermistor_2.clicked.connect(self.Live_Thermistor_2)
        self.Thermistor_3.setText(_translate("MainWindow", "Thermistor 3"))
        self.Thermistor_3.clicked.connect(self.Live_Thermistor_3)
        self.Thermistor_4.setText(_translate("MainWindow", "Thermistor 4"))
        self.Thermistor_4.clicked.connect(self.Live_Thermistor_4)
        self.Display_All.setText(_translate("MainWindow", "Display All"))
        self.Display_All.clicked.connect(self.Live_Display_All)
        self.ListTimeRange.activated[str].connect(self.TimeRange_Live_Plot)
        self.ListTimeRange_2.activated[str].connect(self.TimeRange_Live_Battery_Plot)
        self.Setting.setText(_translate("MainWindow", "Setting"))
        self.SetTimeRange.setText(_translate("MainWindow", "Set"))
        self.MONITORINGIO.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK.setText(_translate("MainWindow", "KONTAK"))
        self.DESK_MONITORINGIO.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Telemetri Nusantara. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.Stgobain_GUI.setTabText(self.Stgobain_GUI.indexOf(self.Live), _translate("MainWindow", "Live"))

        #======== Retranslate Historical Tab =================================
        self.Thermistor.setText(_translate("MainWindow", "Thermistor"))
        self.Thermistor1.setText(_translate("MainWindow", "Thermistor 1"))
        self.Thermistor1.clicked.connect(self.Historical_Thermistor_1)
        self.Thermistor2.setText(_translate("MainWindow", "Thermistor 2"))
        self.Thermistor2.clicked.connect(self.Historical_Thermistor_2)
        self.Thermistor3.setText(_translate("MainWindow", "Thermistor 3"))
        self.Thermistor3.clicked.connect(self.Historical_Thermistor_3)
        self.Thermistor4.setText(_translate("MainWindow", "Thermistor 4"))
        self.Thermistor4.clicked.connect(self.Historical_Thermistor_4)
        self.Display_All_2.setText(_translate("MainWindow", "Display All"))
        self.Display_All_2.clicked.connect(self.Live_Display_All_Battery)
        self.Setting_2.setText(_translate("MainWindow", "Setting"))
        self.BeginTime_String.setText(_translate("MainWindow", "Begin Time"))
        self.EndTime_String.setText(_translate("MainWindow", "End Time"))
        self.SetTimeRange_2.setText(_translate("MainWindow", "Set"))
        self.SetTimeRange_2.clicked.connect(self.SetHistory)
        self.DESK_MONITORINGIO_2.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Widya Karya. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.MONITORINGIO_2.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK_2.setText(_translate("MainWindow", "KONTAK"))
        self.Stgobain_GUI.setTabText(self.Stgobain_GUI.indexOf(self.Historical), _translate("MainWindow", "Historical"))

        #========= Retranslate Battery Tab ==================================
        self.BV_Label.setText(_translate("MainWindow", "Battery Voltage"))
        self.BV_Thermistor1.setText(_translate("MainWindow", "Thermistor 1"))
        self.BV_Thermistor1.clicked.connect(self.BV_Thermistor_1)
        self.BV_Thermistor2.setText(_translate("MainWindow", "Thermistor 2"))
        self.BV_Thermistor2.clicked.connect(self.BV_Thermistor_2)
        self.BV_Thermistor3.setText(_translate("MainWindow", "Thermistor 3"))
        self.BV_Thermistor3.clicked.connect(self.BV_Thermistor_3)
        self.BV_THermistor4.setText(_translate("MainWindow", "Thermistor 4"))
        self.BV_THermistor4.clicked.connect(self.BV_Thermistor_4)
        self.Setting_Label.setText(_translate("MainWindow", "Setting"))
        self.SetTimeRange_3.setText(_translate("MainWindow", "Set"))
        self.MONITORINGIO_3.setText(_translate("MainWindow", "MONITORING.IO"))
        self.KONTAK_3.setText(_translate("MainWindow", "KONTAK"))
        self.DESK_MONITORINGIO_3.setText(_translate("MainWindow", "Aplikasi Monitoring.io adalah aplikasi untuk pemantauan kondisi struktur oleh PT. Gundala Widya Karya. Untuk informasi lebih lanjut klik www.gundala.co.id"))
        self.DES_KONTAK_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Jl.Tebet Timur dalam III-D no.11, Jakarta Selatan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">support@gundala.co.id</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 853 2125 1627</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">+ 62 21 21282553</p></body></html>"))
        self.Stgobain_GUI.setTabText(self.Stgobain_GUI.indexOf(self.Battery), _translate("MainWindow", "Battery"))

        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 0
        self.D_All_Thermistor = 0


        self.B1 = 0
        self.B2 = 0
        self.B3 = 0
        self.B4 = 0
        self.D_All_Battery = 0


    #====== Push Button Live Tab Command ===========================
    def Live_Thermistor_1(self):
        self.configure_LivePlot(1,15,12,'Thermistor 1',1,1,1,1)
        self.T1_Live = 1
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 0
        self.D_All_Thermistor = 0

    def Live_Thermistor_2(self):
        self.configure_LivePlot(2,15,12,'Thermistor 2',1,1,1,1)
        self.T1_Live = 0
        self.T2_Live = 1
        self.T3_Live = 0
        self.T4_Live = 0
        self.D_All_Thermistor = 0

    def Live_Thermistor_3(self):
        self.configure_LivePlot(3,15,12,'Thermistor 3',1,1,1,1)
        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 1
        self.T4_Live = 0
        self.D_All_Thermistor = 0

    def Live_Thermistor_4(self):
        self.configure_LivePlot(4,15,12,'Thermistor 4',1,1,1,1)
        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 1
        self.D_All_Thermistor = 0

    def Live_Display_All(self):
        self.configure_LivePlot(4,9,12,'Thermistor 4',1,1,1,1)
        self.add_Live_Plot(3,9,12,'Thermistor 3',1,0,1,1)
        self.add_Live_Plot(2,9,12,'Thermistor 2',0,1,1,1)
        self.add_Live_Plot(1,9,12,'Thermistor 1',0,0,1,1)
        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 0
        self.D_All_Thermistor = 1

    def TimeRange_Live_Plot(self, text):
        if self.T1_Live == 1:
            self.Live_Plot_Time(1,text,'Thermistor 1')
        elif self.T2_Live == 1:
            self.Live_Plot_Time(2, text, 'Thermistor 2')
        elif self.T3_Live == 1:
            self.Live_Plot_Time(3, text, 'Thermistor 3')
        elif self.T4_Live == 1:
            self.Live_Plot_Time(4, text, 'Thermistor 4')
        elif self.D_All_Thermistor == 1:
            self.Live_Plot_Time_Multi(text)
        
    def Live_Plot_Time(self, ID, text, title):
        if text == '1 minute':
            self.configure_LivePlot(ID,5,12,title,1,1,1,1)
        elif text == '5 minutes':
            self.configure_LivePlot(ID,5,60,title,1,1,1,1)
        elif text == '15 minutes':
            self.configure_LivePlot(ID,15,60,title,1,1,1,1)
        elif text == '30 minutes':
            self.configure_LivePlot(ID,15,120,title,1,1,1,1)
        elif text == '1 hour':
            self.configure_LivePlot(ID,15,240,title,1,1,1,1)
        elif text == '4 hours':
            self.configure_LivePlot(ID,15,960,title,1,1,1,1)
        elif text == '12 hours':
            self.configure_LivePlot(ID,15,2880,title,1,1,1,1)
        elif text == '1 day':
            self.configure_LivePlot(ID,15,5760,title,1,1,1,1)
        else:
            self.configure_LivePlot(ID,15,12,title,1,1,1,1)

    def Live_Plot_Time_Multi(self,text):
        if text == '1 minute':
            self.configure_LivePlot(4,5,12,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,5,12,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,5,12,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,5,12,'Thermistor 1',0,0,1,1)
        elif text == '5 minutes':
            self.configure_LivePlot(4,5,60,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,5,60,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,5,60,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,5,60,'Thermistor 1',0,0,1,1)
        elif text == '15 minutes':
            self.configure_LivePlot(4,5,180,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,5,180,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,5,180,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,5,180,'Thermistor 1',0,0,1,1)
        elif text == '30 minutes':
            self.configure_LivePlot(4,10,180,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,10,180,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,10,180,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,10,180,'Thermistor 1',0,0,1,1)
        elif text == '1 hour':
            self.configure_LivePlot(4,10,360,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,10,360,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,10,360,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,10,360,'Thermistor 1',0,0,1,1)
        elif text == '4 hours':
            self.configure_LivePlot(4,10,1440,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,10,1440,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,10,1440,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,10,1440,'Thermistor 1',0,0,1,1)
        elif text == '12 hours':
            self.configure_LivePlot(4,10,4320,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,10,4320,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,10,4320,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,10,4320,'Thermistor 1',0,0,1,1)
        elif text == '1 day':
            self.configure_LivePlot(4,10,8640,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,10,8640,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,10,8640,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,10,8640,'Thermistor 1',0,0,1,1)
        else:
            self.configure_LivePlot(4,9,12,'Thermistor 4',1,1,1,1)
            self.add_Live_Plot(3,9,12,'Thermistor 3',1,0,1,1)
            self.add_Live_Plot(2,9,12,'Thermistor 2',0,1,1,1)
            self.add_Live_Plot(1,9,12,'Thermistor 1',0,0,1,1)
    #========== Push Button Battery Tab Command =================
    def BV_Thermistor_1(self):
        self.configure_LiveBatteryPlot(1,15,12,'Battery Volt Thermistor 1',1,1,1,1)
        self.B1 = 1
        self.B2 = 0
        self.B3 = 0
        self.B4 = 0
        self.D_All_Battery = 0

    def BV_Thermistor_2(self):
        self.configure_LiveBatteryPlot(2,15,12,'Battery Volt Thermistor 2',1,1,1,1)
        self.B1 = 0
        self.B2 = 1
        self.B3 = 0
        self.B4 = 0
        self.D_All_Battery = 0

    def BV_Thermistor_3(self):
        self.configure_LiveBatteryPlot(3,15,12,'Battery Volt Thermistor 3',1,1,1,1)
        self.B1 = 0
        self.B2 = 0
        self.B3 = 1
        self.B4 = 0
        self.D_All_Battery = 0
        
    def BV_Thermistor_4(self):
        self.configure_LiveBatteryPlot(4,15,12,'Battery Volt Thermistor 4',1,1,1,1)
        self.B1 = 0
        self.B2 = 0
        self.B3 = 0
        self.B4 = 1
        self.D_All_Battery = 0
        
    def Live_Display_All_Battery(self):
        self.configure_LiveBatteryPlot(4,9,12,'Battery Volt Thermistor 4',1,1,1,1)
        self.add_Live_Plot_Battery(3,9,12,'Battery Volt Thermistor 3',1,0,1,1)
        self.add_Live_Plot_Battery(2,9,12,'Battery Volt Thermistor 2',0,1,1,1)
        self.add_Live_Plot_Battery(1,9,12,'Battery Volt Thermistor 1',0,0,1,1)
        self.B1 = 0
        self.B2 = 0
        self.B3 = 0
        self.B4 = 0
        self.D_All_Battery = 1

    def TimeRange_Live_Battery_Plot(self, text):
        if self.B1 == 1:
            self.Live_Plot_Time_Battery(1,text,'Battery Volt Thermistor 1')
        elif self.B2 == 1:
            self.Live_Plot_Time_Battery(2, text, 'Battery Volt Thermistor 2')
        elif self.B3 == 1:
            self.Live_Plot_Time_Battery(3, text, 'Battery Volt Thermistor 3')
        elif self.B4 == 1:
            self.Live_Plot_Time_Battery(4, text, 'Battery Volt Thermistor 4')
        elif self.D_All_Battery == 1:
            self.Live_Plot_Time_Multi_Battery(text)

    def Live_Plot_Time_Battery(self, ID, text, title):
        if text == '1 minute':
            self.configure_LiveBatteryPlot(ID,5,12,title,1,1,1,1)
        elif text == '5 minutes':
            self.configure_LiveBatteryPlot(ID,5,60,title,1,1,1,1)
        elif text == '15 minutes':
            self.configure_LiveBatteryPlot(ID,15,60,title,1,1,1,1)
        elif text == '30 minutes':
            self.configure_LiveBatteryPlot(ID,15,120,title,1,1,1,1)
        elif text == '1 hour':
            self.configure_LiveBatteryPlot(ID,15,240,title,1,1,1,1)
        elif text == '4 hours':
            self.configure_LiveBatteryPlot(ID,15,960,title,1,1,1,1)
        elif text == '12 hours':
            self.configure_LiveBatteryPlot(ID,15,2880,title,1,1,1,1)
        elif text == '1 day':
            self.configure_LiveBatteryPlot(ID,15,5760,title,1,1,1,1)
        else:
            self.configure_LiveBatteryPlot(ID,15,12,title,1,1,1,1)

    def Live_Plot_Time_Multi_Battery(self,text):
        if text == '1 minute':
            self.configure_LiveBatteryPlot(4,5,12,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,5,12,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,5,12,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,5,12,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '5 minutes':
            self.configure_LiveBatteryPlot(4,5,60,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,5,60,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,5,60,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,5,60,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '15 minutes':
            self.configure_LiveBatteryPlot(4,5,180,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,5,180,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,5,180,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,5,180,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '30 minutes':
            self.configure_LiveBatteryPlot(4,10,180,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,10,180,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,10,180,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,10,180,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '1 hour':
            self.configure_LiveBatteryPlot(4,10,360,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,10,360,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,10,360,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,10,360,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '4 hours':
            self.configure_LiveBatteryPlot(4,10,1440,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,10,1440,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,10,1440,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,10,1440,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '12 hours':
            self.configure_LiveBatteryPlot(4,10,4320,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,10,4320,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,10,4320,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,10,4320,'Battery Volt Thermistor 1',0,0,1,1)
        elif text == '1 day':
            self.configure_LiveBatteryPlot(4,10,8640,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,10,8640,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,10,8640,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,10,8640,'Battery Volt Thermistor 1',0,0,1,1)
        else:
            self.configure_LiveBatteryPlot(4,9,12,'Battery Volt Thermistor 4',1,1,1,1)
            self.add_Live_Plot_Battery(3,9,12,'Battery Volt Thermistor 3',1,0,1,1)
            self.add_Live_Plot_Battery(2,9,12,'Battery Volt Thermistor 2',0,1,1,1)
            self.add_Live_Plot_Battery(1,9,12,'Battery Volt Thermistor 1',0,0,1,1)
    
    def configure_LivePlot(self,ID,N_data,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.Live_Plot_Layout.count())): 
                self.Live_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Update_Plot(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID,N_data,step,title)
        self.plot.update_figure(ID,N_data,step,title)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

    def add_Live_Plot(self,ID,N_data,step,title,cor_0,cor_1,cor_2,cor_3):
        self.plot = Update_Plot(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID,N_data,step,title)
        self.plot.update_figure(ID,N_data,step,title)
        self.Live_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

    def configure_LiveBatteryPlot(self,ID,N_data,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.Battery_Plot_Layout.count())): 
                self.Battery_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Update_Battery_Plot(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID,N_data,step,title)
        self.plot.update_figure(ID,N_data,step,title)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)
    
    def add_Live_Plot_Battery(self,ID,N_data,step,title,cor_0,cor_1,cor_2,cor_3):
        self.plot = Update_Battery_Plot(self.Live_Plot_Widget)
        self.plot.ubah_Parameter(ID,N_data,step,title)
        self.plot.update_figure(ID,N_data,step,title)
        self.Battery_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)





  #========== Push Button Historical Tab Command =================
    def Historical_Thermistor_1(self):
        self.T1_Live = 1
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 0

    def Historical_Thermistor_2(self):
        self.T1_Live = 0
        self.T2_Live = 1
        self.T3_Live = 0
        self.T4_Live = 0
    
    def Historical_Thermistor_3(self):
        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 1
        self.T4_Live = 0
  
    def Historical_Thermistor_4(self):
        self.T1_Live = 0
        self.T2_Live = 0
        self.T3_Live = 0
        self.T4_Live = 1

    def SetHistory(self):

        time_begin = self.Begin_Time.time().toString()
        time_end = self.End_Time.time().toString()

        date_begin = self.Begin_Date.date().toString()
        date_begin = date_begin.split(' ')

        self.configure_date(date_begin)
        
        datetime_begin = date_begin[3]+'-'+date_begin[1]+'-'+date_begin[2]+' '+time_begin
        datetime_begin = str(datetime_begin)
        
        date_end = self.End_Date.date().toString()
        date_end = date_end.split(' ')

        self.configure_date(date_end)
    
        datetime_end = date_end[3]+'-'+date_end[1]+'-'+date_end[2]+' '+time_end
        datetime_end = str(datetime_end)

        if self.T1_Live == 1:
            self.configure_HistoryPlot(1, datetime_begin, datetime_end, 60, 'Thermistor 1',1,1,1,1)
        elif self.T2_Live == 1:
            self.configure_HistoryPlot(2,datetime_begin,datetime_end,60,'Thermistor 2',1,1,1,1)
        elif self.T3_Live == 1:
            self.configure_HistoryPlot(3,datetime_begin,datetime_end,60,'Thermistor 3',1,1,1,1)
        elif self.T4_Live == 1:
            self.configure_HistoryPlot(4,datetime_begin,datetime_end,60,'Thermistor 4',1,1,1,1)

    def configure_date(self, date):
        if date[1] =='Jan':
            date[1] = str('01')
        elif date[1] == 'Feb':
            date[1] = str('02')
        elif date[1] == 'Mar':
            date[1] = str('03')
        elif date[1] == 'Apr':
            date[1] = str('04')
        elif date[1] == 'Mei':
            date[1] = str('05')
        elif date[1] == 'Jun':
            date[1] = str('06')
        elif date[1] == 'Jul':
            date[1] = str('07')
        elif date[1] == 'Agu':
            date[1] = str('08')
        elif date[1] == 'Sep':
            date[1] = str('09')
        elif date[1] == 'Okt':
            date[1] = str('10')
        elif date[1] == 'Nov':
            date[1] = str('11')
        else:
            date[1] = str('12')

        if date[2] =='1':
            date[2] = str('01')
        elif date[2] == '2':
            date[2] = str('02')
        elif date[2] == '3':
            date[2] = str('03')
        elif date[2] == '4':
            date[2] = str('04')
        elif date[2] == '5':
            date[2] = str('05')
        elif date[2] == '6':
            date[2] = str('06')
        elif date[2] == '7':
            date[2] = str('07')
        elif date[2] == '8':
            date[2] = str('08')
        elif date[2] == '9':
            date[2] = str('09')

    def configure_HistoryPlot(self,ID,date_begin,date_end,step,title,cor_0,cor_1,cor_2,cor_3):
        
        for i in reversed(range(self.History_Plot_Layout.count())): 
                self.History_Plot_Layout.itemAt(i).widget().setParent(None)

        self.plot = Static_Plot(self.History_Plot_Widget)
        self.plot.ubah_Parameter_Static(ID, date_begin, date_end, step, title)
        self.plot.update_figure_static(ID,date_begin,date_end,step,title)
        self.History_Plot_Layout.addWidget(self.plot, cor_0, cor_1, cor_2, cor_3)

#===========================================================================App Configuration===========================================================================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
