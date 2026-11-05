from turtle import Turtle, Screen

# Constraints
VISUAL_LOS = 280

class UIManager:
    """Manages standalone menu self.screens, static lines, and visual alerts."""
    def __init__(self):
        self.screen = Screen()
        self.menu_writer = Turtle()
        self.game_over_writer = Turtle()

        self.score_writer = Turtle()
        self.score_writer.clear()
        self.score_writer.hideturtle()
        self.score_writer.color("white")
        self.score_writer.penup()
        self.score_writer.goto(0, 280)
        self.score = 0

        self.draw_boundary()
        self.write_score()


    def draw_boundary(self):
        self.screen.tracer(0)

        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.color("white")
        writer.goto(-VISUAL_LOS, -VISUAL_LOS)
        writer.setheading(90)
        writer.pendown()

        self.screen.update()
        self.screen.tracer(1)

        for _ in range(4):
            writer.forward(VISUAL_LOS * 2)
            writer.setheading(writer.heading() - 90)
        writer.penup()

    def write_menu(self, msg: str):
        # setup message writer
        self.menu_writer.clear()
        self.menu_writer.hideturtle()
        self.menu_writer.penup()
        self.menu_writer.color("white")

        # write the message
        self.menu_writer.goto(0, 240)
        self.menu_writer.write(msg, align="center", font=("Courier", 12, "normal"))
        self.screen.update()

    def clear_menu(self):
        self.menu_writer.clear()
        self.screen.update()

    def write_game_over(self, msg1: str, msg2: str):
        self.game_over_writer.clear()
        self.game_over_writer.hideturtle()
        self.game_over_writer.penup()
        self.game_over_writer.color("red")
        self.game_over_writer.goto(0, 40)
        self.game_over_writer.write(msg1, align="center", font=("Courier", 24, "bold"))
        self.game_over_writer.color("white")
        self.game_over_writer.goto(0, 0)
        self.game_over_writer.write(msg2, align="center", font=("Courier", 14, "normal"))
        self.screen.update()

    def clear_game_over(self):
        self.game_over_writer.clear()
        self.screen.update()

    def write_score(self):
        self.score_writer.clear()
        self.score_writer.write(f"SCORE: {self.score}", align="center", font=("Courier", 10, "normal") )
        self.screen.update()

    def update_score(self):
        self.score +=1
        self.write_score()

    def reset_score(self):
        self.score = 0
        self.write_score()