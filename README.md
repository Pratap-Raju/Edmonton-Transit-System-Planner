🚌 ETS Transit Tracker (Python)

A Python-based transit routing tool that analyzes Edmonton Transit Service (ETS) bus routes to determine direct and single-transfer paths between user-specified stops using structured lists and modular design.


Features:

- Accepts human-readable stop names as input
- Finds:
    - Direct routes (no transfers)
    - Single-transfer routes (one valid transfer stop)
- Uses list-based data structures only (no dictionaries), as per software constraints
- Includes robust input validation
- Modular, readable, and well-documented code
- Outputs routes in a clear, user-friendly format


🛠️ How It Works:

- Reads transit stop codes and route data from text files
- Converts user input (stop names) into internal stop codes
- Searches for:
    - A direct route containing both stops
    - Otherwise, two distinct routes sharing a common transfer stop
- Displays the full stop-by-stop path for the route(s)


▶️ Usage

Run the program using Python:

bus_routes.py

Example interaction:

Enter Starting Point: southgate
Enter Destination: university

Example output:

Transfer option found:

Take route 009 and get off at Garneau.
Then take route 004 to your destination.

Route 009: Southgate -> Pleasantview -> Allendale -> Queen Alexandra -> Garneau ->
Route 004: University -> Garneau -> Strathcona -> King Edward Park -> Capilano ->


🧠 Technical Highlights

Structured Lists: All data is stored as nested lists (e.g., [route_id, [stop1, stop2, ...]])
Separation of Concerns:
 - Input handling
 - Route computation
 - Output formatting
Early Exit Optimization: Stops searching once a valid route is found
No Forbidden Constructs: Complies with academic constraints (no dictionaries, no external libraries)


🧪 Tested Scenarios

✔ Direct route available
✔ Route requiring a single transfer
✔ No valid route exists
✔ Invalid user input (with re-prompting)


🎓 Academic Context

This project was completed as part of CMPUT 175 (Introduction to the Foundations of Computation II) and demonstrates:

- Algorithmic thinking
- List-based data modeling
- Modular function design
- Clear program flow and validation


📈 Future Improvements

- Support for multi-transfer routes
- Shortest-path optimization
- Graph-based routing approach
- Interactive or GUI-based interface

👤 Author

Pratap Kolukuluri
Computer Science Student
