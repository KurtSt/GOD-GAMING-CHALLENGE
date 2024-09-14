import random

# Capped win rates for each game
win_rates = {
    "Bughouse Chess": min(64.00, 75.00) / 100,
    "Brawlhalla": min(62.96, 75.00) / 100,
    "Geoguessr": min(60.76, 75.00) / 100,
    "Mario Kart": min(70.59, 75.00) / 100,
    "Fortnite": min(17.65, 75.00) / 100,
    "Fall Guys": min(42.42, 75.00) / 100,
    "Rocket League": min(88.89, 75.00) / 100,
    "Halo": min(75.00, 75.00) / 100,
    "Valorant": min(100.00, 75.00) / 100,
    "League of Legends": min(44.44, 75.00) / 100,
    "Overwatch": min(66.67, 75.00) / 100
}

# Adjusted game times for these 10 games
game_times = {
    "Bughouse Chess": 5,
    "Brawlhalla": 5,
    "Geoguessr": 10,
    "Mario Kart": 10,
    "Fortnite": 25,
    "Fall Guys": 15,
    "Rocket League": 10,
    "Halo": 15,
    "Valorant": 30,
    "League of Legends": 30,
    "Overwatch": 15
}

# Function to simulate playing a game
def play_game(game_name, win_rate):
    return random.random() < win_rate

# Function to simulate playing all games, resetting on loss, with adjusted 80% Geoguessr and 20% Brawlhalla
def simulate_games():
    total_time = 0
    runs = 0

    while True:
        runs += 1
        for i, game in enumerate(["Bughouse Chess", "Brawlhalla/Geoguessr", "Mario Kart", "Fortnite", "Fall Guys",
                                  "Rocket League", "Halo", "Valorant", "League of Legends", "Overwatch"]):
            if game == "Brawlhalla/Geoguessr":
                # 80% chance of playing Geoguessr, 20% chance of playing Brawlhalla
                game = "Geoguessr" if random.random() < 0.8 else "Brawlhalla"
            
            win_rate = win_rates[game]
            game_time = game_times[game]

            # Play the current game
            total_time += game_time
            won = play_game(game, win_rate)

            if won:
                continue
            else:
                # Lost the game, reset
                break
        else:
            # All games won
            break

    return total_time, runs

# Function to simulate multiple runs and return results for every 100 steps
def run_multiple_simulations(n):
    results = []  # Store total time and runs for each simulation
    
    for _ in range(n):
        total_time, runs = simulate_games()
        results.append((total_time, runs))

    # Sort results by total time
    results.sort(key=lambda x: x[0])
    
    # Extract every 100th simulation (1st, 100th, 200th, ..., 900th)
    every_100th = [(i + 1, results[i]) for i in range(0, n, 1000)]
    
    return every_100th

# Run 1000 simulations and retrieve results for every 100 steps
every_100th_simulation = run_multiple_simulations(10000)

# Output the results
print("Simulation results for every 100 steps (time in minutes, runs):")
for step, (time, runs) in every_100th_simulation:
    print(f"{step}th simulation: Time: {time} minutes, Runs: {runs}")
