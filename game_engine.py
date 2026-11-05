from snake import Snake
from ui import UIManager
from food import Food
from screen import screen

class GameEngine:
    """Orchestrates loop cycles, active state controls, and event listeners."""
    def __init__(self):
        self.ui = UIManager()
        self.snake = Snake()
        self.food = Food()
        self.is_game_on = False
        
        self.setup_game()

    def setup_game(self):
        self.ui.write_menu("Press SPACE to start the game.")
        screen.listen()
        screen.onkey(self.start_game, 'space')

    def start_game(self):
        self.ui.clear_menu()
        self.food.position_food()
        screen.onkey(None, 'space')

        screen.onkey(self.snake.turn_up, "w")
        screen.onkey(self.snake.turn_down, "s")
        screen.onkey(self.snake.turn_right, "d")
        screen.onkey(self.snake.turn_left, "a")

        self.is_game_on = True
        self.game_loop()
    
    def game_loop(self):
        if not self.is_game_on:
            return
        
        self.snake.move()

        # Check collision with food
        if self.snake.segments[0].distance(self.food) < 15.0:
            self.food.hideturtle()
            self.snake.add_segment()
            self.ui.update_score()
            self.food.position_food()

        # Check collision with wall or tail
        if self.snake.has_collided():
            self.is_game_on = False
            self.ui.write_game_over("GAME OVER!", "Press 'r' to play again.")
            screen.onkey(self.restart_game, 'r')
            return

        screen.ontimer(self.game_loop, 100)

    def restart_game(self):
        screen.onkey(None, 'r')
        self.ui.clear_game_over()
        self.ui.reset_score()
        self.snake.snake_reset()
        self.setup_game()


