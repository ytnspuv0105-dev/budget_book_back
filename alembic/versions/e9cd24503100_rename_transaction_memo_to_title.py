"""rename transaction memo to title

Revision ID: e9cd24503100
Revises: 5710668d522e
Create Date: 2026-08-09 18:15:47.677232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9cd24503100'
down_revision: Union[str, Sequence[str], None] = '5710668d522e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "transactions",
        "memo",
        new_column_name="title",
    )


def downgrade() -> None:
    """Downgrade schema."""
    p.alter_column(
        "transactions",
        "title",
        new_column_name="memo",
    )
