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


class AdapterHostFcInterfaceAllOf(object):
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
        'admin_state': 'str',
        'ep_dn': 'str',
        'host_fc_interface_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'original_wwnn': 'str',
        'original_wwpn': 'str',
        'peer_dn': 'str',
        'wwnn': 'str',
        'wwpn': 'str',
        'adapter_unit': 'AdapterUnit',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'admin_state': 'AdminState',
        'ep_dn': 'EpDn',
        'host_fc_interface_id': 'HostFcInterfaceId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'original_wwnn': 'OriginalWwnn',
        'original_wwpn': 'OriginalWwpn',
        'peer_dn': 'PeerDn',
        'wwnn': 'Wwnn',
        'wwpn': 'Wwpn',
        'adapter_unit': 'AdapterUnit',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 admin_state=None,
                 ep_dn=None,
                 host_fc_interface_id=None,
                 name=None,
                 oper_state=None,
                 operability=None,
                 original_wwnn=None,
                 original_wwpn=None,
                 peer_dn=None,
                 wwnn=None,
                 wwpn=None,
                 adapter_unit=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """AdapterHostFcInterfaceAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_state = None
        self._ep_dn = None
        self._host_fc_interface_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._original_wwnn = None
        self._original_wwpn = None
        self._peer_dn = None
        self._wwnn = None
        self._wwpn = None
        self._adapter_unit = None
        self._registered_device = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if ep_dn is not None:
            self.ep_dn = ep_dn
        if host_fc_interface_id is not None:
            self.host_fc_interface_id = host_fc_interface_id
        if name is not None:
            self.name = name
        if oper_state is not None:
            self.oper_state = oper_state
        if operability is not None:
            self.operability = operability
        if original_wwnn is not None:
            self.original_wwnn = original_wwnn
        if original_wwpn is not None:
            self.original_wwpn = original_wwpn
        if peer_dn is not None:
            self.peer_dn = peer_dn
        if wwnn is not None:
            self.wwnn = wwnn
        if wwpn is not None:
            self.wwpn = wwpn
        if adapter_unit is not None:
            self.adapter_unit = adapter_unit
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def admin_state(self):
        """Gets the admin_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The admin_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this AdapterHostFcInterfaceAllOf.


        :param admin_state: The admin_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._admin_state = admin_state

    @property
    def ep_dn(self):
        """Gets the ep_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The ep_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ep_dn

    @ep_dn.setter
    def ep_dn(self, ep_dn):
        """Sets the ep_dn of this AdapterHostFcInterfaceAllOf.


        :param ep_dn: The ep_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._ep_dn = ep_dn

    @property
    def host_fc_interface_id(self):
        """Gets the host_fc_interface_id of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The host_fc_interface_id of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: int
        """
        return self._host_fc_interface_id

    @host_fc_interface_id.setter
    def host_fc_interface_id(self, host_fc_interface_id):
        """Sets the host_fc_interface_id of this AdapterHostFcInterfaceAllOf.


        :param host_fc_interface_id: The host_fc_interface_id of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: int
        """

        self._host_fc_interface_id = host_fc_interface_id

    @property
    def name(self):
        """Gets the name of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The name of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdapterHostFcInterfaceAllOf.


        :param name: The name of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """Gets the oper_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The oper_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this AdapterHostFcInterfaceAllOf.


        :param oper_state: The oper_state of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """Gets the operability of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The operability of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """Sets the operability of this AdapterHostFcInterfaceAllOf.


        :param operability: The operability of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._operability = operability

    @property
    def original_wwnn(self):
        """Gets the original_wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The original_wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._original_wwnn

    @original_wwnn.setter
    def original_wwnn(self, original_wwnn):
        """Sets the original_wwnn of this AdapterHostFcInterfaceAllOf.


        :param original_wwnn: The original_wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._original_wwnn = original_wwnn

    @property
    def original_wwpn(self):
        """Gets the original_wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The original_wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._original_wwpn

    @original_wwpn.setter
    def original_wwpn(self, original_wwpn):
        """Sets the original_wwpn of this AdapterHostFcInterfaceAllOf.


        :param original_wwpn: The original_wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._original_wwpn = original_wwpn

    @property
    def peer_dn(self):
        """Gets the peer_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The peer_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._peer_dn

    @peer_dn.setter
    def peer_dn(self, peer_dn):
        """Sets the peer_dn of this AdapterHostFcInterfaceAllOf.


        :param peer_dn: The peer_dn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._peer_dn = peer_dn

    @property
    def wwnn(self):
        """Gets the wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this AdapterHostFcInterfaceAllOf.


        :param wwnn: The wwnn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """Gets the wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """Sets the wwpn of this AdapterHostFcInterfaceAllOf.


        :param wwpn: The wwpn of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._wwpn = wwpn

    @property
    def adapter_unit(self):
        """Gets the adapter_unit of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The adapter_unit of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: AdapterUnit
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """Sets the adapter_unit of this AdapterHostFcInterfaceAllOf.


        :param adapter_unit: The adapter_unit of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: AdapterUnit
        """

        self._adapter_unit = adapter_unit

    @property
    def registered_device(self):
        """Gets the registered_device of this AdapterHostFcInterfaceAllOf.  # noqa: E501


        :return: The registered_device of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this AdapterHostFcInterfaceAllOf.


        :param registered_device: The registered_device of this AdapterHostFcInterfaceAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

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
        if not isinstance(other, AdapterHostFcInterfaceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdapterHostFcInterfaceAllOf):
            return True

        return self.to_dict() != other.to_dict()
