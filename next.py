


class NextRound():
    def __init__(self):
        self.round_counter = 0
        print(self.round_counter)

    def get_num_rounds(self):
        return self.round_counter
    
    # def increase_round(self):
    #     self.round_counter

    def next_round(self):
        self.round_counter += 1
        # if hasattr(self, 'defender_window'):
        #     self.defender_window.defender_budget_label.setText(str(self.budget["defender"]))
        # if hasattr(self, 'attacker_window'):
        #     self.attacker_window.attacker_budget_label.setText(str(self.budget["attacker"]))

        # output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
        # if output_text is None:
        #     # Create QTextEdit widget if not found
        #     output_text = QTextEdit()
        #     output_text.setObjectName('output_text')
        #     self.centralWidget().layout.addWidget(output_text)

        # if output_text.toPlainText() == "--- Game Started ---":
        #     output_text.append(f"\n--- Round {self.round_counter} ---")
        # else:
        #     output_text.append("\nAfter turn:")
        #     output_text.append(self.cybercity.status())
        return self.round_counter

            

        # if self.round_counter % 2 == 0 and self.title == "attacker":
        #     # Switch to attacker window
        #     self.attacker_window = AttackerWindow(self)
        #     self.attacker_window.setWindowTitle("Attacker's Turn")
        #     self.setCentralWidget(self.attacker_window)
        # elif self.round_counter % 2 != 0 and self.title == "defender":
        #     # Switch to defender window
        #     self.defender_window = DefenderWindow(self)
        #     self.defender_window.setWindowTitle("Defender's Turn")
        #     self.setCentralWidget(self.defender_window)




