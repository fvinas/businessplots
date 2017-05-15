# -*- encoding: utf-8 -*-

from setuptools import setup

setup(
	name="businessplots",
	version="0.1",
	description="A matplotlib extension to help draw business quality charts",
	url="https://github.com/fvinas/businessplots",
	author="Fabien Vinas",
	author_email="fabien.vinas@gmail.com",
	license="",
	packages=["businessplots"],
	install_requires=[
		"matplotlib"
	],
	zip_safe=False
)	
