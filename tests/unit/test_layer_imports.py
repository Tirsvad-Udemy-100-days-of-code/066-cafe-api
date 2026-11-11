"""Checks that the inner layers import no framework or outer layer."""

import ast
from pathlib import Path

import pytest

PACKAGE_ROOT = Path(__file__).resolve().parents[2] / "src" / "cafe_api"
FORBIDDEN_PREFIXES = (
    "flask",
    "flask_sqlalchemy",
    "sqlalchemy",
    "cafe_api.infrastructure",
    "cafe_api.presentation",
)


def _imported_modules(path: Path) -> list[str]:
    modules: list[str] = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            modules.append(node.module)
    return modules


def _is_forbidden(module: str) -> bool:
    return any(
        module == prefix or module.startswith(prefix + ".")
        for prefix in FORBIDDEN_PREFIXES
    )


@pytest.mark.parametrize("layer", ["domain", "application"])
def test_inner_layer_imports_no_framework_or_outer_layer(layer: str) -> None:
    files = sorted((PACKAGE_ROOT / layer).rglob("*.py"))
    assert files, "layer has no source files"

    offenders = [
        f"{path.relative_to(PACKAGE_ROOT)} imports {module}"
        for path in files
        for module in _imported_modules(path)
        if _is_forbidden(module)
    ]

    assert offenders == []
