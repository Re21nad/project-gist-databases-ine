from .models import Gist

def search_gists(db_connection, **kwargs):
    if 'github_id' in kwargs:
        params = {
            'github_id': kwargs.get('github_id')
        }
        cursor = db_connection.execute('SELECT * FROM gists WHERE github_id = :github_id', params)
    elif 'created_at' in kwargs:
        params = {
            'created_at': kwargs.get('created_at')
        }
        cursor = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)',params)
    else:
        cursor = db_connection.execute('SELECT * FROM gists')


    gist_list = []
    for gist in gist_list:
        gist_list.append(Gist(gist))
    return gist_list