# Network Build and Import

## netgenerate (synthetic networks)
- Grid example:
  netgenerate --grid --grid.number 4 --grid.length 100 -o grid.net.xml
- Spider example:
  netgenerate --spider --spider.arm-number 6 --spider.circle-number 4 -o spider.net.xml
- Add traffic lights if needed with --tls.guess true.

## netconvert (import/convert)
- OSM import example:
  netconvert --osm map.osm.xml -o map.net.xml
- Plain XML import example:
  netconvert --node-files nodes.nod.xml --edge-files edges.edg.xml --output-file net.net.xml

## netedit (GUI)
- Use netedit to inspect or edit networks and demand visually.
- Save the edited network as .net.xml for use with sumo.

## OSM download tooling (optional)
- Use $SUMO_HOME/tools/osmGet.py to download OSM data, then convert with netconvert.
- On Windows, replace $SUMO_HOME with %SUMO_HOME%.
