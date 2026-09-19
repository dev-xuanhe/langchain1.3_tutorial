# -*- coding: utf-8 -*-
# langchain1.3_tutorial - 项目名称
# 05-fake-sever - 文件名称
# by 深秋 - 当前用户
# 2026/9/19 - 当前日期
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

#构造一个虚拟的DeepSeek服务端，客户端接收到的响应是 人为构造 的，主要目的是为了观察不同模式下LangChain会从响应中的哪些字段中抽取信息。
class FakeDeepSeekHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length).decode("utf-8")
        print("\n" + "=" * 100)
        json_body = None
        try:
            json_body = json.loads(raw_body)
            print("[JSON BODY]")
            print(json.dumps(json_body, ensure_ascii=False, indent=2))
        except Exception as e:
            print("[JSON PARSE ERROR]")
            print(repr(e))

        # 固定返回一个普通 JSON 字符串
        response = {
            "id": "chatcmpl-test",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": "any",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [
                            {
                                "id": "call_1",
                                "type": "function",
                                "function": {
                                    "name": json_body["tools"][0]
                                    ["function"]["name"],
                                    "arguments": json.dumps(
                                        {
                                            #故意把字段写错，用来检验
                                         'title1': '盗梦空间',
                                         'year1': 2010,
                                         'director': '克里斯托弗·诺兰',
                                         'rating': 9.3},
                                        ensure_ascii=False
                                    )
                                }
                            }
                        ]
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 1,
                "completion_tokens": 1,
                "total_tokens": 2
            }
        }

        print("\n" + "=" * 100)
        print("[RESPONSE]")
        print(json.dumps(response, ensure_ascii=False, indent=2))
        body = json.dumps(response, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

def main():
    server = HTTPServer(("127.0.0.1", 8889), FakeDeepSeekHandler)
    print("Fake DeepSeek server running at http://127.0.0.1:8889")
    server.serve_forever()

if __name__ == "__main__":
    main()