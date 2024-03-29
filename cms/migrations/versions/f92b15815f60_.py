"""empty message

Revision ID: f92b15815f60
Revises: 8b464bf92361
Create Date: 2019-10-04 14:47:43.955808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92b15815f60'
down_revision = '8b464bf92361'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ky_files',
    sa.Column('fid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('path', sa.String(length=800), nullable=False),
    sa.PrimaryKeyConstraint('fid'),
    mysql_charset='utf8'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ky_files')
    # ### end Alembic commands ###
