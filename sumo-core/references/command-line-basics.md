# Command Line Basics

## Option syntax
- Use --option value, --option=value, or short -o value.
- Boolean options can be toggled with true/false.
- Append list options from a config file with +a or +n.

## Config files
- XML root <configuration>.
- Options as element names with value or v attribute.
- Run with sumo -c file.sumocfg (or pass file directly).
- For sumo-gui the extension .sumocfg is required.

## Minimal config example
```xml
<configuration>
  <input>
    <net-file value="net.net.xml"/>
    <route-files value="routes.rou.xml"/>
    <additional-files value="extras.add.xml"/>
  </input>
</configuration>
```

## Templates
- Use --save-template FILE to generate a template config.
- Use --save-schema FILE to export the XSD for validation.
