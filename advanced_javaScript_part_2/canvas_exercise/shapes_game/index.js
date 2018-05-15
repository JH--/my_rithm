window.addEventListener("load", function() {

  function chooseRandom(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
  }

  function clear(ctx, width, height) {
    ctx.clearRect(0, 0, width, height);
  }

  function drawTriangle(x, y) {
    ctx.beginPath();
    ctx.lineTo(x,y);
    ctx.lineTo(x+(width*0.2), y+(height*0.2));
    ctx.lineTo(x, y+(height*0.2));
    ctx.fill();
    ctx.closePath();
  }

  function drawRedTriangle() {
    ctx.fillStyle = "red";
    drawTriangle(chooseRandom(0, width - (width * 0.2)),
                 chooseRandom(0, height - (height * 0.2)));
    expectedKey = "ArrowLeft";
  }

  function drawWhiteTriangle() {
    ctx.fillStyle = "white";
    drawTriangle(chooseRandom(0, width - (width * 0.2)),
                 chooseRandom(0, height - (height * 0.2)));
    expectedKey = "ArrowUp"; 
  }

  function drawSquare(x, y) {
    ctx.beginPath();
    ctx.moveTo(x,y);
    ctx.lineTo(x+(width*0.2), y);
    ctx.lineTo(x+(width*0.2), y+(height*0.2));
    ctx.lineTo(x, y+(height*0.2));
    ctx.fill();
    ctx.closePath();
  }

  function drawRedSquare() {
    ctx.fillStyle = "red";
    drawSquare(chooseRandom(0, width - (width * 0.2)),
               chooseRandom(0, height - (height * 0.2)));
    expectedKey = "ArrowDown";
  }

  function drawWhiteSquare() {
    ctx.fillStyle = "white";
    drawSquare(chooseRandom(0, width - (width * 0.2)),
               chooseRandom(0, height - (height * 0.2)));
    expectedKey = "ArrowRight";    
  }

  function drawRandomShape(shapes) {
    shapes[chooseRandom(0, shapes.length)]();
  }

  function drawGameStartText(ctx, width, height) {
    ctx.fillStyle = "white";
    ctx.fillText("Press the space bar to start a new game", width, height);
  }

  function startGame(ctx, width, height, shapes) {
    clear(ctx, width, height);
    [score, scoreSpan.textContent] = [0, 0];
    [seconds, timerSpan.textContent] = [30, 30];
    gameOn = true;
    drawRandomShape(shapes);
    //set interval to count down seconds of time until 0 then end the game
    let timer = setInterval(() => {
      seconds -= 1;
      timerSpan.textContent = seconds;
      if(seconds === 0){
        clearInterval(timer);
        endGame(ctx, width, height);
      }
    }, 1000);
  }

  function update(ctx, score, shapes) {
    scoreSpan.textContent = score;
    clear(ctx, width, height);
    drawRandomShape(shapes);
  }

  function endGame(ctx, width, height) {
    clear(ctx, width, height);
    ctx.fillStyle = "white";
    ctx.fillText(`Game over! You scored ${score} point${(() => Math.abs(score) !== 1 ? 's' : '')()}`, width/2, height/2);
    drawGameStartText(ctx, width/2, height - (height/10));
    gameOn = false;
  }

  let canvas = document.getElementById("shapes-game"),
      height = canvas.scrollHeight,
      width = canvas.scrollWidth,
      gameOn = false,
      expectedKey = undefined,
      ctx = canvas.getContext('2d'),
      timerSpan = document.getElementById("time-remaining"),
      scoreSpan = document.getElementById("score-val"),
      seconds = 30,
      score = 0,
      shapes = [drawRedTriangle, drawWhiteSquare, drawRedSquare, drawWhiteTriangle];

  canvas.width = width;
  canvas.height = height;
  ctx.font = '40px sans-serif';
  ctx.textAlign = "center";
 
  drawGameStartText(ctx, width/2, height/2);

  document.addEventListener("keyup", function(e) {
    if(e.code === "Space" && !(gameOn)){
      startGame(ctx, width, height, shapes);
    } else if(e.key === expectedKey && gameOn){
      score += 1;
      update(ctx, score, shapes);
    } else if(gameOn){
      score -= 1;
      update(ctx, score, shapes);
    }
  });
});