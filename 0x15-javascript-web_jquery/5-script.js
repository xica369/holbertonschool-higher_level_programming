// adds a LI element to a list when the user clicks on the tag DIV#add_item

$('DIV#add_item').click(function () {
  $('<li>Item</li>').appendTo('UL.my_list');
});
