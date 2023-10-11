"""create building table

Revision ID: 7ede255b7202
Revises: 
Create Date: 2023-10-11 20:37:35.277247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ede255b7202'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('building', schema=None) as batch_op:
        batch_op.drop_index('ix_building_number')
        batch_op.drop_index('ix_building_timestamp')

    op.drop_table('building')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('building',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('number', sa.BIGINT(), nullable=False),
    sa.Column('latitude', sa.FLOAT(), nullable=False),
    sa.Column('longitude', sa.FLOAT(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('answer', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('latitude'),
    sa.UniqueConstraint('longitude')
    )
    with op.batch_alter_table('building', schema=None) as batch_op:
        batch_op.create_index('ix_building_timestamp', ['timestamp'], unique=False)
        batch_op.create_index('ix_building_number', ['number'], unique=False)

    # ### end Alembic commands ###
