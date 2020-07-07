from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='unogame',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    description='Play custom Uno game.',
    version='0.1',
    url='https://github.com/gcastella/UnoGame',
    author='Gerard Castellà Canals',
    author_email='gcastella.91@gmail.com',
    keywords=['python', 'board games', 'uno', 'game', 'play']
    )
