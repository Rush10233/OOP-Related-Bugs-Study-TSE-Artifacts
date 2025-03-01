from urllib import request
import time


class GetUrl:
    def __init__(self,is_gcc:bool):
        if is_gcc:
            self.url='https://gcc.gnu.org/bugzilla/show_bug.cgi?id='
        else:
            self.url='https://bugs.llvm.org/show_bug.cgi?id='

    def request_url(self, bugno, filedirname ,localize=True):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        # 请求对象 + 响应对象 + 提取内容
        url=self.url + str(bugno)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        if localize is True:
            # 保存文件至本地
            filename = filedirname + str(bugno) + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
        res.close()
        time.sleep(1)
        return html

