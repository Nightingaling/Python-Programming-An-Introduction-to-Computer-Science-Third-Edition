# **Question 9**
**Code**:
```python
from graphics import *

class Interface:

    def __init__(self):
        self.win = GraphWin('Breakout', 600, 600)
        self.win.setBackground('grey')
        #Paddle
        self.drawPaddle()
        #Ball
        self.drawBall()
        #Bricks
        self.drawBricks()
        #Lives
        self.lives = []
        x, y = 30, 30
        for i in range(3):
            life = Circle(Point(x,y), 10)
            life.setFill('white')
            life.setOutline('white')
            life.draw(self.win)
            self.lives.append(life)
            x = x + 25
        #Score
        self.displayScore = Text(Point(300,35), 0)
        self.displayScore.setFill('white')
        self.displayScore.setStyle('bold')
        self.displayScore.setSize(30)
        self.displayScore.draw(self.win)

    def drawBall(self):
        self.ball = Circle(Point(300,540), 10)
        self.ball.setFill('white')
        self.ball.setOutline('white')
        self.ball.draw(self.win)

    def drawBricks(self):
        color = ['blue','red','yellow','green']
        x, y = 75, 75
        x1, y1 = 135, 105
        self.Bricks = []
        for i in range(4):
            for j in range(7):
                brick = Rectangle(Point(x,y),Point(x1,y1))
                brick.setFill(color[i])
                brick.setOutline(color[i])
                self.Bricks.append(brick)
                brick.draw(self.win)
                x, x1 = x + 65, x1 + 65
            x, x1 = 75, 135
            y, y1 = (y + 35), (y1 + 35)

    def getBricks(self):
        return self.Bricks

    def checkBrick(self, brick):
        if brick.getP1().getX() <= self.ball.getP2().getX() <= brick.getP2().getX() and brick.getP1().getY() <= self.ball.getP2().getY() <= brick.getP2().getY():
            if brick.getP1().getX() <= self.ball.getCenter().getX() <= brick.getP2().getX():
                return 'top'
            elif brick.getP1().getY() <= self.ball.getCenter().getY() <= brick.getP2().getY():
                return 'left'
            else:
                return 'topleft'
        elif brick.getP1().getX() <= self.ball.getP1().getX() <= brick.getP2().getX() and brick.getP1().getY() <= self.ball.getP1().getY() <= brick.getP2().getY():
            if brick.getP1().getX() <= self.ball.getCenter().getX() <= brick.getP2().getX():
                return 'bottom'
            elif brick.getP1().getY() <= self.ball.getCenter().getY() <= brick.getP2().getY():
                return 'right'
            else:
                return 'bottomright'
        elif brick.getP1().getX() <= self.ball.getP2().getX() <= brick.getP2().getX() and brick.getP1().getY() <= self.ball.getP1().getY() <= brick.getP2().getY():
            return 'bottomleft'
        elif brick.getP1().getX() <= self.ball.getP1().getX() <= brick.getP2().getX() and brick.getP1().getY() <= self.ball.getP2().getY() <= brick.getP2().getY():
            return 'topright'

    def deleteBrick(self, brick):
        brick.undraw()
        self.Bricks.remove(brick)

    def checkKey(self):
        return self.win.checkKey()

    def drawPaddle(self):
        self.paddle = Rectangle(Point(240,555), Point(360,565))
        self.paddle.setFill('white')
        self.paddle.setOutline('white')
        self.paddle.draw(self.win)

    def getPaddle(self, pt, axis):
        if pt == 1 and axis == 'x':
            return self.paddle.getP1().getX()
        elif pt == 2 and axis == 'x':
            return self.paddle.getP2().getX()
        elif pt == 1 and axis == 'y':
            return self.paddle.getP1().getY()
        elif pt == 2 and axis == 'y':
            return self.paddle.getP2().getY()
        elif axis == 'center':
            return self.paddle.getCenter().getX()

    def movePaddle(self, direction, ballMoving):
        if direction == 'left' and (not ballMoving):
            self.paddle.move(-10,0)
            self.ball.move(-10,0)
        elif direction == 'right' and (not ballMoving):
            self.paddle.move(10,0)
            self.ball.move(10,0)
        elif direction == 'left' and ballMoving:
            self.paddle.move(-10,0)
        else:
            self.paddle.move(10,0)

    def getBall(self, pt, axis):
        if pt == 1 and axis == 'x':
            return self.ball.getP1().getX()
        elif pt == 2 and axis == 'x':
            return self.ball.getP2().getX()
        elif pt == 1 and axis == 'y':
            return self.ball.getP1().getY()
        elif pt == 2 and axis == 'y':
            return self.ball.getP2().getY()
        elif axis == 'center':
            return self.ball.getCenter().getX()

    def moveBall(self, dx, dy):
        self.ball.move(dx,dy)

    def undrawBall(self):
        self.ball.undraw()

    def ballHitPaddleCenter(self):
        return (self.getPaddle(None, 'center') == self.getBall(None, 'center'))

    def ballHitPaddleY(self):
        return (self.getPaddle(1, 'y') <= self.getBall(2, 'y') <= self.getPaddle(2, 'y'))

    def ballHitPaddleX(self):
        if self.getPaddle(1, 'x') <= self.getBall(2, 'x') <= self.getPaddle(2, 'x'):
            return True
        elif self.getPaddle(1, 'x') <= self.getBall(1, 'x') <= self.getPaddle(2, 'x'):
            return True
        else:
            return False

    def updateLives(self):
        self.lives[-1].undraw()
        del self.lives[-1]
        self.paddle.undraw()
        self.drawPaddle()
        self.ball.undraw()
        self.drawBall()

    def updateScore(self, score):
        self.displayScore.setText(score)

    def GameOver(self, score):
        display_rec = Rectangle(Point(150,200), Point(450,400))
        display_rec.setOutline('white')
        display_rec.setWidth(3)
        display_rec.draw(self.win)
        display_text = Text(Point(300,250), 'GAME OVER')
        display_text.setSize(28)
        display_text.setStyle('bold')
        display_text.setTextColor('white')
        display_text.draw(self.win)
        display_text = Text(Point(300,320), 'SCORE')
        display_text.setSize(18)
        display_text.setStyle('bold')
        display_text.setTextColor('white')
        display_text.draw(self.win)
        display_text = Text(Point(300,360), score)
        display_text.setSize(18)
        display_text.setStyle('bold')
        display_text.setTextColor('white')
        display_text.draw(self.win)
        self.win.getMouse()
        self.win.close()


class Breakout:

    def __init__(self):
        self.dx, self.dy = -0.5, -1
        self.ballMoving = False
        self.lives = 3
        self.score = 0
        self.dt = 300

    def run(self, interface):
        while self.lives != 0:
            key = interface.checkKey()
            if key == 'Left':
                if interface.getPaddle(1, 'x') != 0:
                    interface.movePaddle('left', self.ballMoving)
            elif key == 'Right':
                if interface.getPaddle(2, 'x') != 600:
                    interface.movePaddle('right', self.ballMoving)
            elif key == 'Up' or key == 'space':
                self.ballMoving = True
            if self.ballMoving:
                interface.moveBall(self.dx, self.dy)
                if interface.getBall(1, 'x') <= 0 or interface.getBall(2, 'x') >= 600:
                    self.dx = -self.dx
                elif interface.getBall(1, 'y') <= 0:
                    self.dy = -self.dy
                elif interface.ballHitPaddleY():
                    if interface.ballHitPaddleCenter():
                        self.dy = -self.dy
                    if interface.ballHitPaddleX():
                        self.dy = -self.dy
                        ballMiddle = interface.getBall(None, 'center')
                        paddleMiddle = interface.getPaddle(None, 'center')
                        self.dx = (ballMiddle - paddleMiddle) / 60
                elif interface.getBall(1, 'y') <= 210:
                    Bricks = interface.getBricks()
                    for brick in Bricks:
                        brickHit = interface.checkBrick(brick)
                        if brickHit in ['top', 'bottom', 'topleft', 'bottomleft', 'topright', 'bottomright']:
                            self.dy = -self.dy
                            self.score = self.score + 50
                            interface.deleteBrick(brick)
                            interface.updateScore(self.score)
                        elif brickHit == 'left' or brickHit == 'right':
                            self.dx = -self.dx
                            self.score = self.score + 50
                            interface.deleteBrick(brick)
                            interface.updateScore(self.score)
                elif interface.getBall(1, 'y') > 600:
                    self.lives = self.lives - 1
                    interface.updateLives()
                    self.ballMoving = False
                    self.dx, self.dy = -0.5, -1
                    self.dt = 300
                if interface.getBricks() == []:
                    self.dt = self.dt + 50
                    interface.drawBricks()
            update(self.dt)
        interface.GameOver(self.score)


def main():
    Breakout().run(Interface())


if __name__ == '__main__':
    main()
