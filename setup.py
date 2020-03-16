import setuptools
import os
import glob


class GetPybind11Include:
    def __init__(
        self,
        user,
    ):
        self.user = user

    def __str__(
        self,
    ):
        import pybind11

        return pybind11.get_include(
            user=self.user,
        )


setuptools.setup(
    name='fastzy',
    version='0.1.3',
    author='Gal Ben David',
    author_email='gal@intsights.com',
    url='https://github.com/Intsights/fastzy',
    project_urls={
        'Source': 'https://github.com/Intsights/fastzy',
    },
    license='MIT',
    description='Python library for fast fuzzy search over a big file leveraging C++ and mbleven algorithm',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='fuzzy levenshtein mbleven wagner-fischer c++ approximate',
    python_requires='>=3.6',
    zip_safe=False,
    install_requires=[
        'pybind11',
    ],
    setup_requires=[
        'pybind11',
    ],
    package_data={},
    include_package_data=True,
    ext_modules=[
        setuptools.Extension(
            name='fastzy',
            sources=glob.glob(
                pathname=os.path.join(
                    'src',
                    'fastzy.cpp',
                ),
            ),
            language='c++',
            extra_compile_args=[
                '-Ofast',
                '-std=c++17',
            ],
            extra_link_args=[
                '-lpthread',
            ],
            include_dirs=[
                'src',
                GetPybind11Include(False),
                GetPybind11Include(True),
            ]
        ),
    ],
)
