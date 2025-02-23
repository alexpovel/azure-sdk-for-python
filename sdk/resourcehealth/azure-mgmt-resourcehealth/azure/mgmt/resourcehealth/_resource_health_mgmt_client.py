# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import ResourceHealthMgmtClientConfiguration
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ResourceHealthMgmtClient(MultiApiClientMixin, _SDKClient):
    """The Resource Health Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2022-10-01'
    _PROFILE_TAG = "azure.mgmt.resourcehealth.ResourceHealthMgmtClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version: Optional[str]=None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles=KnownProfiles.default,
        **kwargs: Any
    ):
        self._config = ResourceHealthMgmtClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ResourceHealthMgmtClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-01-01: :mod:`v2015_01_01.models<azure.mgmt.resourcehealth.v2015_01_01.models>`
           * 2018-07-01: :mod:`v2018_07_01.models<azure.mgmt.resourcehealth.v2018_07_01.models>`
           * 2022-10-01: :mod:`v2022_10_01.models<azure.mgmt.resourcehealth.v2022_10_01.models>`
        """
        if api_version == '2015-01-01':
            from .v2015_01_01 import models
            return models
        elif api_version == '2018-07-01':
            from .v2018_07_01 import models
            return models
        elif api_version == '2022-10-01':
            from .v2022_10_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def availability_statuses(self):
        """Instance depends on the API version:

           * 2015-01-01: :class:`AvailabilityStatusesOperations<azure.mgmt.resourcehealth.v2015_01_01.operations.AvailabilityStatusesOperations>`
           * 2018-07-01: :class:`AvailabilityStatusesOperations<azure.mgmt.resourcehealth.v2018_07_01.operations.AvailabilityStatusesOperations>`
           * 2022-10-01: :class:`AvailabilityStatusesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.AvailabilityStatusesOperations>`
        """
        api_version = self._get_api_version('availability_statuses')
        if api_version == '2015-01-01':
            from .v2015_01_01.operations import AvailabilityStatusesOperations as OperationClass
        elif api_version == '2018-07-01':
            from .v2018_07_01.operations import AvailabilityStatusesOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import AvailabilityStatusesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'availability_statuses'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def child_availability_statuses(self):
        """Instance depends on the API version:

           * 2015-01-01: :class:`ChildAvailabilityStatusesOperations<azure.mgmt.resourcehealth.v2015_01_01.operations.ChildAvailabilityStatusesOperations>`
           * 2022-10-01: :class:`ChildAvailabilityStatusesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.ChildAvailabilityStatusesOperations>`
        """
        api_version = self._get_api_version('child_availability_statuses')
        if api_version == '2015-01-01':
            from .v2015_01_01.operations import ChildAvailabilityStatusesOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import ChildAvailabilityStatusesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'child_availability_statuses'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def child_resources(self):
        """Instance depends on the API version:

           * 2015-01-01: :class:`ChildResourcesOperations<azure.mgmt.resourcehealth.v2015_01_01.operations.ChildResourcesOperations>`
           * 2022-10-01: :class:`ChildResourcesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.ChildResourcesOperations>`
        """
        api_version = self._get_api_version('child_resources')
        if api_version == '2015-01-01':
            from .v2015_01_01.operations import ChildResourcesOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import ChildResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'child_resources'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def emerging_issues(self):
        """Instance depends on the API version:

           * 2018-07-01: :class:`EmergingIssuesOperations<azure.mgmt.resourcehealth.v2018_07_01.operations.EmergingIssuesOperations>`
           * 2022-10-01: :class:`EmergingIssuesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.EmergingIssuesOperations>`
        """
        api_version = self._get_api_version('emerging_issues')
        if api_version == '2018-07-01':
            from .v2018_07_01.operations import EmergingIssuesOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import EmergingIssuesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'emerging_issues'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def event(self):
        """Instance depends on the API version:

           * 2022-10-01: :class:`EventOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.EventOperations>`
        """
        api_version = self._get_api_version('event')
        if api_version == '2022-10-01':
            from .v2022_10_01.operations import EventOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'event'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def events(self):
        """Instance depends on the API version:

           * 2018-07-01: :class:`EventsOperations<azure.mgmt.resourcehealth.v2018_07_01.operations.EventsOperations>`
           * 2022-10-01: :class:`EventsOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.EventsOperations>`
        """
        api_version = self._get_api_version('events')
        if api_version == '2018-07-01':
            from .v2018_07_01.operations import EventsOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import EventsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'events'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def impacted_resources(self):
        """Instance depends on the API version:

           * 2022-10-01: :class:`ImpactedResourcesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.ImpactedResourcesOperations>`
        """
        api_version = self._get_api_version('impacted_resources')
        if api_version == '2022-10-01':
            from .v2022_10_01.operations import ImpactedResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'impacted_resources'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metadata(self):
        """Instance depends on the API version:

           * 2018-07-01: :class:`MetadataOperations<azure.mgmt.resourcehealth.v2018_07_01.operations.MetadataOperations>`
           * 2022-10-01: :class:`MetadataOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.MetadataOperations>`
        """
        api_version = self._get_api_version('metadata')
        if api_version == '2018-07-01':
            from .v2018_07_01.operations import MetadataOperations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import MetadataOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metadata'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-01-01: :class:`Operations<azure.mgmt.resourcehealth.v2015_01_01.operations.Operations>`
           * 2018-07-01: :class:`Operations<azure.mgmt.resourcehealth.v2018_07_01.operations.Operations>`
           * 2022-10-01: :class:`Operations<azure.mgmt.resourcehealth.v2022_10_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-01-01':
            from .v2015_01_01.operations import Operations as OperationClass
        elif api_version == '2018-07-01':
            from .v2018_07_01.operations import Operations as OperationClass
        elif api_version == '2022-10-01':
            from .v2022_10_01.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def security_advisory_impacted_resources(self):
        """Instance depends on the API version:

           * 2022-10-01: :class:`SecurityAdvisoryImpactedResourcesOperations<azure.mgmt.resourcehealth.v2022_10_01.operations.SecurityAdvisoryImpactedResourcesOperations>`
        """
        api_version = self._get_api_version('security_advisory_impacted_resources')
        if api_version == '2022-10-01':
            from .v2022_10_01.operations import SecurityAdvisoryImpactedResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'security_advisory_impacted_resources'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
