# app.py
import random as r
import direcrion
from flask import Flask, render_template, Response, request  # importing the render_template function

x = direcrion.wordStartingpoint("bana")

print(x)
# TODO
# must be words under size 13
word_list = [
        # "Intelligence",
        "dogs",
        "far",
        "jack",
        "poops",
        "fenced",
        "cream",
        "aorta",
        "donkeykong",
        "hacker",
        "donut",
        "cheeze",
        "lightness",
        "jumbo",
        "mediterranean",
        "ryan",
        "consume"
        ]

#       we have a 13X13 init to 0's
#       find a location for the word to fit
#       check if it doesnt overlap with other words
#       fill in the locations with letters
#       repeat 6 times 
#       after all words inserted, fill in 0's with random chars
#       use flask to send data to the html 

app = Flask(__name__)

grid_size = 13

# home route
@app.route("/",  methods=['POST', 'GET'])
def hello():
    # init the grid to grid_size
    grid = init_grid(size=grid_size)
    # grid[12][8] = "Q"
    # print_grid(grid)
    # print("grid has been init")
    countsss = 0
    # new_grid = insert_into_grid([9,9,7], grid, "word")
    while countsss != 5:
        try:
            x = direcrion.wordStartingpoint(r.choice(word_list))
            if(grid[x[0][0]][x[0][0]] == 0):
                new_grid = insert_into_grid(x[0],grid,x[1])
                print()
                # new_grid = insert_into_grid([5,5,6],grid,x[1])
                countsss = countsss +1
            else:
                break
        except Exception as e:
                print("Exception: ",end='')
                print(e,end="\n\n\n\n")
    # print_grid(new_grid)
    final_grid = fill_random(new_grid)
    # print_grid(final_grid)


    count = 0
    mega_str = ""
    for x in range(grid_size):
        for y in range(grid_size):
            mega_str = mega_str+ str(final_grid[x][y])
            count = count + 1

    return render_template('index.html', grid=mega_str)

def init_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0]*size)
    return(grid)

def fill_random(grid):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(grid)):
        for y in range(13):
            if (grid[x][y] == 0):
                grid[x][y] = r.choice(all_letters)
            else:
                pass
    return(grid)

def print_grid(grid):
    print()
    for x in range(len(grid)):
        print(grid[x])
    print()

def check_if_fit():
    pass

def insert_into_grid(cords, grid, word):
    # format: [x,y,direction]
    grid_coppy = grid

    temp  = cords[0]
    cords[0] = cords[1]
    cords[1] = temp

    word_len = len(word)

    print("cords: ", end='')
    print(cords)
    print("word: ", end='')
    print(word)

    # up  
    if (cords[2] == "up"):
        #        grid_coppy = grid

        print("trying up" )
        for x in range(word_len):
            if (grid_coppy[cords[0]-x][cords[1]] == 0):
                grid_coppy[cords[0]-x][cords[1]] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]-z][cords[1]] = word[z]
                        if z == word_len -1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)

    # down  
    if (cords[2] == "down"):
        #        #        grid_coppy = grid
        print("trying down")
        for x in range(word_len):
            if (grid_coppy[cords[0]+x][cords[1]] == 0):
                grid_coppy[cords[0]+x][cords[1]] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]+z][cords[1]] = word[z]
                        if z == word_len -1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0

                return (grid)
        return(grid_coppy)

    # left  
    if (cords[2] == "left"):
        #        #        grid_coppy = grid


        print("trying left")
        for x in range(word_len):
            if(grid_coppy[cords[0]][cords[1]-x] == 0): 
                grid_coppy[cords[0]][cords[1]-x] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]][cords[1]-z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)

    # right  
    if (cords[2] == "right"):
        #        grid_coppy = grid

        print("trying right")
        for x in range(word_len):
            if (grid_coppy[cords[0]][cords[1]+x] == 0): 
                grid_coppy[cords[0]][cords[1]+x] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]][cords[1]+z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)

    # \ diaginal up 
    if (cords[2] == "DiagUpRight"):
        #        grid_coppy = grid

        print("trying DiagUpRight")
        for x in range(word_len):
            if (grid_coppy[cords[0]-x][cords[1]+x] == 0): 
                grid_coppy[cords[0]-x][cords[1]+x] = 0
                if x == word_len - 1:
                    for z in word_len:
                        grid_coppy[cords[0]-z][cords[1]+z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return(grid)
        return(grid_coppy)

    # \ diaginal  down
    
    if (cords[2] == "diagUpLeft"):
        #        grid_coppy = grid

        print("trying diagUpLeft")
        for x in range(word_len):
            if (grid_coppy[cords[0]-x][cords[1]-x] == 0):
                grid_coppy[cords[0]-x][cords[1]-x] = 0
                if x == word_len - 1:
                    for z in word_len:
                        grid_coppy[cords[0]-z][cords[1]-z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)

    # / diaginal  up
    if (cords[2] == "diagDownRight"):
        #        grid_coppy = grid

        print("trying diagDownRight")
        for x in range(word_len):
            if (grid_coppy[cords[0]+x][cords[1]+x] == 0):
                grid_coppy[cords[0]+x][cords[1]+x] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]+z][cords[1]+z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)
    
    # / diaginal  down
    if (cords[2] == "diagDownLeft"):
        #        grid_coppy = grid

        print("diagDownLeft")
        for x in range(word_len):
            if (grid_coppy[cords[0]+x][cords[1]-x] == 0):
                grid_coppy[cords[0]+x][cords[1]-x] = 0
                if x == word_len - 1:
                    for z in range(word_len):
                        grid_coppy[cords[0]+z][cords[1]-z] = word[z]
                        if z == word_len - 1:
                            break
                else:
                    continue
            else:
                grid_coppy[cords[0]-x][cords[1]] = 0
                return (grid)
        return(grid_coppy)

app.run(debug = True) 
