import datetime
import json


class App:
    def __init__(self, env, start_response):
        """Конструктор класса"""
        self.env = env
        self.start_response = start_response

    def get_response_data(self):
        """Задание формата вывода"""
        cur_url = self.env['HTTP_HOST'] + self.env['RAW_URI']
        cur_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return {'time': cur_time, 'url': cur_url}

    def res(self):
        """Получение объекта JSON response"""
        response = json.dumps(self.get_response_data()).encode('utf-8')
        headers = [('Content-Type', 'application/json'),
                   ('Content-Length', str(len(response)))]
        self.start_response('200 OK', headers)
        yield response


def application(env, start_response):
    return App(env, start_response).res()
