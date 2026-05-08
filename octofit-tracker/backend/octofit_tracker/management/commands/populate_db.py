from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from djongo import models

from pymongo import MongoClient

# Sample data
USERS = [
    {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
    {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
    {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "dc"},
    {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
    {"name": "Steve Rogers", "email": "captain@marvel.com", "team": "marvel"},
    {"name": "Peter Parker", "email": "spiderman@marvel.com", "team": "marvel"},
]

TEAMS = [
    {"name": "marvel"},
    {"name": "dc"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "fly", "duration": 60},
    {"user_email": "batman@dc.com", "activity": "train", "duration": 90},
    {"user_email": "ironman@marvel.com", "activity": "fly", "duration": 45},
]

LEADERBOARD = [
    {"team": "marvel", "points": 300},
    {"team": "dc", "points": 250},
]

WORKOUTS = [
    {"name": "Pushups", "difficulty": "easy"},
    {"name": "Flight", "difficulty": "super"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Unique index on email
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
