# ui.py
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)
from PyQt6.QtCore import QCoreApplication

class Ui_MainWindow(object):
    """
    애플리케이션의 UI를 정의하는 클래스입니다.
    위젯 생성, 속성 설정, 레이아웃 배치를 담당합니다.
    """
    def setupUi(self, MainWindow: QMainWindow):
        # 윈도우 기본 설정
        MainWindow.setWindowTitle("덧셈 계산기")
        MainWindow.setFixedSize(300, 150)

        # 중앙 위젯 및 전체 레이아웃
        self.centralWidget = QWidget()
        MainWindow.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout(self.centralWidget)

        # 숫자 입력 위젯
        self.edit1 = QLineEdit()
        self.edit1.setPlaceholderText("첫 번째 숫자를 입력하세요")
        self.verticalLayout.addWidget(self.edit1)

        self.edit2 = QLineEdit()
        self.edit2.setPlaceholderText("두 번째 숫자를 입력하세요")
        self.verticalLayout.addWidget(self.edit2)

        # 계산 버튼
        self.addButton = QPushButton("add")
        self.verticalLayout.addWidget(self.addButton)

        # 결과 표시 레이블
        self.resultLabel = QLabel("결과: ")
        self.verticalLayout.addWidget(self.resultLabel)

        QCoreApplication.translate
