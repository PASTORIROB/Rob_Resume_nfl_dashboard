import os
from pathlib import Path
import pandas as pd
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

#PAGE_TITLE = "Rob Pastori" # Assuming you have these defined elsewhere
#PAGE_ICON = "📊" # Assuming you have these defined elsewhere

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rob Pastori | Digital Resume & NFL Project & Portfolio VAR Calculator"
PAGE_ICON = ":football:"
# --- THIS MUST BE THE FIRST STREAMLIT COMMAND ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
# --- STREAMLIT SETTINGS ---
#st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
def inject_ga():
    # Your Google Analytics Measurement ID (starts with 'G-')
    GA_MEASUREMENT_ID = "G-WLP3VDCMGF" # Replace with your actual ID
    """Injects Google Analytics Gtag script into the Streamlit app."""
    GA_CODE = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_MEASUREMENT_ID}');
    </script>
    """
    components.html(GA_CODE, height=0, width=0) # height and width 0 make it invisible

# Call the function at the beginning of your Streamlit app script
inject_ga()
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "testrp.jpg"
data_file = current_dir / "Merged_NFL_Data.csv"


NAME = "Robert Pastori"

DESCRIPTION = "Problem solver at heart—specializing in data analytics, automation, and building tools that save time and uncover value"
EMAIL = "PastoriRob@gmail.com"

# --- SOCIAL MEDIA ---
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rpastori/",
    "GitHub": "https://github.com/PASTORIROB",
}

PROJECTS = {
    "🏆 FINRA Series 7": "https://brokercheck.finra.org/individual/summary/6603334",
    "🏆 MBA from University of Central Florida": "https://ucf.edu",
    "🏆 Finance BS from University of Central Florida": "https://ucf.edu",
}



with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- NAVIGATION ---
with st.sidebar:
    st.markdown("""
        <style>
        .sidebar-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #FF5733;
            padding-bottom: 10px;
        }
        .option-menu .nav-link.active {
            background-color: #FF5733 !important;
            color: white !important;
        }
        .option-menu .nav-link {
            font-weight: bold;
            font-size: 1.1em;
            padding: 0.75em 1em;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-title">🔀 Navigate</div>', unsafe_allow_html=True)

    selected = option_menu(
        menu_title="",
        options=["Rob's Digital Resume", "NFL Project - 2024 Stats","Portfolio VAR Calculator"],
        icons=["person-badge-fill", "bar-chart-line-fill"],
        menu_icon="cast",
        default_index=0
    )

# --- RESUME PAGE ---
if selected == "Rob's Digital Resume":
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    st.write("\n")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write("""
- ✔️ 13 Years of experience in Finance
- ✔️ Strong hands-on coding experience with Python, UiPath, Tableau, Power BI and VBA
- ✔️ Excellent communicator with both tech and non-tech teams
""")

    st.subheader("Hard Skills")
    st.write("""
- 👨‍💻 Python, SQL, VBA, TypeScript
- 📊 Tableau, Power BI, Plotly
- 🗄️ Oracle, MySQL, PostgreSQL, MS Access
- 🤖 UiPath, Power Automate, n8n, Automation Anywhere
- 💻 MS Excel, MS Power Query, MS Access, MS Visual Studio Code, MS SharePoint, MS Visio, MS PowerPoint, MS Teams
- 📌 JIRA, Confluence, Agile, Waterfall, Sharepoint, Miro
""")

    st.subheader("Work History")
    st.write("---")
    st.write("🚧 **Business Technical Liaison Senior Analyst | BNY Mellon – Pershing**")
    st.write("03/2022 - Present")
    st.write("""● Stakeholder Collaboration: Collaborated with Directors, Product Owners, and end-users drawing upon over a
decade of financial markets expertise to identify comprehensive functional and data requirements. This collaboration
facilitated seamless technical solution development.

● Reporting and Visualization: Utilized SQL and other ETL tools to develop sophisticated ad-hoc reports from raw trade
data. Subsequently, these reports were transformed into daily refreshable Tableau/Power BI visualizations, effectively
presenting key metrics to Directors.

● Data Transformation & Analysis: Expertly curated, synthesized, and transformed intricate market operations data
through Python scripting, guaranteeing data integrity and reliability for pivotal business insights.

● Automation and Efficiency: Developed and implemented business-critical automations that enabled the Compliance
team to meet stringent deadlines.

● RPA & Workflow Optimization: Designed and deployed UiPath Studio Pro robots and MS Power Automate flows
yielding hundreds of hours of time savings and significantly reducing data entry errors.

● Technical Leadership: Served as the in-house MS Excel expert, building macros and custom pivot tables. Mentored
coworkers on advanced automation solutions and effectively communicate complex technical concepts to
non-technical stakeholders using flowcharts and diagrams.

● Issue Resolution: Independently drove initiatives, diagnosed complex issues, and implemented effective resolution
strategies, maintaining robust data frameworks and ensuring completion of objectives.

● Prompt Engineering: Leveraged AI to build innovative solutions for trading teams, directly contributing to increased
operational efficiency, reduced manual errors, and more precise business insights and reporting.
""")

    st.write("\n")
    st.write("🚧 **Operations Analyst | Cowen Inc.**")
    st.write("04/2017 - 03/2022")
    st.write("""
● Process Automation & Reporting: Programmed and automated a daily dashboard for Managing Directors and the
COO, providing a clear, real-time view of firm-wide breaks and their resolution.

● Global Team Leadership: Managed a global team of analysts responsible for reconciling hundreds of accounts,
ensuring accuracy and accountability for auditor-identified flaws.

● Financial Data Expertise: Applied extensive experience in Payments (Swift - MT, FIX messages, ACH formats) and
Securities messages, contributing to the development of key performance indicators (KPIs) for insightful reporting.

● Trade Processing & Reconciliation: Proficiently utilized the Broadridge system for end-to-end DTC settlements, trade
processing, matching, and reconciliation, ensuring accuracy and timeliness.

● Data Optimization: Constructed macros to optimize datasets for efficient upload, meticulously reconciling shares and
cash related to DTC CNS via the PNS account.

● Audit & Compliance: Led quarterly and yearly presentations on reporting procedures and results to both internal and
external auditors, demonstrating strong communication and compliance adherence.
""")

    st.write("\n")
    st.write("🚧 **Operations Associate | Convergex Execution Services**")
    st.write("01/2018 - 02/2022")
    st.write(""" ●System Optimization: Transformed a completely manual back-office reconciliation system by implementing
automations and advanced MS Excel functions, significantly improving efficiency.

● Complex Reconciliation: Reconciled 950 cash statements with internal data across over 150 foreign and domestic
markets, resolving intricate trade issues with settlement, middle office, stock loan, and treasury teams.

● Adaptability & Problem Solving: Successfully navigated two order management system transitions, reconfiguring
daily workflows and effectively explaining cash and equity breaks to auditors during audits.

""")

    st.subheader("Projects & Accomplishments")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

# --- NFL DASHBOARD PAGE ---
if selected == "NFL Project - 2024 Stats":
    import plotly.express as px

    df = pd.read_csv(data_file)
    df[["PF", "Yds_x", "W", "Cmp_y", "Att_y", "Yds", "Sk", "Int_y"]] = df[["PF", "Yds_x", "W", "Cmp_y", "Att_y", "Yds", "Sk", "Int_y"]].apply(pd.to_numeric, errors='coerce')

    division_mapping = {
        'Buffalo Bills': 'AFC East', 'Miami Dolphins': 'AFC East', 'New England Patriots': 'AFC East', 'New York Jets': 'AFC East',
        'Cincinnati Bengals': 'AFC North', 'Cleveland Browns': 'AFC North', 'Baltimore Ravens': 'AFC North', 'Pittsburgh Steelers': 'AFC North',
        'Houston Texans': 'AFC South', 'Indianapolis Colts': 'AFC South', 'Jacksonville Jaguars': 'AFC South', 'Tennessee Titans': 'AFC South',
        'Denver Broncos': 'AFC West', 'Kansas City Chiefs': 'AFC West', 'Las Vegas Raiders': 'AFC West', 'Los Angeles Chargers': 'AFC West',
        'Dallas Cowboys': 'NFC East', 'New York Giants': 'NFC East', 'Philadelphia Eagles': 'NFC East', 'Washington Commanders': 'NFC East',
        'Chicago Bears': 'NFC North', 'Detroit Lions': 'NFC North', 'Green Bay Packers': 'NFC North', 'Minnesota Vikings': 'NFC North',
        'Atlanta Falcons': 'NFC South', 'Carolina Panthers': 'NFC South', 'New Orleans Saints': 'NFC South', 'Tampa Bay Buccaneers': 'NFC South',
        'Arizona Cardinals': 'NFC West', 'Los Angeles Rams': 'NFC West', 'San Francisco 49ers': 'NFC West', 'Seattle Seahawks': 'NFC West'
    }

    df["Division"] = df["Team"].map(division_mapping)

    selected_division = st.selectbox("Select Division:", ["All Divisions"] + sorted(df['Division'].dropna().unique()))
    filtered_df = df if selected_division == "All Divisions" else df[df['Division'] == selected_division]

    fig1 = px.scatter(filtered_df, x="Yds_x", y="PF", text="Team", color="Team",
                      title="Total Yards vs Points For",
                      labels={"Yds_x": "Total Yards", "PF": "Points For"})

    fig2 = px.bar(filtered_df, x="Team", y="W", title="Wins per Team")

    fig3 = px.scatter(filtered_df, x="Cmp_y", y="Yds", size="Att_y", color="Team", text="Team",
                      title="Passing Completions vs Passing Yards",
                      labels={"Cmp_y": "Completions", "Yds": "Passing Yards", "Att_y": "Attempts"})

    fig4 = px.bar(filtered_df.sort_values('Sk', ascending=True), y="Team", x="Sk", orientation='h',
                  title="Sacks per Team (Horizontal Bar)", color="Sk", color_continuous_scale="Reds")

    fig5 = px.scatter(filtered_df.sort_values('Int_y', ascending=False), x="Team", y="Int_y", size="Int_y",
                      title="Interceptions per Team (Bubble Style)", color="Team")

    st.plotly_chart(fig3)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)

    st.markdown("""
    <div style='font-size:0.8em; color:#666; text-align:center; margin-top:30px;'>
        Data courtesy of <a href=\"https://www.pro-football-reference.com/years/2024/#site_menu_link\" target=\"_blank\">Sports Reference</a>
    </div>
    """, unsafe_allow_html=True)



