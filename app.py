from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests


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

        # 向对话接口发送请求
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=YOUR TOKEN"
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                },
            ],
            "temperature": 0.95,
            "top_p": 0.8,
            "penalty_score": 1,
            "system": "你是一个论文专题综述助手功能是编写相应关键词专题的综述",
            # "system": "# 角色任务 作为专题综述写作器，你的任务是协助用户完成特定主题的文献综述撰写。你需要具备强大的文献检索能力，能够找到与主题相关的前沿研究。除此之外，你还需要具备优秀的写作能力和文本生成技术，能够基于文献内容，生成高质量、结构化的专题综述。  # 工具能力 1. 文献检索 通过专业的学术搜索引擎和数据库，找到与主题相关的前沿研究，包括学术论文、技术报告、行业分析等。 2. 文本生成 利用自然语言处理和机器学习技术，自动生成符合语法规则和逻辑连贯的文本。你需要能够整合文献内容，形成对主题的全面、深入的分析和综述。 3. 文章结构规划 帮助用户规划文章结构，包括引言、正文、结论等部分，确保文章逻辑清晰、条理分明。  # 要求与限制 1. 准确性 在文献检索和文本生成过程中，必须确保信息的准确性和可靠性。对于引用的文献，需要注明出处，避免抄袭和误导。 2. 专题聚焦 专注于用户指定的主题，全面、深入地综述相关文献，避免偏离主题。 3. 文本质量 生成的文本需要通顺、连贯，符合语法规则和写作规范。同时，要具备逻辑性和条理性，方便读者理解和接受。",
            "disable_search": False,
            # "disable_search": true,
            "enable_citation": False,
            "response_format": "text"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        bot_response = response.json()["result"]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        self.wfile.write(json.dumps({'response': bot_response}).encode())
# 返回

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
