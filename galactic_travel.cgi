#!/usr/bin/python
import cgi
import math

print("Content-type: text/html\n\n")

#Dennis Stephens

#Global lists for possible units of measurement
distance_units = ["parsec", "lightyear", "kilometer", "xlarn"]
angle_units = ["radian", "degree", "xarnian"]

def main():

    form = cgi.FieldStorage()

    # Creates a dictionary for the input from the user
    input_dict = {
            "distx": 1,
            "unitx": "parsec",
            "disty": 1,
            "unity": "parsec",
            "anglea": 1, 
            "unita": "degree",
            "unitanswer": "parsec", 
        }

    # If the form has all components we will continue with the program.
    # Otherwise it presents an error message
    if (validate_form(form)):

        # Inserts the users values in the input dictionary after validating the data
        (input_dict["distx"], input_dict["unitx"],\
                input_dict["disty"], input_dict["unity"],\
                input_dict["anglea"], input_dict["unita"],\
                input_dict["unitanswer"]) = validate_input(form)
        
        # Output
        print("Origin (Distance from Earth): %0.3f %s<br>" %(input_dict["distx"],input_dict["unitx"]))
        print("Destination (Distance from Earth): %0.3f %s<br>" %(input_dict["disty"], input_dict["unity"]))
        print("Angle (between above vectors): %0.3f %s<br>" %(input_dict["anglea"], input_dict["unita"]))

        # Converts all the units to a standard for calculation
        input_dict["distx"] = convert(input_dict["distx"],input_dict["unitx"], "lightyear")
        input_dict["disty"] = convert(input_dict["disty"],input_dict["unity"], "lightyear")
        input_dict["anglea"] = convert(input_dict["anglea"],input_dict["unita"], "radian")

        # Computes the distance using the law of cosines
        final_distance = compute(input_dict["distx"], input_dict["disty"], input_dict["anglea"])
        
        # Converts to the distance the user wanted
        final_distance = convert(final_distance, "lightyear", input_dict["unitanswer"])

        print("Distance between the two planets is %.3f %s" % (final_distance,input_dict["unitanswer"]))
    
    else :
    
        print("Sorry, we did not get all of the information. Input is required in all fields!")

def validate_form(form):
    
    form_ok = 0

    # If the form has all keys returns true
    if form.has_key("distx") and form.has_key("unitx") \
        and form.has_key("disty") and form.has_key("unity") \
        and form.has_key("anglea") and form.has_key("unita") \
        and form.has_key("unitanswer"):
            form_ok = 1

    return (form_ok)

def validate_input(form):

    # If the user inputs a string of characters rejects the input and 
    # gives a default value
    try:
        distx = float(form["distx"].value)
    except ValueError:
        print("The first distance was not a number.<br>")
        distx = 1

    try:
        disty = float(form["disty"].value)
    except ValueError:
        print("The second distance was not a number.<br>")
        disty = 1

    try:
        anglea = float(form["anglea"].value)
    except ValueError:
        print("The angle input was not a number.<br>")
        anglea = 1


    # If the form somehow got an input other than what was provided
    # tells the user and gives a default value
    if (form["unitx"].value) in distance_units:
        unitx = form["unitx"].value
    else:
        print("Unit selected for first distance is invalid!<br>")
        unitx = "parsec"

    if (form["unity"].value) in distance_units:
        unity = form["unity"].value
    else:
        print("Unit selected for second distance is invalid!<br>")
        unity = "parsec"
    
    if (form["unita"].value) in angle_units:
        unita = form["unita"].value
    else:
        print("Unit selected for the angle is invalid!<br>")
        unita = "radian"
    
    if (form["unitanswer"].value) in distance_units:
        unitanswer = form["unitanswer"].value
    else:
        print("Unit selected for the answer is invalid!<br>")
        unitanswer = "parsec"
    
    return (distx, unitx, disty, unity, anglea, unita, unitanswer)



def convert(number_to_convert, original_unit, converted_unit):

    conversion_factor = 1.0

    if original_unit in distance_units:

        if original_unit == "parsec":

            if converted_unit == "lightyear":

                conversion_factor = 3.26

            elif converted_unit == "xlarn":

                conversion_factor = (1/6.3762)

            elif converted_unit == "kilometer":

                conversion_factor = (3.26*(9.461*(10**12)))

            else:

                conversion_factor = 1

        elif original_unit == "lightyear":

            if converted_unit == "parsec":

                conversion_factor = (1/3.26)

            elif converted_unit == "xlarn":

                conversion_factor = (6.3762*3.26)

            elif converted_unit == "kilometer":

                conversion_factor = (9.461*(10**12))
            
            else:

                conversion_factor = 1

        elif original_unit == "xlarn":

            if converted_unit == "parsec":

                conversion_factor = 6.3762

            elif converted_unit == "lightyear":

                conversion_factor = (6.3762*3.26)

            elif converted_unit == "kilometer":

                conversion_factor = (6.3762*3.26*(9.461*(10**12)))

            else:

                conversion_factor = 1

        else:

            if converted_unit == "parsec":

                conversion_factor = ((1/(9.461(10**12)))*(1/3.26))

            elif converted_unit == "lightyear":

                conversion_factor = 1/(9.461(10**12))

            elif converted_unit == "xlarn":

                conversion_factor = ((1/(9.461*(10**12)))*(1/3.26)*(1/6.3762))

            else:

                conversion_factor = 1

    else:

        if original_unit == "degree":

            if converted_unit == "radian":

                conversion_factor = 0.0174533

            elif converted_unit == "xarnian":

                conversion_factor = (1/0.572958)

            else:

                conversion_factor = 1

        elif original_unit == "radian":

            if converted_unit == "degree":

                conversion_factor = (1/0.0174533)

            elif converted_unit == "xarnian":

                conversion_factor = 100

            else:

                conversion_factor = 1

        else:

            if converted_unit == "degree":

                conversion_factor = .572958

            elif converted_unit == "radian":

                conversion_factor = 1/100

            else:

                conversion_factor = 1
    
    
    # Converts the number with a simple equation.
    converted_number = number_to_convert * conversion_factor

    return converted_number

def compute(distance1, distance2, angle):

    # Uses the equation for the law of cosines and returns the value
    final_distance = ((distance1**2) + (distance2**2) - (2*distance1*distance2) * (math.cos(angle)))
    
    final_distance = math.sqrt(final_distance)

    return final_distance
    
main()
