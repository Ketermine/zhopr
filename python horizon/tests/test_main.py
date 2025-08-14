import unittest
import sys
import os

# Add the application directory to the Python path
# This is a bit of a hack to handle the space in the directory name 'python horizon'
# A better solution would be to rename the directory, but we stick to the original structure.
sys.path.insert(0, os.path.abspath('python horizon'))

from main import filter_jobs

class TestFilterJobs(unittest.TestCase):

    def setUp(self):
        """Set up sample job data before each test."""
        self.sample_jobs = [
            {
                "id": "1",
                "title": "IT-Systemmanager",
                "company": "Tech Solutions GmbH",
                "job_type": ["Full-time", "Hybrid"],
                "salary_min": 75000,
            },
            {
                "id": "2",
                "title": "Systemadministrator",
                "company": "Innovate AG",
                "job_type": ["Full-time"],
                "salary_min": 60000,
            },
            {
                "id": "3",
                "title": "Junior IT Manager",
                "company": "DataCorp",
                "job_type": ["Full-time", "Remote"],
                "salary_min": 50000,
            },
            {
                "id": "4",
                "title": "Head of IT Systems",
                "company": "Global Networks",
                # This job intentionally has no job_type key
                "salary_min": 110000,
            }
        ]

    def test_no_filters(self):
        """Test that with no filters, all jobs are returned."""
        filtered = filter_jobs(self.sample_jobs, None, None, None)
        self.assertEqual(len(filtered), 4)

    def test_search_query_title(self):
        """Test filtering by a search query in the job title."""
        filtered = filter_jobs(self.sample_jobs, "manager", None, None)
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['id'], "1")
        self.assertEqual(filtered[1]['id'], "3")

    def test_search_query_company(self):
        """Test filtering by a search query in the company name."""
        filtered = filter_jobs(self.sample_jobs, "tech", None, None)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['id'], "1")

    def test_min_salary(self):
        """Test filtering by minimum salary."""
        filtered = filter_jobs(self.sample_jobs, None, 70000, None)
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['id'], "1")
        self.assertEqual(filtered[1]['id'], "4")

    def test_min_salary_invalid(self):
        """Test that invalid salary input is ignored."""
        filtered = filter_jobs(self.sample_jobs, None, "abc", None)
        self.assertEqual(len(filtered), 4)

    def test_job_type(self):
        """Test filtering by job type."""
        filtered = filter_jobs(self.sample_jobs, None, None, "Hybrid")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['id'], "1")

        filtered = filter_jobs(self.sample_jobs, None, None, "Full-time")
        self.assertEqual(len(filtered), 3)

        filtered = filter_jobs(self.sample_jobs, None, None, "Remote")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['id'], "3")

    def test_job_type_missing_key(self):
        """Test that filtering by job type doesn't fail with missing keys."""
        # This test implicitly checks that the loop doesn't crash on job 4
        filtered = filter_jobs(self.sample_jobs, None, None, "NonExistentType")
        self.assertEqual(len(filtered), 0)

    def test_combined_filters(self):
        """Test a combination of all filters."""
        filtered = filter_jobs(self.sample_jobs, "manager", 50000, "Full-time")
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['id'], "1")
        self.assertEqual(filtered[1]['id'], "3")

if __name__ == '__main__':
    unittest.main()
