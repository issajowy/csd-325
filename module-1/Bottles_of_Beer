def beer_song():
    try:
        count = int(input("How many beers are on the wall?"))

        if count < 0:
            print("Are you blind? MY BAR IS FULL!")

        while count > 0:
            current_beers = "bottles" if count != 1 else "bottle"
            beer_count = count - 1
            next_beer = "bottles" if beer_count != 1 else "bottle"

            print(f"{count} {current_beers} of beers on the wall, {count} {current_beers} of beers")

            if beer_count > 0:
                print(f"Take one down, pass it around, {beer_count} {next_beer} of beer on the wall. \n") 
            else: 
                print(f"Take one down, pass it around, no more bottles of BEER ON THE WALL! \n")

            count -= 1

        print("No more bottles of beer on the wall, no more bottles of beer!")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.") 

    except ValueError:
        print("Please tell me to the next fullest beer!")

if __name__ == "__main__":
    beer_song()

