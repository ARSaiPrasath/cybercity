import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox, QTextEdit, QFormLayout, QMessageBox
from cybercity import Cybercity


class DefenderWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # self.main_window = parent()
        # print("defend")
        self.cybercity = parent.cybercity
        self.budget = parent.budget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # self.create_widgets()

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
        # self.parent().active = False
        # self.parent().increase_round()
        self.parent().round_switch()