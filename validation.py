import pandas as pd

# Load cleaned datasets
matches = pd.read_csv(r"E:\Desktop\Projects\IPL\matches_clean.csv")
deliveries = pd.read_csv(r"E:\Desktop\Projects\IPL\deliveries_clean.csv")

print("\n--- VALIDATION REPORT ---")

# 1. Team names check
print("\n[Teams] Unique Teams (after cleaning):")
print(sorted(set(matches["team1"].unique()).union(set(matches["team2"].unique()))))

# 2. Abandoned matches check
abandoned_count = matches["is_abandoned"].sum()
print(f"\n[Matches] Number of abandoned/no-result matches: {abandoned_count}")

# 3. Boundary checks
print("\n[Boundaries] Total counts:")
print("Total 4s:", deliveries["is_boundary_4"].sum())
print("Total 6s:", deliveries["is_boundary_6"].sum())

# 4. Wicket checks
print("\n[Wickets] Summary:")
print("Total wickets (all kinds):", deliveries["is_wicket"].sum())
print("Wickets credited to bowler:", deliveries["is_wicket_for_bowler"].sum())

# 5. Sample deliveries with flags
print("\n[Sample Deliveries] First 15 rows with new flags:")
print(deliveries[["match_id", "over", "ball", "batsman", "bowler",
                  "batsman_runs", "dismissal_kind", 
                  "is_boundary_4", "is_boundary_6", 
                  "is_wicket", "is_wicket_for_bowler"]].head(15))

# 6. Match sample with new columns
print("\n[Sample Matches] First 10 rows with new columns:")
print(matches[["id", "season", "date", "team1", "team2", "winner", "is_abandoned", "year"]].head(10))
ṇ