import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GoToTab-Biton55", # Replace with your own username
    version="0.0.1",
    author="IG: @idan_biton",
    author_email="idanbit80@gmail.com",
    description='''
    # A selenium addon (Needs to setup selenium)
    goToTab(browser=browser, tabURL="https://www.facebook.com/groups/feed/")
    ''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)