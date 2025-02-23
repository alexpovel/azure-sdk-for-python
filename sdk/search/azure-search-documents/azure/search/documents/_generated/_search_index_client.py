# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from . import models as _models
from ._configuration import SearchIndexClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import DocumentsOperations


class SearchIndexClient:  # pylint: disable=client-accepts-api-version-keyword
    """Client that can be used to query an index and upload, merge, or delete documents.

    :ivar documents: DocumentsOperations operations
    :vartype documents: search_index_client.operations.DocumentsOperations
    :param endpoint: The endpoint URL of the search service. Required.
    :type endpoint: str
    :param index_name: The name of the index. Required.
    :type index_name: str
    :keyword api_version: Api Version. Default value is "2023-10-01-Preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, index_name: str, **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}/indexes('{indexName}')"
        self._config = SearchIndexClientConfiguration(endpoint=endpoint, index_name=index_name, **kwargs)
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.documents = DocumentsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, "str"),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "SearchIndexClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
