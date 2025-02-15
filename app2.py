from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# 星火认知大模型Spark Max的URL值
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
# 星火认知大模型调用秘钥信息
SPARKAI_APP_ID = 'YOUR ID'  # 替换为你的app_id
SPARKAI_API_SECRET = 'SECRET'  # 替换为你的api_secret
SPARKAI_API_KEY = 'YOUR KEY'  # 替换为你的api_key
# 星火认知大模型的domain值
SPARKAI_DOMAIN = 'generalv3.5'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        content = json.loads(post_data)

        user_input = content['message']

        # 使用科大讯飞的ChatSparkLLM接口进行聊天生成
        spark = ChatSparkLLM(
            spark_api_url=SPARKAI_URL,
            spark_app_id=SPARKAI_APP_ID,
            spark_api_key=SPARKAI_API_KEY,
            spark_api_secret=SPARKAI_API_SECRET,
            spark_llm_domain=SPARKAI_DOMAIN,
            streaming=False,
        )

        # 创建消息对象
        messages = [ChatMessage(
            role="user",
            content=user_input
        )]

        # 创建一个回调处理程序来处理响应
        handler = ChunkPrintHandler()

        # 调用模型生成响应
        response = spark.generate([messages], callbacks=[handler])

        # 提取模型生成的回复
        bot_response = response['data']['response']

        # 发送响应回客户端
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps({'response': bot_response}).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
