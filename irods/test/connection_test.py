#! /usr/bin/env python2.6
import unittest
import os
import sys


class TestConnections(unittest.TestCase):
    """
    """

    def setUp(self):
        from irods.session import iRODSSession
        import config

        self.sess = iRODSSession(host=config.IRODS_SERVER_HOST,
                                 port=config.IRODS_SERVER_PORT,  # 4444: why?
                                 user=config.IRODS_USER_USERNAME,
                                 password=config.IRODS_USER_PASSWORD,
                                 zone=config.IRODS_SERVER_ZONE)

    def test_connection(self):
        """
        @TODO: what does get_collection return?
        There should be a better way to test this...
        Wouldn't the iRODSSession init establish the connection?
        """
        coll = self.sess.get_collection('/tempZone/home/rods')
        self.assertTrue(coll, "Connection failed.")


if __name__ == '__main__':
    # let the tests find the parent irods lib
    sys.path.insert(0, os.path.abspath('../..'))
    unittest.main()
