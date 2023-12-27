"""Adding isNotified Col

Revision ID: 06baabaea123
Revises: 019ab566e5f7
Create Date: 2023-12-25 09:56:49.779689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06baabaea123'
down_revision: Union[str, None] = '019ab566e5f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alert_rules', sa.Column('isNotified', sa.Boolean(), server_default=sa.false() , default=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alert_rules', 'isNotified')
    # ### end Alembic commands ###
