"""merge heads (test/server-testing only)

Joined c3d9e1f5a7b2 (another test-only no-op) and main's e3a7c1d9b5f2 while
#487 and #493 were both unmerged. Both are on main now; this stays, a no-op,
because the test server's database may be stamped here or at c3d9e1f5a7b2 and
alembic must still find them. It belongs to the test branch only.

Revision ID: f6b2d8a4c0e1
Revises: c3d9e1f5a7b2, e3a7c1d9b5f2
Create Date: 2026-10-16

"""
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = 'f6b2d8a4c0e1'
down_revision: Union[str, Sequence[str], None] = ('c3d9e1f5a7b2', 'e3a7c1d9b5f2')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
