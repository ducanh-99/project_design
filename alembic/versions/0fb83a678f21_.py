"""empty message

Revision ID: 0fb83a678f21
Revises: c55005c3ed00
Create Date: 2021-06-23 21:57:20.414815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fb83a678f21'
down_revision = 'c55005c3ed00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('clinic_predict', sa.String(length=255), nullable=True))
    op.add_column('history', sa.Column('clinic_reality', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'clinic_reality')
    op.drop_column('history', 'clinic_predict')
    # ### end Alembic commands ###
