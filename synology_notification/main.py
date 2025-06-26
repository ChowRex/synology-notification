#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main function

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/24 16:52
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
from pathlib import Path

from flask import Flask, request

from ._verify import verify_api, verify_headers, SupportedAPIProviders

app = Flask(__name__)


@verify_headers
@verify_api
@app.route('/', methods=["POST", "GET"])
def root():
    """
    Webhook root entrance
    If request use GET method, return the help document.
    If request use POST method, call the send notice method.
    :return:
    """
    if request.method == "GET":
        docs = Path(__file__).parent / "html/index.html"
        with open(docs, "r", encoding="utf-8") as _:
            return _.read()
    provider = request.args.get("api")
    provider = SupportedAPIProviders.get_provider(provider)
    result = provider.send()
    return result
