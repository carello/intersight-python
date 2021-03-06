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


class NtpPolicyAllOf(object):
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
        'enabled': 'bool',
        'ntp_servers': 'list[str]',
        'appliance_account': 'IamAccount',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'enabled': 'Enabled',
        'ntp_servers': 'NtpServers',
        'appliance_account': 'ApplianceAccount',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 enabled=None,
                 ntp_servers=None,
                 appliance_account=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """NtpPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._ntp_servers = None
        self._appliance_account = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if appliance_account is not None:
            self.appliance_account = appliance_account
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def enabled(self):
        """Gets the enabled of this NtpPolicyAllOf.  # noqa: E501

        State of NTP service on the endpoint.    # noqa: E501

        :return: The enabled of this NtpPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NtpPolicyAllOf.

        State of NTP service on the endpoint.    # noqa: E501

        :param enabled: The enabled of this NtpPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this NtpPolicyAllOf.  # noqa: E501


        :return: The ntp_servers of this NtpPolicyAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this NtpPolicyAllOf.


        :param ntp_servers: The ntp_servers of this NtpPolicyAllOf.  # noqa: E501
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def appliance_account(self):
        """Gets the appliance_account of this NtpPolicyAllOf.  # noqa: E501


        :return: The appliance_account of this NtpPolicyAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._appliance_account

    @appliance_account.setter
    def appliance_account(self, appliance_account):
        """Sets the appliance_account of this NtpPolicyAllOf.


        :param appliance_account: The appliance_account of this NtpPolicyAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._appliance_account = appliance_account

    @property
    def organization(self):
        """Gets the organization of this NtpPolicyAllOf.  # noqa: E501


        :return: The organization of this NtpPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this NtpPolicyAllOf.


        :param organization: The organization of this NtpPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this NtpPolicyAllOf.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile objects.   # noqa: E501

        :return: The profiles of this NtpPolicyAllOf.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this NtpPolicyAllOf.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile objects.   # noqa: E501

        :param profiles: The profiles of this NtpPolicyAllOf.  # noqa: E501
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
        if not isinstance(other, NtpPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NtpPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
