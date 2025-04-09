# Test data for populating the octofit_db database

def get_test_data():
    return {
        "users": [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ],
        "teams": [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ],
        "activities": [
            {"user": "user1@example.com", "description": "Running 5km"},
            {"user": "user2@example.com", "description": "Cycling 10km"},
        ],
        "leaderboards": [
            {"team": "Team Alpha", "score": 100},
        ],
        "workouts": [
            {"name": "Morning Yoga"},
            {"name": "Evening Cardio"},
        ],
    }
