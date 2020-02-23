"""add favorable swells to spots

Revision ID: 41fa67432f6c
Revises: a17941a522a1
Create Date: 2020-02-23 00:54:31.504744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41fa67432f6c'
down_revision = 'a17941a522a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spots', sa.Column('favorable_swells', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spots', 'favorable_swells')
    # ### end Alembic commands ###
