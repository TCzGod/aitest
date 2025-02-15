# 论文综述写作器系统介绍

ChatGPT作为一个强大的大语言模型，事先进行过巨量的迭代训练和大力的人为评测测试，为各个领域的发展和应用提供了无限的充满希望的前景。本文研究聚焦基于ChatGPT的专题综述写作器系统，意义在于它不同于以往传统的专题综述辅助写作工具，会额外提供给使用者AI化的功能来助力他们的写作工作，具有自动化，交互性强等一系列新型产品属性。 

# 前端技术实现说明

前端基于 HTML、CSS 和 JavaScript 实现了一个简洁的聊天界面。通过与后端 API 进行交互，用户能够方便地提交请求并接收生成的文本综述。

## HTML 是用于创建网页的标准标记语言。在本示例中，HTML 用于构建聊天界面的基本结构：

- `<div>`: 创建一个容器来包含整个聊天界面。
- `<div></div>`: 一个用于显示消息的盒子。
- `<input type="text" />`: 一个文本输入框，用户可以在这里输入问题。
- `<button>发送</button>`: 一个按钮，当用户点击时会触发 `sendMessage` 函数。

```html
<div id="chat-container">
  <div id="chat-box"></div>
  <input type="text" id="user-input" />
  <button onclick="sendMessage()">发送</button>
</div>

## JavaScript 是一种脚本语言，常用于创建动态和交互式的网页内容。在本示例中，JavaScript 用于处理用户输入、与后端通信以及更新页面内容：

- `sendMessage():`: 当用户点击“发送”按钮时调用此函数。获取输入框的内容并将其添加到聊天盒子中。使用 fetch API 向后端发送 POST 请求，并传递用户的输入。获取后端返回的数据并显示在聊天界面中。清空输入框，以便用户继续输入。
- `fetch()`: 向后端发送一个 HTTP 请求，并处理响应。请求的内容是用户输入的数据，响应则是从后端返回的聊天信息。

# 后端技术实现说明

这个Python代码实现了一个简单的HTTP服务器，用于接收POST请求并与一个对话接口（假设是百度的API）进行交互。代码涉及到的技术包括：

## HTTP 服务器技术
**BaseHTTPRequestHandler 和 HTTPServer**：这些是Python标准库 `http.server` 模块中的类，用于创建一个简单的HTTP服务器。`BaseHTTPRequestHandler` 负责处理不同的HTTP请求方法（如 POST），而 `HTTPServer` 用于启动并运行服务器。

## JSON 处理
**json 模块**：Python内建的 `json` 模块用于处理JSON数据。`json.loads()` 将收到的请求体（POST请求数据）解析成Python的字典对象，`json.dumps()` 将Python字典对象转换为JSON格式的字符串来响应客户端。

## 与外部API交互
**requests 模块**：这个第三方库用于向外部API发送HTTP请求。`requests.post()` 用于发送POST请求，携带JSON数据并接收来自百度API的响应。该API接口是 百度的对话接口，具体用于根据用户输入生成对话内容。

## 数据响应
从API返回的数据中提取生成的对话内容（`response.json()["result"]`），然后通过 `wfile.write()` 将响应以JSON格式返回给客户端。






