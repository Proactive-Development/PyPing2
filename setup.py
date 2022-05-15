import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyping2',
    url='https://github.com/Proactive-Development/PyPing2',
    packages=['pyping2'],
    install_requires=['requests'],
    version="0.1.1",
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='An easy to use pinging tool'
)