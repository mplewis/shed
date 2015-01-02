from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='shed-sh',
    version='1.0.0',
    description=('Don\'t run "curl | sh" again. '
                 'Use "curl | shed" to verify scripts before running.'),
    long_description=long_description,
    url='https://github.com/mplewis/shed',
    license='MIT',
    author='Matthew Lewis',
    author_email='matt@mplewis.com',
    py_modules=['shed'],
    entry_points={
        'console_scripts': [
            'shed = shed:main',
            'bashed = shed:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
        'Topic :: Text Processing :: Markup'
    ],
)
