# coding:utf-8
# @__Author__ = "WDdeBWT"
# @__Date__ : "2018/05/07"

import os
import json

import tornado.ioloop
import tornado.web
import tornado.options
from tornado.escape import json_decode

import account_tools

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("MainHandler - GET")
        return

class AccountHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        # verify account
        user_name = self.get_argument('user_name', '')
        password = self.get_argument('password', '')
        user_type = self.get_argument('user_type', '')
        return_message = account_tools.verify_account(user_name, password, user_type)
        if return_message:
            self.write(json.dumps(return_message))
            return
        else:
            self.write(json.dumps('disallow'))
            return


    def post(self):
        data=json_decode(self.request.body)

        if data['user_type'] == 'student':
            if not account_tools.verify_account(data['user_name'], data['password'], data['user_type']):
                self.write(json.dumps('disallow')) #如果密码错误，返回禁止访问信息
                return

            if data['option_type'] == 'update_password':
                if account_tools.update_password(data['user_name'], data['password'], data['the_password'], data['user_type']):
                    self.write(json.dumps('True'))
                    return
                else:
                    self.write(json.dumps('Error: AccountManagementHandler POST update_password'))
                    return
            self.write(json.dumps('Error: AccountManagementHandler POST student'))
            return

        elif data['user_type'] == 'admin':
            if not account_tools.verify_account(data['user_name'], data['password'], 'admin'):
                self.write(json.dumps('disallow')) #如果密码错误，返回禁止访问信息
                return

            if data['option_type'] == 'update_password':
                if account_tools.update_password(data['user_name'], data['password'], data['the_password'], data['user_type']):
                    self.write(json.dumps('True'))
                    return
                else:
                    self.write(json.dumps('Error: AccountManagementHandler POST update_password'))
                    return
            elif data['option_type'] == 'create_account':
                self.write(json.dumps(account_tools.create_account(data['the_user_name'], data['the_password'], data['the_user_type'], data['the_real_name'])))
                return
            elif data['option_type'] == 'delete_account':
                self.write(json.dumps(account_tools.delete_account(data['the_user_name'])))
                return
            elif data['option_type'] == 'init_password':
                self.write(json.dumps(account_tools.init_password(data['the_user_name'])))
                return
        else:
            self.write(json.dumps('Error: Unknown user_type'))
            return
    
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class ManagementHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write("Hello world - GET")
        return

    def post(self):
        file_path = 'temp.xlsx'
        with open(file_path, 'wb') as up:
            up.write(self.request.body)
        account_tools.batch_import_users(file_path)
        return
    
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class AjaxHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write("Hello world - GET")
        return

    def post(self):
        self.write("Hello world - POST")
        return
    
    def options(self):
        # no body
        self.set_status(204)
        self.finish()

settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/ajax_test", AjaxHandler),
    (r"/ajax_account", AccountHandler),
    (r"/ajax_management", ManagementHandler)
    ],**settings)

if __name__ == '__main__':
    application.listen(8088)
    tornado.ioloop.IOLoop.instance().start()
