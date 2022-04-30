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
    game_player2 = game.getPlayer2()
    return render_template("index.html", mapdata=map, n_row=len(map),n_col=len(map[0]), playerdata = game_player,playerdata2 = game_player2)

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]
    
    data, ret = game.move(dx,dy)
    if ret:
        socketio.emit("response", data) 
        socketio.emit("responseP1", data) 
    
    #return render_template("main.js", playerdata = game_player_m)
@socketio.on("move2")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move2 ws message")
    dx = json['dx']
    dy = json["dy"]
    
    data, ret = game.move2(dx,dy)
    if ret:
        socketio.emit("response", data)  
        socketio.emit("responseP2", data) 
    
    #return render_template("main.js", playerdata = game_player_m)

@socketio.on("move_enemies")
def on_move_enemy_msg():
    print("received move enemies message")
    all_enemies_data = game.move_enemies()
    socketio.emit("response_enemies", all_enemies_data)

@socketio.on("attack1")
def attack1_msg():
    print("attack 1 message")
    attack1_data = game.attack1()
    socketio.emit("attack 1 data", attack1_data)

@socketio.on("attack2")
def attack2_msg():
    print("attack 2 message")
    attack1_data = game.attack1()
    socketio.emit("attack 2 data", attack1_data)

if __name__=="__main__":
    socketio.run(app, port=5001)

