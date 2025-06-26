#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Entrance point for uWSGI

- Author: Rex Zhou <879582094@qq.com>
- Created Time: 2025/6/24 17:01
- Copyright: Copyright © 2025 Rex Zhou. All rights reserved.
"""
from logging import basicConfig, DEBUG

from synology_notification import application

application.config["ENV"] = "production"

if __name__ == '__main__':
    basicConfig(level=DEBUG)
    application.config["ENV"] = "development"
    application.debug = True
    application.run(host="0.0.0.0", port=5555)
