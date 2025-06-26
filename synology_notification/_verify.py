#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify the requests headers module

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/24 17:18
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
__all__ = [
    "SupportedAPIProviders",
    "verify_headers",
    "verify_api",
]

from enum import Enum
from functools import wraps
from typing import Callable

from flask import request, current_app

from .api import AbstractServiceProvider
from .api import WecomGroupBotSender


# pylint: disable=invalid-name
class SupportedAPIProviders(Enum):
    """Supported API providers"""

    wecom_group_bot = WecomGroupBotSender

    @classmethod
    def _all_providers(cls) -> dict[str, type[AbstractServiceProvider]]:
        """
        Return dict of supported API providers
        :return:
        """
        providers = {_.name: _.value for _ in cls}
        return providers

    @classmethod
    def get_provider(cls, provider: str) -> AbstractServiceProvider:
        """
        Get a specific API provider.
        :param provider: Provider name.
        :return:
        """
        providers = cls._all_providers()
        if not provider:
            msg = "Must provide a provider name"
            raise ValueError(msg)
        if provider not in providers:
            msg = f"Unsupported API provider: {provider}"
            current_app.logger.critical(msg)
            raise ValueError(msg)
        instance = providers[provider]()
        return instance


def verify_api(function: Callable):
    """
    Decorator to verify and convert api string to instance
    :param function: Function to decorate
    :return:
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        if request.method != "POST":
            return function(*args, **kwargs)
        api = request.args.get("api", "")
        current_app.logger.debug("Specify API: %s", api)
        api_provider = SupportedAPIProviders.get_provider(api)
        current_app.logger.debug("Converted API provider: %s", api_provider)
        kwargs["api"] = api_provider
        return function(*args, **kwargs)

    return wrapper


def verify_headers(function: Callable):
    """
    Decorator to verify request headers
    :param function: Function to decorate
    :return:
    """

    @wraps
    def wrapper(*args, **kwargs) -> Callable:
        """
        Check request headers
        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return:
        """
        if request.method != "POST":
            return function(*args, **kwargs)
        headers = request.headers
        provider = kwargs["api"]
        assert isinstance(provider, AbstractServiceProvider)
        for required in provider.required_header_keys():
            if required not in headers:
                msg = f"Missing required header key: {required}"
                current_app.logger.critical(msg)
                raise ValueError(msg)
        return function(*args, **kwargs)

    return wrapper
