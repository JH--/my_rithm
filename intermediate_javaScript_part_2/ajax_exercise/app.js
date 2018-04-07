$(document).ready(() => {
  $("form").on("submit", event => {
    event.preventDefault();
    const query = ($("#query").val() ? $("#query").val() : false);
    if(!query){return;}
    const giphyAPI = `http://api.giphy.com/v1/gifs/search?q=${query}&api_key=dc6zaTOxFJmzC`;
    $.getJSON(giphyAPI).done(response => {
      const gif = response.data[Math.floor(Math.random() * response.data.length)].images.downsized.url;
      const $gif = $("<div>", {class:"col-auto my-1"}).append($("<img>", {src:gif}));
      $("#gifCity").append($gif);
    })
    .always( () => $("#query").val(''));
  })

  $("#delete").on("click", e => $("#gifCity").empty());
})

