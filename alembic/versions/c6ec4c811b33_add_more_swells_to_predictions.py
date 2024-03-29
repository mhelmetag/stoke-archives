'''add more swells to predictions

Revision ID: c6ec4c811b33
Revises: 955a35618860
Create Date: 2020-03-12 21:57:40.514412

'''
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6ec4c811b33'
down_revision = '955a35618860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('predictions', sa.Column('swell4_direction', sa.Float()))
    op.add_column('predictions', sa.Column('swell4_height', sa.Float()))
    op.add_column('predictions', sa.Column('swell4_period', sa.Integer()))
    op.add_column('predictions', sa.Column('swell5_direction', sa.Float()))
    op.add_column('predictions', sa.Column('swell5_height', sa.Float()))
    op.add_column('predictions', sa.Column('swell5_period', sa.Integer()))
    op.add_column('predictions', sa.Column('swell6_direction', sa.Float()))
    op.add_column('predictions', sa.Column('swell6_height', sa.Float()))
    op.add_column('predictions', sa.Column('swell6_period', sa.Integer()))
    op.execute(
        '''
            UPDATE predictions
            SET
                swell4_direction = 0.0,
                swell4_height = 0.0,
                swell4_period = 0,
                swell5_direction = 0.0,
                swell5_height = 0.0,
                swell5_period = 0,
                swell6_direction = 0.0,
                swell6_height = 0.0,
                swell6_period = 0
            WHERE
                swell4_direction IS NULL AND
                swell4_height IS NULL AND
                swell4_period IS NULL AND
                swell5_direction IS NULL AND
                swell5_height IS NULL AND
                swell5_period IS NULL AND
                swell6_direction IS NULL AND
                swell6_height IS NULL AND
                swell6_period IS NULL
        '''
    )
    op.alter_column('predictions', 'swell4_direction', nullable=False)
    op.alter_column('predictions', 'swell4_height', nullable=False)
    op.alter_column('predictions', 'swell4_period', nullable=False)
    op.alter_column('predictions', 'swell5_direction', nullable=False)
    op.alter_column('predictions', 'swell5_height', nullable=False)
    op.alter_column('predictions', 'swell5_period', nullable=False)
    op.alter_column('predictions', 'swell6_direction', nullable=False)
    op.alter_column('predictions', 'swell6_height', nullable=False)
    op.alter_column('predictions', 'swell6_period', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('predictions', 'swell6_period')
    op.drop_column('predictions', 'swell6_height')
    op.drop_column('predictions', 'swell6_direction')
    op.drop_column('predictions', 'swell5_period')
    op.drop_column('predictions', 'swell5_height')
    op.drop_column('predictions', 'swell5_direction')
    op.drop_column('predictions', 'swell4_period')
    op.drop_column('predictions', 'swell4_height')
    op.drop_column('predictions', 'swell4_direction')
    # ### end Alembic commands ###
