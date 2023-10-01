import pandas as pd

movie_data = pd.read_csv('/Users/tanaydulipala/Downloads/archive/movies_metadata.csv')

user_genre = input("What movie genre do you like:")
movies_filter = movie_data[movie_data['genres'].str.contains(user_genre)]

if not movies_filter.empty:
    recommendations = movies_filter.sample(n=10, random_state=42)
    
    print("Recommended Movies:")
    for index, row in recommendations.iterrows():
        print(f"{row['title']} ({row['release_date']}) - Rating: {row['vote_average']}")
    option = input("Do you want to know the synopsis of any of these movies:(y/n)")

else:
    print(f"No movies found for the genre '{user_genre}'. Please try another genre.")