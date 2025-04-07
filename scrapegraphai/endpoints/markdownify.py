import time
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint
from scrapegraph_py import Client


class MarkdownifyEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the markdownify endpoint.
        """
        def generator():
            client = Client(api_key=settings["api_key"])
            response = client.markdownify(
                website_url=r["website_url"]
            )
            for result in response["results"]:
                time.sleep(1)
                yield f"{result['title']} <br>"

        return Response(generator(), status=200, content_type="text/html")
