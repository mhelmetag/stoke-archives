"""add gathering data on spot

Revision ID: 955a35618860
Revises: 4b826f718fb0
Create Date: 2020-03-11 00:18:35.772159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955a35618860'
down_revision = '4b826f718fb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spots', sa.Column('gathering_data', sa.Boolean()))
    op.execute(
        'UPDATE spots SET gathering_data = true WHERE gathering_data IS NULL')
    op.alter_column('spots', 'gathering_data', nullable=False)
    op.create_index(op.f('ix_spots_gathering_data'), 'spots',
                    ['gathering_data'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_spots_gathering_data'), table_name='spots')
    op.drop_column('spots', 'gathering_data')
    # ### end Alembic commands ###