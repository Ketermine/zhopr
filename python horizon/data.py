# data.py
# This module stores and manages the application's data.

# Mock data for IT System Manager jobs in Darmstadt
INITIAL_JOBS = [
    {
        "id": "1",
        "title": "IT-Systemmanager",
        "company": "Tech Solutions GmbH",
        "location": "Darmstadt",
        "salary_min": 75000,
        "salary_max": 95000,
        "experience": "Senior-Level",
        "job_type": ["Full-time", "Hybrid"],
        "posted_days_ago": 2,
        "company_logo": "https://via.placeholder.com/40",
        "company_employees": "501-1,000"
    },
    {
        "id": "2",
        "title": "Systemadministrator",
        "company": "Innovate AG",
        "location": "Darmstadt",
        "salary_min": 60000,
        "salary_max": 80000,
        "experience": "Mid-Level",
        "job_type": ["Full-time"],
        "posted_days_ago": 5,
        "company_logo": "https://via.placeholder.com/40",
        "company_employees": "1,001-5,000"
    },
    {
        "id": "3",
        "title": "Junior IT Manager",
        "company": "DataCorp",
        "location": "Darmstadt",
        "salary_min": 50000,
        "salary_max": 65000,
        "experience": "Entry-Level",
        "job_type": ["Full-time", "Remote"],
        "posted_days_ago": 10,
        "company_logo": "https://via.placeholder.com/40",
        "company_employees": "51-200"
    },
    {
        "id": "4",
        "title": "Head of IT Systems",
        "company": "Global Networks",
        "location": "Darmstadt",
        "salary_min": 110000,
        "salary_max": 140000,
        "experience": "Director",
        "job_type": ["Full-time", "Hybrid"],
        "posted_days_ago": 1,
        "company_logo": "https://via.placeholder.com/40",
        "company_employees": "10,000+"
    }
]

# Mock data for charts and activity feed
MOCK_INSIGHTS = {
    "salary_distribution": [
        {"range": "€40k-60k", "count": 12},
        {"range": "€60k-80k", "count": 25},
        {"range": "€80k-100k", "count": 18},
        {"range": "€100k-120k", "count": 8},
        {"range": "€120k+", "count": 5},
    ],
    "experience_distribution": [
        {"name": "Entry-Level", "value": 15},
        {"name": "Mid-Level", "value": 45},
        {"name": "Senior-Level", "value": 30},
        {"name": "Director", "value": 10},
    ],
    "salary_trend": [
        {"month": "Jan", "avg_salary": 85000},
        {"month": "Feb", "avg_salary": 86500},
        {"month": "Mar", "avg_salary": 87200},
        {"month": "Apr", "avg_salary": 88000},
        {"month": "May", "avg_salary": 89500},
        {"month": "Jun", "avg_salary": 91000},
    ]
}

MOCK_ACTIVITY = [
    {"user": "Anna Schmidt", "action": "applied for IT-Systemmanager", "timestamp": "2 hours ago"},
    {"user": "System", "action": "updated 3 new jobs from 'Innovate AG'", "timestamp": "5 hours ago"},
    {"user": "Max Müller", "action": "viewed Head of IT Systems", "timestamp": "1 day ago"},
]