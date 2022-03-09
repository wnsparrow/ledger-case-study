import csv

from django.core.management.base import BaseCommand

from ...models import AutoPolicy


class Command(BaseCommand):
    help = "Load policy data"

    def add_arguments(self, parser):
        parser.add_argument(dest="file", help="the csv file to load from")
        parser.add_argument("--max", type=int, action="store", default=10000)

    def handle(self, *args, **options):
        csv_file = options["file"]
        max_count = options["max"]
        self.stdout.write("Loading {} policies from {}".format(max_count, csv_file))

        # clean out existing policy data
        AutoPolicy.objects.all().delete()

        with open(csv_file, "r") as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)

            count = 0
            for row in reader:
                AutoPolicy.objects.create(
                    year=row[0],
                    month=row[1],
                    driver_age=row[2],
                    driver_gender=row[3].lower(),
                    driver_employment=row[4].lower(),
                    driver_marital=row[5].lower(),
                    driver_location=row[6].lower(),
                    vehicle_age=row[7],
                    vehicle_model=row[8].lower(),
                    insurance_premium=row[9],
                    insurance_claims=row[10],
                    insurance_losses=row[11],
                )

                if count < max_count - 1:
                    count += 1
                else:
                    break

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully loaded {} auto policies".format(
                    AutoPolicy.objects.all().count()
                )
            )
        )
