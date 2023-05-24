import random

# ������� ��� ������������� ������� �����
def initialize_grid(size):
    grid = [[0] * size for _ in range(size)]
    return grid

# ������� ��� ���������� ����� ��������� ������ (2 ��� 4) � �����
def add_new_tile(grid):
    size = len(grid)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if grid[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[row][col] = random.choice([2, 4])

# ������� ��� ��������, �������� �� ����
def is_game_over(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                return False
            if i < size - 1 and grid[i][j] == grid[i + 1][j]:
                return False
            if j < size - 1 and grid[i][j] == grid[i][j + 1]:
                return False
    return True

# ������� ��� ���������� ������ ����� �� �����
def swipe_left(grid):
    size = len(grid)
    for i in range(size):
        j = 0
        while j < size - 1:
            if grid[i][j] == 0:
                k = j + 1
                while k < size and grid[i][k] == 0:
                    k += 1
                if k < size:
                    grid[i][j] = grid[i][k]
                    grid[i][k] = 0
            if j < size - 1 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
            j += 1

# ������� ��� ���������� ������ ������ �� �����
def swipe_right(grid):
    size = len(grid)
    for i in range(size):
        j = size - 1
        while j > 0:
            if grid[i][j] == 0:
                k = j - 1
                while k >= 0 and grid[i][k] == 0:
                    k -= 1
                if k >= 0:
                    grid[i][j] = grid[i][k]
                    grid[i][k] = 0
            if j > 0 and grid[i][j] == grid[i][j - 1]:
                grid[i][j] *= 2
                grid[i][j - 1] = 0
            j -= 1

# ������� ��� ���������� ������ ����� �� �����
def swipe_up(grid):
    size = len(grid)
    for j in range(size):
        i = 0
        while i < size - 1:
            if grid[i][j] == 0:
                k = i + 1
                while k < size and grid[k][j] == 0:
                    k += 1
                if k < size:
                    grid[i][j] = grid[k][j]
                    grid[k][j] = 0
            if i < size - 1 and grid[i][j] == grid[i + 1][j]:
                grid[i][j] *= 2
                grid[i + 1][j] = 0
            i += 1

# ������� ��� ���������� ������ ���� �� �����
def swipe_down(grid):
    size = len(grid)
    for j in range(size):
        i = size - 1
        while i > 0:
            if grid[i][j] == 0:
                k = i - 1
                while k >= 0 and grid[k][j] == 0:
                    k -= 1
                if k >= 0:
                    grid[i][j] = grid[k][j]
                    grid[k][j] = 0
            if i > 0 and grid[i][j] == grid[i - 1][j]:
                grid[i][j] *= 2
                grid[i - 1][j] = 0
            i -= 1

# ������� ��� ������ ������� �����
def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

# ������� ���������� ������� ����������
def save_best_score(score):
    with open("best_score.txt", "w") as file:
        file.write(str(score))

# ������� ��� �������� ���������� ����������
def load_best_score():
    try:
        with open("best_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# ������� ��� ��������������� ����
def play_game(size):
    grid = initialize_grid(size)
    add_new_tile(grid)
    print("Welcome to 2048!")
    print_grid(grid)
    score = 0
    best_score = load_best_score()
    while not is_game_over(grid):
        move = input("Enter your move (w/a/s/d/bot): ").lower()
        if move == 'w':
            swipe_up(grid)
        elif move == 'a':
            swipe_left(grid)
        elif move == 's':
            swipe_down(grid)
        elif move == 'd':
            swipe_right(grid)
        elif move == 'bot':
            # ��� ������������� ���� �������������
            bot_play(grid)
        else:
            print("Invalid move! Please try again.")
            continue
        add_new_tile(grid)
        print_grid(grid)
        score += 1
        if score > best_score:
            best_score = score
            save_best_score(best_score)
        print("Current Score:", score)
        print("Best Score:", best_score)
    print("Game over! Your score is:", score)

# ������� ��� ��������������� ��������������� ���� �����
def bot_play(grid):
    # ���������� ���� ������ ���� �����
    # ��� ������� ���, ������� �������� ��������� ���
    moves = ['w', 'a', 's', 'd']
    random_move = random.choice(moves)
    print("Bot move:", random_move)
    if random_move == 'w':
        swipe_up(grid)
    elif random_move == 'a':
        swipe_left(grid)
    elif random_move == 's':
        swipe_down(grid)
    elif random_move == 'd':
        swipe_right(grid)

# �������� ������� ��� ������� ����
def main():
    level = input("Choose the level (easy/medium/difficult): ").lower()
    if level == 'easy':
        play_game(6)
    elif level == 'medium':
        play_game(5)
    elif level == 'difficult':
        play_game(4)
    else:
        print("Invalid level! Please try again.")

# nachat igru
if __name__ == '__main__':
    main()

