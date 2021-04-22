class Paddle():
    def __init__(self, x=None, y=None, paddle_width=20, paddle_height=100):
        self.x = x
        self.y = height - paddle_height
        self.width = paddle_width
        self.height = paddle_height
        self.y_speed = 0
        
        if y is not None:
            self.x = x
        
    def update(self):
        if (self.y + self.y_speed >= 0) and (self.y + self.y_speed <= width - self.width):
            self.y += self.y_speed
        
    def draw(self):
        push()
        fill(255)
        rect(self.x, self.y, self.width, self.height)
        pop()
