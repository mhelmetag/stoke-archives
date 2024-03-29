'''add predictions

Revision ID: 4b826f718fb0
Revises: b22cca33828c
Create Date: 2020-03-06 23:46:18.955153

'''
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b826f718fb0'
down_revision = 'b22cca33828c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'predictions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('spot_id', sa.Integer(), nullable=False),
        sa.Column('created_on', sa.DateTime(), nullable=False),
        sa.Column('forecasted_for', sa.DateTime(), nullable=False),
        sa.Column('surfline_height', sa.Float(), nullable=False),
        sa.Column('stoke_height', sa.Float(), nullable=False),
        sa.Column('swell1_height', sa.Float(), nullable=False),
        sa.Column('swell1_period', sa.Integer(), nullable=False),
        sa.Column('swell1_direction', sa.Float(), nullable=False),
        sa.Column('swell2_height', sa.Float(), nullable=False),
        sa.Column('swell2_period', sa.Integer(), nullable=False),
        sa.Column('swell2_direction', sa.Float(), nullable=False),
        sa.Column('swell3_height', sa.Float(), nullable=False),
        sa.Column('swell3_period', sa.Integer(), nullable=False),
        sa.Column('swell3_direction', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['spot_id'], ['spots.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_predictions_created_on'),
                    'predictions', ['created_on'], unique=False)
    op.create_index(op.f('ix_predictions_forecasted_for'),
                    'predictions', ['forecasted_for'], unique=False)
    op.create_index(op.f('ix_predictions_spot_id'),
                    'predictions', ['spot_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_predictions_spot_id'), table_name='predictions')
    op.drop_index(op.f('ix_predictions_forecasted_for'),
                  table_name='predictions')
    op.drop_index(op.f('ix_predictions_created_on'), table_name='predictions')
    op.drop_table('predictions')
    # ### end Alembic commands ###
