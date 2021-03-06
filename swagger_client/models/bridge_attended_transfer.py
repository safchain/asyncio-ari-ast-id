# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BridgeAttendedTransfer(object):
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
        'destination_application': 'str',
        'destination_bridge': 'str',
        'destination_link_first_leg': 'Channel',
        'destination_link_second_leg': 'Channel',
        'destination_threeway_bridge': 'Bridge',
        'destination_threeway_channel': 'Channel',
        'destination_type': 'str',
        'is_external': 'bool',
        'replace_channel': 'Channel',
        'result': 'str',
        'transfer_target': 'Channel',
        'transferee': 'Channel',
        'transferer_first_leg': 'Channel',
        'transferer_first_leg_bridge': 'Bridge',
        'transferer_second_leg': 'Channel',
        'transferer_second_leg_bridge': 'Bridge'
    }

    attribute_map = {
        'destination_application': 'destination_application',
        'destination_bridge': 'destination_bridge',
        'destination_link_first_leg': 'destination_link_first_leg',
        'destination_link_second_leg': 'destination_link_second_leg',
        'destination_threeway_bridge': 'destination_threeway_bridge',
        'destination_threeway_channel': 'destination_threeway_channel',
        'destination_type': 'destination_type',
        'is_external': 'is_external',
        'replace_channel': 'replace_channel',
        'result': 'result',
        'transfer_target': 'transfer_target',
        'transferee': 'transferee',
        'transferer_first_leg': 'transferer_first_leg',
        'transferer_first_leg_bridge': 'transferer_first_leg_bridge',
        'transferer_second_leg': 'transferer_second_leg',
        'transferer_second_leg_bridge': 'transferer_second_leg_bridge'
    }

    def __init__(self, destination_application=None, destination_bridge=None, destination_link_first_leg=None, destination_link_second_leg=None, destination_threeway_bridge=None, destination_threeway_channel=None, destination_type=None, is_external=None, replace_channel=None, result=None, transfer_target=None, transferee=None, transferer_first_leg=None, transferer_first_leg_bridge=None, transferer_second_leg=None, transferer_second_leg_bridge=None):  # noqa: E501
        """BridgeAttendedTransfer - a model defined in Swagger"""  # noqa: E501

        self._destination_application = None
        self._destination_bridge = None
        self._destination_link_first_leg = None
        self._destination_link_second_leg = None
        self._destination_threeway_bridge = None
        self._destination_threeway_channel = None
        self._destination_type = None
        self._is_external = None
        self._replace_channel = None
        self._result = None
        self._transfer_target = None
        self._transferee = None
        self._transferer_first_leg = None
        self._transferer_first_leg_bridge = None
        self._transferer_second_leg = None
        self._transferer_second_leg_bridge = None
        self.discriminator = None

        if destination_application is not None:
            self.destination_application = destination_application
        if destination_bridge is not None:
            self.destination_bridge = destination_bridge
        if destination_link_first_leg is not None:
            self.destination_link_first_leg = destination_link_first_leg
        if destination_link_second_leg is not None:
            self.destination_link_second_leg = destination_link_second_leg
        if destination_threeway_bridge is not None:
            self.destination_threeway_bridge = destination_threeway_bridge
        if destination_threeway_channel is not None:
            self.destination_threeway_channel = destination_threeway_channel
        self.destination_type = destination_type
        self.is_external = is_external
        if replace_channel is not None:
            self.replace_channel = replace_channel
        self.result = result
        if transfer_target is not None:
            self.transfer_target = transfer_target
        if transferee is not None:
            self.transferee = transferee
        self.transferer_first_leg = transferer_first_leg
        if transferer_first_leg_bridge is not None:
            self.transferer_first_leg_bridge = transferer_first_leg_bridge
        self.transferer_second_leg = transferer_second_leg
        if transferer_second_leg_bridge is not None:
            self.transferer_second_leg_bridge = transferer_second_leg_bridge

    @property
    def destination_application(self):
        """Gets the destination_application of this BridgeAttendedTransfer.  # noqa: E501

        Application that has been transferred into  # noqa: E501

        :return: The destination_application of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: str
        """
        return self._destination_application

    @destination_application.setter
    def destination_application(self, destination_application):
        """Sets the destination_application of this BridgeAttendedTransfer.

        Application that has been transferred into  # noqa: E501

        :param destination_application: The destination_application of this BridgeAttendedTransfer.  # noqa: E501
        :type: str
        """

        self._destination_application = destination_application

    @property
    def destination_bridge(self):
        """Gets the destination_bridge of this BridgeAttendedTransfer.  # noqa: E501

        Bridge that survived the merge result  # noqa: E501

        :return: The destination_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: str
        """
        return self._destination_bridge

    @destination_bridge.setter
    def destination_bridge(self, destination_bridge):
        """Sets the destination_bridge of this BridgeAttendedTransfer.

        Bridge that survived the merge result  # noqa: E501

        :param destination_bridge: The destination_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :type: str
        """

        self._destination_bridge = destination_bridge

    @property
    def destination_link_first_leg(self):
        """Gets the destination_link_first_leg of this BridgeAttendedTransfer.  # noqa: E501

        First leg of a link transfer result  # noqa: E501

        :return: The destination_link_first_leg of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._destination_link_first_leg

    @destination_link_first_leg.setter
    def destination_link_first_leg(self, destination_link_first_leg):
        """Sets the destination_link_first_leg of this BridgeAttendedTransfer.

        First leg of a link transfer result  # noqa: E501

        :param destination_link_first_leg: The destination_link_first_leg of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._destination_link_first_leg = destination_link_first_leg

    @property
    def destination_link_second_leg(self):
        """Gets the destination_link_second_leg of this BridgeAttendedTransfer.  # noqa: E501

        Second leg of a link transfer result  # noqa: E501

        :return: The destination_link_second_leg of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._destination_link_second_leg

    @destination_link_second_leg.setter
    def destination_link_second_leg(self, destination_link_second_leg):
        """Sets the destination_link_second_leg of this BridgeAttendedTransfer.

        Second leg of a link transfer result  # noqa: E501

        :param destination_link_second_leg: The destination_link_second_leg of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._destination_link_second_leg = destination_link_second_leg

    @property
    def destination_threeway_bridge(self):
        """Gets the destination_threeway_bridge of this BridgeAttendedTransfer.  # noqa: E501

        Bridge that survived the threeway result  # noqa: E501

        :return: The destination_threeway_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Bridge
        """
        return self._destination_threeway_bridge

    @destination_threeway_bridge.setter
    def destination_threeway_bridge(self, destination_threeway_bridge):
        """Sets the destination_threeway_bridge of this BridgeAttendedTransfer.

        Bridge that survived the threeway result  # noqa: E501

        :param destination_threeway_bridge: The destination_threeway_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :type: Bridge
        """

        self._destination_threeway_bridge = destination_threeway_bridge

    @property
    def destination_threeway_channel(self):
        """Gets the destination_threeway_channel of this BridgeAttendedTransfer.  # noqa: E501

        Transferer channel that survived the threeway result  # noqa: E501

        :return: The destination_threeway_channel of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._destination_threeway_channel

    @destination_threeway_channel.setter
    def destination_threeway_channel(self, destination_threeway_channel):
        """Sets the destination_threeway_channel of this BridgeAttendedTransfer.

        Transferer channel that survived the threeway result  # noqa: E501

        :param destination_threeway_channel: The destination_threeway_channel of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._destination_threeway_channel = destination_threeway_channel

    @property
    def destination_type(self):
        """Gets the destination_type of this BridgeAttendedTransfer.  # noqa: E501

        How the transfer was accomplished  # noqa: E501

        :return: The destination_type of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this BridgeAttendedTransfer.

        How the transfer was accomplished  # noqa: E501

        :param destination_type: The destination_type of this BridgeAttendedTransfer.  # noqa: E501
        :type: str
        """
        if destination_type is None:
            raise ValueError("Invalid value for `destination_type`, must not be `None`")  # noqa: E501

        self._destination_type = destination_type

    @property
    def is_external(self):
        """Gets the is_external of this BridgeAttendedTransfer.  # noqa: E501

        Whether the transfer was externally initiated or not  # noqa: E501

        :return: The is_external of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this BridgeAttendedTransfer.

        Whether the transfer was externally initiated or not  # noqa: E501

        :param is_external: The is_external of this BridgeAttendedTransfer.  # noqa: E501
        :type: bool
        """
        if is_external is None:
            raise ValueError("Invalid value for `is_external`, must not be `None`")  # noqa: E501

        self._is_external = is_external

    @property
    def replace_channel(self):
        """Gets the replace_channel of this BridgeAttendedTransfer.  # noqa: E501

        The channel that is replacing transferer_first_leg in the swap  # noqa: E501

        :return: The replace_channel of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._replace_channel

    @replace_channel.setter
    def replace_channel(self, replace_channel):
        """Sets the replace_channel of this BridgeAttendedTransfer.

        The channel that is replacing transferer_first_leg in the swap  # noqa: E501

        :param replace_channel: The replace_channel of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._replace_channel = replace_channel

    @property
    def result(self):
        """Gets the result of this BridgeAttendedTransfer.  # noqa: E501

        The result of the transfer attempt  # noqa: E501

        :return: The result of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BridgeAttendedTransfer.

        The result of the transfer attempt  # noqa: E501

        :param result: The result of this BridgeAttendedTransfer.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def transfer_target(self):
        """Gets the transfer_target of this BridgeAttendedTransfer.  # noqa: E501

        The channel that is being transferred to  # noqa: E501

        :return: The transfer_target of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._transfer_target

    @transfer_target.setter
    def transfer_target(self, transfer_target):
        """Sets the transfer_target of this BridgeAttendedTransfer.

        The channel that is being transferred to  # noqa: E501

        :param transfer_target: The transfer_target of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._transfer_target = transfer_target

    @property
    def transferee(self):
        """Gets the transferee of this BridgeAttendedTransfer.  # noqa: E501

        The channel that is being transferred  # noqa: E501

        :return: The transferee of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._transferee

    @transferee.setter
    def transferee(self, transferee):
        """Sets the transferee of this BridgeAttendedTransfer.

        The channel that is being transferred  # noqa: E501

        :param transferee: The transferee of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """

        self._transferee = transferee

    @property
    def transferer_first_leg(self):
        """Gets the transferer_first_leg of this BridgeAttendedTransfer.  # noqa: E501

        First leg of the transferer  # noqa: E501

        :return: The transferer_first_leg of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._transferer_first_leg

    @transferer_first_leg.setter
    def transferer_first_leg(self, transferer_first_leg):
        """Sets the transferer_first_leg of this BridgeAttendedTransfer.

        First leg of the transferer  # noqa: E501

        :param transferer_first_leg: The transferer_first_leg of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """
        if transferer_first_leg is None:
            raise ValueError("Invalid value for `transferer_first_leg`, must not be `None`")  # noqa: E501

        self._transferer_first_leg = transferer_first_leg

    @property
    def transferer_first_leg_bridge(self):
        """Gets the transferer_first_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501

        Bridge the transferer first leg is in  # noqa: E501

        :return: The transferer_first_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Bridge
        """
        return self._transferer_first_leg_bridge

    @transferer_first_leg_bridge.setter
    def transferer_first_leg_bridge(self, transferer_first_leg_bridge):
        """Sets the transferer_first_leg_bridge of this BridgeAttendedTransfer.

        Bridge the transferer first leg is in  # noqa: E501

        :param transferer_first_leg_bridge: The transferer_first_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :type: Bridge
        """

        self._transferer_first_leg_bridge = transferer_first_leg_bridge

    @property
    def transferer_second_leg(self):
        """Gets the transferer_second_leg of this BridgeAttendedTransfer.  # noqa: E501

        Second leg of the transferer  # noqa: E501

        :return: The transferer_second_leg of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Channel
        """
        return self._transferer_second_leg

    @transferer_second_leg.setter
    def transferer_second_leg(self, transferer_second_leg):
        """Sets the transferer_second_leg of this BridgeAttendedTransfer.

        Second leg of the transferer  # noqa: E501

        :param transferer_second_leg: The transferer_second_leg of this BridgeAttendedTransfer.  # noqa: E501
        :type: Channel
        """
        if transferer_second_leg is None:
            raise ValueError("Invalid value for `transferer_second_leg`, must not be `None`")  # noqa: E501

        self._transferer_second_leg = transferer_second_leg

    @property
    def transferer_second_leg_bridge(self):
        """Gets the transferer_second_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501

        Bridge the transferer second leg is in  # noqa: E501

        :return: The transferer_second_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :rtype: Bridge
        """
        return self._transferer_second_leg_bridge

    @transferer_second_leg_bridge.setter
    def transferer_second_leg_bridge(self, transferer_second_leg_bridge):
        """Sets the transferer_second_leg_bridge of this BridgeAttendedTransfer.

        Bridge the transferer second leg is in  # noqa: E501

        :param transferer_second_leg_bridge: The transferer_second_leg_bridge of this BridgeAttendedTransfer.  # noqa: E501
        :type: Bridge
        """

        self._transferer_second_leg_bridge = transferer_second_leg_bridge

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
        if issubclass(BridgeAttendedTransfer, dict):
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
        if not isinstance(other, BridgeAttendedTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
