"""Initial Migration

Revision ID: d6994d0c6fbe
Revises: 5400aaf41599
Create Date: 2020-02-14 20:43:52.927497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6994d0c6fbe'
down_revision = '5400aaf41599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('comment', sa.Integer(), nullable=True))
    op.alter_column('pitches', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'pitches', 'comments', ['comment'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.alter_column('pitches', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('pitches', 'comment')
    op.drop_table('comments')
    # ### end Alembic commands ###