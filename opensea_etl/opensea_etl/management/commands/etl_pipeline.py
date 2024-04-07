# In your_app/management/commands/rundailyetl.py
from datetime import datetime

from django.core.management.base import BaseCommand
from opensea_etl.utils import fetch_all_results, transform, load, write_dicts_to_csv


class Command(BaseCommand):
    help = 'Runs the ETL pipeline daily'

    def add_arguments(self, parser):
        parser.add_argument('--limit', type=int, default=50, help='Limit of records to be processed')

    def handle(self, *args, **options):
        limit = options['limit']

        # 1. Extract data
        data = fetch_all_results(limit=limit)

        # 2. Transform data
        transformed_data = transform(data)

        # 3. Load transformed data
        load(transformed_data)

        self.stdout.write(self.style.SUCCESS(f'{datetime.now()} ETL pipeline executed successfully for {limit} records.'))

# raw_records = fetch_all_results(300)
# transformed_data = utils.transform(raw_records)
# write_dicts_to_csv(transformed_data)
# load(transformed_data)
