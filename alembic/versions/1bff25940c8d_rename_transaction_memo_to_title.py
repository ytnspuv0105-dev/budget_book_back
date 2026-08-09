"""rename transaction memo to title

Revision ID: 1bff25940c8d
Revises: e9cd24503100
Create Date: 2026-08-09 18:30:33.560005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bff25940c8d'
down_revision: Union[str, Sequence[str], None] = 'e9cd24503100'
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
