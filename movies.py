import sys
import random
import math
import movie_storage  # Import the module


def list_movies():
    """ Lists all movies from the database. """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in the database.")
        return

    count = 0
    for title, data in movies.items():
        print(f"{title} ({data['year']}): {data['rating']}")
        count += 1
    print(f"{count} movies in total")


def add_movie():
    """ Adds a movie to the movies database. """
    movies = movie_storage.get_movies()

    title = input("Enter a movie title: ")
    if title in movies:
        print(f"Movie '{title}' already exists!")
        return

    rating = float(input("Enter movie rating: "))
    year = input("Enter movie year: ")  

    movie_storage.add_movie(title, year, rating)
    print(f"Movie '{title}' successfully added.")


def delete_movie():
    """ Deletes a movie from the movies database. """
    movies = movie_storage.get_movies()

    title = input("Enter movie title to delete: ")
    if title not in movies:
        print(f"Movie '{title}' not found.")
        return

    movie_storage.delete_movie(title)
    print(f"Movie '{title}' has been deleted.")


def update_movie():
    """ Updates a movie's rating in the movies database. """
    movies = movie_storage.get_movies()

    title = input("Enter movie title to update: ")
    if title not in movies:
        print(f"Movie '{title}' not found.")
        return

    new_rating = float(input("Enter new rating: "))
    movie_storage.update_movie(title, new_rating)
    print(f"Movie '{title}' rating updated to {new_rating}.")


def stats():
    """ Displays statistics based on movie ratings. """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies available for statistics.")
        return

    ratings = [data["rating"] for data in movies.values()]
    average = sum(ratings) / len(ratings)
    ratings.sort()
    median = ratings[len(ratings) // 2] if len(ratings) % 2 == 1 else \
             (ratings[len(ratings) // 2 - 1] + ratings[len(ratings) // 2]) / 2
    max_rating = max(ratings)
    min_rating = min(ratings)

    best_movies = [title for title, data in movies.items() if math.isclose(data["rating"], max_rating)]
    worst_movies = [title for title, data in movies.items() if math.isclose(data["rating"], min_rating)]

    print("Statistics:")
    print(f"- Average rating: {round(average, 2)}")
    print(f"- Median rating: {round(median, 2)}")
    print(f"- Best movie(s): {best_movies} with rating {max_rating}")
    print(f"- Worst movie(s): {worst_movies} with rating {min_rating}")


def random_movie():
    """ Selects a random movie from the database. """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in the database to choose from.")
        return
    title, data = random.choice(list(movies.items()))
    print(f"Random movie: {title} ({data['year']} - {data['rating']})")


def search_movie():
    """ Searches for movies by title. """
    movies = movie_storage.get_movies()
    query = input("Enter part of movie name: ").lower()
    found = False
    for title, data in movies.items():
        if query in title.lower():
            print(f"{title} ({data['year']}): {data['rating']}")
            found = True
    if not found:
        print(f"No movies found matching '{query}'.")


def movies_sorted_by_rating():
    """ Displays movies sorted by rating in descending order. """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in the database.")
        return
    for title, data in sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True):
        print(f"{title} ({data['year']}): {data['rating']}")


def main():
    """ Main function that displays the menu and handles user input. """
    while True:
        print("\n********** My Movies Database **********")
        print("\nMenu:")
        print("0. Exit")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Update movie")
        print("5. Stats")
        print("6. Random movie")
        print("7. Search movie")
        print("8. Movies sorted by rating")

        try:
            choice = int(input("\nEnter choice (0-8): "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")
            continue

        if choice == 0:
            print("Bye!")
            sys.exit(0)
        elif choice == 1:
            list_movies()
        elif choice == 2:
            add_movie()
        elif choice == 3:
            delete_movie()
        elif choice == 4:
            update_movie()
        elif choice == 5:
            stats()
        elif choice == 6:
            random_movie()
        elif choice == 7:
            search_movie()
        elif choice == 8:
            movies_sorted_by_rating()
        else:
            print("Invalid choice. Select a number between 0 and 8.")


if __name__ == "__main__":
    main()
