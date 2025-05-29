import os
from pathlib import Path
import pandas as pd
from PIL import Image

import streamlit as st
from streamlit_option_menu import option_menu

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "testrp.jpg"
data_file = current_dir / "Merged_NFL_Data.csv"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Rob Pastori | Digital Resume & NFL Project"
PAGE_ICON = ":football:"
NAME = "Robert Pastori"

DESCRIPTION = "Data Analyst obsessed with Automation, and building dashboards (click arrow to find NFL Dashboard Project)"
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

# --- STREAMLIT SETTINGS ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

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
        options=["Rob's Digital Resume", "NFL Project"],
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
- 📊 Tableau, Power BI, Excel, Plotly
- 🗄️ Oracle, MySQL, MS Access
- 🤖 UiPath, Power Automate, n8n, Automation Anywhere
""")

    st.subheader("Work History")
    st.write("---")
    st.write("🚧 **Business Technical Liaison Senior Analyst | BNY Mellon – Pershing**")
    st.write("03/2022 - Present")
    st.write("""● Stakeholder Collaboration: Collaborated with Directors, Product Owners and end-users, leveraging 10+ years of
financial markets expertise to elicit comprehensive functional and data requirements, facilitating seamless technical
solution development.

● Data Transformation & Analysis: Expertly collected, synthesized, and transformed complex markets operations data
using Python scripting, ensuring data integrity and reliability for critical business insights.

● Automation & Efficiency: Developed and implemented daily automations, including a Python script to monitor
reports and a reconciliation process for vendor data, saving the firm hundreds of thousands of dollars by verifying fee
accuracy.

● Prompt Engineering: Leveraged AI to build innovative solutions for trading teams, directly contributing to increased
operational efficiency, reduced manual errors, and more precise business insights and reporting.

● RPA & Workflow Optimization: Designed and deployed UiPath Studio Pro robots and MS Power Automate flows
(using TypeScript), yielding hundreds of hours of time savings and significantly reducing data entry errors.

● Reporting & Visualization: Constructed sophisticated ad-hoc reports using SQL and Python, and created Power BI
visualizations from raw trade data, effectively presenting metrics from complex financial instruments to Directors.

● Technical Leadership: Served as the in-house MS Excel expert, building macros and custom pivot tables. Mentored
coworkers on advanced automation solutions and effectively communicate complex technical concepts to
non-technical stakeholders using flowcharts and diagrams.

● Issue Resolution: Independently drove initiatives, diagnosed complex issues, and implem
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

● Audit & Compliance: Led quarterly and yearly presentations on reporting procedures.
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
if selected == "NFL Project":
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
