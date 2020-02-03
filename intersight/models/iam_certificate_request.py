# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IamCertificateRequest(object):
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
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'email_address': 'str',
        'name': 'str',
        'request': 'str',
        'self_signed': 'bool',
        'subject': 'PkixDistinguishedName',
        'subject_alternate_name': 'PkixSubjectAlternateName',
        'account': 'IamAccountRef',
        'certificate': 'IamCertificateRef',
        'private_key_spec': 'IamPrivateKeySpecRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'email_address': 'EmailAddress',
        'name': 'Name',
        'request': 'Request',
        'self_signed': 'SelfSigned',
        'subject': 'Subject',
        'subject_alternate_name': 'SubjectAlternateName',
        'account': 'Account',
        'certificate': 'Certificate',
        'private_key_spec': 'PrivateKeySpec'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, email_address=None, name=None, request=None, self_signed=None, subject=None, subject_alternate_name=None, account=None, certificate=None, private_key_spec=None):
        """
        IamCertificateRequest - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._email_address = None
        self._name = None
        self._request = None
        self._self_signed = None
        self._subject = None
        self._subject_alternate_name = None
        self._account = None
        self._certificate = None
        self._private_key_spec = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if email_address is not None:
          self.email_address = email_address
        if name is not None:
          self.name = name
        if request is not None:
          self.request = request
        if self_signed is not None:
          self.self_signed = self_signed
        if subject is not None:
          self.subject = subject
        if subject_alternate_name is not None:
          self.subject_alternate_name = subject_alternate_name
        if account is not None:
          self.account = account
        if certificate is not None:
          self.certificate = certificate
        if private_key_spec is not None:
          self.private_key_spec = private_key_spec

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamCertificateRequest.
        The Account ID for this managed object.  

        :return: The account_moid of this IamCertificateRequest.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamCertificateRequest.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamCertificateRequest.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this IamCertificateRequest.
        The time when this managed object was created.  

        :return: The create_time of this IamCertificateRequest.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamCertificateRequest.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamCertificateRequest.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamCertificateRequest.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamCertificateRequest.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamCertificateRequest.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamCertificateRequest.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamCertificateRequest.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamCertificateRequest.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamCertificateRequest.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamCertificateRequest.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamCertificateRequest.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this IamCertificateRequest.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamCertificateRequest.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this IamCertificateRequest.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamCertificateRequest.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this IamCertificateRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamCertificateRequest.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this IamCertificateRequest.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamCertificateRequest.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamCertificateRequest.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamCertificateRequest.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamCertificateRequest.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamCertificateRequest.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamCertificateRequest.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamCertificateRequest.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamCertificateRequest.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamCertificateRequest.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IamCertificateRequest.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamCertificateRequest.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IamCertificateRequest.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamCertificateRequest.
        The versioning info for this managed object.   

        :return: The version_context of this IamCertificateRequest.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamCertificateRequest.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamCertificateRequest.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamCertificateRequest.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamCertificateRequest.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamCertificateRequest.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamCertificateRequest.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this IamCertificateRequest.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamCertificateRequest.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamCertificateRequest.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamCertificateRequest.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this IamCertificateRequest.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this IamCertificateRequest.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this IamCertificateRequest.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this IamCertificateRequest.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def email_address(self):
        """
        Gets the email_address of this IamCertificateRequest.
        User input email address, an optional part of the subject of the certificate request.  

        :return: The email_address of this IamCertificateRequest.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this IamCertificateRequest.
        User input email address, an optional part of the subject of the certificate request.  

        :param email_address: The email_address of this IamCertificateRequest.
        :type: str
        """

        self._email_address = email_address

    @property
    def name(self):
        """
        Gets the name of this IamCertificateRequest.
        Name of the certificate request.  

        :return: The name of this IamCertificateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamCertificateRequest.
        Name of the certificate request.  

        :param name: The name of this IamCertificateRequest.
        :type: str
        """

        self._name = name

    @property
    def request(self):
        """
        Gets the request of this IamCertificateRequest.
        Generated certificate signing request (CSR) in PEM format.  

        :return: The request of this IamCertificateRequest.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this IamCertificateRequest.
        Generated certificate signing request (CSR) in PEM format.  

        :param request: The request of this IamCertificateRequest.
        :type: str
        """

        self._request = request

    @property
    def self_signed(self):
        """
        Gets the self_signed of this IamCertificateRequest.
        Whether the user wants the generated CSR to be self-signed by the appliance.  

        :return: The self_signed of this IamCertificateRequest.
        :rtype: bool
        """
        return self._self_signed

    @self_signed.setter
    def self_signed(self, self_signed):
        """
        Sets the self_signed of this IamCertificateRequest.
        Whether the user wants the generated CSR to be self-signed by the appliance.  

        :param self_signed: The self_signed of this IamCertificateRequest.
        :type: bool
        """

        self._self_signed = self_signed

    @property
    def subject(self):
        """
        Gets the subject of this IamCertificateRequest.
        The x.509 distinguished name of the subject of the certificate request.  

        :return: The subject of this IamCertificateRequest.
        :rtype: PkixDistinguishedName
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this IamCertificateRequest.
        The x.509 distinguished name of the subject of the certificate request.  

        :param subject: The subject of this IamCertificateRequest.
        :type: PkixDistinguishedName
        """

        self._subject = subject

    @property
    def subject_alternate_name(self):
        """
        Gets the subject_alternate_name of this IamCertificateRequest.
        The x.509 subject alternate name values of the certificate request.   

        :return: The subject_alternate_name of this IamCertificateRequest.
        :rtype: PkixSubjectAlternateName
        """
        return self._subject_alternate_name

    @subject_alternate_name.setter
    def subject_alternate_name(self, subject_alternate_name):
        """
        Sets the subject_alternate_name of this IamCertificateRequest.
        The x.509 subject alternate name values of the certificate request.   

        :param subject_alternate_name: The subject_alternate_name of this IamCertificateRequest.
        :type: PkixSubjectAlternateName
        """

        self._subject_alternate_name = subject_alternate_name

    @property
    def account(self):
        """
        Gets the account of this IamCertificateRequest.
        The account associated with the CertificateRequest. 

        :return: The account of this IamCertificateRequest.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamCertificateRequest.
        The account associated with the CertificateRequest. 

        :param account: The account of this IamCertificateRequest.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def certificate(self):
        """
        Gets the certificate of this IamCertificateRequest.
        A collection of references to the [iam.Certificate](mo://iam.Certificate) Managed Object.  When this managed object is deleted, the referenced [iam.Certificate](mo://iam.Certificate) MO on the other side of the relationship is deleted. 

        :return: The certificate of this IamCertificateRequest.
        :rtype: IamCertificateRef
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this IamCertificateRequest.
        A collection of references to the [iam.Certificate](mo://iam.Certificate) Managed Object.  When this managed object is deleted, the referenced [iam.Certificate](mo://iam.Certificate) MO on the other side of the relationship is deleted. 

        :param certificate: The certificate of this IamCertificateRequest.
        :type: IamCertificateRef
        """

        self._certificate = certificate

    @property
    def private_key_spec(self):
        """
        Gets the private_key_spec of this IamCertificateRequest.
        A collection of references to the [iam.PrivateKeySpec](mo://iam.PrivateKeySpec) Managed Object.  When this managed object is deleted, the referenced [iam.PrivateKeySpec](mo://iam.PrivateKeySpec) MO on the other side of the relationship is deleted. 

        :return: The private_key_spec of this IamCertificateRequest.
        :rtype: IamPrivateKeySpecRef
        """
        return self._private_key_spec

    @private_key_spec.setter
    def private_key_spec(self, private_key_spec):
        """
        Sets the private_key_spec of this IamCertificateRequest.
        A collection of references to the [iam.PrivateKeySpec](mo://iam.PrivateKeySpec) Managed Object.  When this managed object is deleted, the referenced [iam.PrivateKeySpec](mo://iam.PrivateKeySpec) MO on the other side of the relationship is deleted. 

        :param private_key_spec: The private_key_spec of this IamCertificateRequest.
        :type: IamPrivateKeySpecRef
        """

        self._private_key_spec = private_key_spec

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
        if not isinstance(other, IamCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other