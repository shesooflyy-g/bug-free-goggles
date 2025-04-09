# Test data for populating the octofit_db database

def get_test_data():
    return {
        "users": [
            {"email": "student1@example.com", "name": "Student One"},
            {"email": "student2@example.com", "name": "Student Two"},
            {"email": "student3@example.com", "name": "Student Three"},
            {"email": "student4@example.com", "name": "Student Four"},
            {"email": "student5@example.com", "name": "Student Five"},
        ],
        "teams": [
            {"name": "Team Alpha", "members": ["student1@example.com", "student2@example.com"]},
            {"name": "Team Beta", "members": ["student3@example.com", "student4@example.com"]},
            {"name": "Team Gamma", "members": ["student5@example.com"]},
        ],
        "activities": [
            {"user": "student1@example.com", "description": "Ran 5km in 30 minutes"},
            {"user": "student2@example.com", "description": "Cycled 10km in 45 minutes"},
            {"user": "student3@example.com", "description": "Completed 1-hour yoga session"},
            {"user": "student4@example.com", "description": "Did 30 minutes of strength training"},
            {"user": "student5@example.com", "description": "Swam 20 laps in 40 minutes"},
        ],
        "leaderboards": [
            {"team": "Team Alpha", "score": 150},
            {"team": "Team Beta", "score": 120},
            {"team": "Team Gamma", "score": 100},
        ],
        "workouts": [
            {"name": "Morning Run", "description": "A 5km run to start the day"},
            {"name": "Cycling Session", "description": "A 10km cycling workout"},
            {"name": "Yoga Flow", "description": "A 1-hour yoga session for flexibility"},
            {"name": "Strength Training", "description": "A 30-minute strength workout"},
            {"name": "Swimming Laps", "description": "A 20-lap swimming session"},
        ],
    }
