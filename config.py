#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5834555904:AAEL70n470e-hjaCWKEMXIQjw_cV6bKXUeQ")
    API_ID = int(os.environ.get("API_ID", "13965888"))
    API_HASH = os.environ.get("API_HASH", "5f2f806877d357ba957b7e5e1fc95a3e")
    AUTH_USERS = "6126200262"

