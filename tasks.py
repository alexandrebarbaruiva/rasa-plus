from invoke import task


@task
def uni(c):
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("python3 -m twine upload --skip-existing --repository testpypi dist/*")