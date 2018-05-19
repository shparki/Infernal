from setuptools import find_packages, setup

setup(
	name='infernal',
	version='0.1.1',
	description='Riot API wrapper and extension in Python',
	url='https://github.com/shparki/Infernal',
	author='Shparki',
	author_email='murrmat@gmail.com',
	license='MIT',
	packages=find_packages(),
	zip_safe=False,
	install_requires=[
		'pandas',
		'numpy',
	]
)