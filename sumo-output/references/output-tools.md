# Output Tools

## Attribute statistics
- Compute stats:
  python $SUMO_HOME/tools/output/attributeStats.py --element tripinfo --attribute timeLoss tripinfo.xml
- Compare two runs:
  python $SUMO_HOME/tools/output/attributeDiff.py run1.xml run2.xml --xml-output diff.xml

## Detector generation
- Generic detector generation:
  python $SUMO_HOME/tools/output/generateDetectors.py -n net.net.xml -o detectors.add.xml --detector-type instantInductionLoop
- TLS detector helpers:
  python $SUMO_HOME/tools/output/generateTLSE1Detectors.py -n net.net.xml -o e1.add.xml
  python $SUMO_HOME/tools/output/generateTLSE2Detectors.py -n net.net.xml -o e2.add.xml
  python $SUMO_HOME/tools/output/generateTLSE3Detectors.py -n net.net.xml -o e3.add.xml

## Windows note
- Replace $SUMO_HOME with %SUMO_HOME%.
