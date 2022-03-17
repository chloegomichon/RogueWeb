from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game, player

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()

@app.route("/")
def index():
    map = game.getMap()
    game_player = game.getPlayer()
    return render_template("index.html", mapdata=map, n_row=len(map),n_col=len(map[0]), playerdata = game_player)

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]
    game_player = game.getPlayer()
    print(game_player.money)
    data, ret = game.move(dx,dy)
    if ret:
        socketio.emit("response", data)  
    

if __name__=="__main__":
    socketio.run(app, port=5001)


