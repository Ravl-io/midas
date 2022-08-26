""""remove_project_flag"

Revision ID: 00a6ba287712
Revises: 12015f05eab7
Create Date: 2017-07-19 09:20:31.570518

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

# revision identifiers, used by Alembic.

revision = '00a6ba287712'
down_revision = '654de385756b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cloudsite', sa.Column('remove_project', sa.Boolean(), nullable=False))
    cs_table = sa.table('cloudsite', sa.Column('remove_project', sa.Boolean(), nullable=False))
    bind = op.get_bind()
    session = Session(bind=bind)
    set_remove_project = sa.update(cs_table).values(remove_project=True)
    try:
        session.execute(set_remove_project)
        session.commit()
    finally:
        session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cloudsite', 'remove_project')
    # ### end Alembic commands ###