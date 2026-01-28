# Parsing and Conversion

## XML to CSV
- Convert XML outputs:
  python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml
- Customize separator:
  python $SUMO_HOME/tools/xml/xml2csv.py tripinfo.xml --separator ";"

## XML to protobuf
- Convert to protobuf (requires schema):
  python $SUMO_HOME/tools/xml/xml2protobuf.py -x schema.xsd tripinfo.xml

## Notes
- Output files are XML by default.
- Use sumolib or pandas for custom parsing and analysis.
- On Windows, replace $SUMO_HOME with %SUMO_HOME%.
