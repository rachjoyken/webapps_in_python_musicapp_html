from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
import os
from flask import Flask, request, render_template
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

#Example:

@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

#Exercise:

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums.html", albums=albums)

#Challenge:








# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

