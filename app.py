from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game, player

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()

@app.route("/")
def index():
    map = game.getMap()
    game_player1 = game.getPlayer1()
    game_player2 = game.getPlayer2()
    return render_template("index.html", mapdata=map, n_row=len(map),n_col=len(map[0]), playerdata1 = game_player1,playerdata2 = game_player2)

@socketio.on("move_P1")
def on_move_msg_P1(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]
    
    data, ret = game.move_P1(dx,dy)
    if ret:
        socketio.emit("response", data)  
    

@socketio.on("move_P2")
def on_move_msg_P2(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]
    
    data, ret = game.move_P2(dx,dy)
    if ret:
        socketio.emit("response", data)  
    

@socketio.on("move_enemies")
def on_move_enemy_msg():
    print("received move enemies message")
    all_enemies_data = game.move_enemies()
    socketio.emit("response_enemies", all_enemies_data)

if __name__=="__main__":
    socketio.run(app, port=5001)

