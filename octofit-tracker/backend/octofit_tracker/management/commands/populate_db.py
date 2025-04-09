from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='user1@example.com', name='User One')
        user2 = User.objects.create(email='user2@example.com', name='User Two')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, description='Running 5km')
        Activity.objects.create(user=user2, description='Cycling 10km')

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
