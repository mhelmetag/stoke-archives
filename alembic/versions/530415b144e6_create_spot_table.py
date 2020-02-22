"""create spots table

Revision ID: 530415b144e6
Revises: 
Create Date: 2020-02-19 00:15:35.491123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '530415b144e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'spots',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('surfline_id', sa.String(50), nullable=False),
        sa.Column('surfline_spot_id', sa.String(50), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('now()'), nullable=False)        
    )

def downgrade():
    op.drop_table('spots')
