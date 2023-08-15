# from flask import Flask, render_template, request
# from cybercity import Cybercity

# def validate_input(prompt, valid_inputs):
#     while True:
#         user_input = input(prompt)
#         if user_input in valid_inputs:
#             return user_input
#         else:
#             print(f"Invalid input! Please enter one of the following: {', '.join(valid_inputs)}")

# cybercity = Cybercity()

# budget = {
#     "defender": 50000,
#     "attacker": 50000
# }

# protection_actions = {
#     "Firewall": {"effect": 0.30, "probability": 0.7},
#     "Virus Protection": {"effect": 0.15, "probability": 0.8},
#     "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
#     "User Training": {"effect": 0.20, "probability": 1.0},
#     "Turn Off Lights": {"effect": 0, "probability": 1.0}
# }

# hacking_actions = {
#     "Phishing": {"effect": 0.35, "probability": 0.7},
#     "Virus": {"effect": 0.25, "probability": 0.8},
#     "Malware": {"effect": 0.20, "probability": 0.9},
#     "Skip Turn": {"effect": 0, "probability": 1.0}
# }

# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/attacker', methods=['GET', 'POST'])
# def attacker_game():
#     if request.method == 'POST':
#         n_locations = request.form.get("locations_hack")
#         if n_locations and n_locations.strip() != "":
#             for _ in range(int(n_locations.strip())):
#                 action = request.form.get("action_hack")
#                 district = request.form.get("district_hack")
#                 cost = int(budget['attacker'] * hacking_actions[action]["probability"])
#                 budget['attacker'] -= cost
#                 if action != "Skip Turn":
#                     if cybercity.hackSuccessful(hacking_actions[action]["probability"]):
#                         cybercity.turnOffLight(district)
#                 cybercity.refresh()

#         return render_template('attacker.html', game_finished=True, cybercity=cybercity)
#     else:
#         return render_template('attacker.html', game_finished=False, cybercity=cybercity)

# @app.route('/defender', methods=['GET', 'POST'])
# def defender_game():
#     if request.method == 'POST':
#         n_locations = request.form.get("locations_protect")
#         if n_locations and n_locations.strip() != "":
#             for _ in range(int(n_locations.strip())):
#                 action = request.form.get("action_protect")
#                 district = request.form.get("district_protect")
#                 cost = int(budget['defender'] * protection_actions[action]["probability"])
#                 budget['defender'] -= cost
#                 if action != "Turn Off Lights":
#                     cybercity.turnOnLight(district)
#                 else:
#                     cybercity.turnOffLight(district)
#                 cybercity.refresh()

#         return render_template('defender.html', game_finished=True, cybercity=cybercity)
#     else:
#         return render_template('defender.html', game_finished=False, cybercity=cybercity)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
from cybercity import Cybercity

app = Flask(__name__)

cybercity = Cybercity()

budget = {
    "defender": 50000,
    "attacker": 50000
}

protection_actions = {
    "Firewall": {"effect": 0.30, "probability": 0.7},
    "Virus Protection": {"effect": 0.15, "probability": 0.8},
    "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
    "User Training": {"effect": 0.20, "probability": 1.0},
    "Turn Off Lights": {"effect": 0, "probability": 1.0}
}

hacking_actions = {
    "Phishing": {"effect": 0.35, "probability": 0.7},
    "Virus": {"effect": 0.25, "probability": 0.8},
    "Malware": {"effect": 0.20, "probability": 0.9},
    "Skip Turn": {"effect": 0, "probability": 1.0}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/attacker', methods=['GET', 'POST'])
def attacker_game():
    if request.method == 'POST':
        role = "attacker"
        player_budget = budget['attacker']
        player_actions = hacking_actions
        player_template = 'attacker.html'
        opponent_role = 'defender'
        opponent_actions = protection_actions
        opponent_template = 'defender.html'

        n_locations = request.form.get("locations")
        if n_locations and n_locations.strip() != "":
            n_locations = int(n_locations.strip())

            for _ in range(n_locations):
                action = request.form.get("action")
                district = request.form.get("district")

                cost = int(player_budget * player_actions[action]["probability"])
                player_budget -= cost

                if action != "Skip Turn":
                    if cybercity.hackSuccessful(player_actions[action]["probability"]):
                        cybercity.turnOffLight(district)

                cybercity.refresh()

                # Swap roles for the next iteration
                role, opponent_role = opponent_role, role
                player_budget, opponent_budget = budget[opponent_role], player_budget
                player_actions, opponent_actions = opponent_actions, player_actions
                player_template, opponent_template = opponent_template, player_template

        return render_template(player_template, game_finished=True, role=role, cybercity=cybercity)
    else:
        return render_template('attacker.html', game_finished=False, cybercity=cybercity)

@app.route('/defender', methods=['GET', 'POST'])
def defender_game():
    if request.method == 'POST':
        role = "defender"
        player_budget = budget['defender']
        player_actions = protection_actions
        player_template = 'defender.html'
        opponent_role = 'attacker'
        opponent_actions = hacking_actions
        opponent_template = 'attacker.html'

        n_locations = request.form.get("locations")
        if n_locations and n_locations.strip() != "":
            n_locations = int(n_locations.strip())

            for _ in range(n_locations):
                action = request.form.get("action")
                district = request.form.get("district")

                cost = int(player_budget * player_actions[action]["probability"])
                player_budget -= cost

                if action != "Turn Off Lights":
                    cybercity.turnOnLight(district)
                else:
                    cybercity.turnOffLight(district)

                cybercity.refresh()

                # Swap roles for the next iteration
                role, opponent_role = opponent_role, role
                player_budget, opponent_budget = budget[opponent_role], player_budget
                player_actions, opponent_actions = opponent_actions, player_actions
                player_template, opponent_template = opponent_template, player_template

        return render_template(player_template, game_finished=True, role=role, cybercity=cybercity)
    else:
        return render_template('defender.html', game_finished=False, cybercity=cybercity)

if __name__ == '__main__':
    app.run(debug=True)
