
// ARRAYS:
var ROBOT_APPLICATIONS = ["Arc Welding", "Cleaning", "Coating", "Collaboration", "Cutting", "Deburring", "Depalletizing", "Die Casting", "Dispensing", "Enamelling", "Full Layer Palletizing", "Glazing", "Gluing", "Grinding", "Heavy Arc Welding", "Injection Moulding", "Item Picking", "Loading", "Loading and Unloading"," Machine Tending", "Machine Handling", "Measuring", "Packing", "Painting", "Palletizing", "Part Inspection", "Picking", "Polishing", "Powdering", "Powertrain Assembly", "Pre-Machining", "Press Automation", "Press Brake Tending", "Press Tending", "Rubber Insertion", "Screw Driving", "Sealing", "Small Parts Assembly", "Spot Welding", "Spraying", "Testing", "Unloading", ]
var FIND_ROBOT_PARAMETER = {
    "reach":["float",["reach","Specify Reach","m"]],
    "payload":["float",["payload","Specify Payload","kg"]],
    "application":["multi-select",["application","Choose Application Type",ROBOT_APPLICATIONS]],
    "performance_rating":["int",["performance_rating","Specify Performance Rating Range"]],
    "customer_rating":["int",["customer_rating","Specify Customer Rating Range"]],
    "axis_number":["multi-select",["axis_number","Specify Axis Number"]],
    "brand":["text",["brand","Specify Brand Name",false]],
    "repeatability":["float",["repeatability","Specify Repeatability","mm"]],
    "picking_cycle":["float",["picking_cycle","Specify Picking Cycle","s"]],
    "mounting":["multi-select",["mounting","Specify Mounting Type"]],
    "weight":["int",["weight","Specify Weight","kg"]],
    "speed":["float",["speed","Specify Speed","m/s"]],
}

//----------------------TEMPLATES--------------------
class FloatField {
    constructor(id,text,unit) {
    this.div = document.createElement("div");
    this.div.id = id
    this.div.className = "input-group mb-3";
    if (unit != false){
    this.div.innerHTML = `
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
    this.div.innerHTML = `
        <div class="input-group-prepend">
            <span class="input-group-text">${text}</span>
        </div>
        <input type="text" id=${id} name=${id} class="form-control">
         `
    }
    //TODO: id ler iki kez tanımlanıyor. hem input ta hem de div de.
    this.div.innerHTML += `
        <div class="input-group-prepend">
        <button type="button" style='color: red;' onclick="remove_field('${this.div.id}')">
            <i class="fas fa-trash float-center"></i>
        </button>
        </div>
    `
    }
}
class MultiSelectField {
    constructor(id,text,choices) {
    this.div = document.createElement("div");
    this.select = document.createElement("select");
    this.select.id = id;
    this.select.setAttribute("multiple","");
    this.select.className = "mdb-select md-form";
    for (var i = 0; i <choices.length;i++){
        var option = document.createElement("option");
        option.textContent = choices[i];
        option.value = choices[i];
        this.select.appendChild(option);
    }
    this.div.appendChild(this.select);
    }
    }
class SingleSelectField {
    constructor(id, text, choices, values = choices){
    this.div = document.createElement("div");
    this.select = document.createElement("select");
    this.select.id = id;
    this.select.className ="browser-default custom-select mb-3";
    this.select.addEventListener("change", add_field);
    var default_option = document.createElement("option");
    default_option.textContent =text;
    default_option.value = "default";
    this.select.appendChild(default_option);
    for (var i = 0; i <choices.length;i++){
        var option = document.createElement("option");
        option.textContent = choices[i];
        option.value = values[i];
        this.select.appendChild(option);
    }
    this.div.appendChild(this.select);
    }
}
//------------------FUNCTIONS----------------
var field_select = "";
function field_selector() {
    parameters = Object.values(FIND_ROBOT_PARAMETER);
    var choices = [];
    var values = [];
    for (var i = 0; i < parameters.length; i++) {
        choices.push(parameters[i][1][1]);
        values.push(parameters[i][1][0]);
    }
    field_select = new SingleSelectField("select_field","Choose a search parameter",choices,values).div;
    document.getElementById("findrobot_form").appendChild(field_select);
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
        field = new FloatField(...params[1]);
        break;
    case "single-select":
        field = new SingleSelectField(...params[1]);
        break;
    case "multi-select":
        field = new MultiSelectField(...params[1]);
        break;
    }
    document.getElementById("findrobot_form").appendChild(field.div);
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