from flask import Flask, redirect, session
from flask_login import LoginManager
from routes.task_routes import task_bp
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.score_routes import score_bp
from routes.auto_task_routes import auto_task_bp
from routes.default_task_routes import default_tasks_bp
from routes.game_routes import game_bp
from services.permission_service import PermissionService
from models.user_model import User
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = "gizli_anahtar_123"  # Gerçek ortamda .env ile sakla
    app.config['SHEET_ID'] = 'your-sheet-id'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    # Session configuration
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    app.config['SESSION_COOKIE_SECURE'] = False  # Development için False, production'da True olmalı
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    # Login manager setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.auth_login_route'  # Blueprint adı ve route fonksiyonu adıyla eşleştirdik
    login_manager.session_protection = "strong"

    # Route kayıtları
    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(score_bp, url_prefix="/score")
    app.register_blueprint(auto_task_bp, url_prefix="/auto")
    app.register_blueprint(default_tasks_bp)
    app.register_blueprint(game_bp)

    # Initialize services
    permission_service = PermissionService()

    @login_manager.user_loader
    def load_user(user_id):  # Flask-Login user_id'yi string olarak gönderir
        # First try to get from session
        user_data = session.get('user_data')
        if user_data and user_data['username'] == user_id:
            return User(
                username=user_id,
                password='',  # Password not needed for session
                is_admin=user_data['is_admin']
            )
        
        # If not in session, get from sheets
        user_data = permission_service.get_user(user_id)
        if user_data:
            is_admin = (user_data.get('role', 'user').lower() == 'admin')
            # Cache in session
            session['user_data'] = {
                'username': user_id,
                'is_admin': is_admin
            }
            return User(
                username=user_id,
                password=user_data['password'],
                is_admin=is_admin
            )
        return None

    @app.route("/")
    def index():
        return redirect("/auth/login")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5500)