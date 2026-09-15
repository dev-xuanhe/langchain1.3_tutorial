# -*- coding: utf-8 -*-
# langchain1.3_tutorial - 项目名称
# 06-ainvoke - 文件名称
# by 深秋 - 当前用户
# 2026/9/13 - 当前日期
import asyncio
import time

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

#优先加载配置文件
load_dotenv(override=True)

API_KEY = os.getenv("DASHSCOPE_API_KEY")
BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

#初始化大模型
model_openai = init_chat_model(
    model='qwen3.7-flash',
    model_provider='openai',
    api_key=API_KEY,
    base_url=BASE_URL,
)

#定义一个携程方法
async def demo_async_invoke():
    print("=== 演示：ainvoke 的异步（非阻塞）效果 ===")
    # 记录开始时间
    start_time = time.perf_counter()

    print("程序开始。。。")

    #1. 创建任务,不会立即执行的，会挂起，在await当前任务后才执行完成,这个需要创建一个任务
    print(">>> 发起异步模型调用 (ainvoke) 。。。")
    async_task = asyncio.create_task(model_openai.ainvoke("用一句话解释人工智能。"))

    #2. 并发执行其他任务
    print(">>> 模型请求已经在后台发送，继续执行本地逻辑。。。")
    for i in range(3):
        #使用异步等待，释放控制权，await会切换任务给其他的任务执行
        await asyncio.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务。。。（已经耗时{time.perf_counter() - start_time:.2f}s）")

    #3. 获取模型的结果
    print(">>> 本地任务完成，检查模型的状态。。。")
    # 返回结果
    response = await async_task

    end_time = time.perf_counter()
    print(f">>> 模型返回：{response.content}")
    print(f"=== 总运行耗时：{end_time - start_time:.2f}s ===")

async def main():
    """
    主函数
    Returns:
    """
    await demo_async_invoke()

if __name__ == '__main__':
    asyncio.run(main())








