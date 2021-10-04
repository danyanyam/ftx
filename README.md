# ftx

async ftx api model from korgi team

## Async examples:

```python
import os
import asyncio
from library.ftx.asyncronous.account import Account


async def main():
    acc = Account(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    info = await acc.get_account_information()
    print(info)


if __name__ == "__main__":
    asyncio.run(main())

```

## Sync example:

```python
import os
from library.ftx.account import Account


def main():
    acc = Account(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    info = acc.get_account_information()
    print(info)


if __name__ == "__main__":
   main()

```

## How to use logger

```python
from library.logging import Logger, info, warning, error, critical
```

```python
def use_case1():
    # создаем инстанс логгера. Такой логгер будет выводить аутпут только в консоль
    logger = Logger('use_case1').get_logger()

    # пользуемся логгером
    logger.info('test')      # 2021-10-04 23:04:16,893 - [I] use_case1 | (logger_examples.py:6) - test
    logger.warning('test')   # 2021-10-04 23:04:16,893 - [W] use_case1 | (logger_examples.py:6) - test
    logger.error('test')     # 2021-10-04 23:04:16,893 - [E] use_case1 | (logger_examples.py:6) - test
    logger.critical('test')  # 2021-10-04 23:04:16,893 - [C] use_case1 | (logger_examples.py:6) - test
```

```python
def use_case2():
    # создаем инстанс логгера. Такой логгер будет выводить аутпут в консоль и в указанный путь
    logger = Logger('use_case2', 'logs/my_logs.log').get_logger()

    # пользуемся логгером
    logger.info('test')      # 2021-10-04 23:04:16,893 - [I] use_case1 | (logger_examples.py:6) - test
    logger.warning('test')   # 2021-10-04 23:04:16,893 - [W] use_case1 | (logger_examples.py:6) - test
    logger.error('test')     # 2021-10-04 23:04:16,893 - [E] use_case1 | (logger_examples.py:6) - test
    logger.critical('test')  # 2021-10-04 23:04:16,893 - [C] use_case1 | (logger_examples.py:6) - test
```

```python
def use_case3():
    # допустим ты хочешь выводить в консоль все дебаг сообщения, а в логи только критические:
    logger = Logger('use_case3', 'logs/my_logs.log', console_level='DEBUG', out_level='CRITICAL').get_logger()

    # пользуемся логгером
    # попадет в консоль
    logger.info('test')      # 2021-10-04 23:04:16,893 - [I] use_case1 | (logger_examples.py:6) - test
    # попадет в консоль
    logger.warning('test')   # 2021-10-04 23:04:16,893 - [W] use_case1 | (logger_examples.py:6) - test
    # попадет в консоль
    logger.error('test')     # 2021-10-04 23:04:16,893 - [E] use_case1 | (logger_examples.py:6) - test
    # попадет в консоль и в логи
    logger.critical('test')  # 2021-10-04 23:04:16,893 - [C] use_case1 | (logger_examples.py:6) - test
```

```python
def use_case4():
    # хочешь видеть в консоли только сообщения с ошибками
    logger = Logger('use_case4', 'logs/my_logs.log', console_level='ERROR').get_logger()

    # пользуемся логгером
    # не уидишь это сообщение
    info('test')      # 2021-10-04 23:17:32,273 - [I] use_case3 | (logger.py:36) - test
    # не уидишь это сообщение
    warning('test')   # 2021-10-04 23:17:32,273 - [W] use_case3 | (logger.py:44) - test
    # увидишь это в консоли
    error('test')     # 2021-10-04 23:17:32,273 - [E] use_case3 | (logger.py:48) - test
    # увидишь это в консоли
    critical('test')  # 2021-10-04 23:17:32,273 - [C] use_case3 | (logger.py:52) - test
```
