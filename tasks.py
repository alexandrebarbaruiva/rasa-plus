from invoke import task
import shutil


@task
def clean(c):
    shutil.rmtree("dist/", ignore_errors=True)
    shutil.rmtree("build/", ignore_errors=True)
    shutil.rmtree("rasa_plus.egg-info/", ignore_errors=True)
    shutil.rmtree("rasa_plus/__pycache__/", ignore_errors=True)


@task
def upload(c):
    clean(c)
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("python3 -m twine upload --skip-existing --repository testpypi dist/*")


@task
def release(c):
    clean(c)
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("python3 -m twine upload --skip-existing dist/*")


@task
def t(c):
    c.run("python3 -m pytest tests/tests.py",)
