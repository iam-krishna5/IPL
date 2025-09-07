🏏 IPL Analytics Dashboard
📌 Project Overview

This project analyzes Indian Premier League (IPL) data to uncover insights into batting, bowling, fielding, toss decisions, and venue performance.
The final deliverable is an interactive Power BI dashboard supported by Python-based preprocessing and KPI generation.

🔄 Workflow
1. Data Collection

Datasets:

matches.csv – match-level data (seasons, teams, toss, results).

deliveries.csv – ball-by-ball data (runs, wickets, players, dismissals).

2. Data Cleaning & Preparation

Standardized team, player, and venue names.

Handled missing values and corrected column data types.

Derived additional flags in deliveries:

is_legal_ball, is_boundary_4, is_boundary_6, is_wicket, is_fielding_dismis.

Exported cleaned datasets:

matches_clean.csv

deliveries_clean.csv

3. Data Modeling & KPI Definitions

Relationship built: matches_clean[id] (1) → deliveries_clean[match_id] (many).

KPIs created using DAX in Power BI:

Batting → Runs, Balls, Strike Rate, Average, Boundary %.

Bowling → Wickets, Economy Rate, Bowling Average, Strike Rate.

Team → Matches Won, Win %.

Toss Impact → Toss Decision Counts, Toss Win → Match Win %.

4. Dashboard Creation (Power BI)

Created a 6-page Power BI dashboard:

Executive Overview → Total matches, runs, wickets, wins by team, runs per season.

Batting Analysis → Top batsmen, strike rate vs average.

Bowling Analysis → Top bowlers, economy vs wickets.

Fielding Analysis → Top fielders by dismissals.

Toss & Outcome → Toss decisions, toss impact on match results.

Venue Insights → Matches by city, most successful team per venue.

5. Insights, Validation & Deliverables

Validation → Cross-checked runs & wickets between matches and deliveries.

Insights:

Identified top-performing batsmen & bowlers across seasons.

Assessed toss impact on winning probability.

Highlighted venues with highest match counts and team dominance.

Deliverables:

IPL_Dashboard.pbix (Power BI file)

Exported dashboards as PDF/PNG for reporting

Insight summary document

🛠️ Tech Stack

Python (Pandas, Matplotlib) → Data cleaning & KPI CSVs

Power BI → Data modeling, DAX measures, and dashboard creation

GitHub → Project version control & documentation

📂 Repository Structure
IPL-Analytics/
│── data/
│   ├── matches.csv
│   ├── deliveries.csv
│   ├── matches_clean.csv
│   ├── deliveries_clean.csv
│
│── modeling_csv/     # KPI outputs
│   ├── batting_kpis.csv
│   ├── bowling_kpis.csv
│   ├── fielding_kpis.csv
│   ├── team_kpis.csv
│   ├── toss_stats.csv
│   ├── city_matches.csv
│
│── scripts/
│   ├── cleaning.py
│   ├── kpi_modeling.py
│
│── dashboard/
│   ├── IPL_Dashboard.pbix
│   ├── Dashboard_Export.pdf
│
│── README.md

🚀 How to Run

Clone this repository

git clone https://github.com/your-username/IPL-Analytics.git
cd IPL-Analytics


Run preprocessing in Python

python scripts/cleaning.py
python scripts/kpi_modeling.py


Open Power BI file

Load matches_clean.csv & deliveries_clean.csv

Use pre-defined DAX measures for KPIs

Explore dashboards with slicers (Season, Team, Player, Venue).

📊 Final Output

✔️ Cleaned datasets
✔️ KPI CSVs (batting, bowling, fielding, teams, toss, venues)
✔️ Power BI Dashboard (6 pages)
✔️ Exported insights (PDF/PNG)
