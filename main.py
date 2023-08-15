import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox, QTextEdit, QFormLayout, QMessageBox
from cybercity import Cybercity
from attacker import *
from defender import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberCity Game")
        self.cybercity = Cybercity()
        width = 960
        height = 540 
        # self.setFixedHeight(height)
        # self.setFixedWidth(width)
        # self.setGeometry(0, 0, width, height)
        self.budget = {"defender": 50000, "attacker": 50000}
        self.round_counter = 0
        self.protection_actions = {
            "Firewall": {"effect": 0.30, "probability": 0.7},
            "Virus Protection": {"effect": 0.15, "probability": 0.8},
            "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
            "User Training": {"effect": 0.20, "probability": 1.0},
            "Turn Off Lights": {"effect": 0, "probability": 1.0}
        }
        
        self.hacking_actions = {
            "Phishing": {"effect": 0.35, "probability": 0.7},
            "Virus": {"effect": 0.25, "probability": 0.8},
            "Malware": {"effect": 0.20, "probability": 0.9},
            "Skip Turn": {"effect": 0, "probability": 1.0}
        }

        # Adding 'Business' district to both dictionaries
        for district in self.cybercity.districts.keys():
            if district not in self.protection_actions:
                self.protection_actions[district] = {"effect": 0, "probability": 1.0}
            if district not in self.hacking_actions:
                self.hacking_actions[district] = {"effect": 0, "probability": 1.0}

        # Create defender window
        self.defender_window = DefenderWindow(self)
        self.defender_window.setWindowTitle("Defender's Turn")
        self.setCentralWidget(self.defender_window)

    def next_round(self):
        if self.round_counter >= 10:
            output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
            if output_text is None:
                # Create QTextEdit widget if not found
                output_text = QTextEdit()
                output_text.setObjectName('output_text')
                self.centralWidget().layout.addWidget(output_text)

            output_text.append("\n--- End of Game ---")
            return
        self.round_counter += 1

        if self.round_counter % 2 == 0:
            # Switch to attacker window
            self.attacker_window = AttackerWindow(self)
            self.attacker_window.setWindowTitle("Attacker's Turn")
            self.setCentralWidget(self.attacker_window)
        else:
            # Switch to defender window
            self.defender_window = DefenderWindow(self)
            self.defender_window.setWindowTitle("Defender's Turn")
            self.setCentralWidget(self.defender_window)

        if hasattr(self, 'defender_window'):
            self.defender_window.defender_budget_label.setText(str(self.budget["defender"]))
        if hasattr(self, 'attacker_window'):
            self.attacker_window.attacker_budget_label.setText(str(self.budget["attacker"]))

        output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
        if output_text is None:
            # Create QTextEdit widget if not found
            output_text = QTextEdit()
            output_text.setObjectName('output_text')
            self.centralWidget().layout.addWidget(output_text)

        if output_text.toPlainText() == "--- Game Started ---":
            output_text.append(f"\n--- Round {self.round_counter} ---")
        else:
            output_text.append("\nAfter turn:")
            output_text.append(self.cybercity.status())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())