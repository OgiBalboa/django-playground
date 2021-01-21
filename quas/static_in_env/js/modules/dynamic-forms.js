// ARRAYS:
/*var js_script = document.createElement('script');
js_script.type = 'text/html';
js_script.src = "js/jquery-3.4.1.min.js";
var multiple_script = document.createElement('script');
multiple_script.type = 'text/html';
multiple_script.src = "multiple-select.min.js"
*/
var ROBOT_APPLICATIONS = ["Arc Welding", "Cleaning", "Coating", "Collaboration", "Cutting", "Deburring", "Depalletizing", "Die Casting", "Dispensing", "Enamelling", "Full Layer Palletizing", "Glazing", "Gluing", "Grinding", "Heavy Arc Welding", "Injection Moulding", "Item Picking", "Loading", "Loading and Unloading"," Machine Tending", "Machine Handling", "Measuring", "Packing", "Painting", "Palletizing", "Part Inspection", "Picking", "Polishing", "Powdering", "Powertrain Assembly", "Pre-Machining", "Press Automation", "Press Brake Tending", "Press Tending", "Rubber Insertion", "Screw Driving", "Sealing", "Small Parts Assembly", "Spot Welding", "Spraying", "Testing", "Unloading", ]
var AXIS_NUMBER = [1,2,3,4,5,6];
var MOUNTING_TYPES = ["Any", "Floor", "Wall", "Tilted", "Invert Mount",];
var FIND_ROBOT_PARAMETER = {
    "reach":["float",["reach","Specify Reach","m"]],
    "payload":["float",["payload","Specify Payload","kg"]],
    "application":["multi-select",["application","Choose Application Type",ROBOT_APPLICATIONS]],
    "performance_rating":["int",["performance_rating","Specify Performance Rating Range"]],
    "customer_rating":["int",["customer_rating","Specify Customer Rating Range"]],
    "axis_number":["multi-select",["axis_number","Specify Axis Number",AXIS_NUMBER]],
    "brand":["text",["brand","Specify Brand Name",false]],
    "repeatability":["float",["repeatability","Specify Repeatability","mm"]],
    "picking_cycle":["float",["picking_cycle","Specify Picking Cycle","s"]],
    "mounting":["multi-select",["mounting","Specify Mounting Type",MOUNTING_TYPES]],
    "weight":["int",["weight","Specify Weight","kg"]],
    "speed":["float",["speed","Specify Speed","m/s"]],
}
//TODO: parametreleri şu formatta düzenle: [id, [["text1,unit1], [text2,unit2]] ] böylece sınırsız text field açarsın.
//----------------------FIELDS--------------------
var FIELDS = {};
class StringField {
    constructor(id,text,unit) {
    this.div = document.createElement("div");
    this.id = id //TODO:(LATER)WHAT IF THERE ARE MORE THAN ONE OF SAME FIELDS?
    var id = id; //TODO:(learn) this değişkenleri alt fonksiyonlarda kullanılamıyor. bu sebeple var ile değişken atadık. Alternatif çözümü var mı?
    this.div.className = "input-group mb-3";
    //---------------------------------------
    var inner_div = document.createElement("div");
    inner_div.className = "input-group-prepend";
    var span = document.createElement("span");
    span.className = "input-group-text";
    span.textContent = text;
    inner_div.appendChild(span);
    this.div.appendChild(inner_div);
    //---------------------------------------
    this.input = document.createElement("INPUT");
    this.input.setAttribute("type", "text");
    //this.input.id = id;
    this.input.className = "form-control";
    this.div.appendChild(this.input);
    if (unit != false){
        var unit_div = document.createElement("div");
        var span2 = document.createElement("span");
        span2.className = "input-group-text";
        span2.textContent = unit;
        unit_div.appendChild(span2);
        this.div.appendChild(unit_div);
    }
    this.remove_button = document.createElement("button");
    this.remove_button.setAttribute("style", "color:red;");
    this.remove_button.addEventListener("click",function(){remove_field(id)});
    var img = document.createElement("i");
    img.className = "fas fa-trash float-center";
    this.remove_button.appendChild(img);
    var inner_div2 = document.createElement("div");
    inner_div2.className = "input-group-prepend";
    inner_div2.appendChild(this.remove_button);
    this.div.appendChild(inner_div2);
    }
    get_value(){
    return this.input.value;
    }
}
class MultiSelectField {
    constructor(id,text,choices,values = choices) {
    this.selected = [];
    this.on_selected = this.on_selected.bind(this);
    //-------------MAIN DIV-------------
    this.div = document.createElement("div");
    this.div.className = "col"
    this.id = id;
    var id = id;
    //-------------SELECT -------------
    this.select = document.createElement("select");
    this.select.id = id;
    //this.select.setAttribute("multiple","multiple");
    this.select.setAttribute("searchable","Search");
    this.select.className = "mdb-select multiple-select md-form";
    this.default_option = document.createElement("option");
    this.default_option.setAttribute("disabled","disabled");
    this.default_option.setAttribute("selected","selected");
    this.default_option.style = "color:red"
    this.default_option.value = "default";
    this.default_option.textContent = text;
    this.select.addEventListener("change",this.on_selected);
    this.select.appendChild(this.default_option);
    for (var i = 0; i <choices.length;i++){
        var option = document.createElement("option");
        option.textContent = choices[i];
        option.value = choices[i];
        this.select.appendChild(option);
    }
    this.div.appendChild(this.select);
    //-----------------------------------

    }
    get_value(){
      return this.selected;
    }
    on_selected(event) {
    var selectElement = event.target;
    var value = selectElement.value;
    if (value == "default") return;
    if (this.selected.includes(value)) {
        this.change_option_name(selectElement,value,value);
        this.selected = this.selected.filter(function(opt){if (opt != value){return opt} });
    }
    else {
        this.selected.push(value);
        this.change_option_name(selectElement,value,value+" (selected)");
    }
    selectElement.selectedIndex = 0;
     if (this.selected.length >0) {
    var selected_names = ""
    for (var i=0; i<this.selected.length; i++) {
        selected_names += this.selected[i] + ", ";
    }}
    else selected_names = "Choose Application Type";
    this.change_option_name(selectElement, "default", selected_names);
    }
    //-----------CHANGE OPTION NAME FUNCTION-----------
    change_option_name(select,val,name){
        for (var i=0; i<select.length; i++) {
        if (select.options[i].value == val){
            select.options[i].innerHTML = name;
            }
        }
    }

    }
