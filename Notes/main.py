from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from models import db, Note
from forms import NoteForm

main = Blueprint('main', __name__)

@main.route('/')

def index():
    return render_template('index.html')

@main.route('/dashboard')
# @login_required
def dashboard():
    # print("jhcjbdsjdbsjbdsjhdbjdsbvdsjh",current_user)
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', notes=notes)

@main.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_note = Note(title=title, content=content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('note_form.html', form=form)

@main.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        return redirect(url_for('main.dashboard'))
    
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    form.title.data = note.title
    form.content.data = note.content
    return render_template('note_form.html', form=form)

@main.route('/delete_note/<int:note_id>')
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500