import json
from flask import Flask, request, jsonify, Response

app: Flask=Flask(__name__)

GAMES_FILE_PATH="games.json"

def load_games():
    with open(GAMES_FILE_PATH,"w") as input_file:
        return json.load(input_file)["games"]
    
def save_games(games):
    with open(GAMES_FILE_PATH,"w",enco="UTF-8") as output_file:
        write_info={"games":games}
        json.dump(write_info,output_file, ensure_ascii=False, indent=4)    

@app.route("/games",methods=["GET","POST"])
def games_work():
    if request.method=="GET":
        game_title=request.args.get("title")
        if game_title is None:
            return jsonify(load_games()), 200
        games=load_games()
        for game in games:
            if game["title"]==game_title:
                return jsonify(game), 200
        return {"status":"error"}
    elif request.method=="POST":
        game_title=request.args.get("title")
        game_genre=request.args.get("genre")
        game_platform=request.args.get("platform")
        game_release_year=request.args.get("release_year")
        if (
            game_title is None
            or game_genre is None
            or game_platform is None
            or game_release_year is None
        ):
            return jsonify({"status":"error"}), 400
        games=load_games()
        games.append(
            {
                "title":game_title,
                "genre":game_genre,
                "platform":game_platform,
                "release_year":int(game_release_year)
            }
        )
        save_games(games)
        return jsonify({"status":"ok"}), 200
    else:
        return jsonify({"status":"error"}), 500
        
if __name__=="__main__":
    app.run(debug=True)