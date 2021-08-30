import asyncio


async def f():
    print('f() function')


async def g():
    print('g() function')
    await asyncio.sleep(5)
    print('g() function completed!')


async def main():
    main_loop.create_task(g())
    await f()


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())  # Запуск задачи (работает пока не выполняется функиця)
main_loop.run_forever()