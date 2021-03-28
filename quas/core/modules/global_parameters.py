CATEGORY_CHOICES = (
    ('IR', 'Industrial Robots'),
    ('RGV', 'RGV Robots'),
    ('CO', 'Cobots')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('A', 'success'),
    ('W', 'warning'),
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
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

DATASHEET = ["number_of_axes", "payload", "reach", "repeatability", "picking_cycle", "mounting",
             "weight", "axis1_speed", "axis1_movement", "axis2_speed", "axis2_movement", "axis3_speed", "axis3_movement",
             "axis4_speed", "axis4_movement", "axis5_speed", "axis5_movement", "axis6_speed", "axis6_movement"]
parameter_groups = [MOUNTING,AXIS_MOVEMENT,PRIMARY_FEATURES, ROBOT_APPLICATIONS, CATEGORY_CHOICES, LABEL_CHOICES]

def match_parameter_with_short_name(parameter_name):
    for parameter_group in parameter_groups:
        for parameter in parameter_group:
            if parameter_name == parameter[1]:
                print(parameter[0])
                return parameter[0]
    return "NO MATCH"