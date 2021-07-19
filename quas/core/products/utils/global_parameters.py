CATEGORY_CHOICES = (
    ('IR', 'Industrial Robots'),
    ('RGV', 'RGV Robots'),
    ('CO', 'Cobots'),
    ('WM', 'Welding Machines'),
)
PRODUCT_TYPES = (
    ('IR', 'Industrial Robots'),
    ('RGV', 'RGV Robots'),
    ('CO', 'Cobots'),
    ('WM', 'Welding Machines'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('A', 'success'),
    ('W', 'warning'),
)

UNIT_TYPES = (
    ('kg', 'kilogrammes'),
    ('g', 'grammes'),
    ('m', 'meters'),
    ('mm', 'millimeters'),
    ('s', 'seconds'),
    ('ms', 'milliseconds'),
    ('q', 'quantity'),
    ('kV', 'kilo-voltage'),
    ('kVA', 'kilo-volt-amper'),
    ('kW', 'kilowatts'),
    ('V', 'voltage'),
    ('C', 'Celsius'),
    ('dB', 'decibels'),
    ('null', 'null'),
)
DATA_TYPES = (
    ('int', 'Integer'),
    ('dec', 'Decimal'),
    ('str', 'String'),
    ('list', 'List'),
    ('dict', 'Dict'),
)
IMAGE_TYPES = (
    ('default', 'Default'),
    ('working_range', 'Working Range'),
)
ROBOT_APPLICATIONS = (
    ('AS', 'Assembly'),
    ('AW', 'Arc Welding'),
    ('CL', 'Cleaning'),
    ('CO', 'Coating'),
    ('CB', 'Collaboration'),
    ('CU', 'Cutting'),
    ('DB', 'Deburring'),
    ('DP', 'Depalletizing'),
    ('DC', 'Die Casting'),
    ('DI', 'Dispensing'),
    ('EN', 'Enamelling'),
    ('FP', 'Full Layer Palletizing'),
    ('GZ', 'Glazing'),
    ('GU', 'Gluing'),
    ('GR', 'Grinding'),
    ('HW', 'Heavy Arc Welding'),
    ('IM', 'Injection Moulding'),
    ('IP', 'Item Picking'),
    ('LO', 'Loading'),
    ('LU', 'Loading and Unloading'),
    ('MT', 'Machine Tending'),
    ('MH', 'Machine Handling'),
    ('ME', 'Measuring'),
    ('PC', 'Packing'),
    ('PA', 'Painting'),
    ('PT', 'Palletizing'),
    ('PI', 'Part Inspection'),
    ('PK', 'Picking'),
    ('PO', 'Polishing'),
    ('PW', 'Powdering'),
    ('PS', 'Powertrain Assembly'),
    ('PM', 'Pre-Machining'),
    ('PU', 'Press Automation'),
    ('PB', 'Press Brake Tending'),
    ('PE', 'Press Tending'),
    ('RI', 'Rubber Insertion'),
    ('SD', 'Screw Driving'),
    ('SE', 'Sealing'),
    ('SA', 'Small Parts Assembly'),
    ('SW', 'Spot Welding'),
    ('SP', 'Spraying'),
    ('TE', 'Testing'),
    ('UL', 'Unloading'),
)
PRIMARY_FEATURES = (
    ('SP', 'Speed'),
    ('MO', 'Moment'),
    ('PL', 'Payload'),

)
AXIS_NUMBER = (
    ('1', 'J1'),
    ('2', 'J2'),
    ('3', 'J3'),
    ('4', 'J4'),
    ('5', 'J5'),
    ('6', 'J6'),
    ('7', 'J7'),
)
AXIS_MOVEMENT = (
    ('R', 'Rotation'),
    ('A', 'Arm'),
    ('W', 'Wrist'),
    ('B', 'Bend'),
    ('T', 'Turn'),
)

MOUNTING = (
    ('A', 'Any'),
    ('F', 'Floor'),
    ('W', 'Wall'),
    ('T', 'Tilted'),
    ('I', 'Invert Mount'),
)

DATASHEET = ["number_of_axes", "payload", "reach", "repeatability", "mounting",
             "axis1_speed", "axis1_movement", "axis2_speed", "axis2_movement",
             "axis3_speed", "axis3_movement",
             "axis4_speed", "axis4_movement", "axis5_speed", "axis5_movement",
             "axis6_speed", "axis6_movement"]
ATTRIBUTE_GROUPS = {
    "Information": ["brand", "title", "description", "performance_rating",
                    "customer_rating", "number_of_axes"],
    "Application": ["mounting", "application"],
    "Psychical": ["payload", "reach", "repeatability", "weight",
                  "picking_cycle"],
    "Axis": ["axis"]
}
parameter_groups = [MOUNTING, AXIS_MOVEMENT, PRIMARY_FEATURES,
                    ROBOT_APPLICATIONS, CATEGORY_CHOICES, LABEL_CHOICES]


def match_parameter_with_short_name(parameter_name):
    for parameter_group in parameter_groups:
        for parameter in parameter_group:
            if parameter_name == parameter[1]:
                print(parameter[0])
                return parameter[0]
    return "NO MATCH"


if __name__ == "__main__":
    import json

    d = {"applications": []}
    for p in ROBOT_APPLICATIONS:
        d['applications'].append({
            "name": p[1],
            "slug": p[1].lower().replace(" ", "_")
        })
    json.dump(d, open("applications.json", "w"))
