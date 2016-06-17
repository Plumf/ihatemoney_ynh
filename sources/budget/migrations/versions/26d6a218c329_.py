"""Add Person.weight column

Revision ID: 26d6a218c329
Revises: b9a10d5d63ce
Create Date: 2016-06-15 09:22:04.069447

"""

# revision identifiers, used by Alembic.
revision = '26d6a218c329'
down_revision = 'b9a10d5d63ce'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('weight', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'weight')
    ### end Alembic commands ###
