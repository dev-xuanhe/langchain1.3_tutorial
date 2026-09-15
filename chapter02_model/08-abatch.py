# -*- coding: utf-8 -*-
# langchain1.3_tutorial - 项目名称
# 08-abatch - 文件名称
# by 深秋 - 当前用户
# 2026/9/14 - 当前日期
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import asyncio
import time
import os

load_dotenv(override=True)

#用DeepSeek的
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

#初始化
model_deepseek = init_chat_model(
    model='deepseek-flash',
    model_provider='deepseek',
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

async def demo_async_abatch():
    print("=== 演示：abatch 的异步（非阻塞）效果 ===")

    start_time = time.perf_counter()

    print("程序开始。。。")

    # 1. 发起异步批量请求
    # 关键修改：使用 create_task 让协程立即在后台执行
    print(">>> 发起异步模型调用 (abatch) 。。。")
    async_task = asyncio.create_task(model_deepseek.abatch("用一句话解释人工智能。"))

    # 2. 在等待批量处理的同时，执行其他任务
    print(">>> 批量任务已在后台运行，主程序继续执行...")
    for i in range(3):
        # 关键修改：使用 asyncio.sleep 允许后台任务获取 CPU 时间片进行网络请求
        await asyncio.sleep(1)
        print(f">>> 正在执行第{i + 1}个任务... (已耗时 {time.perf_counter() - start_time:.2f}s)")

    # 3. 等待批量处理结果
    print(">>> 其他任务已完成，现在获取后台批量任务的结果...")
    # 此时 batch_task 可能已经完成，或者我们在这里等待它完成
    responses = await async_task

    end_time = time.perf_counter()

    for res in responses:
        content = res.content if hasattr(res, "content") else str(res)
        print(f">>> 响应内容：{content}")

    print(f"{end_time - start_time:.2f}s")

async def main():
    await demo_async_abatch()

if __name__ == "__main__":
    asyncio.run(main())