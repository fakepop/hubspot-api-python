# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.timeline.configuration import Configuration


class TimelineEventIFrame(object):
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
        "link_label": "str",
        "header_label": "str",
        "url": "str",
        "width": "int",
        "height": "int",
    }

    attribute_map = {
        "link_label": "linkLabel",
        "header_label": "headerLabel",
        "url": "url",
        "width": "width",
        "height": "height",
    }

    def __init__(
        self,
        link_label=None,
        header_label=None,
        url=None,
        width=None,
        height=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """TimelineEventIFrame - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._link_label = None
        self._header_label = None
        self._url = None
        self._width = None
        self._height = None
        self.discriminator = None

        self.link_label = link_label
        self.header_label = header_label
        self.url = url
        self.width = width
        self.height = height

    @property
    def link_label(self):
        """Gets the link_label of this TimelineEventIFrame.  # noqa: E501

        The text displaying the link that will display the iframe.  # noqa: E501

        :return: The link_label of this TimelineEventIFrame.  # noqa: E501
        :rtype: str
        """
        return self._link_label

    @link_label.setter
    def link_label(self, link_label):
        """Sets the link_label of this TimelineEventIFrame.

        The text displaying the link that will display the iframe.  # noqa: E501

        :param link_label: The link_label of this TimelineEventIFrame.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and link_label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `link_label`, must not be `None`"
            )  # noqa: E501

        self._link_label = link_label

    @property
    def header_label(self):
        """Gets the header_label of this TimelineEventIFrame.  # noqa: E501

        The label of the modal window that displays the iframe contents.  # noqa: E501

        :return: The header_label of this TimelineEventIFrame.  # noqa: E501
        :rtype: str
        """
        return self._header_label

    @header_label.setter
    def header_label(self, header_label):
        """Sets the header_label of this TimelineEventIFrame.

        The label of the modal window that displays the iframe contents.  # noqa: E501

        :param header_label: The header_label of this TimelineEventIFrame.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and header_label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `header_label`, must not be `None`"
            )  # noqa: E501

        self._header_label = header_label

    @property
    def url(self):
        """Gets the url of this TimelineEventIFrame.  # noqa: E501

        The URI of the iframe contents.  # noqa: E501

        :return: The url of this TimelineEventIFrame.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TimelineEventIFrame.

        The URI of the iframe contents.  # noqa: E501

        :param url: The url of this TimelineEventIFrame.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

    @property
    def width(self):
        """Gets the width of this TimelineEventIFrame.  # noqa: E501

        The width of the modal window in pixels.  # noqa: E501

        :return: The width of this TimelineEventIFrame.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TimelineEventIFrame.

        The width of the modal window in pixels.  # noqa: E501

        :param width: The width of this TimelineEventIFrame.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and width is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `width`, must not be `None`"
            )  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this TimelineEventIFrame.  # noqa: E501

        The height of the modal window in pixels.  # noqa: E501

        :return: The height of this TimelineEventIFrame.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TimelineEventIFrame.

        The height of the modal window in pixels.  # noqa: E501

        :param height: The height of this TimelineEventIFrame.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and height is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `height`, must not be `None`"
            )  # noqa: E501

        self._height = height

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
        if not isinstance(other, TimelineEventIFrame):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineEventIFrame):
            return True

        return self.to_dict() != other.to_dict()
