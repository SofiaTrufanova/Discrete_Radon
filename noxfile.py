"""Nox sessions."""

import tempfile

import nox


nox.options.sessions = "lint", "safety", "tests", "mypy", "pytype", "black", "xdoctest"


locations = "src", "tests", "noxfile.py", "docs/conf.py"


@nox.session(python=["3"])
def lint(session) -> None:
    """Checks codestyle."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python=["3"])
def tests(session) -> None:
    """Runs tests."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python="3")
def black(session) -> None:
    """Runs black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3")
def safety(session) -> None:
    """Checks safety."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3"])
def mypy(session) -> None:
    """Runs mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python="3")
def pytype(session) -> None:
    """Run the static type checker."""
    args = session.posargs or ["--disable=import-error", *locations]
    session.install("pytype")
    session.run("pytype", *args)


package = "radon_sofia"


@nox.session(python=["3"])
def typeguard(session) -> None:
    """Checks types."""
    args = session.posargs or ["-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("pytest", "pytest-mock", "typeguard")
    session.run("pytest", f"--typeguard-packages={package}", *args)


@nox.session(python=["3"])
def xdoctest(session) -> None:
    """Run examples with xdoctest."""
    args = session.posargs or ["all"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)


@nox.session(python="3")
def docs(session) -> None:
    """Build the documentation."""
    session.run("poetry", "install", "--no-dev", external=True)
    session.install("sphinx", "sphinx-autodoc-typehints")
    session.run("sphinx-build", "docs", "docs/_build")
