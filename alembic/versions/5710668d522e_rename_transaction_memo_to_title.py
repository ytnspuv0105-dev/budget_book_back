"""rename transaction memo to title

Revision ID: 5710668d522e
Revises: eb5c1c92c8dc
Create Date: 2026-08-09 18:07:32.490182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5710668d522e'
down_revision: Union[str, Sequence[str], None] = 'eb5c1c92c8dc'
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
    op.alter_column(
        "transactions",
        "title",
        new_column_name="memo",
    )
