"""create students table

Revision ID: e4f36296f8a8
Revises:
Create Date: 2026-03-07 13:13:24.816053

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "e4f36296f8a8"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("number_of_studak", sa.Integer(), nullable=False),
        sa.Column("number_of_group", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("father_name", sa.String(), nullable=True),
        sa.Column("phone_number", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_students")),
        sa.UniqueConstraint(
            "number_of_studak", name=op.f("uq_students_number_of_studak")
        ),
        sa.UniqueConstraint("phone_number", name=op.f("uq_students_phone_number")),
        sa.UniqueConstraint("telegram_id", name=op.f("uq_students_telegram_id")),
    )


def downgrade() -> None:
    op.drop_table("students")
