class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        
        self.x = 0
        self.y = 0
        
        # East, North, West, South
        self.dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        self.dir_names = ["East", "North", "West", "South"]
        
        self.dir = 0
        self.perimeter = 2 * (width + height) - 4

    def step(self, num):
        k = num % self.perimeter
        
        # 🔥 IMPORTANT FIX
        if k == 0:
            k = self.perimeter
        
        for _ in range(k):
            dx, dy = self.dirs[self.dir]
            nx, ny = self.x + dx, self.y + dy
            
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                # turn CCW
                self.dir = (self.dir + 1) % 4
                dx, dy = self.dirs[self.dir]
                nx, ny = self.x + dx, self.y + dy
            
            self.x, self.y = nx, ny

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dir_names[self.dir]