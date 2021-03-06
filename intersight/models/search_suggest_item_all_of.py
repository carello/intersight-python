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


class SearchSuggestItemAllOf(object):
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
        'complete_mo': 'bool',
        'rawquery': 'str',
        'skip': 'int',
        'suggest_term': 'str',
        'top': 'int',
        'type': 'str'
    }

    attribute_map = {
        'complete_mo': 'CompleteMo',
        'rawquery': 'Rawquery',
        'skip': 'Skip',
        'suggest_term': 'SuggestTerm',
        'top': 'Top',
        'type': 'Type'
    }

    def __init__(self,
                 complete_mo=None,
                 rawquery=None,
                 skip=None,
                 suggest_term=None,
                 top=None,
                 type=None,
                 local_vars_configuration=None):  # noqa: E501
        """SearchSuggestItemAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._complete_mo = None
        self._rawquery = None
        self._skip = None
        self._suggest_term = None
        self._top = None
        self._type = None
        self.discriminator = None

        if complete_mo is not None:
            self.complete_mo = complete_mo
        if rawquery is not None:
            self.rawquery = rawquery
        if skip is not None:
            self.skip = skip
        if suggest_term is not None:
            self.suggest_term = suggest_term
        if top is not None:
            self.top = top
        if type is not None:
            self.type = type

    @property
    def complete_mo(self):
        """Gets the complete_mo of this SearchSuggestItemAllOf.  # noqa: E501

        Flag for returning complete objects that matched the global search criteria.    # noqa: E501

        :return: The complete_mo of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._complete_mo

    @complete_mo.setter
    def complete_mo(self, complete_mo):
        """Sets the complete_mo of this SearchSuggestItemAllOf.

        Flag for returning complete objects that matched the global search criteria.    # noqa: E501

        :param complete_mo: The complete_mo of this SearchSuggestItemAllOf.  # noqa: E501
        :type: bool
        """

        self._complete_mo = complete_mo

    @property
    def rawquery(self):
        """Gets the rawquery of this SearchSuggestItemAllOf.  # noqa: E501

        Additional filter parameters for global search. You can also specify OData select fields here. Maximum Query Length is limited to 10000.    # noqa: E501

        :return: The rawquery of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rawquery

    @rawquery.setter
    def rawquery(self, rawquery):
        """Sets the rawquery of this SearchSuggestItemAllOf.

        Additional filter parameters for global search. You can also specify OData select fields here. Maximum Query Length is limited to 10000.    # noqa: E501

        :param rawquery: The rawquery of this SearchSuggestItemAllOf.  # noqa: E501
        :type: str
        """

        self._rawquery = rawquery

    @property
    def skip(self):
        """Gets the skip of this SearchSuggestItemAllOf.  # noqa: E501

        Starting offset for the results to be returned from external search engine.    # noqa: E501

        :return: The skip of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this SearchSuggestItemAllOf.

        Starting offset for the results to be returned from external search engine.    # noqa: E501

        :param skip: The skip of this SearchSuggestItemAllOf.  # noqa: E501
        :type: int
        """

        self._skip = skip

    @property
    def suggest_term(self):
        """Gets the suggest_term of this SearchSuggestItemAllOf.  # noqa: E501

        Main search term used for global search across all Managed Objects that has search enabled. Search Term can be up to 200 characters long.    # noqa: E501

        :return: The suggest_term of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._suggest_term

    @suggest_term.setter
    def suggest_term(self, suggest_term):
        """Sets the suggest_term of this SearchSuggestItemAllOf.

        Main search term used for global search across all Managed Objects that has search enabled. Search Term can be up to 200 characters long.    # noqa: E501

        :param suggest_term: The suggest_term of this SearchSuggestItemAllOf.  # noqa: E501
        :type: str
        """

        self._suggest_term = suggest_term

    @property
    def top(self):
        """Gets the top of this SearchSuggestItemAllOf.  # noqa: E501

        Maximum number of results to be returned from external search engine.    # noqa: E501

        :return: The top of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this SearchSuggestItemAllOf.

        Maximum number of results to be returned from external search engine.    # noqa: E501

        :param top: The top of this SearchSuggestItemAllOf.  # noqa: E501
        :type: int
        """

        self._top = top

    @property
    def type(self):
        """Gets the type of this SearchSuggestItemAllOf.  # noqa: E501

        Object type filter of a Managed Object. Search will be restricted only on the specified object types.  Do not provide IndexMoTypes filter in the rawquery, if you specify values in this field.      # noqa: E501

        :return: The type of this SearchSuggestItemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchSuggestItemAllOf.

        Object type filter of a Managed Object. Search will be restricted only on the specified object types.  Do not provide IndexMoTypes filter in the rawquery, if you specify values in this field.      # noqa: E501

        :param type: The type of this SearchSuggestItemAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SearchSuggestItemAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchSuggestItemAllOf):
            return True

        return self.to_dict() != other.to_dict()
