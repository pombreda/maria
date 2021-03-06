#!/usr/bin/python
#coding:utf-8


class Config(object):

    def __init__(self):
        self.debug = False
        self.log_file = '/tmp/maria.log'
        self.host_key = 'host.key'
        self.auth_timeout = 20
        self.check_timeout = 10
        self.select_timeout = 10
        self.host = "0.0.0.0"
        self.port = 2200
        # TODO:
        # maria.gssh.GSSHServer
        # maria.ghttp.GHTTPServer
        self.worker = "maria.gssh.GSSHServer"
        self.git_path = "git"
        self.repos_path = ""

        self.gssh_interface = "maria.gssh.GSSHInterface"
        self.ghttp_interface = "maria.ghttp.GHTTPInterface"

    def parser(self, args):
        for key in dir(args):
            if key.startswith('_'):
                continue
            new_conf = getattr(args, key)
            orig_conf = getattr(self, key, None)
            if orig_conf == new_conf:
                continue
            setattr(self, key, new_conf)

config = Config()
