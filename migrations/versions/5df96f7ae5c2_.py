"""empty message

Revision ID: 5df96f7ae5c2
Revises: e353df520226
Create Date: 2018-02-25 10:54:28.284343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5df96f7ae5c2'
down_revision = 'e353df520226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'create_time')
    # ### end Alembic commands ###