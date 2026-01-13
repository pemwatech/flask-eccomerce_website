from flask import Blueprint,session,redirect,url_for
admin=Blueprint('admin',__name__)

@admin.before_request
def admin_before_request():
    if 'admin_role' not in session or session['admin_role']!='admin':
        return redirect(url_for('auth.login'))
    
from . import routes