# --- Portfolio VAR Calculator ---
if selected == "Portfolio VAR Calculator":
    import yfinance as yf
    import numpy as np
    from scipy.stats import norm
    
    import plotly.graph_objects as go


    st.title("📉 Rob Pastori's Portfolio Value at Risk (VaR) Calculator")
    st.write("Simulate potential portfolio losses using Monte Carlo simulations.")

    def get_stock_data(tickers, start_date, end_date):
        stock_data = pd.DataFrame()
        for ticker in tickers:
            data = yf.download(ticker, start=start_date, end=end_date)
            stock_data[ticker] = data['Close']
        return stock_data

    def calculate_returns(stock_data):
        returns = stock_data.pct_change().dropna()
        return returns

    def monte_carlo_simulation_paths(returns, num_simulations, time_horizon, weights, portfolio_value, volatility_multiplier=1.0):
        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        cov_matrix *= volatility_multiplier 
        num_assets = len(returns.columns)

        dt = 1
        mean_matrix = np.full((time_horizon, num_assets), mean_returns.values)
        chol_cov_matrix = np.linalg.cholesky(cov_matrix)

        simulation_paths = []
        final_returns = []
        for _ in range(num_simulations):
            Z = np.random.normal(size=(time_horizon, num_assets))
            correlated_randomness = Z @ chol_cov_matrix.T
            returns_path = mean_matrix + correlated_randomness
            portfolio_returns = returns_path @ weights
            portfolio_values = [portfolio_value]
            for r in portfolio_returns:
                portfolio_values.append(portfolio_values[-1] * (1 + r))
            simulation_paths.append(portfolio_values[1:])
            final_returns.append((portfolio_values[-1] - portfolio_value) / portfolio_value)

        final_returns = np.array(final_returns)
        var = np.percentile(final_returns, 5)
        cvar = np.mean(final_returns[final_returns <= var])

        return np.array(simulation_paths), final_returns * portfolio_value, var * portfolio_value, cvar * portfolio_value

    tickers = st.text_input("Enter stock tickers separated by commas (e.g., AAPL,MSFT,GOOGL):", "SPY,NVDA,PLTR,PEP,AAPL,MSFT,GOOGL,META,HOOD,BK")
    tickers = [ticker.strip().upper() for ticker in tickers.split(",") if ticker.strip()]

    start_date = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("2025-01-01"))
    num_simulations = st.number_input("Number of Monte Carlo Simulations", min_value=10, max_value=1000, value=100, step=10)
    time_horizon = st.number_input("Simulation Days", min_value=1, max_value=252, value=30, step=1)
    portfolio_value = st.number_input("Portfolio Value ($)", min_value=1000, value=10000, step=500)
    volatility_multiplier = st.slider("Volatility Multiplier", 0.5, 5.0, 1.0, step=0.1)
    st.subheader("Portfolio Allocation (%)")
    weights = []
    total_weight = 0
    for ticker in tickers:
        weight = st.slider(f"{ticker} Allocation %", 0, 100, 100 // len(tickers))
        weights.append(weight / 100)
        total_weight += weight

    if total_weight != 100:
        st.error("Total allocation must sum to 100%.")
    elif st.button("Run Monte Carlo Simulations"):
        stock_data = get_stock_data(tickers, start_date, end_date)
        returns = calculate_returns(stock_data)
        sim_paths, final_cash_changes, var_cash, cvar_cash = monte_carlo_simulation_paths(
            returns, num_simulations, time_horizon, np.array(weights), portfolio_value
        )

        # Chart 1: Stacked line chart of all simulations
        fig1 = go.Figure()
        for i in range(min(200, num_simulations)):
            fig1.add_trace(go.Scatter(
                y=sim_paths[i],
                mode='lines',
                line=dict(width=1),
                name=f"Sim {i+1}",
                showlegend=False
            ))

        fig1.update_layout(
            title="Monte Carlo Simulated Portfolio Value Paths",
            xaxis_title="Days",
            yaxis_title="Portfolio Value ($)",
            showlegend=False
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Chart 2: Histogram of ending values
        fig2 = go.Figure()
        fig2.add_trace(go.Histogram(
            x=final_cash_changes,
            nbinsx=100,
            marker_color="lightskyblue",
            name="Final Portfolio Changes"
        ))
        fig2.add_vline(x=var_cash, line=dict(color="red", dash="dash"), name="VaR")
        fig2.add_vline(x=cvar_cash, line=dict(color="orange", dash="dash"), name="CVaR")

        fig2.update_layout(
            title="Histogram of Ending Portfolio Value Changes",
            xaxis_title="Change in Portfolio Value ($)",
            yaxis_title="Frequency",
            showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.success(f"💸 Value at Risk (VaR): -${abs(var_cash):,.2f}")
        st.warning(f"📉 Conditional VaR (CVaR): -${abs(cvar_cash):,.2f}")

