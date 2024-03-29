"""empty message

Revision ID: 0eeabb89bb3b
Revises:
Create Date: 2021-04-28 12:33:24.951005

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0eeabb89bb3b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "homework",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, index=True),
        sa.Column("text", sa.String(50)),
        sa.Column("deadline", sa.DateTime),
        sa.Column("created", sa.DateTime),
    )
    op.create_table(
        "student",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, index=True),
        sa.Column("last_name", sa.String(50)),
        sa.Column("first_name", sa.String(50)),
    )
    op.create_table(
        "homework_result",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, index=True),
        sa.Column("homework_id", sa.Integer, sa.ForeignKey("homework.id")),
        sa.Column("solution", sa.String(50)),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("student.id")),
        sa.Column("created", sa.DateTime),
    )
    op.create_table(
        "teacher",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, index=True),
        sa.Column("last_name", sa.String(50)),
        sa.Column("first_name", sa.String(50)),
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("homework")
    op.drop_table("student")
    op.drop_table("homework_result")
    op.drop_table("teacher")
    # ### end Alembic commands ###
