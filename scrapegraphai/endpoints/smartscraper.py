import time
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint


class SmartScraperEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the smart scraper endpoint.
        """
        def generator():
            for i in range(10):
                time.sleep(1)
                yield f"Smart scrape result {i} <br>"

        return Response(generator(), status=200, content_type="text/html")
