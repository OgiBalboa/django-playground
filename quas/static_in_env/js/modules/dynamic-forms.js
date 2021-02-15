// ARRAYS:
/*var js_script = document.createElement('script');
js_script.type = 'text/html';
js_script.src = "js/jquery-3.4.1.min.js";
var multiple_script = document.createElement('script');
multiple_script.type = 'text/html';
multiple_script.src = "multiple-select.min.js"
*/
/*
TODO:
1. Multi Select düzenle
2. Min Max değer girdileri
3. Marka isimleri multiselect yapılacak.
4. Robot kartları düzenlenecek.

*/
//---------------GLOBAL PARAMETERS---------------------------------
var MAIN = document.getElementsByTagName("main")[0];
var FIELD_SELECT = "";
var FIELDS = {};
var FORM_div = document.getElementById("findrobot_form_div");
var FORM = document.getElementById("findrobot_form");
var SUBMIT = document.createElement("button");
SUBMIT.className = "btn btn-info btn-block unique-color my-4waves-effect active mb-4";
SUBMIT.textContent = "Find BestRobot!";
SUBMIT.addEventListener("click",FindBestRobot);
SUBMIT.type = "button";
SUBMIT.setAttribute("autofocus","autofocus");
//TODO: parametreleri şu formatta düzenle: [id, [["text1,unit1], [text2,unit2]] ] böylece sınırsız text field açarsın.

class ShowRobots{
    constructor() {

        this.exist = false;
        this.header = document.createElement('h1');
        this.header.align = 'center';
        this.header.textContent = "Best Robot is One of these:";

        this.container = document.createElement('div');
        this.container.className = "container";

        this.section = document.createElement('section');
        this.section.className = "text-center mt-4 mb-4";

        this.row = document.createElement('div');
        this.row.className = "row wow fadeIn";

        this.container.appendChild(this.section);
        this.section.appendChild(this.row);

    }
    initialize() {
        this.exist = true;
        MAIN.appendChild(this.header);
        MAIN.appendChild(this.container);
    }
    show(data) {
        if (this.exist != true) this.initialize();
        if (data == "ROBOT DOES NOT EXIST"){
            //this.row.innerHTML = "<div class='container'><h4 align='center'>Unfortunately, could not find matching robot...</h4></div>";
            this.header.textContent = "Unfortunately, could not find matching robot...";
        }
        else{
            this.row.innerHTML = ``;
            for (var robot of data) {
                var card = new RobotCard(robot,this.row);
            }
        }
    }
}
//----------------------FIELDS--------------------
class StringField {
    constructor(id,text,unit,hint="single") {
        this.div = document.createElement("div");
        this.id = id //TODO:(LATER)WHAT IF THERE ARE MORE THAN ONE OF SAME FIELDS?
        var id = id; //TODO:(learn) this değişkenleri alt fonksiyonlarda kullanılamıyor. bu sebeple var ile değişken atadık. Alternatif çözümü var mı?
        this.div.id = id;
        this.hint = hint;
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
        return [this.input.value];
    }
}
class MultiSelectField {
    constructor(id,text,choices,values = choices,hint = "multi",) {
        this.selected = [];
        this.on_selected = this.on_selected.bind(this);
        //-------------MAIN DIV-------------
        this.div = document.createElement("div");
        this.div.className = "card mt-3 mb-3";
        this.id = id;
        var id = id;
        this.hint = hint;
        //-------------SELECT -------------
        this.selected_values = document.createElement("p");
        this.selected_values.style = "color:black";
        this.selected_values.innerHTML = "Choose Application Type";
        this.div.appendChild(this.selected_values);

        this.select = document.createElement("select");
        this.select.id = id;
        this.select.setAttribute("multiple","multiple");
        this.select.setAttribute("searchable","Search");
        this.select.className = "form-select";
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
         if (this.selected.length >0) {
            var selected_names = ""
            for (var i=0; i<this.selected.length; i++) {
                selected_names += this.selected[i] + ", ";
            }
        }
        else {
            selected_names = "Choose Application Type";
            }
        this.change_option_name(selectElement, "default", selected_names);
        this.selected_values.innerHTML = selected_names;
    }
    //-----------CHANGE OPTION NAME FUNCTION-----------
    change_option_name(select,val,name){
        for (var i=0; i<select.length; i++) {
        if (select.options[i].value == val){
            select.options[i].innerHTML = name;
            // (selected ekler veya normale çevirir)
            select.options[i].selected = false;
            }
        }
    }
}
class SingleSelectField {
    constructor(id, text, choices, values = choices, hint = "single"){
        this.div = document.createElement("div");
        this.select = document.createElement("select");
        this.id = id;
        this.id = id;
        this.hint = hint;
        this.select.className ="browser-default custom-select mb-3 text-center";
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
    get_value() {

    }
}
//------------------FUNCTIONS----------------
function add_field(event) {
//TODO:add error handling here also parameters can be a class
    var selectElement = event.target;
    var value = selectElement.value;
    var params = FIND_ROBOT_PARAMETER[value];
    FIELD_SELECT.select.selectedIndex = 0; // RESET SELECTOR
    // DON'T DUPLICATE FIELDS
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
    let data = {};
    for (let key in FIELDS) {
        data[key] = [FIELDS[key].hint,FIELDS[key].get_value()];
    }
    return data;
}
show_robots = new ShowRobots();
function FindBestRobot () {
    $.ajax({
      url: '/findrobot',
      type: 'GET',
      data: {'parameters': JSON.stringify(pull_form()),
              'query': true,},

      success: function( data )
            {
               //console.log(data);
               show_robots.show(data);
            }
            })
    }
// MAIN FUNCTION -- SCRIPT STARTS HERE --
function field_selector() {
    parameters = Object.values(FIND_ROBOT_PARAMETER);
    var choices = [];
    var values = [];
    for (var i = 0; i < parameters.length; i++) {
        choices.push(parameters[i][1][1]);
        values.push(parameters[i][1][0]);
    }
    FIELD_SELECT = new SingleSelectField("select_field","Choose a search parameter",choices,values);
    FIELD_SELECT.select.addEventListener("change", add_field);
    FORM_div.appendChild(FIELD_SELECT.div);
    FORM.appendChild(SUBMIT);
}