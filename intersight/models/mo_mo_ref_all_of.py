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


class MoMoRefAllOf(object):
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
    openapi_types = {'moid': 'str', 'object_type': 'str', 'selector': 'str'}

    attribute_map = {
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'selector': 'Selector'
    }

    def __init__(self,
                 moid=None,
                 object_type=None,
                 selector=None,
                 local_vars_configuration=None):  # noqa: E501
        """MoMoRefAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._moid = None
        self._object_type = None
        self._selector = None
        self.discriminator = None

        if moid is not None:
            self.moid = moid
        self.object_type = object_type
        if selector is not None:
            self.selector = selector

    @property
    def moid(self):
        """Gets the moid of this MoMoRefAllOf.  # noqa: E501

        The Moid of the referenced REST resource.    # noqa: E501

        :return: The moid of this MoMoRefAllOf.  # noqa: E501
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """Sets the moid of this MoMoRefAllOf.

        The Moid of the referenced REST resource.    # noqa: E501

        :param moid: The moid of this MoMoRefAllOf.  # noqa: E501
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """Gets the object_type of this MoMoRefAllOf.  # noqa: E501

        The Object Type of the referenced REST resource.    # noqa: E501

        :return: The object_type of this MoMoRefAllOf.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this MoMoRefAllOf.

        The Object Type of the referenced REST resource.    # noqa: E501

        :param object_type: The object_type of this MoMoRefAllOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_type is None:  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type`, must not be `None`"
            )  # noqa: E501

        self._object_type = object_type

    @property
    def selector(self):
        """Gets the selector of this MoMoRefAllOf.  # noqa: E501

        An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of 'moid' by clients. If 'moid' is set this field is ignored. If 'selector' is set and 'moid' is empty/absent from the request, Intersight will determine the Moid of the resource matching the filter expression and populate it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq '3AA8B7T11'.      # noqa: E501

        :return: The selector of this MoMoRefAllOf.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this MoMoRefAllOf.

        An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of 'moid' by clients. If 'moid' is set this field is ignored. If 'selector' is set and 'moid' is empty/absent from the request, Intersight will determine the Moid of the resource matching the filter expression and populate it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq '3AA8B7T11'.      # noqa: E501

        :param selector: The selector of this MoMoRefAllOf.  # noqa: E501
        :type: str
        """

        self._selector = selector

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
        if not isinstance(other, MoMoRefAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MoMoRefAllOf):
            return True

        return self.to_dict() != other.to_dict()
