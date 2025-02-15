import time

# 在顶部导入openai模块
import openai

# 在初始化函数中设置OpenAI API密钥
openai.api_key = 'YOUR_OPENAI_API_KEY'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # ... 其他方法保持不变 ...

    def query_openai(self, user_input):
        start_time = time.time()
        # 调用OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            temperature=0.7
        )
        end_time = time.time()
        response_time = end_time - start_time
        return response.choices[0].text, response_time

    def do_POST(self):
        # ... 其他处理保持不变 ...

        user_input = content['message']

        openai_response, openai_response_time = self.query_openai(user_input)

        if openai_response_time > TIME_THRESHOLD:
            # 如果OpenAI响应时间超过阈值，切换回使用百度API
            bot_response = self.query_baidu_api(user_input)
        else:
            bot_response = openai_response

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps({'response': bot_response}).encode())
