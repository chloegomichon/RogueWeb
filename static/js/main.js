
window.addEventListener("DOMContentLoaded", (event) => {
    var socket = io.connect("http://" + document.domain + ":" + location.port );

    document.onkeydown = function(e){
        switch(e.keyCode){
            case 37:
                socket.emit("move", {dx:-1, dy:0});
                break;
            case 38:
                socket.emit("move", {dx:0, dy:-1});
                break;
            case 39:
                socket.emit("move", {dx:1, dy:0});
                break;
            case 40:
                socket.emit("move", {dx:0, dy:1});
                break;
        }


    };
    
    var btn_n = document.getElementById("go_n");
    btn_n.onclick = function(e) {
        console.log("Clicked on button north");
        socket.emit("move", {dx:0, dy:-1});
    };

    var btn_s = document.getElementById("go_s");
    btn_s.onclick = function(e) {
        console.log("Clicked on button south");
        socket.emit("move", {dx:0, dy:1});
    };

    var btn_w = document.getElementById("go_w");
    btn_w.onclick = function(e) {
        console.log("Clicked on button w");
        socket.emit("move", {dx:-1, dy:0});
    };

    var btn_e = document.getElementById("go_e");
    btn_e.onclick = function(e) {
        console.log("Clicked on button e");
        socket.emit("move", {dx:1, dy:0});
    };

    socket.on("response", function(data){
        //console.log(data);
        for( var i=0; i<2; i++){
            var cell_id = "cell " + data[i].i + "-" + data[i].j;
            var span_to_modif = document.getElementById(cell_id);
            var pass_on_cash = data[i].pass_on_cash
            if (pass_on_cash == true){
                span_to_modif.style.backgroundColor = 'azure';
                }
            span_to_modif.textContent = data[i].content;
        };

        if (data !== []){
            let money_tag = document.getElementById("money")
            let life_tag = document.getElementById("life")
            let weapon_tag = document.getElementById("weapons")
            let treasure = data[1].treasure
            console.log('trésor trouvé')

            money_tag.textContent = `Nombre de pièces : ${data[2]}`
            life_tag.textContent = `Points de vie : ${data[3]}`
            weapon_tag.textContent = `Armes : ${data[4]}`

            if(data[3] == 0){
                document.getElementById('hideaway').style.display='block'
            }

            if(treasure){
                treasure == false
                document.getElementById('win').style.display='block'
                socket.emit("next")
                window.location.reload(true);
            }
        }
        
        
    });
    

    socket.on("response_enemies", function(enemies_data){
        console.log(enemies_data);
        for(let data of enemies_data){
            for(var i=0; i<2; i++){
                var cell_id = "cell " + data[i].i + "-" + data[i].j;
                var span_to_modif = document.getElementById(cell_id);    
                span_to_modif.textContent = data[i].content;
            }
        }
    });

    setInterval(function(){
        socket.emit("move_enemies")
    }, 500);

    let money = player_data_m.money;

    
});