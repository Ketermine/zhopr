# components/charts.py
import plotly.express as px
import pandas as pd

def create_salary_distribution_chart(df):
    """Generates a dynamic bar chart for salary distribution from a DataFrame."""
    if df.empty:
        return "<p>No salary data for this selection.</p>"
    
    bins = [40000, 60000, 80000, 100000, 120000, float('inf')]
    labels = ["€40k-60k", "€60k-80k", "€80k-100k", "€100k-120k", "€120k+"]
    df['salary_range'] = pd.cut(df['salary_min'], bins=bins, labels=labels, right=False)
    
    data = df['salary_range'].value_counts().reset_index()
    data.columns = ['range', 'count']
    
    fig = px.bar(data, x='range', y='count', labels={'range': 'Salary Range', 'count': 'Number of Jobs'}, title="Salary Distribution")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def create_experience_distribution_chart(df):
    """Generates a dynamic pie chart for experience level distribution."""
    if df.empty:
        return "<p>No experience data for this selection.</p>"
        
    data = df['experience'].value_counts().reset_index()
    data.columns = ['name', 'value']
    
    fig = px.pie(data, names='name', values='value', title="Experience Level", hole=.3)
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)')
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def create_salary_trend_chart(data):
    """Generates a static line chart for salary trends (using mock data)."""
    # This chart remains static as it represents a general market trend, not a filtered result.
    df = pd.DataFrame(data)
    fig = px.line(df, x='month', y='avg_salary', labels={'month': 'Month', 'avg_salary': 'Average Salary (€)'}, title="Average Salary Trend")
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig.to_html(full_html=False, include_plotlyjs='cdn')