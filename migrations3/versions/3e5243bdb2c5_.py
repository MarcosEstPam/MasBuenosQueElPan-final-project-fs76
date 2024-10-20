"""empty message

Revision ID: 3e5243bdb2c5
Revises: 94673f996adb
Create Date: 2024-10-04 15:23:35.524585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e5243bdb2c5'
down_revision = '94673f996adb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart__items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Numeric(precision=100), nullable=False),
    sa.Column('product_id', sa.Numeric(precision=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart__items')
    # ### end Alembic commands ###
