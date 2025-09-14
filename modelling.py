import pandas as pd
import os

# ---------------- LOAD CLEANED DATA ---------------- #
matches = pd.read_csv("E:\\Desktop\\Projects\\IPL\\matches_clean.csv")
deliveries = pd.read_csv("E:\\Desktop\\Projects\\IPL\\deliveries_clean.csv")

# ---------------- OUTPUT DIRECTORY ---------------- #
output_dir = "E:\\Desktop\\Projects\\IPL\\modeling_csv"
os.makedirs(output_dir, exist_ok=True)

# =====================================================
# 1. BATSMAN KPIs
# =====================================================
batting = deliveries.groupby("batsman").agg(
    runs_scored=("batsman_runs", "sum"),
    balls_faced=("is_legal_ball", "sum"),
    fours=("is_boundary_4", "sum"),
    sixes=("is_boundary_6", "sum"),
    dismissals=("is_wicket", "sum")
).reset_index()

batting["average"] = batting["runs_scored"] / batting["dismissals"].replace(0, pd.NA)
batting["strike_rate"] = (batting["runs_scored"] / batting["balls_faced"]) * 100
batting["boundary_runs"] = batting["fours"]*4 + batting["sixes"]*6
batting["boundary_pct"] = (batting["boundary_runs"] / batting["runs_scored"]) * 100

top_batsmen = batting.sort_values(by="runs_scored", ascending=False).head(10)
print("\n--- BATTING KPIs (Top 10 by Runs) ---")
print(top_batsmen)

batting.to_csv(os.path.join(output_dir, "batting_kpis.csv"), index=False)

# =====================================================
# 2. BOWLING KPIs
# =====================================================
bowling = deliveries.groupby("bowler").agg(
    balls_bowled=("is_legal_ball", "sum"),
    runs_conceded=("total_runs", "sum"),
    wickets=("is_wicket_for_bowler", "sum")
).reset_index()

bowling["overs_bowled"] = bowling["balls_bowled"] // 6 + (bowling["balls_bowled"] % 6) / 6
bowling["economy_rate"] = bowling["runs_conceded"] / (bowling["balls_bowled"] / 6)
bowling["bowling_avg"] = bowling["runs_conceded"] / bowling["wickets"].replace(0, pd.NA)
bowling["strike_rate"] = bowling["balls_bowled"] / bowling["wickets"].replace(0, pd.NA)

top_bowlers = bowling.sort_values(by="wickets", ascending=False).head(10)
print("\n--- BOWLING KPIs (Top 10 by Wickets) ---")
print(top_bowlers)

bowling.to_csv(os.path.join(output_dir, "bowling_kpis.csv"), index=False)

# =====================================================
# 3. FIELDING KPIs
# =====================================================
fielding = deliveries[deliveries["fielder"].notna()].groupby("fielder").agg(
    catches=("dismissal_kind", lambda x: (x == "caught").sum()),
    runouts=("dismissal_kind", lambda x: (x == "run out").sum()),
    stumpings=("dismissal_kind", lambda x: (x == "stumped").sum())
).reset_index()

fielding["total_dismissals"] = fielding["catches"] + fielding["runouts"] + fielding["stumpings"]

top_fielders = fielding.sort_values(by="total_dismissals", ascending=False).head(10)
print("\n--- FIELDING KPIs (Top 10 by Dismissals) ---")
print(top_fielders)

fielding.to_csv(os.path.join(output_dir, "fielding_kpis.csv"), index=False)

# =====================================================
# 4. TEAM KPIs
# =====================================================
team_stats = matches.groupby("winner").agg(
    matches_won=("winner", "count")
).reset_index().rename(columns={"winner": "team"})

total_matches = matches.groupby("team1").size() + matches.groupby("team2").size()
team_stats["matches_played"] = team_stats["team"].map(total_matches)
team_stats["win_percentage"] = (team_stats["matches_won"] / team_stats["matches_played"]) * 100

top_teams = team_stats.sort_values(by="matches_won", ascending=False).head(10)
print("\n--- TEAM KPIs (Top 10 by Wins) ---")
print(top_teams)

team_stats.to_csv(os.path.join(output_dir, "team_kpis.csv"), index=False)

# =====================================================
# 5. EXTRA AGGREGATIONS FROM PROJECT BRIEF
# =====================================================

# --- Most Sixes (Players) ---
most_sixes_players = batting.sort_values(by="sixes", ascending=False).head(10)
print("\n--- MOST SIXES (Players) ---")
print(most_sixes_players[["batsman", "sixes"]])
most_sixes_players.to_csv(os.path.join(output_dir, "most_sixes_players.csv"), index=False)

# --- Most Fours (Players) ---
most_fours_players = batting.sort_values(by="fours", ascending=False).head(10)
print("\n--- MOST FOURS (Players) ---")
print(most_fours_players[["batsman", "fours"]])
most_fours_players.to_csv(os.path.join(output_dir, "most_fours_players.csv"), index=False)

# --- Most Sixes & Fours (Teams) ---
team_boundaries = deliveries.groupby("batting_team").agg(
    total_sixes=("is_boundary_6", "sum"),
    total_fours=("is_boundary_4", "sum")
).reset_index()
print("\n--- TEAM BOUNDARIES (Sixes & Fours) ---")
print(team_boundaries.sort_values(by="total_sixes", ascending=False).head(5))
team_boundaries.to_csv(os.path.join(output_dir, "team_boundaries.csv"), index=False)

# --- Toss Analysis ---
toss_stats = matches.groupby("toss_decision").size().reset_index(name="count")
toss_outcome = (matches["toss_winner"] == matches["winner"]).mean() * 100

print("\n--- TOSS DECISION COUNTS ---")
print(toss_stats)
print(f"\n--- TOSS -> MATCH WIN PERCENTAGE: {toss_outcome:.2f}% ---")

toss_stats.to_csv(os.path.join(output_dir, "toss_stats.csv"), index=False)

# --- Matches hosted by City ---
city_matches = matches["city"].value_counts().reset_index()
city_matches.columns = ["city", "matches"]
print("\n--- MATCHES HOSTED BY CITY ---")
print(city_matches.head(10))
city_matches.to_csv(os.path.join(output_dir, "city_matches.csv"), index=False)

print(f"\n All CSVs saved in: {output_dir}")
