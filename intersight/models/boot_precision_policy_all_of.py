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


class BootPrecisionPolicyAllOf(object):
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
        'boot_devices': 'list[BootDeviceBase]',
        'configured_boot_mode': 'str',
        'enforce_uefi_secure_boot': 'bool',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'boot_devices': 'BootDevices',
        'configured_boot_mode': 'ConfiguredBootMode',
        'enforce_uefi_secure_boot': 'EnforceUefiSecureBoot',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 boot_devices=None,
                 configured_boot_mode='Legacy',
                 enforce_uefi_secure_boot=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """BootPrecisionPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._boot_devices = None
        self._configured_boot_mode = None
        self._enforce_uefi_secure_boot = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if boot_devices is not None:
            self.boot_devices = boot_devices
        if configured_boot_mode is not None:
            self.configured_boot_mode = configured_boot_mode
        if enforce_uefi_secure_boot is not None:
            self.enforce_uefi_secure_boot = enforce_uefi_secure_boot
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def boot_devices(self):
        """Gets the boot_devices of this BootPrecisionPolicyAllOf.  # noqa: E501


        :return: The boot_devices of this BootPrecisionPolicyAllOf.  # noqa: E501
        :rtype: list[BootDeviceBase]
        """
        return self._boot_devices

    @boot_devices.setter
    def boot_devices(self, boot_devices):
        """Sets the boot_devices of this BootPrecisionPolicyAllOf.


        :param boot_devices: The boot_devices of this BootPrecisionPolicyAllOf.  # noqa: E501
        :type: list[BootDeviceBase]
        """

        self._boot_devices = boot_devices

    @property
    def configured_boot_mode(self):
        """Gets the configured_boot_mode of this BootPrecisionPolicyAllOf.  # noqa: E501

        Sets the BIOS boot mode. UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme.    # noqa: E501

        :return: The configured_boot_mode of this BootPrecisionPolicyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._configured_boot_mode

    @configured_boot_mode.setter
    def configured_boot_mode(self, configured_boot_mode):
        """Sets the configured_boot_mode of this BootPrecisionPolicyAllOf.

        Sets the BIOS boot mode. UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme.    # noqa: E501

        :param configured_boot_mode: The configured_boot_mode of this BootPrecisionPolicyAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Legacy", "Uefi"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and configured_boot_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `configured_boot_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(configured_boot_mode, allowed_values))

        self._configured_boot_mode = configured_boot_mode

    @property
    def enforce_uefi_secure_boot(self):
        """Gets the enforce_uefi_secure_boot of this BootPrecisionPolicyAllOf.  # noqa: E501

        If UEFI secure boot is enabled, the boot mode is set to UEFI by default. Secure boot enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).     # noqa: E501

        :return: The enforce_uefi_secure_boot of this BootPrecisionPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_uefi_secure_boot

    @enforce_uefi_secure_boot.setter
    def enforce_uefi_secure_boot(self, enforce_uefi_secure_boot):
        """Sets the enforce_uefi_secure_boot of this BootPrecisionPolicyAllOf.

        If UEFI secure boot is enabled, the boot mode is set to UEFI by default. Secure boot enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).     # noqa: E501

        :param enforce_uefi_secure_boot: The enforce_uefi_secure_boot of this BootPrecisionPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enforce_uefi_secure_boot = enforce_uefi_secure_boot

    @property
    def organization(self):
        """Gets the organization of this BootPrecisionPolicyAllOf.  # noqa: E501


        :return: The organization of this BootPrecisionPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this BootPrecisionPolicyAllOf.


        :param organization: The organization of this BootPrecisionPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this BootPrecisionPolicyAllOf.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the profile objects that this policy is a part of.   # noqa: E501

        :return: The profiles of this BootPrecisionPolicyAllOf.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this BootPrecisionPolicyAllOf.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Reference to the profile objects that this policy is a part of.   # noqa: E501

        :param profiles: The profiles of this BootPrecisionPolicyAllOf.  # noqa: E501
        :type: list[PolicyAbstractConfigProfile]
        """

        self._profiles = profiles

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
        if not isinstance(other, BootPrecisionPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BootPrecisionPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()