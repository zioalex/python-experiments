#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import facebook
import simple_facebook
from unittest import mock
import unittest

class SimpleFacebookTestCase(unittest.TestCase):
    @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
    def test_post_message(self, mock_put_object):
        sf = simple_facebook.SimpleFacebook("fake oauth token")
        sf.post_message("Hello World ")
        # verify
        mock_put_object.assert_called_with(message="Hello World!")


if __name__ == "__main__":
    unittest.main()
