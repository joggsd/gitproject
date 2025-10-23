# main.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# ui.py에서 정의한 Ui_MainWindow 클래스를 가져옵니다.
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    메인 윈도우 클래스입니다.
    UI 설정과 시그널-슬롯 연결을 담당합니다.
    """
    def __init__(self):
        super().__init__()

        # UI 초기화
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 위젯의 시그널을 슬롯(메서드)에 연결
        self.ui.addButton.clicked.connect(self.perform_addition)

    def perform_addition(self):
        """
        두 입력창의 숫자를 더하고 결과를 레이블에 표시합니다.
        """
        try:
            num1 = float(self.ui.edit1.text() or 0)
            num2 = float(self.ui.edit2.text() or 0)
            result = num1 + num2
            self.ui.resultLabel.setText(f"결과: {result}")
        except ValueError:
            # 숫자로 변환할 수 없는 값이 입력된 경우
            self.ui.resultLabel.setText("결과: 유효한 숫자를 입력하세요.")


if __name__ == "__main__":
    # 애플리케이션 실행
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
