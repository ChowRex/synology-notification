#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test for Wecom Group Bot

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/26 22:54
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""

# pylint: disable=unused-import
from synology_notification.api import WecomGroupBotSender as WGBSender
from . import client, BOT_KEY


# pylint: disable=protected-access,redefined-outer-name
def test_wrong_provider(client):
    """
    Test home POST route for wrong provider
    :param client: TestClient object
    :return:
    """
    data = {
        "api": "wrong_provider",
        "text": "This is a test message.",
    }
    headers = {
        WGBSender._Required_Headers_Key: BOT_KEY,
        "Content-Type": "application/json"
    }
    response = client.post("/", query_string=data, headers=headers)
    assert response.status_code == 406 and "Unsupported API provider" in response.text


# pylint: disable=protected-access,redefined-outer-name
def test_none_provider(client):
    """
    Test home POST route for None provider
    :param client: TestClient object
    :return:
    """
    data = {
        "api": "",
        "text": "This is a test message.",
    }
    headers = {
        WGBSender._Required_Headers_Key: BOT_KEY,
        "Content-Type": "application/json"
    }
    response = client.post("/", query_string=data, headers=headers)
    assert response.status_code == 400 and "Must provide a provider name" in response.text


# pylint: disable=protected-access,redefined-outer-name
def test_lack_provider_required_header_key(client):
    """
    Test home POST route for lack provider required header key
    :param client: TestClient object
    :return:
    """
    data = {
        "api": "wecom_group_bot",
        "text": "This is a test message.",
    }
    headers = {"Wrong-Key": BOT_KEY, "Content-Type": "application/json"}
    response = client.post("/", query_string=data, headers=headers)
    assert response.status_code == 400 and "Missing required header key" in response.text


# pylint: disable=protected-access,redefined-outer-name
def test_success(client):
    """
    Test home POST route
    :param client: TestClient object
    :return:
    """
    data = {
        "api": "wecom_group_bot",
        "text": "This is a test message.",
    }
    assert WGBSender._Required_Headers_Key in WGBSender.required_header_keys()
    headers = {
        WGBSender._Required_Headers_Key: BOT_KEY,
        "Content-Type": "application/json"
    }
    response = client.post("/", query_string=data, json=data, headers=headers)
    assert response.status_code == 200
