import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)
from PyQt6.QtCore import QTimer


class ClickGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("点击小球")
        self.setFixedSize(520, 620)

        self.score = 0
        self.seconds_left = 30
        self.running = False

        root = QWidget(self)
        root.setStyleSheet("background: #f4f7fb;")
        self.setCentralWidget(root)

        self.status = QLabel("点击“开始游戏”，尽可能多地点击小球！", root)
        self.status.setGeometry(20, 20, 480, 45)
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.score_label = QLabel("得分：0", root)
        self.score_label.setGeometry(45, 80, 180, 35)
        self.score_label.setStyleSheet("font-size: 20px;")

        self.time_label = QLabel("剩余时间：30 秒", root)
        self.time_label.setGeometry(275, 80, 200, 35)
        self.time_label.setStyleSheet("font-size: 20px;")

        self.start_button = QPushButton("开始游戏", root)
        self.start_button.setGeometry(175, 540, 170, 50)
        self.start_button.setStyleSheet("font-size: 18px; background: #3b82f6; color: white;")
        self.start_button.clicked.connect(self.start_game)

        self.target = QPushButton("●", root)
        self.target.setFixedSize(70, 70)
        self.target.setStyleSheet(
            "font-size: 42px; color: white; border: none; border-radius: 35px; background: #ef4444;"
        )
        self.target.clicked.connect(self.hit_target)
        self.target.hide()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)

    def start_game(self):
        self.score = 0
        self.seconds_left = 30
        self.running = True
        self.start_button.setText("重新开始")
        self.status.setText("快点点击红色小球！")
        self.update_labels()
        self.move_target()
        self.target.show()
        self.timer.start(1000)

    def hit_target(self):
        if not self.running:
            return
        self.score += 1
        self.update_labels()
        self.move_target()

    def move_target(self):
        self.target.move(random.randint(15, 435), random.randint(130, 450))

    def tick(self):
        self.seconds_left -= 1
        self.update_labels()
        if self.seconds_left <= 0:
            self.running = False
            self.timer.stop()
            self.target.hide()
            self.status.setText(f"游戏结束！你的得分是 {self.score} 分。")

    def update_labels(self):
        self.score_label.setText(f"得分：{self.score}")
        self.time_label.setText(f"剩余时间：{self.seconds_left} 秒")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickGame()
    window.show()
    sys.exit(app.exec())
