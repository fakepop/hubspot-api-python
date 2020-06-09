# coding: utf-8

"""
    CMS Site Search

    Use these endpoints for searching content on your HubSpot hosted CMS website(s).  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.site_search.configuration import Configuration


class IndexedData(object):
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
    openapi_types = {"id": "str", "type": "str", "fields": "dict(str, SearchHitField)"}

    attribute_map = {"id": "id", "type": "type", "fields": "fields"}

    def __init__(
        self, id=None, type=None, fields=None, local_vars_configuration=None
    ):  # noqa: E501
        """IndexedData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._fields = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.fields = fields

    @property
    def id(self):
        """Gets the id of this IndexedData.  # noqa: E501


        :return: The id of this IndexedData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndexedData.


        :param id: The id of this IndexedData.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this IndexedData.  # noqa: E501


        :return: The type of this IndexedData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IndexedData.


        :param type: The type of this IndexedData.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "LANDING_PAGE",
            "BLOG_POST",
            "SITE_PAGE",
            "DOCUMENT",
            "KNOWLEDGE_ARTICLE",
            "LISTING_PAGE",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def fields(self):
        """Gets the fields of this IndexedData.  # noqa: E501


        :return: The fields of this IndexedData.  # noqa: E501
        :rtype: dict(str, SearchHitField)
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this IndexedData.


        :param fields: The fields of this IndexedData.  # noqa: E501
        :type: dict(str, SearchHitField)
        """
        if (
            self.local_vars_configuration.client_side_validation and fields is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `fields`, must not be `None`"
            )  # noqa: E501

        self._fields = fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, IndexedData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndexedData):
            return True

        return self.to_dict() != other.to_dict()
