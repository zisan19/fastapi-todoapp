"""Phone number column adding for our users table

Revision ID: 52610eda9abc
Revises: 
Create Date: 2026-11-04 13:49:47.817366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52610eda9abc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('Phone_number', sa.String(20), nullable=True))


def downgrade() -> None:
    """Downgrade Schema"""
    pass
