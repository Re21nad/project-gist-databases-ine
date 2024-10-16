import requests

def import_gists_to_database(db, username, commit=True):
    try:
        requirement = requests.get("https://api.github.com/users/{}/gists".format(username))
        data = requirement.json()

    except:
        raise requests.HTTPError
    
    for i in data:
        db.execute('INSERT INTO gists VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', [
            None, i['id'], i['html_url'], i['git_pull_url'], i['git_push_url'], i['commits_url'], i['forks_url'], i['public'], i['created_at'], i['updated_at'], i['comments'], i['comments_url']
        ])
