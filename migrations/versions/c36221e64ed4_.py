"""empty message

Revision ID: c36221e64ed4
Revises: 
Create Date: 2020-06-26 17:09:15.272447

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c36221e64ed4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('code', sa.String(length=80), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('listing_date', sa.String(length=80), nullable=True),
                    sa.Column('hit_new_date', sa.String(length=80), nullable=True),
                    sa.Column('second_bord', sa.String(length=80), nullable=True),
                    sa.Column('extend_one', sa.String(length=80), nullable=True),
                    sa.Column('extend_two', sa.String(length=80), nullable=True),
                    sa.Column('note', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('code')
                    )
    op.create_table('test',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('name2', sa.String(length=80), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.Column('extend_one', sa.String(length=81), nullable=True),
                    sa.Column('extend_two', sa.String(length=80), nullable=True),
                    sa.Column('note', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('name'),
                    sa.UniqueConstraint('name2')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.Column('extend_one', sa.String(length=81), nullable=True),
                    sa.Column('extend_two', sa.String(length=80), nullable=True),
                    sa.Column('note', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('user_stock',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('stock_code', sa.String(length=80), nullable=False),
                    sa.Column('user_name', sa.String(length=80), nullable=False),
                    sa.Column('extend_one', sa.String(length=80), nullable=True),
                    sa.Column('extend_two', sa.String(length=80), nullable=True),
                    sa.Column('note', sa.String(length=255), nullable=True),
                    sa.ForeignKeyConstraint(['stock_code'], ['stock.code'], ),
                    sa.ForeignKeyConstraint(['user_name'], ['user.name'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_stock')
    op.drop_table('user')
    op.drop_table('test')
    op.drop_table('stock')
    # ### end Alembic commands ###
