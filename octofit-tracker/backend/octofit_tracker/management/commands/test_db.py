from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Test the MongoDB connection through djongo'

    def handle(self, *args, **kwargs):
        self.stdout.write('Testing database connection...')
        
        try:
            # Test Django's connection through djongo
            connection = connections['default']
            connection.ensure_connection()
            self.stdout.write(self.style.SUCCESS('Successfully connected to MongoDB through djongo!'))
            
            # Get database name from connection settings
            db_name = connection.settings_dict['NAME']
            self.stdout.write(f'Connected to database: {db_name}')
            
            # Test direct MongoDB connection
            client = MongoClient('mongodb://localhost:27017/')
            db = client[db_name]
            self.stdout.write('Database collections:')
            for collection in db.list_collection_names():
                self.stdout.write(f'- {collection}')
                
        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f'Could not connect to MongoDB: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
