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


class HyperflexNodeConfigPolicyAllOf(object):
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
        'data_ip_range': 'HyperflexIpAddrRange',
        'hxdp_ip_range': 'HyperflexIpAddrRange',
        'mgmt_ip_range': 'HyperflexIpAddrRange',
        'node_name_prefix': 'str',
        'cluster_profiles': 'list[HyperflexClusterProfile]',
        'organization': 'OrganizationOrganization'
    }

    attribute_map = {
        'data_ip_range': 'DataIpRange',
        'hxdp_ip_range': 'HxdpIpRange',
        'mgmt_ip_range': 'MgmtIpRange',
        'node_name_prefix': 'NodeNamePrefix',
        'cluster_profiles': 'ClusterProfiles',
        'organization': 'Organization'
    }

    def __init__(self,
                 data_ip_range=None,
                 hxdp_ip_range=None,
                 mgmt_ip_range=None,
                 node_name_prefix=None,
                 cluster_profiles=None,
                 organization=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexNodeConfigPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_ip_range = None
        self._hxdp_ip_range = None
        self._mgmt_ip_range = None
        self._node_name_prefix = None
        self._cluster_profiles = None
        self._organization = None
        self.discriminator = None

        if data_ip_range is not None:
            self.data_ip_range = data_ip_range
        if hxdp_ip_range is not None:
            self.hxdp_ip_range = hxdp_ip_range
        if mgmt_ip_range is not None:
            self.mgmt_ip_range = mgmt_ip_range
        if node_name_prefix is not None:
            self.node_name_prefix = node_name_prefix
        if cluster_profiles is not None:
            self.cluster_profiles = cluster_profiles
        if organization is not None:
            self.organization = organization

    @property
    def data_ip_range(self):
        """Gets the data_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501


        :return: The data_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: HyperflexIpAddrRange
        """
        return self._data_ip_range

    @data_ip_range.setter
    def data_ip_range(self, data_ip_range):
        """Sets the data_ip_range of this HyperflexNodeConfigPolicyAllOf.


        :param data_ip_range: The data_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: HyperflexIpAddrRange
        """

        self._data_ip_range = data_ip_range

    @property
    def hxdp_ip_range(self):
        """Gets the hxdp_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501


        :return: The hxdp_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: HyperflexIpAddrRange
        """
        return self._hxdp_ip_range

    @hxdp_ip_range.setter
    def hxdp_ip_range(self, hxdp_ip_range):
        """Sets the hxdp_ip_range of this HyperflexNodeConfigPolicyAllOf.


        :param hxdp_ip_range: The hxdp_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: HyperflexIpAddrRange
        """

        self._hxdp_ip_range = hxdp_ip_range

    @property
    def mgmt_ip_range(self):
        """Gets the mgmt_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501


        :return: The mgmt_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: HyperflexIpAddrRange
        """
        return self._mgmt_ip_range

    @mgmt_ip_range.setter
    def mgmt_ip_range(self, mgmt_ip_range):
        """Sets the mgmt_ip_range of this HyperflexNodeConfigPolicyAllOf.


        :param mgmt_ip_range: The mgmt_ip_range of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: HyperflexIpAddrRange
        """

        self._mgmt_ip_range = mgmt_ip_range

    @property
    def node_name_prefix(self):
        """Gets the node_name_prefix of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501

        The node name prefix that is used to automatically generate the default hostname for each server.  A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60, must only contain alphanumeric characters or dash (-), and must start with an alphanumeric character.      # noqa: E501

        :return: The node_name_prefix of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._node_name_prefix

    @node_name_prefix.setter
    def node_name_prefix(self, node_name_prefix):
        """Sets the node_name_prefix of this HyperflexNodeConfigPolicyAllOf.

        The node name prefix that is used to automatically generate the default hostname for each server.  A dash (-) will be appended to the prefix followed by the node number to form a hostname. This default naming scheme can be manually overridden in the node configuration. The maximum length of a prefix is 60, must only contain alphanumeric characters or dash (-), and must start with an alphanumeric character.      # noqa: E501

        :param node_name_prefix: The node_name_prefix of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: str
        """

        self._node_name_prefix = node_name_prefix

    @property
    def cluster_profiles(self):
        """Gets the cluster_profiles of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :return: The cluster_profiles of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: list[HyperflexClusterProfile]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """Sets the cluster_profiles of this HyperflexNodeConfigPolicyAllOf.

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :param cluster_profiles: The cluster_profiles of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: list[HyperflexClusterProfile]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def organization(self):
        """Gets the organization of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501


        :return: The organization of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this HyperflexNodeConfigPolicyAllOf.


        :param organization: The organization of this HyperflexNodeConfigPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

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
        if not isinstance(other, HyperflexNodeConfigPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexNodeConfigPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
