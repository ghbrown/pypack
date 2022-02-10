

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='<PACKAGE_NAME>',  
    version='0.0.0',
    scripts=['bin/<PACKAGE_NAME>'] ,
    author='Gabriel H. Brown',
    author_email='gabriel.h.brown@gmail.com',
    description=<PACKAGE_DESCRIPTION>,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ghbrown/'<PACKAGE_NAME>,
    packages=setuptools.find_packages(),
    #include_package_data = True, #include non-Python files specified in MANIFEST.in
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
    ],
    keywords=[
        <LIST_OF_KEYWORDS>
        'scientific',
        'engineering',
    ],
    install_requires=[
        <REQUIRED_PACKAGES>
        'numpy',
        'matplotlib',
    ],
 )
