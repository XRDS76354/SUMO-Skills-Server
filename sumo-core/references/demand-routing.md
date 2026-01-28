# Demand and Routing

## randomTrips.py
- Generate trips:
  python $SUMO_HOME/tools/randomTrips.py -n net.net.xml -e 3600 -p 1 -o trips.trips.xml
- Generate routes directly (calls duarouter):
  python $SUMO_HOME/tools/randomTrips.py -n net.net.xml -e 3600 -p 1 --route-file routes.rou.xml
- Use --random or --seed for repeatable randomness.
- On Windows, replace $SUMO_HOME with %SUMO_HOME%.

## od2trips (OD matrices)
- Convert OD to trips:
  od2trips -n taz.xml -d od.csv -o trips.trips.xml

## duarouter
- Compute routes from trips:
  duarouter -n net.net.xml -r trips.trips.xml -o routes.rou.xml

## Notes
- Load routes in sumo via --route-files or in a .sumocfg.
- For OD workflows, ensure TAZ definitions exist.
