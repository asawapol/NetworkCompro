import asyncio

async def main():
    print('asawapol')
    task = asyncio.create_task(foo('text')) # สร้าง task และส่งค่า text ไปให้ foo   
    await task
    print('finish')

async def foo(text):
    print(text)
    await asyncio.sleep(5)

asyncio.run(main())