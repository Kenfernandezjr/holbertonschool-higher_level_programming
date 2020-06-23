const chtr = $('DIV#character');
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    chtr.text(data.name);
  }
});
