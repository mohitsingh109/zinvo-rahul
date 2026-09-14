from app.models.user import User


def test_users_table_name():
    assert User.__tablename__ == "users"


def test_user_columns():
    columns = {column.name for column in User.__table__.columns}
    assert columns == {
        "id",
        "email",
        "hashed_password",
        "is_active",
        "created_at",
        "updated_at",
    }
