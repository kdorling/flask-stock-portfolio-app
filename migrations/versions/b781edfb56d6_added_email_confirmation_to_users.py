"""Added email confirmation to users

Revision ID: b781edfb56d6
Revises: f26af1744a9f
Create Date: 2021-06-10 00:10:20.955416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b781edfb56d6'
down_revision = 'f26af1744a9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email_confirmation_sent_on', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('email_confirmed', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('email_confirmed_on', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('registered_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'registered_on')
    op.drop_column('users', 'email_confirmed_on')
    op.drop_column('users', 'email_confirmed')
    op.drop_column('users', 'email_confirmation_sent_on')
    # ### end Alembic commands ###
