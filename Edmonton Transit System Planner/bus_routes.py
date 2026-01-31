# CMPUT 175 - Lab 1: ETS Transit Tracker
#Name: Pratap Kolukuluri
#Student ID: 1849597

#read codes and return as a list of lists, each element is [code, name]
def read_codes(filename):
    codes = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        parts = line.split(",") 
        codes.append([parts[0], parts[1]])
    file.close()
    return codes

#read routes and return as a list of lists, store each route as [route_number, list of stop codes]
def read_routes(filename):
    routes = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        parts = line.split(",")  
        routes.append([parts[0], parts[1:]]) 
    file.close()
    return routes

#get code from name, converts user imput to code (list-based lookup)
def get_code_from_name(name, codes):
    for pair in codes:
        if pair[1].lower() == name.lower(): 
            return pair[0]
    return None

#get name from code (list-based lookup)
def get_name_from_code(code, codes):
    for pair in codes:
        if pair[0] == code:
            return pair[1]
    return ""

#find direct route, direct route is checked first because of priority
def find_direct_route(start, end, routes):
    for route in routes:
        if start in route[1] and end in route[1]:
            return route
    return None

#transfer route, searched for a single transfer between two different routes
def find_transfer_route(start, end, routes):
    start_routes = []
    end_routes = []
    
    for route in routes:
        if start in route[1]:
            start_routes.append(route)
        if end in route[1]:
            end_routes.append(route)
    
    for r1 in start_routes:
        for r2 in end_routes:
            if r1 != r2:
                for stop in r1[1]:
                    if stop in r2[1]:
                        return r1, r2, stop
    return None

#format route for display
def format_route(route, codes):
    text = "Route " + route[0] + ":"
    for stop in route[1]:
        text += " " + get_name_from_code(stop, codes) + " ->"
    return text

#main function, handles user input and output, converts names to codes
def main():
    codes = read_codes("codes.txt")
    routes = read_routes("routes.txt")

    start_name = input("Enter Starting Point: ")
    end_name = input("Enter Destination: ")

    start_code = get_code_from_name(start_name, codes)
    end_code = get_code_from_name(end_name, codes)

    # input validation for starting point
    while start_code is None:
        print("Invalid starting point. Please try again.")
        start_name = input("Enter Starting Point: ")
        start_code = get_code_from_name(start_name, codes)

    # input validation for destination
    while end_code is None:
        print("Invalid destination. Please try again.")
        end_name = input("Enter Destination: ")
        end_code = get_code_from_name(end_name, codes)


    direct = find_direct_route(start_code, end_code, routes)
    
    if direct is not None:
        print("Direct route found: " + direct[0], end="")
        for stop in direct[1]:
            print(" -> " + get_name_from_code(stop, codes), end="")
        print()
    # No direct route found, check for transfer
    else:
        transfer = find_transfer_route(start_code, end_code, routes)

        if transfer is not None:
            r1, r2, transfer_stop = transfer

            print()
            print("Transfer option found:\n")
            print("Take route " + r1[0] + " and get off at " + get_name_from_code(transfer_stop, codes) + ".")
            print("Then take route " + r2[0] + " to your destination.\n")

            print(format_route(r1, codes))
            print(format_route(r2, codes))

        else:
            print("No routes serving that start point and end point")

main()
