# 代码生成时间: 2025-08-07 10:22:40
import sys
import requests
from PyQt5.QtCore import QThread, pyqtSignal

# HTTP请求处理器类
class HttpRequestHandler(QThread):
    # 信号，用于将响应发送回主线程
    response_signal = pyqtSignal(dict)

    def __init__(self, url, method, headers=None, data=None, timeout=10):
        super().__init__()
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data
        self.timeout = timeout

    def run(self):
        """
        线程运行的方法，用于执行HTTP请求。
        """
        try:
            if self.method.upper() == 'GET':
                response = requests.get(self.url, headers=self.headers, timeout=self.timeout)
            elif self.method.upper() == 'POST':
                response = requests.post(self.url, headers=self.headers, data=self.data, timeout=self.timeout)
            else:
                self.response_signal.emit({'error': 'Unsupported HTTP method'})
                return

            # 将响应发送回主线程
            self.response_signal.emit({'status_code': response.status_code,
                                      'headers': dict(response.headers),
                                      'content': response.content})
        except requests.exceptions.RequestException as e:
            self.response_signal.emit({'error': str(e)})

# 示例使用
if __name__ == '__main__':
    # 创建一个HTTP请求处理器实例
    # 这里只是一个例子，实际应用中应根据需要替换URL和参数
    url = 'https://api.example.com/data'
    method = 'GET'
    headers = {'Content-Type': 'application/json'}
    data = None
    http_handler = HttpRequestHandler(url, method, headers, data)

    # 连接信号到槽函数，以便处理响应
    def handle_response(response):
        print('Status Code:', response.get('status_code'))
        print('Headers:', response.get('headers'))
        print('Content:', response.get('content'))

    http_handler.response_signal.connect(handle_response)

    # 启动线程
    http_handler.start()

    # 进入Qt事件循环
    app = QApplication(sys.argv)
    sys.exit(app.exec_())