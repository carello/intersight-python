# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectorBaseMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'encrypted_aes_key': 'str',
        'encryption_key': 'str',
        'secure_properties': 'object'
    }

    attribute_map = {
        'encrypted_aes_key': 'EncryptedAesKey',
        'encryption_key': 'EncryptionKey',
        'secure_properties': 'SecureProperties'
    }

    def __init__(self, encrypted_aes_key=None, encryption_key=None, secure_properties=None):
        """
        ConnectorBaseMessage - a model defined in Swagger
        """

        self._encrypted_aes_key = None
        self._encryption_key = None
        self._secure_properties = None

        if encrypted_aes_key is not None:
          self.encrypted_aes_key = encrypted_aes_key
        if encryption_key is not None:
          self.encryption_key = encryption_key
        if secure_properties is not None:
          self.secure_properties = secure_properties

    @property
    def encrypted_aes_key(self):
        """
        Gets the encrypted_aes_key of this ConnectorBaseMessage.
        The secure properties that have large text content as value can be encrypted using AES key. In these cases, the AES key needs to be encrypted using the device connector public key and passed as the value for this property. The secure properties that are encrypted using the AES key are mapped against the property name with prefix 'AES' in SecureProperties dictionary.  

        :return: The encrypted_aes_key of this ConnectorBaseMessage.
        :rtype: str
        """
        return self._encrypted_aes_key

    @encrypted_aes_key.setter
    def encrypted_aes_key(self, encrypted_aes_key):
        """
        Sets the encrypted_aes_key of this ConnectorBaseMessage.
        The secure properties that have large text content as value can be encrypted using AES key. In these cases, the AES key needs to be encrypted using the device connector public key and passed as the value for this property. The secure properties that are encrypted using the AES key are mapped against the property name with prefix 'AES' in SecureProperties dictionary.  

        :param encrypted_aes_key: The encrypted_aes_key of this ConnectorBaseMessage.
        :type: str
        """

        self._encrypted_aes_key = encrypted_aes_key

    @property
    def encryption_key(self):
        """
        Gets the encryption_key of this ConnectorBaseMessage.
        The public key that was used to encrypt the values present in SecureProperties dictionary. If the given public key is not same as device connector's public key, an error reponse with appropriate error message is thrown back.  

        :return: The encryption_key of this ConnectorBaseMessage.
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """
        Sets the encryption_key of this ConnectorBaseMessage.
        The public key that was used to encrypt the values present in SecureProperties dictionary. If the given public key is not same as device connector's public key, an error reponse with appropriate error message is thrown back.  

        :param encryption_key: The encryption_key of this ConnectorBaseMessage.
        :type: str
        """

        self._encryption_key = encryption_key

    @property
    def secure_properties(self):
        """
        Gets the secure_properties of this ConnectorBaseMessage.
        A dictionary of encrypted secure values mapped against the secure property name. The values that are encrypted using AES key must be mapped against the secure property name with a 'AES' prefix Device connector expects the message body to be a golang template and the template can use the secure property names as placeholders.   

        :return: The secure_properties of this ConnectorBaseMessage.
        :rtype: object
        """
        return self._secure_properties

    @secure_properties.setter
    def secure_properties(self, secure_properties):
        """
        Sets the secure_properties of this ConnectorBaseMessage.
        A dictionary of encrypted secure values mapped against the secure property name. The values that are encrypted using AES key must be mapped against the secure property name with a 'AES' prefix Device connector expects the message body to be a golang template and the template can use the secure property names as placeholders.   

        :param secure_properties: The secure_properties of this ConnectorBaseMessage.
        :type: object
        """

        self._secure_properties = secure_properties

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ConnectorBaseMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
