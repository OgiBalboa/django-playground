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
"""
with open("js_dict.txt","w") as file:
    out = "let ROBOT_APPLICATIONS = ["
    for item in ROBOT_APPLICATIONS:
        out+= item[1] +", "
    out+="]"
    print(out)
    file.write(out)
"""