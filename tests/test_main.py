#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic test module

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/27 10:49
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""

# pylint: disable=unused-import
from . import client


# pylint: disable=redefined-outer-name
def test_root_get(client):
    """
    Test home GET route
    :param client: TestClient object
    :return:
    """
    response = client.get('/')
    assert response.status_code == 200
