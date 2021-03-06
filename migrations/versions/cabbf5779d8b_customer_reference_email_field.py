"""Customer Reference - Email Field

Revision ID: cabbf5779d8b
Revises: bd4bdf990c64
Create Date: 2021-04-07 20:28:20.039074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cabbf5779d8b'
down_revision = 'bd4bdf990c64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('email', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'email')
    # ### end Alembic commands ###
