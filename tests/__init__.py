#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests module

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/26 09:40
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
from logging import basicConfig, DEBUG
from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from pytest import fixture

from synology_notification import app

basicConfig(level=DEBUG, format="%(levelname)s %(name)s %(lineno)d %(message)s")
env_file = Path(__file__).parent.with_name(".env")
load_dotenv(env_file, override=True)
BOT_KEY = getenv("BOT_KEY")


@fixture
def client():
    """
    Create a Flask test client
    :return:
    """
    app.config['TESTING'] = True

    # pylint: disable=redefined-outer-name
    with app.test_client() as client:
        with app.app_context():
            yield client
