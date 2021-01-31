var ROBOT_APPLICATIONS = ["Assembly", "Arc Welding", "Cleaning", "Coating", "Collaboration", "Cutting", "Deburring", "Depalletizing", "Die Casting", "Dispensing", "Enamelling", "Full Layer Palletizing", "Glazing", "Gluing", "Grinding", "Heavy Arc Welding", "Injection Moulding", "Item Picking", "Loading", "Loading and Unloading"," Machine Tending", "Machine Handling", "Measuring", "Packing", "Painting", "Palletizing", "Part Inspection", "Picking", "Polishing", "Powdering", "Powertrain Assembly", "Pre-Machining", "Press Automation", "Press Brake Tending", "Press Tending", "Rubber Insertion", "Screw Driving", "Sealing", "Small Parts Assembly", "Spot Welding", "Spraying", "Testing", "Unloading", ]
var AXIS_NUMBER = [1,2,3,4,5,6];
var MOUNTING_TYPES = ["Any", "Floor", "Wall", "Tilted", "Invert Mount",];
var BRAND_NAMES = ["ABB","NACHI"];
var FIND_ROBOT_PARAMETER = {
    "reach":["float",["reach","Specify Reach","m","gte"]],
    "payload":["float",["payload","Specify Payload","kg","gte"]],
    "application":["multi-select",["application","Choose Application Type",ROBOT_APPLICATIONS]],
    "performance_rating":["text",["performance_rating","Specify Performance Rating Range",false,"gte"]],
    "customer_rating":["text",["customer_rating","Specify Customer Rating Range",false,"gte"]],
    "axis_number":["multi-select",["axis_number","Specify Axis Number",AXIS_NUMBER]],
    "brand":["text",["brand","Specify Brand Name",false,"brand"]],
    "repeatability":["float",["repeatability","Specify Repeatability","mm","gte"]],
    "picking_cycle":["float",["picking_cycle","Specify Picking Cycle","s","gte"]],
    "mounting":["multi-select",["mounting","Specify Mounting Type",MOUNTING_TYPES]],
    "weight":["int",["weight","Specify Weight","kg","gte"]],
    "speed":["float",["speed","Specify Speed","m/s","gte"]],
}

class RobotCard {
    constructor (data,row) {
        //var robot = JSON.parse(data);
        var robot = data;
        this.robot = robot;
        this.col = document.createElement("div");

        this.col.className = "col-lg-3 col-md-6 mb-4 animated fadeInLeft";
        this.col.innerHTML = `
            <div class="card">
                <div class="row">
                    <div class="col-lg-1 mr-2"><span class="badge green"><h4>${robot.performance_rating}</h4></span></div>
                    <div class="col">

                    <img class="card-img-top" src="${robot.image_url}" alt="Card image cap">
                    </div>
                </div>
                <div class="card-body" style="border-top-width: 2px;border-top-style: solid;">
                    <h5>
                      <strong>
                        <a href="${robot.absolute_url}" class="dark-grey-text"><span style="color:darkblue;">${robot.brand_name}</span> ${robot.title}
                         <br />
                          <span class="badge badge-pill success-color">Best Match!</span>
                        </a>
                      </strong>
                    </h5>
                <p class="card-text">Şimdilik Dursun</p>
                <a href="#" class="btn btn-primary">Details</a>
                </div>
            </div>
        `
    row.appendChild(this.col);
    }
    get_absolute_url (){

    }

}
function FindRobot (query,handler) {
    //query = { key: [ hint, [values] ] }
    $.ajax({
      url: '/findrobot',
      type: 'GET',
      data: {'parameters': JSON.stringify(query),
              'query': true,},

      success: function( data )
            {
                /* How to use data :
                for (var robot of data) {
                    var card = new RobotCard(robot,card_div);
                }
                */
               //console.log(data);
              handler(data);
            }
            })
}