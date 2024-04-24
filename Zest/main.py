import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Taille de la grille
ROWS = 50
COLS = 50

# Fonction pour initialiser la grille avec des cellules aléatoirement vivantes ou mortes
def init_grid():
    return np.random.choice([0, 1], size=(ROWS, COLS))

# Fonction pour calculer l'état de la cellule suivante en fonction de ses voisines
def next_cell_state(curr_state, num_neighbors):
    if curr_state == 1:
        if num_neighbors < 2 or num_neighbors > 3:
            return 0  # La cellule meurt de solitude ou de surpopulation
        else:
            return 1  # La cellule reste vivante
    else:
        if num_neighbors == 3:
            return 1  # Une cellule morte renaît
        else:
            return 0  # La cellule reste morte

# Fonction pour calculer le nombre de voisins vivants d'une cellule
def count_neighbors(grid, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i != row or j != col) and 0 <= i < ROWS and 0 <= j < COLS:
                count += grid[i, j]
    return count

# Fonction pour mettre à jour la grille pour la prochaine étape
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(ROWS):
        for j in range(COLS):
            num_neighbors = count_neighbors(grid, i, j)
            new_grid[i, j] = next_cell_state(grid[i, j], num_neighbors)
    return new_grid

# Fonction pour animer la simulation
def animate(frame, img, grid):
    new_grid = update_grid(grid)
    img.set_array(new_grid)
    grid[:] = new_grid[:]
    return img,

# Initialisation de la grille
grid = init_grid()

# Initialisation de la figure
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')

# Animation
ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=100, blit=True, interval=100)
plt.show()
