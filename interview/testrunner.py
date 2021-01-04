from django.test.runner import DiscoverRunner


class NoDbTestRunner(DiscoverRunner):
    """ A test runner to test without database creation """

    def __init__(self, pattern=None, top_level=None, verbosity=1,
                 interactive=True, failfast=True, keepdb=True,
                 reverse=False, debug_mode=False, debug_sql=False, parallel=0,
                 tags=None, exclude_tags=None, **kwargs):

        failfast = True
        keepdb = True
        parallel = False
        reverse = False

        super().__init__(pattern, top_level, verbosity,
                         interactive, failfast, keepdb,
                         reverse, debug_mode, debug_sql, parallel,
                         tags, exclude_tags, **kwargs)

    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass
