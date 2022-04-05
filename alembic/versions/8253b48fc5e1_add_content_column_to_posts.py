"""add content column to posts

Revision ID: 8253b48fc5e1
Revises: 06c6b87ec839
Create Date: 2022-04-03 11:25:08.398192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8253b48fc5e1'
down_revision = '06c6b87ec839'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
