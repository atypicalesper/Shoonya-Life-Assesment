"""Update models

Revision ID: 22756bcec843
Revises: db175835bdae
Create Date: 2024-07-27 20:09:47.967869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22756bcec843'
down_revision: Union[str, None] = 'db175835bdae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
