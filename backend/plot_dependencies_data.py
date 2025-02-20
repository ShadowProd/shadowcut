from settings import Settings
from setup.ioc import get_container

import dishka.plotter


async def main():
    container = get_container(Settings.from_env())
    print(dishka.plotter.render_mermaid(container))
    await container.close()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
