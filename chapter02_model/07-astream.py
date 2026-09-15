# -*- coding: utf-8 -*-
# langchain1.3_tutorial - 项目名称
# 07-astream - 文件名称
# by 深秋 - 当前用户
# 2026/9/14 - 当前日期

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import time
import asyncio

#优先加载配置
load_dotenv(override=True)

API_KEY = os.getenv("DASHSCOPE_API_KEY")
BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

#初始化模型
model_openai = init_chat_model(
    model='qwen3.7-flash',
    model_provider='openai',
    api_key=API_KEY,
    base_url=BASE_URL,
)

async def demo_async_astream():
    print("=== 演示：astream 的异步（非阻塞）效果 ===")
    # 记录开始时间
    start_time = time.perf_counter()

    print("程序开始。。。")

    # 1. 创建任务,不会立即执行的，会挂起，在await当前任务后才执行完成
    print(">>> 发起异步模型调用 (astream) 。。。")
    res = model_openai.astream("请用一句话解释机器学习的基本概念。")

    # 2. 在等待流式响应的同时，执行其他任务
    print(">>> 流式请求已发送，程序无需等待，继续执行其他异步任务...")
    for i in range(3):
        # 使用 asyncio.sleep 而非 time.sleep
        # 这允许事件循环在等待时去处理上面的 stream_resp 网络 IO
        await asyncio.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务... (已耗时 {time.perf_counter() - start_time:.2f}s)")

    # 3. 现在开始处理流式结果
    print(">>> 模拟任务已完成，开始读取缓冲区中的流式结果...")
    end_time = time.perf_counter()
    print(">>> 流式输出：", end="", flush=True)

    async for chunk in res:
        # LangChain的消息块通常通过 .content 获取内容
        content = chunk.content if hasattr(chunk, "content") else str(chunk)
        print(content, end="", flush=True)

    print("\n>>> 流式输出结束\n")
    print(f" === 总运行耗时：{end_time - start_time:.2f}s ===")

async def main():
    await demo_async_astream()

if __name__ == "__main__":
    asyncio.run(main())

