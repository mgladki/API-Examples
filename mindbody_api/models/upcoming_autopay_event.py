# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpcomingAutopayEvent(object):
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
        'client_contract_id': 'int',
        'charge_amount': 'float',
        'payment_method': 'str',
        'schedule_date': 'datetime'
    }

    attribute_map = {
        'client_contract_id': 'ClientContractId',
        'charge_amount': 'ChargeAmount',
        'payment_method': 'PaymentMethod',
        'schedule_date': 'ScheduleDate'
    }

    def __init__(self, client_contract_id=None, charge_amount=None, payment_method=None, schedule_date=None):  # noqa: E501
        """UpcomingAutopayEvent - a model defined in Swagger"""  # noqa: E501

        self._client_contract_id = None
        self._charge_amount = None
        self._payment_method = None
        self._schedule_date = None
        self.discriminator = None

        if client_contract_id is not None:
            self.client_contract_id = client_contract_id
        if charge_amount is not None:
            self.charge_amount = charge_amount
        if payment_method is not None:
            self.payment_method = payment_method
        if schedule_date is not None:
            self.schedule_date = schedule_date

    @property
    def client_contract_id(self):
        """Gets the client_contract_id of this UpcomingAutopayEvent.  # noqa: E501

        The ID of the contract.  # noqa: E501

        :return: The client_contract_id of this UpcomingAutopayEvent.  # noqa: E501
        :rtype: int
        """
        return self._client_contract_id

    @client_contract_id.setter
    def client_contract_id(self, client_contract_id):
        """Sets the client_contract_id of this UpcomingAutopayEvent.

        The ID of the contract.  # noqa: E501

        :param client_contract_id: The client_contract_id of this UpcomingAutopayEvent.  # noqa: E501
        :type: int
        """

        self._client_contract_id = client_contract_id

    @property
    def charge_amount(self):
        """Gets the charge_amount of this UpcomingAutopayEvent.  # noqa: E501

        The amount charged.  # noqa: E501

        :return: The charge_amount of this UpcomingAutopayEvent.  # noqa: E501
        :rtype: float
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """Sets the charge_amount of this UpcomingAutopayEvent.

        The amount charged.  # noqa: E501

        :param charge_amount: The charge_amount of this UpcomingAutopayEvent.  # noqa: E501
        :type: float
        """

        self._charge_amount = charge_amount

    @property
    def payment_method(self):
        """Gets the payment_method of this UpcomingAutopayEvent.  # noqa: E501

        The payment method.  # noqa: E501

        :return: The payment_method of this UpcomingAutopayEvent.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this UpcomingAutopayEvent.

        The payment method.  # noqa: E501

        :param payment_method: The payment_method of this UpcomingAutopayEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Other", "CreditCard", "DebitAccount", "ACH"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def schedule_date(self):
        """Gets the schedule_date of this UpcomingAutopayEvent.  # noqa: E501

        The date and time of the next payment.  # noqa: E501

        :return: The schedule_date of this UpcomingAutopayEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this UpcomingAutopayEvent.

        The date and time of the next payment.  # noqa: E501

        :param schedule_date: The schedule_date of this UpcomingAutopayEvent.  # noqa: E501
        :type: datetime
        """

        self._schedule_date = schedule_date

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
        if issubclass(UpcomingAutopayEvent, dict):
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
        if not isinstance(other, UpcomingAutopayEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other