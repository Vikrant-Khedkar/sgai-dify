import time
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint
from scrapegraph_py import Client




class SearchScraperEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the search scraper endpoint.
        """
        def generator():
            client = Client(api_key=settings["api_key"])
            response = client.searchscraper(
                user_prompt=r["user_prompt"]
            )
            for result in response["results"]:
                time.sleep(1)
                yield f"{result['title']} <br>"

        return Response(generator(), status=200, content_type="text/html")