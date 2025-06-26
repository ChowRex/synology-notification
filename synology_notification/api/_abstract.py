#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abstract module

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/26 08:56
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""

from abc import ABC, abstractmethod
from typing import List


class AbstractServiceProvider(ABC):
    """Abstract notification service provider class"""

    @classmethod
    @abstractmethod
    def required_header_keys(cls) -> List[str]:
        """
        Subclass must implement this method to return required header keys
        :return: List of header keys
        """

    @abstractmethod
    def send(self):
        """
        Subclass must implement this method to send message
        :return:
        """
