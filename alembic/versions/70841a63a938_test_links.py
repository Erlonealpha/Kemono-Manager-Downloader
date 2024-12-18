"""test_links

Revision ID: 70841a63a938
Revises: 
Create Date: 2024-11-03 07:28:07.164947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import sqlmodel.sql
import sqlmodel.sql.sqltypes

# revision identifiers, used by Alembic.
revision: str = '70841a63a938'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kemono_attachment', sa.Column('sha256', sqlmodel.sql.sqltypes.AutoString()))
    op.add_column('kemono_post', sa.Column('links', sqlmodel.sql.sqltypes.AutoString()))
    op.add_column('kemono_post', sa.Column('poll', sqlmodel.sql.sqltypes.AutoString()))
    op.add_column('kemono_post', sa.Column('captions', sqlmodel.sql.sqltypes.AutoString()))
    op.add_column('kemono_post', sa.Column('tags', sqlmodel.sql.sqltypes.AutoString()))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kemono_post', 'tags')
    op.drop_column('kemono_post', 'captions')
    op.drop_column('kemono_post', 'poll')
    op.drop_column('kemono_post', 'links')
    op.drop_column('kemono_attachment', 'sha256')
    # ### end Alembic commands ###
