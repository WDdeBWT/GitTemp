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
import student_tools

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
        return_message = account_tools.verify_account(user_name, password)
        if return_message:
            self.write(json.dumps(return_message))
            return
        else:
            self.write(json.dumps('disallow'))
            return


    def post(self):
        data=json_decode(self.request.body)
        if not account_tools.verify_account(data['user_name'], data['password']):
            self.write(json.dumps('disallow')) #如果密码错误，返回禁止访问信息
            return

        if data['option_type'] == 'update_password':
            if account_tools.update_password(data['user_name'], data['password'], data['the_password']):
                self.write(json.dumps('True'))
                return
            else:
                self.write(json.dumps('Error: AccountHandler POST update_password'))
                return
        self.write(json.dumps('Error: AccountHandler POST'))
        return

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class ManagementAccountHandler(tornado.web.RequestHandler):
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


class ManagementStudentHandler(tornado.web.RequestHandler):
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
        student_tools.batch_import_student(file_path)
        return
    
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class ShowAccountHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        show_list = account_tools.show_account()
        self.write(json.dumps(show_list))
        return

    def post(self):
        self.write("Hello world - POST")
        return

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class JudgeHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write("Hello world - GET")
        return

    def post(self):
        data=json_decode(self.request.body)
        # verify account
        if not account_tools.verify_account(data['user_name'], data['password']):
            self.write(json.dumps('disallow')) #如果密码错误，返回禁止访问信息
            return
        
        if data['option_type'] == 'get_student_list':
            student_list = student_tools.get_student_list(data['user_name'])
            self.write(json.dumps(student_list))
            return
        elif data['option_type'] == 'set_score':
            student_tools.set_score(data['the_student_id'], data['user_name'], data['score_list'])
            self.write(json.dumps('True'))
            return
        elif data['option_type'] == 'get_score':
            class_code = account_tools.get_class_code(data['user_name'])
            score_list = student_tools.export_score_by_class(class_code)
            self.write(json.dumps(score_list))
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
    (r"/ajax_management_account", ManagementAccountHandler),
    (r"/ajax_management_student", ManagementStudentHandler),
    (r"/ajax_show_account", ShowAccountHandler),
    (r"/ajax_judge", JudgeHandler)
    ],**settings)

if __name__ == '__main__':
    application.listen(8088)
    tornado.ioloop.IOLoop.instance().start()
