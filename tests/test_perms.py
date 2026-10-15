from types import SimpleNamespace as N
from src.perms import can_delete


def test_admin_needs_ownership():
    assert not can_delete(N(is_admin=True, id=1), N(owner=2))
