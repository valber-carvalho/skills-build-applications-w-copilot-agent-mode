from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="marvel")
        self.assertEqual(user.name, "Test User")

    def test_team_creation(self):
        team = Team.objects.create(name="marvel")
        self.assertEqual(team.name, "marvel")

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email="test@example.com", activity="run", duration=30)
        self.assertEqual(activity.activity, "run")

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team="marvel", points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", difficulty="easy")
        self.assertEqual(workout.name, "Pushups")
