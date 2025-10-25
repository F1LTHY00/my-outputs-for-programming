print("Welcome to the anime lister.")
juice = ""
anime_list = []

while juice != "ong":
    juice = input("Enter the title of an anime (type 'ong' to finish): " )
    anime_list.append(juice)
    print("'", juice, "' has been added to the list")
print("You have finished listing your anime.")
print(f"Your anime list includes the following shows:")
for show in anime_list:
    print(f"> {show}")