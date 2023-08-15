# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox, QTextEdit
# from cybercity import Cybercity

# class DefenderWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Defender's Turn")
#         self.cybercity = parent.cybercity
#         self.budget = parent.budget
#         self.create_widgets()

#     def create_widgets(self):
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#         self.layout = QVBoxLayout()
#         self.central_widget.setLayout(self.layout)

#         # Create budget labels
#         defender_budget_label = QLabel("Defender's Budget:")
#         self.layout.addWidget(defender_budget_label)
#         self.defender_budget_label = QLabel(str(self.budget["defender"]))
#         self.layout.addWidget(self.defender_budget_label)

#         # Create location selection
#         location_label = QLabel("Locations to Protect / Turn Off Lights:")
#         self.layout.addWidget(location_label)

#         self.location_spinbox = QSpinBox()
#         self.location_spinbox.setMinimum(0)
#         self.location_spinbox.setMaximum(8)
#         self.layout.addWidget(self.location_spinbox)

#         # Create action selection
#         action_label = QLabel("Choose Action:")
#         self.layout.addWidget(action_label)

#         self.action_combobox = QComboBox()
#         self.action_combobox.addItems(["Firewall", "Virus Protection", "Intrusion Detection System", "User Training", "Turn Off Lights"])
#         self.layout.addWidget(self.action_combobox)

#         # Create district selection
#         district_label = QLabel("Choose District:")
#         self.layout.addWidget(district_label)

#         self.district_combobox = QComboBox()
#         self.district_combobox.addItems(list(self.cybercity.districts.keys()))
#         self.layout.addWidget(self.district_combobox)

#         # Create submit button
#         submit_button = QPushButton("Submit")
#         submit_button.clicked.connect(self.submit_defender_turn)
#         self.layout.addWidget(submit_button)

#     def submit_defender_turn(self):
#         n_locations = self.location_spinbox.value()
#         for _ in range(n_locations):
#             action = self.action_combobox.currentText()
#             district = self.district_combobox.currentText()

#             cost = int(self.budget['defender'] * self.parent().protection_actions[action]["probability"])
#             self.budget['defender'] -= cost

#             if action != "Turn Off Lights":
#                 self.cybercity.turnOnLight(district)
#             else:
#                 self.cybercity.turnOffLight(district)

#         self.defender_budget_label.setText(str(self.budget["defender"]))
#         self.parent().switch_turn()

# class AttackerWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Attacker's Turn")
#         self.cybercity = parent.cybercity
#         self.budget = parent.budget
#         self.create_widgets()

#     def create_widgets(self):
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)
#         self.layout = QVBoxLayout()
#         self.central_widget.setLayout(self.layout)

#         # Create budget labels
#         attacker_budget_label = QLabel("Attacker's Budget:")
#         self.layout.addWidget(attacker_budget_label)
#         self.attacker_budget_label = QLabel(str(self.budget["attacker"]))
#         self.layout.addWidget(self.attacker_budget_label)

#         # Create location selection
#         location_label = QLabel("Locations to Hack:")
#         self.layout.addWidget(location_label)

#         self.location_spinbox = QSpinBox()
#         self.location_spinbox.setMinimum(0)
#         self.location_spinbox.setMaximum(8)
#         self.layout.addWidget(self.location_spinbox)

#         # Create action selection
#         action_label = QLabel("Choose Action:")
#         self.layout.addWidget(action_label)

#         self.action_combobox = QComboBox()
#         self.action_combobox.addItems(["Phishing", "Virus", "Malware", "Skip Turn"])
#         self.layout.addWidget(self.action_combobox)

#         # Create district selection
#         district_label = QLabel("Choose District:")
#         self.layout.addWidget(district_label)

#         self.district_combobox = QComboBox()
#         self.district_combobox.addItems(list(self.cybercity.districts.keys()))
#         self.layout.addWidget(self.district_combobox)

#         # Create submit button
#         submit_button = QPushButton("Submit")
#         submit_button.clicked.connect(self.submit_attacker_turn)
#         self.layout.addWidget(submit_button)

#     def submit_attacker_turn(self):
#         n_locations = self.location_spinbox.value()
#         for _ in range(n_locations):
#             action = self.action_combobox.currentText()
#             district = self.district_combobox.currentText()

#             cost = int(self.budget['attacker'] * self.parent().hacking_actions[action]["probability"])
#             self.budget['attacker'] -= cost

#             if action != "Skip Turn":
#                 if self.cybercity.hackSuccessful(self.parent().hacking_actions[action]["probability"]):
#                     self.cybercity.turnOffLight(district)

#         self.attacker_budget_label.setText(str(self.budget["attacker"]))
#         self.parent().switch_turn()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("CyberCity Game")
#         self.cybercity = Cybercity()
#         self.budget = {"defender": 50000, "attacker": 50000}
#         self.round_counter = 0
#         self.protection_actions = {
#             "Firewall": {"effect": 0.30, "probability": 0.7},
#             "Virus Protection": {"effect": 0.15, "probability": 0.8},
#             "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
#             "User Training": {"effect": 0.20, "probability": 1.0},
#             "Turn Off Lights": {"effect": 0, "probability": 1.0}
#         }
#         self.hacking_actions = {
#             "Phishing": {"effect": 0.35, "probability": 0.7},
#             "Virus": {"effect": 0.25, "probability": 0.8},
#             "Malware": {"effect": 0.20, "probability": 0.9},
#             "Skip Turn": {"effect": 0, "probability": 1.0}
#         }

#         # Create defender window
#         self.defender_window = DefenderWindow(self)
#         self.defender_window.show()

#         # Create attacker window
#         self.attacker_window = AttackerWindow(self)

#     def switch_turn(self):
#         if self.round_counter >= 10:
#             self.defender_window.close()
#             self.attacker_window.close()
#             output_text = self.findChild(QTextEdit, 'output_text')
#             if output_text is None:
#                 # Create QTextEdit widget if not found
#                 output_text = QTextEdit()
#                 output_text.setObjectName('output_text')
#                 self.layout.addWidget(output_text)

#             output_text.append("\n--- End of Game ---")
#             return

#         self.round_counter += 1

#         if self.round_counter % 2 == 0:
#             self.defender_window.close()
#             self.attacker_window.show()
#         else:
#             self.attacker_window.close()
#             self.defender_window.show()

#         if hasattr(self, 'defender_window'):
#             self.defender_window.defender_budget_label.setText(str(self.budget["defender"]))
#         if hasattr(self, 'attacker_window'):
#             self.attacker_window.attacker_budget_label.setText(str(self.budget["attacker"]))

#         output_text = self.defender_window.findChild(QTextEdit, 'output_text')
#         if output_text is None:
#             # Create QTextEdit widget if not found
#             output_text = QTextEdit()
#             output_text.setObjectName('output_text')
#             self.defender_window.layout.addWidget(output_text)

#         if output_text.toPlainText() == "":
#             output_text.append(f"--- Round {self.round_counter} ---")
#         else:
#             output_text.append("\nAfter turn:")
#             output_text.append(self.cybercity.status())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     defender_window = MainWindow()
#     attacker_window = MainWindow()
#     defender_window.show()
#     attacker_window.show()
#     sys.exit(app.exec_())