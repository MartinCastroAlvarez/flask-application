source .env/bin/activate
export SECRET="9812398h1982h3981h12"
export DB_PASS="beri_diifiikuult"
export DB_HOST="127.0.0.1"
export DB_PORT="5432"
export DB_USER="postgres"
export DEBUG="yes"
export DB_NAME="maria_dataveis"
export ADMIN_PASSWORD="admin"
export ADMIN_USERNAME="admin"
# export LOGIN_DISABLED="maria_dataveis"
python3 app/main.py
