#!/usr/bin/python3
"""LockedClass with no class or object attribute."""


class LockedClass:
    """that prevents the user from dynamically creating new instance."""
    __slots__ = ['first_name']
