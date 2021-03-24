"""empty message

Revision ID: c71d5301d374
Revises: 
Create Date: 2021-03-22 20:43:03.653834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c71d5301d374'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('number_of_bedrooms', sa.String(length=30), nullable=True),
    sa.Column('number_of_bathrooms', sa.String(length=30), nullable=True),
    sa.Column('price', sa.String(length=200), nullable=True),
    sa.Column('location', sa.String(length=300), nullable=True),
    sa.Column('ptype', sa.String(length=60), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
