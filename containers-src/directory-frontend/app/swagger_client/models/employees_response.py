# coding: utf-8

"""
    DirectoryService

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EmployeesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'message': 'str',
        'employees': 'list[Employee]'
    }

    attribute_map = {
        'message': 'message',
        'employees': 'employees'
    }

    def __init__(self, message=None, employees=None):  # noqa: E501
        """EmployeesResponse - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._employees = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if employees is not None:
            self.employees = employees

    @property
    def message(self):
        """Gets the message of this EmployeesResponse.  # noqa: E501


        :return: The message of this EmployeesResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EmployeesResponse.


        :param message: The message of this EmployeesResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def employees(self):
        """Gets the employees of this EmployeesResponse.  # noqa: E501


        :return: The employees of this EmployeesResponse.  # noqa: E501
        :rtype: list[Employee]
        """
        return self._employees

    @employees.setter
    def employees(self, employees):
        """Sets the employees of this EmployeesResponse.


        :param employees: The employees of this EmployeesResponse.  # noqa: E501
        :type: list[Employee]
        """

        self._employees = employees

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EmployeesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmployeesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
