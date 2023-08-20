import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox, QTextEdit, QFormLayout, QMessageBox
from cybercity import Cybercity
from PyQt5.QtGui import QPixmap


class AttackerWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # self.main_window = MainWindow()
        self.cybercity = parent.cybercity
        self.budget = parent.budget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        # self.create_widgets()


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
    
    def update_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

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
        # self.parent().increase_round()
        self.parent().round_switch()