"""atualizçao das tabelas

Revision ID: 4dfabf6c1bcb
Revises: 
Create Date: 2021-12-02 13:48:49.330357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dfabf6c1bcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grupo_um',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grupo_dois',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('conjuge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['conjuge_id'], ['grupo_um.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('conjuge_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grupo_dois')
    op.drop_table('grupo_um')
    # ### end Alembic commands ###
