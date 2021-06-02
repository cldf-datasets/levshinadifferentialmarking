from setuptools import setup


setup(
    name='cldfbench_levshinadifferentialmarking',
    py_modules=['cldfbench_levshinadifferentialmarking'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'levshinadifferentialmarking=cldfbench_levshinadifferentialmarking:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
