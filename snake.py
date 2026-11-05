from turtle import Turtle, Screen

# Constraints
GRID_SIZE = 20
BOUNDARY_LIMIT = 260

class Snake:
    """Manages the snake's body, core physics movement, and directional state."""
    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.segment_pool = []
        self.current_heading = 0
        self.cords = [(0,0), (-GRID_SIZE, 0), (-2 * GRID_SIZE, 0)]
        self.can_turn = True
        self.setup_snake()

    def create_segment(self):
        segment = Turtle(shape = "square")
        segment.color("white")
        segment.penup()
        return segment

    def setup_snake(self):
        self.screen.tracer(0)
        for _ in range(3):
            self.segments.append(self.create_segment())

        for i, cord in enumerate(self.cords):
            self.segments[i].goto(cord)
        self.screen.update()
        self.screen.tracer(1)

    def move(self):
        self.screen.tracer(0)
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  
    
        self.segments[0].setheading(self.current_heading)  
        self.segments[0].forward(20)
        self.screen.update()
        self.screen.tracer(1)

        self.can_turn = True

    def turn_up(self):
        if self.can_turn and (self.current_heading == 0 or self.current_heading == 180):
            self.current_heading = 90
            self.can_turn = False

    def turn_down(self):
        if self.can_turn and (self.current_heading == 0 or self.current_heading == 180):
            self.current_heading = 270
            self.can_turn = False

    def turn_right(self):
        if self.can_turn and (self.current_heading == 90 or self.current_heading == 270):
            self.current_heading = 0
            self.can_turn = False

    def turn_left(self):
        if self.can_turn and (self.current_heading == 90 or self.current_heading == 270):
            self.current_heading = 180
            self.can_turn = False

    def add_segment(self):
        self.screen.tracer(0)
        if self.segment_pool:
            new_seg = self.segment_pool.pop()
            new_seg.showturtle()
        else:
            new_seg = self.create_segment()

        new_seg.goto(self.segments[-1].position())
        self.segments.append(new_seg)
        self.screen.update()
        self.screen.tracer(1)

    def has_collided(self):
        head_x = self.segments[0].xcor()
        head_y = self.segments[0].ycor()

        # Wall Collision Check
        if abs(head_x) > BOUNDARY_LIMIT or abs(head_y) > BOUNDARY_LIMIT:
            print("Wall collision:", head_x, head_y)
            return True

        # Tail Collision Check
        for index, segment in enumerate(self.segments[2:], start=2):
            distance = self.segments[0].distance(segment)
            if distance < 15:
                print("Body collision:", index, distance,
                    self.segments[0].position(), segment.position())
                return True
            
        return False

    def snake_reset(self):
        self.screen.tracer(0)

        extras = self.segments[3:]
        for extra_seg in extras:
            extra_seg.hideturtle()

        self.segment_pool.extend(extras)
        self.segments = self.segments[:3]

        for segment, position in zip(self.segments, self.cords):
            segment.goto(position)

        self.current_heading = 0
        self.can_turn = True

        self.screen.update()
        self.screen.tracer(1)