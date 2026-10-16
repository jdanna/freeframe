"""merge heads: upload part size + avatar color (test/server-testing only)

Revision ID: c3d9e1f5a7b2
Revises: b8e3d5f7a921
Create Date: 2026-10-13

Once joined the upload-part-size and avatar-colour migrations when both sat on
a7d2c4e6f810. They are one chain now (main's b8c4d2e6f913, then
b8e3d5f7a921), so this is a no-op step after them. It stays because the test
server's database is stamped at this revision, and alembic must still find it.
It belongs to the test branch only.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3d9e1f5a7b2'
down_revision: Union[str, Sequence[str], None] = 'b8e3d5f7a921'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
