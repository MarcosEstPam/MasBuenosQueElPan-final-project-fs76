"""empty message

Revision ID: 72ae9a439b42
Revises: fddb46ad3a47
Create Date: 2024-10-12 04:21:19.287853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ae9a439b42'
down_revision = 'fddb46ad3a47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('volume',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('minimum',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('brief_description',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('brief_description',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('minimum',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('volume',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('weight',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
