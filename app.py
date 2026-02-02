import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import base64

# Page configuration
st.set_page_config(
    page_title="Researcher Profile",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Try to load custom CSS
try:
    local_css("style.css")
except:
    # Default styles if CSS file doesn't exist
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        padding-bottom: 1rem;
        border-bottom: 3px solid #3B82F6;
    }
    .section-header {
        font-size: 1.8rem;
        color: #1E40AF;
        margin-top: 2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #60A5FA;
    }
    .card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3B82F6;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .publication-item {
        background-color: white;
        border-left: 4px solid #3B82F6;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/test-tube.png", width=80)
    st.title("Navigation")
    
    page = st.radio(
        "Go to",
        ["🏠 Overview", "📚 Publications", "🔬 Projects", "📊 Metrics", "📅 Timeline", "👤 About", "📞 Contact"]
    )
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    
    # Example metrics in sidebar
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Citations", "1,234", "+15%")
    with col2:
        st.metric("h-index", "18", "+2")
    
    st.markdown("---")
    st.markdown("### Connect")
    st.markdown("""
    [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white)](https://scholar.google.com)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/KID-AFTERMATH)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kamogelo-monyela-8b5918130/)
    [![ORCID](https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org)
    """, unsafe_allow_html=True)

# Home/Overview Page
if page == "🏠 Overview":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://scontent-jnb2-1.xx.fbcdn.net/v/t39.30808-6/504180479_9439854786119847_7570720266593999856_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeGb5SKuh_tILRrDUzb7IsDoJcuWFjBOfYQly5YWME59hF14s7A54_cAb27gF8cY2c2GtOQD5Vl5bY07qUyepMei&_nc_ohc=DrpL07k3dO4Q7kNvwEIdquN&_nc_oc=AdkLjxcm5qj_hx8YckStiusfsyvwmrUvTYrIkhEkB5H3gaxpL69g-QDK1lAToRfUpO0&_nc_zt=23&_nc_ht=scontent-jnb2-1.xx&_nc_gid=r90qNwJjWoV_7FAKZmGHZQ&oh=00_AfsDDPXgMHtSdGehT1cBmLq0pAruFAtZP52zpsxOXhhq0g&oe=698607FA", 
                 caption="Mr MK Monyela", use_column_width=True)
        
        st.markdown("""
        ### Mr. MK Monyela
        **Associate  of Data Science and Programming**
        
        Department of Computer Science  
        University of Limpopo  
        📧 202009016@myturf.ul.ac.za
        📍 608,Dan village,Tzaneen 
        """)
    
    with col2:
        st.markdown('<div class="main-header">Research Profile</div>', unsafe_allow_html=True)
        
        st.markdown("""
        Welcome to my research profile! I am a **AData Analytics and Programmer** who explores 
        cutting-edge techniques in machine learning, computational statistics, and their applications 
        in healthcare and environmental science.
        
        I also Programme websites, apps and game. my focus languages are JS, python, html5 and php 
        """)
        
        # Key research areas
        st.markdown('<div class="section-header">Research Focus Areas</div>', unsafe_allow_html=True)
        
        research_cols = st.columns(3)
        research_areas = [
            ("🤖", "Explainable AI", "Developing transparent machine learning models"),
            ("🏥", "Healthcare Analytics", "AI applications in medical diagnosis"),
            ("🌍", "Climate Modeling", "Predictive models for environmental science"),
            ("📊", "Statistical Learning", "Advanced statistical methods for big data"),
            ("🔍", "Anomaly Detection", "Identifying patterns in complex systems"),
            ("⚡", "Real-time Analytics", "Streaming data processing and analysis")
        ]
        
        for i, (icon, title, desc) in enumerate(research_areas):
            with research_cols[i % 3]:
                with st.container():
                    st.markdown(f"""
                    <div class="card">
                    <h4>{icon} {title}</h4>
                    <p>{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)

# Publications Page
elif page == "📚 Publications":
    st.markdown('<div class="main-header">Publications</div>', unsafe_allow_html=True)
    
    # Publication categories
    pub_categories = st.multiselect(
        "Filter by category:",
        ["All", "Journal Articles", "Conference Papers", "Book Chapters", "Preprints", "Patents"],
        default=["All"]
    )
    
    # Sample publication data
    publications = [
        {
            "title": " ",
            "authors": " ",
            "venue": " ",
            "type": " ",
            "citations": 0,
            "link": " "
        },
        {
            "title": " ",
            "authors": " ",
            "venue": " ",
            "type": " ",
            "citations": 0,
            "link": " "
        },
        {
            "title": " ",
            "authors": " ",
            "venue": " ",
            "type": " ",
            "citations": 0,
            "link": " "
        },
        {
            "title": " ",
            "authors": " ",
            "venue": " ",
            "type": " ",
            "citations": 0,
            "link": " "
        },
        {
            "title": " ",
            "authors": " ",
            "venue": " ",
            "type": " ",
            "citations": 0,
            "link": " "
        },
    ]
    
    # Filter publications
    if "All" not in pub_categories:
        publications = [p for p in publications if p["type"] in pub_categories]
    
    # Display publications
    for i, pub in enumerate(publications):
        with st.container():
            st.markdown(f"""
            <div class="publication-item">
                <h4>{i+1}. {pub['title']}</h4>
                <p><strong>Authors:</strong> {pub['authors']}</p>
                <p><strong>Published in:</strong> {pub['venue']}</p>
                <p><strong>Citations:</strong> {pub['citations']} | <strong>Type:</strong> {pub['type']}</p>
                <a href="{pub['link']}" target="_blank">📄 Read Paper</a>
            </div>
            """, unsafe_allow_html=True)

# Projects Page
elif page == "🔬 Projects":
    st.markdown('<div class="main-header">Research Projects</div>', unsafe_allow_html=True)
    
    # Current projects
    st.markdown('<div class="section-header">🚀 Active Projects</div>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "AI-Assisted Early Disease Detection",
            "funding": "NIH Grant - $2.1M",
            "duration": "2022-2025",
            "team": "8 researchers",
            "description": "Developing deep learning models for early detection of neurological disorders from medical imaging data."
        },
        {
            "title": "Climate Change Impact Analysis",
            "funding": "NSF Grant - $1.5M",
            "duration": "2023-2026",
            "team": "6 researchers",
            "description": "Building predictive models to assess climate change impacts on coastal ecosystems using satellite data."
        },
        {
            "title": "Fairness in Algorithmic Decision Making",
            "funding": "Industry Partnership - $800K",
            "duration": "2023-2024",
            "team": "4 researchers",
            "description": "Developing frameworks to ensure fairness and transparency in automated decision systems."
        }
    ]
    
    for project in projects:
        with st.expander(f"**{project['title']}** ({project['duration']})"):
            st.markdown(f"""
            **Funding:** {project['funding']}  
            **Team Size:** {project['team']}  
            **Description:** {project['description']}
            
            **Key Objectives:**
            - Develop robust AI models with 95%+ accuracy
            - Create open-source tools for the research community
            - Publish in top-tier conferences and journals
            """)
            
            # Progress bar
            progress = st.slider(f"Progress on {project['title']}", 0, 100, 65, key=f"prog_{project['title']}")
            st.progress(progress)

# Metrics Page
elif page == "📊 Metrics":
    st.markdown('<div class="main-header">Research Metrics</div>', unsafe_allow_html=True)
    
    # Metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card"><h3>1,234</h3><p>Total Citations</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card"><h3>18</h3><p>h-index</p></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card"><h3>45</h3><p>Publications</p></div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card"><h3>12</h3><p>Research Grants</p></div>', unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Citations Over Time")
        # Sample citation data
        years = list(range(2015, 2024))
        citations = [10, 25, 45, 80, 120, 200, 350, 600, 1234]
        
        fig = go.Figure(data=go.Scatter(x=years, y=citations, mode='lines+markers', 
                                        line=dict(width=4, color='#3B82F6')))
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Publication Types")
        pub_types = ['Journal Articles', 'Conference Papers', 'Book Chapters', 'Others']
        counts = [25, 15, 3, 2]
        
        fig = px.pie(values=counts, names=pub_types, 
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)

# Timeline Page
elif page == "📅 Timeline":
    st.markdown('<div class="main-header">Academic Timeline</div>', unsafe_allow_html=True)
    
    # Timeline data
    timeline_data = [
        {"year": "2020-Present", "title": "Associate Professor", "institution": "University of Technology", "description": "Leading research in AI and data science"},
        {"year": "2016-2020", "title": "Assistant Professor", "institution": "State University", "description": "Established research lab, secured first major grants"},
        {"year": "2014-2016", "title": "Postdoctoral Fellow", "institution": "MIT", "description": "Research in computational statistics"},
        {"year": "2010-2014", "title": "Ph.D. Computer Science", "institution": "Stanford University", "description": "Thesis: 'Advanced ML for Healthcare'"},
        {"year": "2006-2010", "title": "B.S. Computer Science", "institution": "UC Berkeley", "description": "Summa Cum Laude"}
    ]
    
    for event in timeline_data:
        with st.container():
            st.markdown(f"""
            <div style='border-left: 3px solid #3B82F6; padding-left: 20px; margin: 20px 0;'>
                <h4>{event['year']}</h4>
                <h3>{event['title']}</h3>
                <p><strong>{event['institution']}</strong></p>
                <p>{event['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# About Page
elif page == "👤 About":
    st.markdown('<div class="main-header">About Me</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Biography
        
        I am a AData Analytics and Programmer who explores cutting-edge techniques in machine learning, computational statistics, and their applications in healthcare and environmental science.
        
        I also Programme websites, apps and game. my focus languages are JS, python, html5 and php.
        
        ### Education
        - **BSc. in Computer Science**, University of Limpopo (2026)
        - **Diploma in Cyber Security**, Oxford Home Study Center (2023)
        
        ### Awards & Honors
        - Huawei cloud-track (2023)
        - Coding fundamentals II (2020)
        - Coding fundamentals I (2020)
        - MIT NSC (2014)
        
        ### Professional Service
        - software development
        - python games
        - Web designs
        """)
    
    with col2:
        st.markdown("### Skills & Expertise")
        
        skills = {
            "Machine Learning": 95,
            "Deep Learning": 90,
            "Statistical Analysis": 88,
            "Python Programming": 92,
            "Data Visualization": 85,
            "Research Mentoring": 90
        }
        
        for skill, level in skills.items():
            st.markdown(f"**{skill}**")
            st.progress(level/100)
            st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### Languages")
        st.markdown("""
        - English (Native)
        - Spanish (Professional)
        - Mandarin (Conversational)
        """)

# Contact Page
elif page == "📞 Contact":
    st.markdown('<div class="main-header">Contact & Collaboration</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ## Get In Touch
        
        I'm always open to discussing research collaborations, student supervision, 
        or speaking opportunities.
        
        **Office Address:**  
        608, Dan Village
        next to Dan clinic, Tzaneen
        Letaba
        0870
        
        **Email:** 202009016@myturf.ul.ac.za  
        **Phone:** (+27) 852-1734  
        **Office Hours:** Mon/Fri 9AM - 4 PM
        
        ### Prospective Students
        I'm currently looking for work In hopes to improve my knowledge. Please Email me when you require my CV or assistance.
        """)
    
    with col2:
        st.markdown("### Send a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            affiliation = st.text_input("Affiliation")
            subject = st.selectbox(
                "Subject",
                ["Research Collaboration", "Speaking Engagement", "Student Supervision", "Other"]
            )
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Message sent! I'll get back to you within 2-3 business days.")
        
        st.markdown("---")
        st.markdown("### Calendar")
        st.info("Schedule a meeting: [Calendly Link](https://calendly.com)")
        st.markdown("""
        **Note:** For urgent matters, please email with "[URGENT]" in the subject line.
        """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Last Updated:** January 2026")

with col2:
    st.markdown("**© 2026 Mr. Kamogelo Monyela**")

