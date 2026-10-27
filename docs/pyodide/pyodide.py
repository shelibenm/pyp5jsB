def setup():
    createCanvas(200, 200)

def draw():
    background(200)
    diameter = sin(frameCount / 60) * 50 + 50
    fill("blue")
    ellipse(100, 100, diameter, diameter)
    fill(23,30,45)
    rect(30,50,89)
    
