import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ImPyParser',  
     version='0.1',
     scripts=['ImPyParser'] ,
     author="Joshua Mayers",
     author_email="joshuamayers@gmail.com",
     description="A python import parser",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/JoshuaRM/ImportParser",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

