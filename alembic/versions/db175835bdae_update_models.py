"""Update models

Revision ID: db175835bdae
Revises: 5e4b64febe19
Create Date: 2024-07-27 20:09:05.215867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db175835bdae'
down_revision: Union[str, None] = '5e4b64febe19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
