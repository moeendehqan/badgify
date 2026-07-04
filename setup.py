from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="badgify",
    version="0.1.0",
    author="Moeen Dehqan",
    author_email="moeen.dehqan@gmail.com",
    description="A Django app for generating dynamic SVG badges with customizable styles, colors, and RTL/LTR support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moeendehqan/badgify",
    project_urls={
        "Bug Tracker": "https://github.com/moeendehqan/badgify/issues",
        "Source Code": "https://github.com/moeendehqan/badgify",
        "Documentation": "https://github.com/moeendehqan/badgify#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
    ],
    include_package_data=True,
    zip_safe=False,
    keywords=["django", "badge", "svg", "dynamic", "shields", "gitlab", "github", "rtl", "badgify"],
)