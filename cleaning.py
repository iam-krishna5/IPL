import pandas as pd

# Load raw datasets (use raw string r"..." for Windows paths)
matches = pd.read_csv(r"E:\Desktop\Projects\IPL\matches (1) - matches (1).csv.csv")
deliveries = pd.read_csv(r"E:\Desktop\Projects\IPL\deliveries - deliveries.csv.csv")

# Standardize team names
team_name_map = {
    "Rising Pune Supergiant": "Rising Pune Supergiants",
    "Delhi Daredevils": "Delhi Capitals",
    "Deccan Chargers": "Sunrisers Hyderabad",
    "Kings XI Punjab": "Punjab Kings"
}
for col in ["team1", "team2", "toss_winner", "winner"]:
    matches[col] = matches[col].replace(team_name_map)

for col in ["batting_team", "bowling_team"]:
    deliveries[col] = deliveries[col].replace(team_name_map)

# Dates
matches["date"] = pd.to_datetime(matches["date"], errors="coerce")
matches["year"] = matches["date"].dt.year

# Derived flags
deliveries["is_legal_ball"] = deliveries.apply(
    lambda x: 0 if (x["wide_runs"] > 0 or x["noball_runs"] > 0) else 1, axis=1
)
deliveries["is_boundary_4"] = (deliveries["batsman_runs"] == 4).astype(int)
deliveries["is_boundary_6"] = (deliveries["batsman_runs"] == 6).astype(int)
deliveries["is_wicket"] = deliveries["player_dismissed"].notnull().astype(int)
bowler_dismissals = ["caught", "bowled", "lbw", "stumped", "caught and bowled", "hit wicket"]
deliveries["is_wicket_for_bowler"] = deliveries["dismissal_kind"].isin(bowler_dismissals).astype(int)

# Abandoned matches
matches["is_abandoned"] = matches["winner"].isnull().astype(int)

# Save cleaned CSVs
matches.to_csv(r"E:\Desktop\Projects\IPL\matches_clean.csv", index=False)
deliveries.to_csv(r"E:\Desktop\Projects\IPL\deliveries_clean.csv", index=False)

print("Cleaning done. Files saved as matches_clean.csv and deliveries_clean.csv")
print("Matches shape:", matches.shape, "Deliveries shape:", deliveries.shape)
