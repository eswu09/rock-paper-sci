import random

import os
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def index():
    return """\
<html>
<style>
.hand {
    width: 256px;
    height: 256px;
    border: 2px solid black;
    float: left;
    margin-right: 20px;
    margin-bottom: 20px;
    background-position: 50% 50%;
    background-size: cover;
}
.options {
    clear: both;
}
.option {
    width: 72px;
    height: 72px;
    border: 2px solid black;
    float: left;
    margin-right: 16px;
    background-position: 50% 50%;
    background-size: cover;
}
.rock { background-image: url("/rock.jpg"); }
.paper { background-image: url("/paper.jpg"); }
.scissors { background-image: url("/scissors.jpg"); }

</style>
<script src="http://code.jquery.com/jquery-2.2.4.min.js"
        integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="
        crossorigin="anonymous">
</script>
<script>
$(document).ready(function() {

    function playHand(player, play) {
        $('.hand.'+player).removeClass('rock paper scissors');
        $('.hand.'+player).addClass(play);
        return play;
    }

    function score(human, computer) {
        var h2 = $('h2');
        if (human === computer) {
            h2.text('Tie!');
        } else if (human === 'rock') {
            if (computer === 'paper') {
                h2.text('You lose!');
            } else {
                h2.text('You win!');
            }
        } else if (human === 'paper') {
            if (computer === 'scissors') {
                h2.text('You lose!');
            } else {
                h2.text('You win!');
            }
        } else if (human === 'scissors') {
            if (computer === 'rock') {
                h2.text('You lose!');
            } else {
                h2.text('You win!');
            }
        }
    }

    $('.option').click(function() {
        var human = playHand('human', $(this).text());
        $.get('/choice', function(play) {
            var computer = playHand('computer', play);
            score(human, computer);
        });

    });
});
</script>

<body>
    <h1>Greetings, rock paper sci!</h1>
    <div class="hand human"></div>
    <div class="hand computer"></div>
    <div class="options">
        <div class="option rock">rock</div>
        <div class="option paper">paper</div>
        <div class="option scissors">scissors</div>
    </div>
    <h2></h2>
</body>
</html>
"""

@app.route("/choice")
def choice():
    return random.choice(['rock', 'paper', 'scissors'])


@app.route("/rock.jpg")
def rock():
    jpg = open('rock.jpg').read()
    return Response(jpg, mimetype='image/jpg')

@app.route("/paper.jpg")
def paper():
    jpg = open('paper.jpg').read()
    return Response(jpg, mimetype='image/jpg')

@app.route("/scissors.jpg")
def scissors():
    jpg = open('scissors.jpg').read()
    return Response(jpg, mimetype='image/jpg')

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    print("Serving on port", port)
    app.run(port=port)
