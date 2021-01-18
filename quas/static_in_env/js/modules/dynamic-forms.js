
// ARRAYS:
var ROBOT_APPLICATIONS = ["Arc Welding", "Cleaning", "Coating", "Collaboration", "Cutting", "Deburring", "Depalletizing", "Die Casting", "Dispensing", "Enamelling", "Full Layer Palletizing", "Glazing", "Gluing", "Grinding", "Heavy Arc Welding", "Injection Moulding", "Item Picking", "Loading", "Loading and Unloading"," Machine Tending", "Machine Handling", "Measuring", "Packing", "Painting", "Palletizing", "Part Inspection", "Picking", "Polishing", "Powdering", "Powertrain Assembly", "Pre-Machining", "Press Automation", "Press Brake Tending", "Press Tending", "Rubber Insertion", "Screw Driving", "Sealing", "Small Parts Assembly", "Spot Welding", "Spraying", "Testing", "Unloading", ]
var FIND_ROBOT_PARAMETER = {
    "reach":["float",["reach","Specify Reach","m"]],
    "payload":["float",["payload","Specify Payload","kg"]],
    "application":["multi-select",["application","Choose Application Type",ROBOT_APPLICATIONS]],
    "performance_rating":["int",["performance_rating","Specify Performance Rating Range"]],
    "customer_rating":["int",["customer_rating","Specify Customer Rating Range"]],
    "axis_number":["multi-select",["axis_number","Specify Axis Number"]],
    "brand":["text",["brand","Specify Brand Name"]],
    "repeatability":["float",["repeatability","Specify Repeatability","mm"]],
    "picking_cycle":["float",["picking_cycle","Specify Picking Cycle","s"]],
    "mounting":["multi-select",["mounting","Specify Mounting Type"]],
    "weight":["int",["weight","Specify Weight","kg"]],
    "speed":["float",["speed","Specify Speed","m/s"]],
}

//----------------------TEMPLATES--------------------
class FloatField {
    constructor(id,text,unit) {
    this.html = document.createElement("div");
    this.html.id = id
    this.html.className = "input-group mb-3";
    if (unit != false){
    this.html.innerHTML = `
        <div class="input-group-prepend">
            <span class="input-group-text">${text}</span>
        </div>
        <input type="text" id=${id} name=${id} class="form-control">
        <div class="input-group-prepend">
            <span class="input-group-text">${unit}</span>
        </div>

    `
    }
    else {
    this.html.innerHTML =`

    `
    }
    //TODO: id ler iki kez tanımlanıyor. hem input ta hem de div de.
    this.html.innerHTML += `
        <div class="input-group-prepend">
        <button type="button" style='color: red;' onclick="remove_field('${this.html.id}')">
            <i class="fas fa-trash float-center"></i>
        </button>
        </div>
    `
    }
}
class IntField {
    constructor(id,text,unit) {
    this.html = "ana"
    }
    }

class TextField {
    constructor(id,text,unit) {

    }
    }
class MultiSelectField {
    constructor(id,text,choices) {
    this.html = document.createElement("select");
    this.html.id = id;
    //this.html.setAttribute("multiple","");
    this.html.className = "mdb-select md-form";
    for (var i = 0; i <choices.length;i++){
    var option = document.createElement("option");
    option.textContent = choices[i][1];
    option.value = choices[i][0];
    this.html.appendChild(option);
    }
    }
    }
class SingleSelectField {
    constructor(id, text, choices){
    this.html = document.createElement("select");
    this.html.id = id;
    this.html.className ="browser-default custom-select mb-3";
    this.html.addEventListener("change", add_field);
    var default_option = document.createElement("option");
    default_option.textContent =text;
    default_option.value = "default";
    this.html.appendChild(default_option);
    for (var i = 0; i <choices.length;i++){
        var option = document.createElement("option");
        option.textContent = choices[i][1];
        option.value = choices[i][0];
        this.html.appendChild(option);
    }
    }
}
//------------------FUNCTIONS----------------
var field_select = "";
function field_selector() {
    values = Object.values(FIND_ROBOT_PARAMETER);
    var choices = [];
    for (var i = 0; i < values.length; i++) {
        choices.push(values[i][1]);
    }
    field_select = new SingleSelectField("select_field","Choose a search parameter",choices).html
    document.getElementById("findrobot_form").appendChild(field_select)
}
function add_field(event) {
//TODO:add error handling here

    var selectElement = event.target;
    var value = selectElement.value;
    var params = FIND_ROBOT_PARAMETER[value];
    field_select.selectedIndex = 0;
    switch (params[0]) {
    case "int":
        field = new FloatField(...params[1]);
        break;
    case "float":
        field = new FloatField(...params[1]);
        break;
    case "text":
        field = new TextField(...params[1]);
        break;
    case "single-select":
        field = new SingleSelectField(...params[1]);
        break;
    case "multi-select":
        field = new MultiSelectField(...params[1]);
        break;
    }
    document.getElementById("findrobot_form").appendChild(field.html);
}
function remove_field(x){
document.getElementById("findrobot_form").removeChild(document.getElementById(x));
}
const a = "vaay";
function create__form() {
document.getElementById("findorobot_form").innerHTML =`
        <!-- Form -->
        <form class="text-center" style="color: #757575;" method="POST">
            <select class="browser-default custom-select mb-3">
              <option selected>Choose Application Type</option>
                 <option value="aa">${a}</option>
            </select>
            <!-- Name -->
            <div class="input-group mb-3" >
                  <div class="input-group-prepend">
                    <span class="input-group-text">Specify Payload</span>
                  </div>
                <input type="text" id="payload" name=payload class="form-control">
                <div class="input-group-prepend">
                    <span class="input-group-text">kg</span>
                </div>
            </div>
            <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Specify Reach</span>
                  </div>
                <input type="text" id="reach" name="reach" class="form-control">
                <div class="input-group-prepend">
                    <span class="input-group-text">m</span>
                </div>
            </div>

            <!-- Sign in button -->
            <button class="btn btn-info btn-block my-4waves-effect" type="submit">Find BestRobot!</button>

        </form>
        <!-- Form -->
`
}