# CSS2026
chpc assignments

# Researcher Profile - Streamlit App

A professional research profile showcase built with Streamlit.

## Features
- Multi-page navigation with sidebar
- Publication showcase with filtering
- Research project details
- Interactive metrics and charts
- Academic timeline
- Contact form
- Responsive design

## Deployment to Streamlit Cloud

1. **Create a GitHub repository** with these files:
   - `app.py` (main application)
   - `requirements.txt` (dependencies)
   - `style.css` (optional custom styles)
   - `README.md` (this file)

2. **requirements.txt:**

streamlit==1.28.0
pandas==2.0.3
plotly==5.17.0


3. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Set main file path to `app.py`
   - Click "Deploy"

## Customization

Replace placeholder data with your actual:
- Research information
- Publications
- Projects
- Contact details
- Images and links

## Local Development

```bash
pip install -r requirements.txt
streamlit run app.py
```


## 4. Quick Setup for Deployment

Create these three files in a folder:

1. **`app.py`** - The main app (copy the full code above)
2. **`requirements.txt`** - Dependencies:
```txt
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
