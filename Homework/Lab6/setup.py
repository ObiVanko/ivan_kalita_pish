from setuptools import setup, find_packages

setup(
    name="Lab2",
    version="0.1",
    author="Калита Иван",
    author_email="ivan.kalita03@gmail.com",
    description="Описание проекта",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "Lab2=Lab2.main:main",  # Создание командной строки
        ],
    },
)