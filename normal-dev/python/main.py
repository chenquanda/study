import asyncio
import time
# 同步版本 - 浪费时间等待
def fetch_data():
    time.sleep(2)  # 模拟网络请求
    return "数据"
    
def main():
    start = time.time()
    print(fetch_data(), time.time() - start)  # 等待2秒
    print(fetch_data(), time.time() - start)  # 再等待2秒
    # 总共4秒

# 异步版本 - 同时处理多个请求
async def async_fetch_data():
    await asyncio.sleep(2)  # 模拟异步网络请求
    return "数据"
    
async def async_main():
    # 同时发起两个请求，总共2秒
    start = time.time()
    result1, result2 = await asyncio.gather(
        async_fetch_data(),
        async_fetch_data()
    )
    print(result1, result2, time.time() - start)

if __name__ == "__main__":
    # asyncio.run(async_main())
    main()
