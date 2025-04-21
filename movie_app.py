import random
from istorage import IStorage


class MovieApp:
    """Main application class for the movie database manager."""

    def __init__(self, storage: IStorage):
        """Initialize the movie application with a storage implementation.
        
        Args:
            storage (IStorage): An implementation of the IStorage interface
                              for movie data persistence.
        """
        self._storage = storage

    def _command_list_movies(self):
        """List all movies in the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return
        
        print(f"\n{len(movies)} movies in total:")
        for title, data in movies.items():
            print(f"{title} ({data['year']}): {data['rating']}")

    def _command_add_movie(self):
        """Add a new movie to the database."""
        title = input("Enter movie title: ")
        year = input("Enter movie year: ")
        rating = float(input("Enter movie rating (0-10): "))
        poster = input("Enter movie poster URL: ")

        if self._storage.add_movie(title, year, rating, poster):
            print(f"Movie '{title}' successfully added")
        else:
            print(f"Movie '{title}' already exists!")

    def _command_delete_movie(self):
        """Delete a movie from the database."""
        title = input("Enter movie title to delete: ")
        if self._storage.delete_movie(title):
            print(f"Movie '{title}' successfully deleted")
        else:
            print(f"Movie '{title}' not found")

    def _command_update_movie(self):
        """Update the rating of a movie in the database."""
        title = input("Enter movie title: ")
        rating = float(input("Enter new rating (0-10): "))
        
        if self._storage.update_movie(title, rating):
            print(f"Movie '{title}' successfully updated")
        else:
            print(f"Movie '{title}' not found")

    def _command_movie_stats(self):
        """Display statistics about the movies in the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        ratings = [movie['rating'] for movie in movies.values()]
        avg_rating = sum(ratings) / len(ratings)
        median_rating = sorted(ratings)[len(ratings) // 2]
        best_movie = max(movies.items(), key=lambda x: x[1]['rating'])
        worst_movie = min(movies.items(), key=lambda x: x[1]['rating'])

        print("\nMovie Statistics:")
        print(f"Average rating: {avg_rating:.2f}")
        print(f"Median rating: {median_rating:.2f}")
        print(f"Best movie: {best_movie[0]} ({best_movie[1]['rating']})")
        print(f"Worst movie: {worst_movie[0]} ({worst_movie[1]['rating']})")

    def _command_random_movie(self):
        """Select and display a random movie from the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        title = random.choice(list(movies.keys()))
        movie = movies[title]
        print(f"\nYour random movie is: {title}")
        print(f"Year: {movie['year']}")
        print(f"Rating: {movie['rating']}")

    def _command_search_movie(self):
        """Search for a movie by title."""
        search_term = input("Enter part of movie name: ").lower()
        movies = self._storage.list_movies()
        found = False

        for title, data in movies.items():
            if search_term in title.lower():
                print(f"{title} ({data['year']}): {data['rating']}")
                found = True

        if not found:
            print(f"No movies found containing '{search_term}'")

    def _command_movies_sorted(self):
        """Display all movies sorted by rating in descending order."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return

        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        print("\nMovies sorted by rating:")
        for title, data in sorted_movies:
            print(f"{title} ({data['year']}): {data['rating']}")

    def _generate_website(self):
        """Generate an HTML website displaying all movies.
        
        Note: Website generation will be implemented in a future update.
        """
        print("Website generation not implemented yet.")

    def run(self):
        """Run the movie application's main loop."""
        commands = {
            "1": ("List movies", self._command_list_movies),
            "2": ("Add movie", self._command_add_movie),
            "3": ("Delete movie", self._command_delete_movie),
            "4": ("Update movie", self._command_update_movie),
            "5": ("Movie statistics", self._command_movie_stats),
            "6": ("Random movie", self._command_random_movie),
            "7": ("Search movie", self._command_search_movie),
            "8": ("Movies sorted by rating", self._command_movies_sorted),
            "9": ("Generate website", self._generate_website),
            "0": ("Exit", None)
        }

        while True:
            print("\nMenu:")
            for key, (description, _) in commands.items():
                print(f"{key}. {description}")

            choice = input("\nEnter choice (0-9): ")
            if choice not in commands:
                print("Invalid choice! Please try again.")
                continue

            if choice == "0":
                print("Goodbye!")
                break

            commands[choice][1]() 