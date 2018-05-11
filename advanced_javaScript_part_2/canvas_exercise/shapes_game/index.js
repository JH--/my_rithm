window.addEventListener("load", function() {

  function clear(ctx, width, height) {
    ctx.clearRect(0, 0, width, height);
  }

  function drawRandomShape(ctx, width, height) {
    
  }

  function drawGameStartText(ctx, width, height) {
    ctx.fillText("Press the space bar to start a new game", width, height);
  }

  function restartGame(ctx, width, height) {
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
      seconds = 3,
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
      startGame(ctx);
    } else if(e.key === expectedKey){
      score += 1;
    } else{
      score -= 1;
    }
    scoreSpan.textContent = score;
    clear(ctx, canvas.width, canvas.height);
    drawRandomShape(ctx, canvas.width, canvas.height);
  });
});



/*
window.addEventListener("load", function() {

  function clear(ctx, width, heigt) {
  }

  function drawRandomShape(ctx, width, height) {
  }

  function drawGameStartText(ctx, width, height, score) {
  }

  function restartGame(ctx, width, height) {
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
      seconds = 3,
      intervalId;

  canvas.width = width;
  canvas.height = height;

  document.addEventListener("keyup", function() {
 
  });
});
*/

