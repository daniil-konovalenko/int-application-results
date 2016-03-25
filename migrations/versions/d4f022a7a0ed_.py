"""empty message

Revision ID: d4f022a7a0ed
Revises: None
Create Date: 2016-03-25 21:46:09.583865

"""

# revision identifiers, used by Alembic.
revision = 'd4f022a7a0ed'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('math_test', sa.Float(), nullable=True),
    sa.Column('math', sa.Float(), nullable=True),
    sa.Column('philology', sa.Float(), nullable=True),
    sa.Column('history', sa.Float(), nullable=True),
    sa.Column('science', sa.Float(), nullable=True),
    sa.Column('comments', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    ### end Alembic commands ###
