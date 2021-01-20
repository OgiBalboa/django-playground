var params =  [ ["reach",[0.475]], ["payload",[]]]
// params =[ [id, [values] ]
function FindBestRobot (parameters) {
$.ajax({
  url: 'findrobot/',
  type: 'GET',
  data: {'parameters': parameters },
  processData: false,
  contentType: false,
  success: function( data )
        {
            $( '#message' ).text(data);
        }
 })
}