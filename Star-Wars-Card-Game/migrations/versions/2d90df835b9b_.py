"""empty message

Revision ID: 2d90df835b9b
Revises: 8d62f4c7bb78
Create Date: 2023-04-27 11:21:42.555151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d90df835b9b'
down_revision = '8d62f4c7bb78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('set_price', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.drop_column('set_price')

    # ### end Alembic commands ###