# Import Pandas
import pandas as pd
# Read video_games_raw.csv into a DataFrame
games_df = pd.read_csv('video_games_raw.csv')
# Display the program title
print("VIDEO GAME CATALOG MANAGER")
# Ask the user for a row position
row_position = int(input("Enter a row number to inspect: "))
# Select that row using .iloc[]
selected_game = games_df.iloc[row_position]
# Display the selected game's information
print("Selected Game Information:")
print(selected_game)
# Ask the user for a new status
new_status = input("Enter a new status: ")
# Find the selected row's index label
row_index = selected_game.name
# Update its Status using .at[]
games_df.at[row_index, 'Status'] = new_status
# Add Recommended and give every row "No"
games_df['Recommended'] = "No"
# Use .loc[] to assign "Yes" where Rating >= 8 AND Price <= 40
games_df.loc[(games_df['Rating'] >= 8) & (games_df['Price'] <= 40), 'Recommended'] = "Yes"
# Use .query() to select the recommended games
recommended_games = games_df.query('Recommended == "Yes"')
# Display their title, platform, price, and rating
print("Recommended Games:")
for index, game in recommended_games.iterrows():
    print(f"Title: {game['Title']}, Platform: {game['Platform']}, Price: ${game['Price']}, Rating: {game['Rating']}")

# Save to video_games_cleaned.csv without the index
games_df.to_csv('video_games_cleaned.csv', index=False)

# Display a confirmation message
print("Data saved to video_games_cleaned.csv")