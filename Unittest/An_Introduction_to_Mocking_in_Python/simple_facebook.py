#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import facebook


class SimpleFacebook(object):
    def __init__(self, oauth_token):
        self.graph = facebook.GraphAPI(oauth_token)
    def post_message(self, message):
        """Posts a message to the Facebook wall."""
        self.graph.put_object("me", "feed", message=message)
