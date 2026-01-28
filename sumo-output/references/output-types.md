# Output Types and Enablement

## Command line outputs (examples)
- --tripinfo-output tripinfo.xml
- --fcd-output fcd.xml
- --summary-output summary.xml
- --vehroute-output vehroute.xml
- --statistic-output stats.xml
- --emission-output emission.xml

## Output prefix and format
- Use --output-prefix TIME to separate runs.
- Use a .gz extension for compressed output.
- Use --output.format csv or parquet where supported.

## Additional-file outputs (detectors)
- Define detectors in an additional file and load it with --additional-files.
- Example detector:
```xml
<additional>
  <inductionLoop id="e1_0" lane="edge_0" pos="10" period="60" file="e1.xml"/>
</additional>
```

## Notes
- Some outputs are enabled only via additional files, not command-line flags.
