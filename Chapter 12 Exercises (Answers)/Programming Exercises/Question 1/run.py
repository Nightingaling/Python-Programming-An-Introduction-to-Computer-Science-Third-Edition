from graphicsinterface import GraphicsInterface
from pokerapp import PokerApp
from splashscreen import SplashScreen

if SplashScreen().enter():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()
