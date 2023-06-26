import os

from mantium_spec.api.applications_api import ApplicationsApi
from mantium_client.api_client import MantiumClient


class MantiumApp:
    """
    Plugin to use Auto-GPT with Mantium.
    """
    def __init__(self):
        client_id = os.getenv('MANTIUM_CLIENT_ID')
        client_secret = os.getenv('MANTIUM_CLIENT_SECRET')

        self.client = MantiumClient(client_id=client_id, client_secret=client_secret)
        self.apps_api = ApplicationsApi(self.client)

    def get_applications(self):
        """Gets all applications available within Mantium."""
        return self.apps_api.list_applications()['items']

    def get_application_detail(self, app_id: str):
        """Grabs details from a single, specified application."""
        return self.apps_api.get_application_detail(app_id)

    def query_application(self, app_id: str, query: str) -> str:
        """Sends query to specific application and retrieves top-5 answers."""
        query_request = {'query': query}
        return self.apps_api.query_application(app_id, query_request)
