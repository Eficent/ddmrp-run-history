# -*- coding: utf-8 -*-
#  Copyright 2018 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import xmlrpclib


def connect_to_odoo_server():
    """Connect via RPC after ask for credentials."""
    server_url = raw_input("Server URL: ")
    db_name = raw_input("Database name: ")
    username = raw_input("User name: ")
    pwd = raw_input("Password: ")
    if not db_name:
        db_name = raw_input("Database name: ")
    server_xmlrpc_common = '%s/xmlrpc/common' % server_url
    server_xmlrpc_object = '%s/xmlrpc/object' % server_url
    # Get the uid
    sock_common = xmlrpclib.ServerProxy(server_xmlrpc_common, allow_none=True)
    uid = sock_common.login(db_name, username, pwd)
    # replace localhost with the address of the server
    sock = xmlrpclib.ServerProxy(server_xmlrpc_object, allow_none=True)
    return db_name, sock, uid, pwd
