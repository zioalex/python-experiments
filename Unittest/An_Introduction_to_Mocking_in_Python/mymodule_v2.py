#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path


class RemovalService(object):
    """A service for removing objects from the filesystem."""
    def __init__(self):
        pass
    def rm(self, filename):
        if os.path.isfile(filename):
            print("File \"{0}\" removed".format(filename))
            os.remove(filename)


class UploadService(object):
    def __init__(self, removal_service):
        self.removal_service = removal_service
    def upload_complete(self, filename):
        self.removal_service.rm(filename)

