import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox, QTextEdit, QFormLayout, QMessageBox
from cybercity import Cybercity

class DefenderWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.cybercity = parent.cybercity
        self.budget = parent.budget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.create_widgets()

    def create_widgets(self):
        # Create budget labels
        defender_budget_label = QLabel("Defender's Budget:")
        self.layout.addWidget(defender_budget_label)
        self.defender_budget_label = QLabel(str(self.budget["defender"]))
        self.layout.addWidget(self.defender_budget_label)

        # Create location selection
        location_label = QLabel("Locations to Protect / Turn Off Lights:")
        self.layout.addWidget(location_label)

        self.location_spinbox = QSpinBox()
        self.location_spinbox.setMinimum(0)
        self.location_spinbox.setMaximum(8)
        self.location_spinbox.valueChanged.connect(self.update_district_selection)
        self.layout.addWidget(self.location_spinbox)

        # Create a form layout to hold district selection and action combo boxes
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)

        # Create submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_defender_turn)
        self.layout.addWidget(submit_button)

    def update_district_selection(self):
        n_locations = self.location_spinbox.value()

        # Clear existing district widgets
        for i in reversed(range(self.form_layout.count())):
            widget = self.form_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Create new district widgets based on the selected number of locations
        for i in range(n_locations):
            district_label = QLabel(f"District {i + 1}:")
            district_combobox = QComboBox()
            district_combobox.addItems(list(self.cybercity.districts.keys()))

            action_label = QLabel(f"Choose Action for District {i + 1}:")
            action_combobox = QComboBox()
            action_combobox.addItems(["Firewall", "Virus Protection", "Intrusion Detection System", "User Training", "Turn Off Lights"])
            self.form_layout.addRow(district_label, district_combobox)
            self.form_layout.addRow(action_label, action_combobox)

    def submit_defender_turn(self):
        n_locations = self.location_spinbox.value()

        start_value = 1
        for i in range(n_locations):
            print(i)
            district_combobox = self.form_layout.itemAt(start_value).widget()
            action_combobox = self.form_layout.itemAt(start_value + 2).widget()
            start_value += 4
            district = district_combobox.currentText()
            action = action_combobox.currentText()

            cost = int(self.budget['defender'] * self.parent().protection_actions[action]["probability"])
            if cost > self.budget['defender']:
                # Show warning message if the budget is not enough for the selected action
                QMessageBox.warning(self, "Insufficient Budget", f"You don't have enough budget to perform the action '{action}' in District {district}.")
            else:
                self.budget['defender'] -= cost

            if action == "Turn Off Lights":
                self.cybercity.turnOffLight(district)
            else:
                print("yes")
                #changed
                if self.cybercity.hackSuccessful(self.parent().protection_actions[action]["probability"]):
                    self.cybercity.applyEffect(district, self.parent().protection_actions[action]["effect"])
                    if self.cybercity.getEffect(district) >= 0:
                        self.cybercity.turnOnLight(district)
                else:
                    QMessageBox.warning(self, "Defense Failed", f"Defense {action} is not successful in District {district}.")

        self.defender_budget_label.setText(str(self.budget["defender"]))
        self.parent().next_round()

class AttackerWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.cybercity = parent.cybercity
        self.budget = parent.budget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.create_widgets()

    def create_widgets(self):
        # Create budget labels
        attacker_budget_label = QLabel("Attacker's Budget:")
        self.layout.addWidget(attacker_budget_label)
        self.attacker_budget_label = QLabel(str(self.budget["attacker"]))
        self.layout.addWidget(self.attacker_budget_label)

        # Create location selection
        location_label = QLabel("Locations to Hack:")
        self.layout.addWidget(location_label)

        self.location_spinbox = QSpinBox()
        self.location_spinbox.setMinimum(0)
        self.location_spinbox.setMaximum(8)
        self.location_spinbox.valueChanged.connect(self.update_widgets)
        self.layout.addWidget(self.location_spinbox)

        # Create a form layout to hold district selection and action combo boxes
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)

        # Create submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_attacker_turn)
        self.layout.addWidget(submit_button)

        # Call the method to initialize widgets
        self.update_widgets()

    def update_widgets(self):
        n_locations = self.location_spinbox.value()

        # Clear existing widgets
        for i in reversed(range(self.form_layout.count())):
            widget = self.form_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        # Create new district widgets based on the selected number of locations
        for i in range(n_locations):
            district_label = QLabel(f"District {i + 1}:")
            district_combobox = QComboBox()
            district_combobox.addItems(list(self.cybercity.districts.keys()))

            action_label = QLabel(f"Choose Action for District {i + 1}:")
            action_combobox = QComboBox()
            action_combobox.addItems(["Phishing", "Virus", "Malware", "Skip Turn"])
            self.form_layout.addRow(district_label, district_combobox)
            self.form_layout.addRow(action_label, action_combobox)

    def submit_attacker_turn(self):
        n_locations = self.location_spinbox.value()
        print(n_locations)
        start_value = 1
        for i in range(n_locations):
            print(i)
            district_combobox = self.form_layout.itemAt(start_value).widget()
            action_combobox = self.form_layout.itemAt(start_value + 2).widget()
            start_value += 4
        # for i in range(n_locations):
            district = district_combobox.currentText()
            action = action_combobox.currentText()
            print(district, action)
            cost = int(self.budget['attacker'] * self.parent().hacking_actions[action]["probability"])
            if cost > self.budget['attacker']:
                # Show warning message if the budget is not enough for the selected action
                QMessageBox.warning(self, "Insufficient Budget", f"You don't have enough budget to perform the action '{action}' in District {district}.")
            else:
                self.budget['attacker'] -= cost
            if action != "Skip Turn":
                print("yes")
                #changed
                if self.cybercity.hackSuccessful(self.parent().hacking_actions[action]["probability"]):
                    self.cybercity.compromiseEffect(district, self.parent().hacking_actions[action]["effect"])
                    if self.cybercity.getEffect(district) < 0:
                        self.cybercity.turnOffLight(district)
                else:
                    QMessageBox.warning(self, "Hack Failed", f"Hack {action} is not successful in District {district}.")

        self.attacker_budget_label.setText(str(self.budget["attacker"]))
        self.parent().next_round()

class MainWindow(QMainWindow):
    def __init__(self, x, y, grid, title):
        super().__init__()
        self.setGeometry(x, y, 960, 540)
        self.setWindowTitle(title)
        self.cybercity = Cybercity()
        # self.grid = grid
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

    # # Override the paintEvent to custom drawing
    # def paintEvent(self, event):
    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawGrid(event, qp)
    #     qp.end()

    # def drawGrid(self, event, qp):
    #     size = self.size()
    #     w = size.width()
    #     h = size.height()

    #     # Create the grid by drawing lines
    #     for i in range(0, w, w // self.grid):
    #         qp.setPen(QColor(0, 0, 0))
    #         qp.drawLine(i, 0, i, h)

    #     for i in range(0, h, h // self.grid):
    #         qp.setPen(QColor(0, 0, 0))
    #         qp.drawLine(0, i, w, i)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # num_rows and num_cols represents the size of game grid
    num_rows = 10
    num_cols = 10

    # Creating the first game window
    game1 = MainWindow(50, 50, num_rows, "Game 1")
    game1.show()

    # Creating the second game window
    game2 = MainWindow(700, 50, num_cols, "Game 2")
    game2.show()

    sys.exit(app.exec_())