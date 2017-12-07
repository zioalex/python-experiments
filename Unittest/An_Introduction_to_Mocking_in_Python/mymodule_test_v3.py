#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

from unittest import mock
import unittest


class RmTestCase(unittest.TestCase):

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")


if __name__ == "__main__":
    unittest.main()
