import random
import pandas as pd

n = int(input("Enter the number of grids: "))
print(f"The game will be played on a {n}x{n} grid.")


def generate_random_nums():
    """Generates random number for dice roll from 1-6"""
    return random.randint(1, 6)


def play_game_until_winner(n):
    """Simulates the game until one player reaches n*n"""
    max_position = n * n
    players = {
        "Player 1": {"position": 0, "dice_rolls": [], "position_history": []},
        "Player 2": {"position": 0, "dice_rolls": [], "position_history": []},
        "Player 3": {"position": 0, "dice_rolls": [], "position_history": []},
        "Player 4": {"position": 0, "dice_rolls": [], "position_history": []},
    }

    winner_found = False

    while not winner_found:
        for player_name in players:
            roll = generate_random_nums()
            players[player_name]["dice_rolls"].append(roll)

            # Update position only if it doesn't exceed max
            new_position = players[player_name]["position"] + roll
            if new_position <= max_position:
                players[player_name]["position"] = new_position

            players[player_name]["position_history"].append(
                players[player_name]["position"]
            )
            if players[player_name]["position"] >= max_position:
                winner_found = True
                break

    data = []
    for player_name in players:
        win_status = 1 if players[player_name]["position"] >= max_position else 0
        data.append(
            {
                "Players": player_name,
                "Dice Roll History": ",".join(
                    map(str, players[player_name]["dice_rolls"])
                ),
                "Position History": ",".join(
                    map(str, players[player_name]["position_history"])
                ),
                "Win Status": win_status,
            }
        )

    df = pd.DataFrame(data)
    df.to_excel("game_results.xlsx", index=False)
    return df


if __name__ == "__main__":
    print(f"Grid Size: {n}")
    result_df = play_game_until_winner(n)
    print(result_df.to_string(index=False))
