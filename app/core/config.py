import os  # Python package

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://user:user123@localhost:5434/invoice-management",
)

# .py (already) (preferred)
# .env (local dev)
# .yml (preferred)
# .conf (me) us.conf, in.conf, uk-lon.conf, jp.conf