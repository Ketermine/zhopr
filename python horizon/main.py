# main.py
from flask import Flask, render_template, request
from data import INITIAL_JOBS, MOCK_INSIGHTS, MOCK_ACTIVITY
from components.charts import (
    create_salary_distribution_chart,
    create_experience_distribution_chart,
    create_salary_trend_chart
)
import pandas as pd

app = Flask(__name__)

def filter_jobs(jobs, search_query, min_salary, job_type):
    """Filters a list of jobs based on criteria."""
    filtered = jobs

    if search_query:
        query = search_query.lower()
        filtered = [
            job for job in filtered 
            if query in job['title'].lower() or query in job['company'].lower()
        ]

    if min_salary:
        try:
            min_salary = int(min_salary)
            filtered = [job for job in filtered if job['salary_min'] >= min_salary]
        except ValueError:
            pass 

    if job_type:
        filtered = [
            job for job in filtered if job_type in job.get('job_type', [])
        ]
        
    return filtered

@app.route('/')
def dashboard():
    search_query = request.args.get('search')
    min_salary = request.args.get('min_salary')
    job_type = request.args.get('job_type')

    filtered_jobs = filter_jobs(INITIAL_JOBS, search_query, min_salary, job_type)
    
    # Convert filtered jobs to a DataFrame for Plotly
    jobs_df = pd.DataFrame(filtered_jobs)
    
    # Generate charts from the filtered DataFrame
    salary_dist_chart = create_salary_distribution_chart(jobs_df)
    exp_dist_chart = create_experience_distribution_chart(jobs_df)
    # Salary trend remains from mock data as it's a general trend
    salary_trend_chart = create_salary_trend_chart(MOCK_INSIGHTS['salary_trend'])
    
    return render_template(
        'index.html',
        jobs=filtered_jobs,
        activities=MOCK_ACTIVITY,
        salary_dist_chart=salary_dist_chart,
        exp_dist_chart=exp_dist_chart,
        salary_trend_chart=salary_trend_chart,
        job_count=len(filtered_jobs),
        search_query=search_query,
        min_salary=min_salary,
        job_type=job_type
    )

if __name__ == '__main__':
    app.run(debug=True)