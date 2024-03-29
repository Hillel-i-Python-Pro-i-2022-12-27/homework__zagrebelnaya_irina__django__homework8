from django.core.management import BaseCommand

from apps.middleware_requests_logging.models import HttpRequestsLog


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-all-logs",
            help="Delete all logging",
            action="store_true",
        )

    def handle(self, *args, **options):
        queryset = HttpRequestsLog.objects.all()
        total_deleted, details = queryset.delete()
