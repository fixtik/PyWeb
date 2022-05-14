from blog.models import Note

def note_to_json(note: Note) -> dict:
    return {
        'id': note.id,
        'title': note.title,
        'message': note.message,
        'public': note.public
    }

def note_create(note: Note) -> dict:
    return {
        'title': note.title,
        'message': note.message,
        'public': note.public,
        'create_at': note.create_at,
        'update_at': note.update_at
    }