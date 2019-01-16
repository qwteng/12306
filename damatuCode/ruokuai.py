# coding:utf-8
import requests
from hashlib import md5


class RClient(object):

    def __init__(self, username, password):
        self.username = username
        try:
            self.password = md5(password).hexdigest()
        except TypeError:
            self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = '120688'
        self.soft_key = '1dc815677da14ad8968ca292421c25ff'
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        print(r)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    rc = RClient('931128603', '',)
    im = open('tkcode', 'rb').read()
    print(rc.rk_create(im, 6113))

