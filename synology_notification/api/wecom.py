#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wecom API provider

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/25 14:33
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
__all__ = ["WecomGroupBotSender"]

from typing import List

from flask import request
from pywgb import SmartBot

from ._abstract import AbstractServiceProvider


class WecomGroupBotSender(AbstractServiceProvider):
    """Wecom GroupBot notification class"""

    _Required_Headers_Key = "Bot-Key"

    @classmethod
    def required_header_keys(cls) -> List[str]:
        """
        Wecom GroupBot notification header keys
        :return: keys
        """
        return [cls._Required_Headers_Key]

    def send(self) -> dict:
        """
        Wecom GroupBot notification send message
        :return: Result dict
        """
        key = request.headers[self._Required_Headers_Key].strip()
        bot = SmartBot(key)
        text = request.args["text"].strip()
        result = bot.send(text)
        return result
