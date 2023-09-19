# -*- coding: utf-8 -*-
from chaoslib.types import Configuration, Secrets
from chaoslib.exceptions import ActivityFailed
from jinja2 import Template, TemplateError
from logzero import logger

__all__ = ["template_file"]


def template_file(
    source: str,
    destination: str,
    context: dict = {},
) -> None:
    tpl = None
    try:
        with open(source) as i:
            tpl = Template(i.read())
    except OSError:
        raise ActivityFailed(f"Cannot read input file {source}")

    try:
        with open(destination, '+w') as out:
            out.write(tpl.render(**context))
    except OSError:
        raise ActivityFailed(f"Cannot write output file {destination}")
    except TemplateError:
        raise ActivityFailed(f"Failed to template file {source}")
