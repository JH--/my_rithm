window.addEventListener("load", function() {

  function clear(ctx, width, height) {
    ctx.clearRect(0, 0, width, height);
  }

  function drawRandomShape(ctx, width, height) {

  }

  function drawGameStartText(ctx, width, height) {
    ctx.fillText("Press the space bar to start a new game", width, height);
  }

  function endGame(ctx, width, height) {
    ctx.clearRect(0, 0, width, height);
    ctx.fillText(`Game over! You scored ${score} point${(() => Math.abs(score) !== 1 ? 's' : '')()}`, width/2, height/2);
    setTimeout(drawGameStartText, 3000, ctx, width/2, height-(height/10));
    gameOn = false;
  }

  function startGame(ctx, width, height){
    clear(ctx, width, height);
    [score, seconds] = [0, 3];
    [scoreSpan.textContent, timerSpan.textContent] = [0, 30];
    gameOn = true;
    drawRandomShape(ctx, width, height);
    //set interval for 1 second updates to time until 0 then game over
    let timer = setInterval(() => {
      seconds -= 1;
      timerSpan.textContent = seconds;
      if(seconds === 0){
        clearInterval(timer);
        endGame(ctx, width, height);
      }
    }, 1000);

  }

  var canvas = document.getElementById("shapes-game"),
      height = canvas.scrollHeight,
      width = canvas.scrollWidth,
      gameOn = false,
      expectedKey = undefined,
      ctx = canvas.getContext('2d'),
      // white triangle = up, red square = down,
      // red triangle = left, white square = right
      expectedKeysMap = {white0: 38, red1: 40, red0: 37, white1: 39},
      timerSpan = document.getElementById("time-remaining"),
      scoreSpan = document.getElementById("score-val"),
      seconds = 30,
      score = 0,
      intervalId;

  canvas.width = width;
  canvas.height = height;
  ctx.font = '40px sans-serif';
  ctx.textAlign = "center";
  ctx.fillStyle = "white";
 
  drawGameStartText(ctx, canvas.width/2, canvas.height/2);

  document.addEventListener("keyup", function(e) {
    if(e.code === "Space" && !(gameOn)){
      startGame(ctx, canvas.width, canvas.height);
    } else if(e.key === expectedKey && gameOn){
      score += 1;
    } else if(gameOn){
      score -= 1;
    }
    scoreSpan.textContent = score;
    clear(ctx, canvas.width, canvas.height);
    drawRandomShape(ctx, canvas.width, canvas.height);
  });
});
