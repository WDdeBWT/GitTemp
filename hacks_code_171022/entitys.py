class Person:

    def __init__(self, name, num_weibo, num_watch, num_fans):
        self.name = name
        self.num_weibo = num_weibo
        self.num_watch = num_watch
        self.num_fans = num_fans

    def __str__(self):
        return "name:"+str(self.name)+"num_weibo:"+str(self.num_weibo)+\
               " num_watch:"+str(self.num_watch)+"num_fans:"+str(self.num_fans)


class Weibo:
    def __init__(self, fanname, time, content, num_like, num_resend, num_comment):
        self.id = fanname
        self.time = time
        self.content = content
        self.num_like = num_like
        self.num_resend = num_resend
        self.num_comment = num_comment
