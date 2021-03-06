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


class AssetDeviceContractInformationAllOf(object):
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
        'contract': 'AssetContractInformation',
        'contract_status': 'str',
        'covered_product_line_end_date': 'str',
        'device_id': 'str',
        'device_type': 'str',
        'end_customer': 'AssetCustomerInformation',
        'end_user_global_ultimate': 'AssetGlobalUltimate',
        'is_valid': 'bool',
        'item_type': 'str',
        'maintenance_purchase_order_number': 'str',
        'maintenance_sales_order_number': 'str',
        'platform_type': 'str',
        'product': 'AssetProductInformation',
        'purchase_order_number': 'str',
        'reseller_global_ultimate': 'AssetGlobalUltimate',
        'sales_order_number': 'str',
        'service_description': 'str',
        'service_end_date': 'datetime',
        'service_level': 'str',
        'service_sku': 'str',
        'service_start_date': 'datetime',
        'state_contract': 'str',
        'warranty_end_date': 'str',
        'warranty_type': 'str',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'contract': 'Contract',
        'contract_status': 'ContractStatus',
        'covered_product_line_end_date': 'CoveredProductLineEndDate',
        'device_id': 'DeviceId',
        'device_type': 'DeviceType',
        'end_customer': 'EndCustomer',
        'end_user_global_ultimate': 'EndUserGlobalUltimate',
        'is_valid': 'IsValid',
        'item_type': 'ItemType',
        'maintenance_purchase_order_number': 'MaintenancePurchaseOrderNumber',
        'maintenance_sales_order_number': 'MaintenanceSalesOrderNumber',
        'platform_type': 'PlatformType',
        'product': 'Product',
        'purchase_order_number': 'PurchaseOrderNumber',
        'reseller_global_ultimate': 'ResellerGlobalUltimate',
        'sales_order_number': 'SalesOrderNumber',
        'service_description': 'ServiceDescription',
        'service_end_date': 'ServiceEndDate',
        'service_level': 'ServiceLevel',
        'service_sku': 'ServiceSku',
        'service_start_date': 'ServiceStartDate',
        'state_contract': 'StateContract',
        'warranty_end_date': 'WarrantyEndDate',
        'warranty_type': 'WarrantyType',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 contract=None,
                 contract_status='Not Covered',
                 covered_product_line_end_date=None,
                 device_id=None,
                 device_type='None',
                 end_customer=None,
                 end_user_global_ultimate=None,
                 is_valid=None,
                 item_type=None,
                 maintenance_purchase_order_number=None,
                 maintenance_sales_order_number=None,
                 platform_type='',
                 product=None,
                 purchase_order_number=None,
                 reseller_global_ultimate=None,
                 sales_order_number=None,
                 service_description=None,
                 service_end_date=None,
                 service_level=None,
                 service_sku=None,
                 service_start_date=None,
                 state_contract='Update',
                 warranty_end_date=None,
                 warranty_type=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetDeviceContractInformationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract = None
        self._contract_status = None
        self._covered_product_line_end_date = None
        self._device_id = None
        self._device_type = None
        self._end_customer = None
        self._end_user_global_ultimate = None
        self._is_valid = None
        self._item_type = None
        self._maintenance_purchase_order_number = None
        self._maintenance_sales_order_number = None
        self._platform_type = None
        self._product = None
        self._purchase_order_number = None
        self._reseller_global_ultimate = None
        self._sales_order_number = None
        self._service_description = None
        self._service_end_date = None
        self._service_level = None
        self._service_sku = None
        self._service_start_date = None
        self._state_contract = None
        self._warranty_end_date = None
        self._warranty_type = None
        self._registered_device = None
        self.discriminator = None

        if contract is not None:
            self.contract = contract
        if contract_status is not None:
            self.contract_status = contract_status
        if covered_product_line_end_date is not None:
            self.covered_product_line_end_date = covered_product_line_end_date
        if device_id is not None:
            self.device_id = device_id
        if device_type is not None:
            self.device_type = device_type
        if end_customer is not None:
            self.end_customer = end_customer
        if end_user_global_ultimate is not None:
            self.end_user_global_ultimate = end_user_global_ultimate
        if is_valid is not None:
            self.is_valid = is_valid
        if item_type is not None:
            self.item_type = item_type
        if maintenance_purchase_order_number is not None:
            self.maintenance_purchase_order_number = maintenance_purchase_order_number
        if maintenance_sales_order_number is not None:
            self.maintenance_sales_order_number = maintenance_sales_order_number
        if platform_type is not None:
            self.platform_type = platform_type
        if product is not None:
            self.product = product
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if reseller_global_ultimate is not None:
            self.reseller_global_ultimate = reseller_global_ultimate
        if sales_order_number is not None:
            self.sales_order_number = sales_order_number
        if service_description is not None:
            self.service_description = service_description
        if service_end_date is not None:
            self.service_end_date = service_end_date
        if service_level is not None:
            self.service_level = service_level
        if service_sku is not None:
            self.service_sku = service_sku
        if service_start_date is not None:
            self.service_start_date = service_start_date
        if state_contract is not None:
            self.state_contract = state_contract
        if warranty_end_date is not None:
            self.warranty_end_date = warranty_end_date
        if warranty_type is not None:
            self.warranty_type = warranty_type
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def contract(self):
        """Gets the contract of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The contract of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetContractInformation
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this AssetDeviceContractInformationAllOf.


        :param contract: The contract of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: AssetContractInformation
        """

        self._contract = contract

    @property
    def contract_status(self):
        """Gets the contract_status of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered.    # noqa: E501

        :return: The contract_status of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._contract_status

    @contract_status.setter
    def contract_status(self, contract_status):
        """Sets the contract_status of this AssetDeviceContractInformationAllOf.

        Calculated contract status that is derived based on the service line status and contract end date. It is different from serviceLineStatus property. serviceLineStatus gives us ACTIVE, OVERDUE, EXPIRED. These are transformed into Active, Expiring Soon and Not Covered.    # noqa: E501

        :param contract_status: The contract_status of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Not Covered", "Active",
                          "Expiring Soon"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and contract_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `contract_status` ({0}), must be one of {1}"  # noqa: E501
                .format(contract_status, allowed_values))

        self._contract_status = contract_status

    @property
    def covered_product_line_end_date(self):
        """Gets the covered_product_line_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501

        End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API.    # noqa: E501

        :return: The covered_product_line_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._covered_product_line_end_date

    @covered_product_line_end_date.setter
    def covered_product_line_end_date(self, covered_product_line_end_date):
        """Sets the covered_product_line_end_date of this AssetDeviceContractInformationAllOf.

        End date of the covered product line. The coverage end date is fetched from Cisco SN2INFO API.    # noqa: E501

        :param covered_product_line_end_date: The covered_product_line_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._covered_product_line_end_date = covered_product_line_end_date

    @property
    def device_id(self):
        """Gets the device_id of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Unique identifier of the Cisco device. This information is used to query Cisco APIx SN2INFO and CCWR databases.    # noqa: E501

        :return: The device_id of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AssetDeviceContractInformationAllOf.

        Unique identifier of the Cisco device. This information is used to query Cisco APIx SN2INFO and CCWR databases.    # noqa: E501

        :param device_id: The device_id of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def device_type(self):
        """Gets the device_type of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Type used to classify the device in Cisco Intersight. Currently supported values are Server and FabricInterconnect. This will be expanded to support more types in future.    # noqa: E501

        :return: The device_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this AssetDeviceContractInformationAllOf.

        Type used to classify the device in Cisco Intersight. Currently supported values are Server and FabricInterconnect. This will be expanded to support more types in future.    # noqa: E501

        :param device_type: The device_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "None", "CiscoUcsServer", "CiscoUcsFI", "CiscoUcsChassis"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and device_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"  # noqa: E501
                .format(device_type, allowed_values))

        self._device_type = device_type

    @property
    def end_customer(self):
        """Gets the end_customer of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The end_customer of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetCustomerInformation
        """
        return self._end_customer

    @end_customer.setter
    def end_customer(self, end_customer):
        """Sets the end_customer of this AssetDeviceContractInformationAllOf.


        :param end_customer: The end_customer of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: AssetCustomerInformation
        """

        self._end_customer = end_customer

    @property
    def end_user_global_ultimate(self):
        """Gets the end_user_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The end_user_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetGlobalUltimate
        """
        return self._end_user_global_ultimate

    @end_user_global_ultimate.setter
    def end_user_global_ultimate(self, end_user_global_ultimate):
        """Sets the end_user_global_ultimate of this AssetDeviceContractInformationAllOf.


        :param end_user_global_ultimate: The end_user_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: AssetGlobalUltimate
        """

        self._end_user_global_ultimate = end_user_global_ultimate

    @property
    def is_valid(self):
        """Gets the is_valid of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs.    # noqa: E501

        :return: The is_valid of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this AssetDeviceContractInformationAllOf.

        Validates if the device is a genuine Cisco device. Validated is done using the Cisco SN2INFO APIs.    # noqa: E501

        :param is_valid: The is_valid of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def item_type(self):
        """Gets the item_type of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Item type of this specific Cisco device. example \"Chassis\".    # noqa: E501

        :return: The item_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this AssetDeviceContractInformationAllOf.

        Item type of this specific Cisco device. example \"Chassis\".    # noqa: E501

        :param item_type: The item_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._item_type = item_type

    @property
    def maintenance_purchase_order_number(self):
        """Gets the maintenance_purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Maintenance purchase order number for the Cisco device.    # noqa: E501

        :return: The maintenance_purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_purchase_order_number

    @maintenance_purchase_order_number.setter
    def maintenance_purchase_order_number(self,
                                          maintenance_purchase_order_number):
        """Sets the maintenance_purchase_order_number of this AssetDeviceContractInformationAllOf.

        Maintenance purchase order number for the Cisco device.    # noqa: E501

        :param maintenance_purchase_order_number: The maintenance_purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._maintenance_purchase_order_number = maintenance_purchase_order_number

    @property
    def maintenance_sales_order_number(self):
        """Gets the maintenance_sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Maintenance sales order number for the Cisco device.    # noqa: E501

        :return: The maintenance_sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_sales_order_number

    @maintenance_sales_order_number.setter
    def maintenance_sales_order_number(self, maintenance_sales_order_number):
        """Sets the maintenance_sales_order_number of this AssetDeviceContractInformationAllOf.

        Maintenance sales order number for the Cisco device.    # noqa: E501

        :param maintenance_sales_order_number: The maintenance_sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._maintenance_sales_order_number = maintenance_sales_order_number

    @property
    def platform_type(self):
        """Gets the platform_type of this AssetDeviceContractInformationAllOf.  # noqa: E501

        The platform type of the Cisco device.    # noqa: E501

        :return: The platform_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this AssetDeviceContractInformationAllOf.

        The platform type of the Cisco device.    # noqa: E501

        :param platform_type: The platform_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "", "APIC", "DCNM", "UCSFI", "IMC", "IMCM4", "IMCM5", "HX",
            "HXTriton", "UCSD", "IntersightAppliance", "PureStorage", "VMware",
            "ServiceEngine"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and platform_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `platform_type` ({0}), must be one of {1}"  # noqa: E501
                .format(platform_type, allowed_values))

        self._platform_type = platform_type

    @property
    def product(self):
        """Gets the product of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The product of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetProductInformation
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AssetDeviceContractInformationAllOf.


        :param product: The product of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: AssetProductInformation
        """

        self._product = product

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Purchase order number for the Cisco device. It is a unique number assigned for every purchase.    # noqa: E501

        :return: The purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this AssetDeviceContractInformationAllOf.

        Purchase order number for the Cisco device. It is a unique number assigned for every purchase.    # noqa: E501

        :param purchase_order_number: The purchase_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def reseller_global_ultimate(self):
        """Gets the reseller_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The reseller_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetGlobalUltimate
        """
        return self._reseller_global_ultimate

    @reseller_global_ultimate.setter
    def reseller_global_ultimate(self, reseller_global_ultimate):
        """Sets the reseller_global_ultimate of this AssetDeviceContractInformationAllOf.


        :param reseller_global_ultimate: The reseller_global_ultimate of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: AssetGlobalUltimate
        """

        self._reseller_global_ultimate = reseller_global_ultimate

    @property
    def sales_order_number(self):
        """Gets the sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Sales order number for the Cisco device. It is a unique number assigned for every sale.    # noqa: E501

        :return: The sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sales_order_number

    @sales_order_number.setter
    def sales_order_number(self, sales_order_number):
        """Sets the sales_order_number of this AssetDeviceContractInformationAllOf.

        Sales order number for the Cisco device. It is a unique number assigned for every sale.    # noqa: E501

        :param sales_order_number: The sales_order_number of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._sales_order_number = sales_order_number

    @property
    def service_description(self):
        """Gets the service_description of this AssetDeviceContractInformationAllOf.  # noqa: E501

        The type of service contract that covers the Cisco device.    # noqa: E501

        :return: The service_description of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._service_description

    @service_description.setter
    def service_description(self, service_description):
        """Sets the service_description of this AssetDeviceContractInformationAllOf.

        The type of service contract that covers the Cisco device.    # noqa: E501

        :param service_description: The service_description of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._service_description = service_description

    @property
    def service_end_date(self):
        """Gets the service_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501

        End date for the Cisco service contract that covers this Cisco device.    # noqa: E501

        :return: The service_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._service_end_date

    @service_end_date.setter
    def service_end_date(self, service_end_date):
        """Sets the service_end_date of this AssetDeviceContractInformationAllOf.

        End date for the Cisco service contract that covers this Cisco device.    # noqa: E501

        :param service_end_date: The service_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: datetime
        """

        self._service_end_date = service_end_date

    @property
    def service_level(self):
        """Gets the service_level of this AssetDeviceContractInformationAllOf.  # noqa: E501

        The type of service contract that covers the Cisco device.    # noqa: E501

        :return: The service_level of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """Sets the service_level of this AssetDeviceContractInformationAllOf.

        The type of service contract that covers the Cisco device.    # noqa: E501

        :param service_level: The service_level of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._service_level = service_level

    @property
    def service_sku(self):
        """Gets the service_sku of this AssetDeviceContractInformationAllOf.  # noqa: E501

        The SKU of the service contract that covers the Cisco device.    # noqa: E501

        :return: The service_sku of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._service_sku

    @service_sku.setter
    def service_sku(self, service_sku):
        """Sets the service_sku of this AssetDeviceContractInformationAllOf.

        The SKU of the service contract that covers the Cisco device.    # noqa: E501

        :param service_sku: The service_sku of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._service_sku = service_sku

    @property
    def service_start_date(self):
        """Gets the service_start_date of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Start date for the Cisco service contract that covers this Cisco device.    # noqa: E501

        :return: The service_start_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._service_start_date

    @service_start_date.setter
    def service_start_date(self, service_start_date):
        """Sets the service_start_date of this AssetDeviceContractInformationAllOf.

        Start date for the Cisco service contract that covers this Cisco device.    # noqa: E501

        :param service_start_date: The service_start_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: datetime
        """

        self._service_start_date = service_start_date

    @property
    def state_contract(self):
        """Gets the state_contract of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Internal property used for triggering and tracking actions for contract information.     # noqa: E501

        :return: The state_contract of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._state_contract

    @state_contract.setter
    def state_contract(self, state_contract):
        """Sets the state_contract of this AssetDeviceContractInformationAllOf.

        Internal property used for triggering and tracking actions for contract information.     # noqa: E501

        :param state_contract: The state_contract of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Update", "OK", "Failed", "Retry"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state_contract not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state_contract` ({0}), must be one of {1}"  # noqa: E501
                .format(state_contract, allowed_values))

        self._state_contract = state_contract

    @property
    def warranty_end_date(self):
        """Gets the warranty_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501

        End date for the warranty that covers the Cisco device.    # noqa: E501

        :return: The warranty_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._warranty_end_date

    @warranty_end_date.setter
    def warranty_end_date(self, warranty_end_date):
        """Sets the warranty_end_date of this AssetDeviceContractInformationAllOf.

        End date for the warranty that covers the Cisco device.    # noqa: E501

        :param warranty_end_date: The warranty_end_date of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._warranty_end_date = warranty_end_date

    @property
    def warranty_type(self):
        """Gets the warranty_type of this AssetDeviceContractInformationAllOf.  # noqa: E501

        Type of warranty that covers the Cisco device.     # noqa: E501

        :return: The warranty_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._warranty_type

    @warranty_type.setter
    def warranty_type(self, warranty_type):
        """Sets the warranty_type of this AssetDeviceContractInformationAllOf.

        Type of warranty that covers the Cisco device.     # noqa: E501

        :param warranty_type: The warranty_type of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :type: str
        """

        self._warranty_type = warranty_type

    @property
    def registered_device(self):
        """Gets the registered_device of this AssetDeviceContractInformationAllOf.  # noqa: E501


        :return: The registered_device of this AssetDeviceContractInformationAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this AssetDeviceContractInformationAllOf.


        :param registered_device: The registered_device of this AssetDeviceContractInformationAllOf.  # noqa: E501
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
        if not isinstance(other, AssetDeviceContractInformationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetDeviceContractInformationAllOf):
            return True

        return self.to_dict() != other.to_dict()