class SingleSelectField {
    constructor(id, text, choices, values = choices){
    this.div = document.createElement("div");
    this.select = document.createElement("select");
    this.id = id;
    this.id = id;
    this.select.className ="browser-default custom-select mb-3";
    this.select.addEventListener("change", add_field);
    var default_option = document.createElement("option");
    default_option.textContent = text;
    default_option.value = "default";
    default_option.setAttribute("disabled","disabled");
    default_option.setAttribute("selected","selected");
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
var FIELD_SELECT = "";
var FORM_div = document.getElementById("findrobot_form_div");
var FORM = document.getElementById("findrobot_form");
var SUBMIT = document.createElement("button");
SUBMIT.className = "btn btn-info btn-block unique-color my-4waves-effect active mb-4";
SUBMIT.textContent = "Find BestRobot!";
SUBMIT.addEventListener("click",pull_form);
SUBMIT.type = "button";
function field_selector() {
    parameters = Object.values(FIND_ROBOT_PARAMETER);
    var choices = [];
    var values = [];
    for (var i = 0; i < parameters.length; i++) {
        choices.push(parameters[i][1][1]);
        values.push(parameters[i][1][0]);
    }
    FIELD_SELECT = new SingleSelectField("select_field","Choose a search parameter",choices,values);
    FORM_div.appendChild(FIELD_SELECT.div);
    FORM.appendChild(SUBMIT);
}
function add_field(event) {
//TODO:add error handling here also parameters can be a class
    var selectElement = event.target;
    var value = selectElement.value;
    var params = FIND_ROBOT_PARAMETER[value];
    FIELD_SELECT.select.selectedIndex = 0; // RESET SELECTOR
    // DONT DUPLICATE FIELDS
    if (value in FIELDS) return;
    switch (params[0]) {
    case "int":
        field = new StringField(...params[1]);
        break;
    case "float":
        field = new StringField(...params[1]);
        break;
    case "text":
        field = new StringField(...params[1]);
        break;
    case "single-select":
        field = new SingleSelectField(...params[1]);
        break;
    case "multi-select":
        field = new MultiSelectField(...params[1]);
        break;
    }

    FIELDS[field.id] = field;
    FORM_div.appendChild(field.div);
}
function remove_field(x){
pull_form();
FORM_div.removeChild(document.getElementById(x));
delete FIELDS[x];
}
function pull_form() {
console.log(FIELDS["application"].get_value());
}
