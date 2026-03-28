"""Create a phone number for user column

Revision ID: 6ade3a62c58b
Revises: 
Create Date: 2026-03-09 23:55:30.826707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ade3a62c58b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column("phone number", sa.String(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
