"""Update models

Revision ID: 5f41d384eb79
Revises: 22756bcec843
Create Date: 2024-07-27 20:19:47.980075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f41d384eb79'
down_revision: Union[str, None] = '22756bcec843'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
