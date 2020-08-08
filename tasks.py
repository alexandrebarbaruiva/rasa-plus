from invoke import task
import shutil


@task
def clean(c):
    """
    Remove distribution files
    """
    shutil.rmtree("dist/", ignore_errors=True)
    shutil.rmtree("build/", ignore_errors=True)
    shutil.rmtree("rasa_plus.egg-info/", ignore_errors=True)
    shutil.rmtree("rasa_plus/__pycache__/", ignore_errors=True)


@task
def upload(c):
    """ Uploads new version to testpypi """
    clean(c)
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("python3 -m twine upload --skip-existing --repository testpypi dist/*")


@task
def release(c):
    """ Uploads new version to pypi aka releases it """
    clean(c)
    c.run("python3 setup.py sdist bdist_wheel")
    c.run("python3 -m twine upload --skip-existing dist/*")


@task
def t(c):
    """
    Run tests and it's coverage.
    """
    c.run("flake8 .")
    c.run("python3 -m pytest tests/tests.py",)


@task
def b(c):
    """
    Formats code according to PEP8's pattern
    """
    c.run("black rasa_plus/ tasks.py")
