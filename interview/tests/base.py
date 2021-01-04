import unittest
from django.test import TestCase


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        if cls._overridden_settings:
            cls._cls_overridden_context = override_settings(
                **cls._overridden_settings)
            cls._cls_overridden_context.enable()
        if cls._modified_settings:
            cls._cls_modified_context = modify_settings(cls._modified_settings)
            cls._cls_modified_context.enable()

    @classmethod
    def tearDownClass(cls):
        # cls._remove_databases_failures()
        if hasattr(cls, '_cls_modified_context'):
            cls._cls_modified_context.disable()
            delattr(cls, '_cls_modified_context')
        if hasattr(cls, '_cls_overridden_context'):
            cls._cls_overridden_context.disable()
            delattr(cls, '_cls_overridden_context')
        unittest.TestCase.tearDownClass()
