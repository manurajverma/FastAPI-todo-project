"""rename phone number column to phone_number

Revision ID: e9711bfa7d2e
Revises: 6ade3a62c58b
Create Date: 2026-03-10 00:16:41.378349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9711bfa7d2e'
down_revision: Union[str, Sequence[str], None] = '6ade3a62c58b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('users', 'phone number', new_column_name='phone_number')


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('users', 'phone_number', new_column_name='phone number')
