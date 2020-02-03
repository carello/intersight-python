# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class FirmwareBaseDistributableAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bundle_type': 'str',
        'guid': 'str',
        'mdfid': 'str',
        'model': 'str',
        'platform_type': 'str',
        'recommended_build': 'str',
        'release_notes_url': 'str',
        'software_type_id': 'str',
        'supported_models': 'list[str]',
        'vendor': 'str'
    }

    attribute_map = {
        'bundle_type': 'BundleType',
        'guid': 'Guid',
        'mdfid': 'Mdfid',
        'model': 'Model',
        'platform_type': 'PlatformType',
        'recommended_build': 'RecommendedBuild',
        'release_notes_url': 'ReleaseNotesUrl',
        'software_type_id': 'SoftwareTypeId',
        'supported_models': 'SupportedModels',
        'vendor': 'Vendor'
    }

    def __init__(self,
                 bundle_type=None,
                 guid=None,
                 mdfid=None,
                 model=None,
                 platform_type=None,
                 recommended_build=None,
                 release_notes_url=None,
                 software_type_id=None,
                 supported_models=None,
                 vendor=None,
                 local_vars_configuration=None):  # noqa: E501
        """FirmwareBaseDistributableAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bundle_type = None
        self._guid = None
        self._mdfid = None
        self._model = None
        self._platform_type = None
        self._recommended_build = None
        self._release_notes_url = None
        self._software_type_id = None
        self._supported_models = None
        self._vendor = None
        self.discriminator = None

        if bundle_type is not None:
            self.bundle_type = bundle_type
        if guid is not None:
            self.guid = guid
        if mdfid is not None:
            self.mdfid = mdfid
        if model is not None:
            self.model = model
        if platform_type is not None:
            self.platform_type = platform_type
        if recommended_build is not None:
            self.recommended_build = recommended_build
        if release_notes_url is not None:
            self.release_notes_url = release_notes_url
        if software_type_id is not None:
            self.software_type_id = software_type_id
        if supported_models is not None:
            self.supported_models = supported_models
        if vendor is not None:
            self.vendor = vendor

    @property
    def bundle_type(self):
        """Gets the bundle_type of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The bundle type of the image, as published on cisco.com.    # noqa: E501

        :return: The bundle_type of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """Sets the bundle_type of this FirmwareBaseDistributableAllOf.

        The bundle type of the image, as published on cisco.com.    # noqa: E501

        :param bundle_type: The bundle_type of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._bundle_type = bundle_type

    @property
    def guid(self):
        """Gets the guid of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The unique identifier for an image in a Cisco repository.    # noqa: E501

        :return: The guid of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this FirmwareBaseDistributableAllOf.

        The unique identifier for an image in a Cisco repository.    # noqa: E501

        :param guid: The guid of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def mdfid(self):
        """Gets the mdfid of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The mdfid of the image provided by cisco.com.    # noqa: E501

        :return: The mdfid of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mdfid

    @mdfid.setter
    def mdfid(self, mdfid):
        """Sets the mdfid of this FirmwareBaseDistributableAllOf.

        The mdfid of the image provided by cisco.com.    # noqa: E501

        :param mdfid: The mdfid of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._mdfid = mdfid

    @property
    def model(self):
        """Gets the model of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The endpoint model for which this firmware image is applicable.     # noqa: E501

        :return: The model of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this FirmwareBaseDistributableAllOf.

        The endpoint model for which this firmware image is applicable.     # noqa: E501

        :param model: The model of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def platform_type(self):
        """Gets the platform_type of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The platform type of the image.    # noqa: E501

        :return: The platform_type of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this FirmwareBaseDistributableAllOf.

        The platform type of the image.    # noqa: E501

        :param platform_type: The platform_type of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._platform_type = platform_type

    @property
    def recommended_build(self):
        """Gets the recommended_build of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The build which is recommended by Cisco.    # noqa: E501

        :return: The recommended_build of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._recommended_build

    @recommended_build.setter
    def recommended_build(self, recommended_build):
        """Sets the recommended_build of this FirmwareBaseDistributableAllOf.

        The build which is recommended by Cisco.    # noqa: E501

        :param recommended_build: The recommended_build of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._recommended_build = recommended_build

    @property
    def release_notes_url(self):
        """Gets the release_notes_url of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The url for the release notes of this image.    # noqa: E501

        :return: The release_notes_url of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._release_notes_url

    @release_notes_url.setter
    def release_notes_url(self, release_notes_url):
        """Sets the release_notes_url of this FirmwareBaseDistributableAllOf.

        The url for the release notes of this image.    # noqa: E501

        :param release_notes_url: The release_notes_url of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._release_notes_url = release_notes_url

    @property
    def software_type_id(self):
        """Gets the software_type_id of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The software type id provided by cisco.com.    # noqa: E501

        :return: The software_type_id of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._software_type_id

    @software_type_id.setter
    def software_type_id(self, software_type_id):
        """Sets the software_type_id of this FirmwareBaseDistributableAllOf.

        The software type id provided by cisco.com.    # noqa: E501

        :param software_type_id: The software_type_id of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._software_type_id = software_type_id

    @property
    def supported_models(self):
        """Gets the supported_models of this FirmwareBaseDistributableAllOf.  # noqa: E501


        :return: The supported_models of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_models

    @supported_models.setter
    def supported_models(self, supported_models):
        """Sets the supported_models of this FirmwareBaseDistributableAllOf.


        :param supported_models: The supported_models of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: list[str]
        """

        self._supported_models = supported_models

    @property
    def vendor(self):
        """Gets the vendor of this FirmwareBaseDistributableAllOf.  # noqa: E501

        The vendor or publisher of this file.     # noqa: E501

        :return: The vendor of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this FirmwareBaseDistributableAllOf.

        The vendor or publisher of this file.     # noqa: E501

        :param vendor: The vendor of this FirmwareBaseDistributableAllOf.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FirmwareBaseDistributableAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirmwareBaseDistributableAllOf):
            return True

        return self.to_dict() != other.to_dict()