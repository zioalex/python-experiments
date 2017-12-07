#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Creating Mock Instances

from mymodule_v2 import RemovalService, UploadService

from unittest import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('mymodule_v2.os.path')
    @mock.patch('mymodule_v2.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")
