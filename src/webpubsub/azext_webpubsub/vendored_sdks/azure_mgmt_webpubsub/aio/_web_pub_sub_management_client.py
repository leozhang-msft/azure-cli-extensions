# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING
from typing_extensions import Self

from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import WebPubSubManagementClientConfiguration
from .operations import (
    Operations,
    UsagesOperations,
    WebPubSubCustomCertificatesOperations,
    WebPubSubCustomDomainsOperations,
    WebPubSubHubsOperations,
    WebPubSubOperations,
    WebPubSubPrivateEndpointConnectionsOperations,
    WebPubSubPrivateLinkResourcesOperations,
    WebPubSubReplicaSharedPrivateLinkResourcesOperations,
    WebPubSubReplicasOperations,
    WebPubSubSharedPrivateLinkResourcesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class WebPubSubManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """REST API for Azure WebPubSub Service.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.webpubsub.aio.operations.Operations
    :ivar web_pub_sub: WebPubSubOperations operations
    :vartype web_pub_sub: azure.mgmt.webpubsub.aio.operations.WebPubSubOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.webpubsub.aio.operations.UsagesOperations
    :ivar web_pub_sub_custom_certificates: WebPubSubCustomCertificatesOperations operations
    :vartype web_pub_sub_custom_certificates:
     azure.mgmt.webpubsub.aio.operations.WebPubSubCustomCertificatesOperations
    :ivar web_pub_sub_custom_domains: WebPubSubCustomDomainsOperations operations
    :vartype web_pub_sub_custom_domains:
     azure.mgmt.webpubsub.aio.operations.WebPubSubCustomDomainsOperations
    :ivar web_pub_sub_hubs: WebPubSubHubsOperations operations
    :vartype web_pub_sub_hubs: azure.mgmt.webpubsub.aio.operations.WebPubSubHubsOperations
    :ivar web_pub_sub_private_endpoint_connections: WebPubSubPrivateEndpointConnectionsOperations
     operations
    :vartype web_pub_sub_private_endpoint_connections:
     azure.mgmt.webpubsub.aio.operations.WebPubSubPrivateEndpointConnectionsOperations
    :ivar web_pub_sub_private_link_resources: WebPubSubPrivateLinkResourcesOperations operations
    :vartype web_pub_sub_private_link_resources:
     azure.mgmt.webpubsub.aio.operations.WebPubSubPrivateLinkResourcesOperations
    :ivar web_pub_sub_replicas: WebPubSubReplicasOperations operations
    :vartype web_pub_sub_replicas: azure.mgmt.webpubsub.aio.operations.WebPubSubReplicasOperations
    :ivar web_pub_sub_replica_shared_private_link_resources:
     WebPubSubReplicaSharedPrivateLinkResourcesOperations operations
    :vartype web_pub_sub_replica_shared_private_link_resources:
     azure.mgmt.webpubsub.aio.operations.WebPubSubReplicaSharedPrivateLinkResourcesOperations
    :ivar web_pub_sub_shared_private_link_resources: WebPubSubSharedPrivateLinkResourcesOperations
     operations
    :vartype web_pub_sub_shared_private_link_resources:
     azure.mgmt.webpubsub.aio.operations.WebPubSubSharedPrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-03-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = WebPubSubManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                AsyncARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub = WebPubSubOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_custom_certificates = WebPubSubCustomCertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_custom_domains = WebPubSubCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_hubs = WebPubSubHubsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_private_endpoint_connections = WebPubSubPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_private_link_resources = WebPubSubPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_replicas = WebPubSubReplicasOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_replica_shared_private_link_resources = WebPubSubReplicaSharedPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.web_pub_sub_shared_private_link_resources = WebPubSubSharedPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
