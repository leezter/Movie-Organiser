from storage_json import StorageJson
from movie_app import MovieApp


def main():
    """
    Main entry point of the movie application.
    Initializes the storage and movie app, then runs the application.
    """
    # Initialize storage with the main movies database file
    storage = StorageJson('movies.json')
    
    # Create the movie application with the storage
    movie_app = MovieApp(storage)
    
    # Run the application
    movie_app.run()


if __name__ == '__main__':
    main() 