import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Configure logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data for the OctoFit Tracker application'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Creating test data...')

            # Clear existing data
            self.stdout.write('Clearing existing data...')
            for user in User.objects.all():
                if user.pk is not None:
                    user.delete()
            for team in Team.objects.all():
                if team.pk is not None:
                    team.delete()
            for activity in Activity.objects.all():
                if activity.pk is not None:
                    activity.delete()
            for leaderboard in Leaderboard.objects.all():
                if leaderboard.pk is not None:
                    leaderboard.delete()
            for workout in Workout.objects.all():
                if workout.pk is not None:
                    workout.delete()

            # Create test users
            self.stdout.write('Creating test users...')
            users = [
                User.objects.create(email='sarah.smith@example.com', name='Sarah Smith'),
                User.objects.create(email='john.doe@example.com', name='John Doe'),
                User.objects.create(email='mary.johnson@example.com', name='Mary Johnson'),
                User.objects.create(email='mike.brown@example.com', name='Mike Brown'),
                User.objects.create(email='lisa.white@example.com', name='Lisa White')
            ]

            # Create test teams
            self.stdout.write('Creating test teams...')
            teams = [
                Team.objects.create(name='Fitness Warriors'),
                Team.objects.create(name='Health Heroes'),
                Team.objects.create(name='Wellness Champions')
            ]

            # Add members to teams
            teams[0].members.add(users[0], users[1])  # Fitness Warriors
            teams[1].members.add(users[2], users[3])  # Health Heroes
            teams[2].members.add(users[4], users[0])  # Wellness Champions

            # Create test workouts
            self.stdout.write('Creating test workouts...')
            workouts = [
                Workout.objects.create(
                    name='Morning HIIT',
                    description='High-intensity interval training with bodyweight exercises'
                ),
                Workout.objects.create(
                    name='Strength Training',
                    description='Full body strength workout with weights'
                ),
                Workout.objects.create(
                    name='Yoga Flow',
                    description='60-minute vinyasa flow yoga session'
                ),
                Workout.objects.create(
                    name='Cardio Blast',
                    description='30-minute intensive cardio workout'
                ),
                Workout.objects.create(
                    name='Core Power',
                    description='Core strengthening and stability exercises'
                )
            ]

            # Create test activities
            self.stdout.write('Creating test activities...')
            activities = [
                Activity.objects.create(
                    user=users[0],
                    description='Completed Morning HIIT workout - 300 calories burned'
                ),
                Activity.objects.create(
                    user=users[1],
                    description='5km run in the park - 400 calories burned'
                ),
                Activity.objects.create(
                    user=users[2],
                    description='1-hour yoga session - 200 calories burned'
                ),
                Activity.objects.create(
                    user=users[3],
                    description='Strength training - 45 minutes, 250 calories burned'
                ),
                Activity.objects.create(
                    user=users[4],
                    description='Swimming - 30 laps, 400 calories burned'
                )
            ]

            # Create test leaderboard entries
            self.stdout.write('Creating test leaderboard entries...')
            leaderboard_entries = [
                Leaderboard.objects.create(team=teams[0], score=850),  # Fitness Warriors
                Leaderboard.objects.create(team=teams[1], score=720),  # Health Heroes
                Leaderboard.objects.create(team=teams[2], score=680)   # Wellness Champions
            ]

            self.stdout.write(self.style.SUCCESS('Successfully created test data!'))
        except Exception as e:
            logger.error(f"Error while populating the database: {e}")
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
