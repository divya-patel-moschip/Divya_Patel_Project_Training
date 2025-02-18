import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element("testsuites")

LOG_ARRAY = []

with open('mylog.log', 'r') as log_file:
    for index, line in enumerate(log_file):
        if index <=5:
            LOG_ARRAY.append(f"{index}: {line.strip()}")

for i in range(6):
    testsuite = ET.Element("testsuite", {
        "name": f"Suite-{i}",
        "tests": "0",
        "failures": "1",
        "errors": "0",
        "skipped": "0",
        "time": "0.123"
    })
    testcase = ET.Element("testcase", {
        "name": LOG_ARRAY[i],
        "classname": f"Suite-{i}",
        "time": "0.123"
    })
    if i % 2 == 0:  # Simulate a failure for every even test case
        failure = ET.Element("failure", {
            "message": f"Failure in Test-{i}",
            "type": "AssertionError"
        })
        failure.text = f"Details about the failure in Test-{i}."
        testcase.append(failure)
    elif i >= 3:
        skipped = ET.Element("skipped", {
            "message": f"Test-{i} was skipped by user"
        })
        testcase.append(skipped)

    testsuite.append(testcase)
    root.append(testsuite)

rough_string = ET.tostring(root, 'utf-8')

parsed = minidom.parseString(rough_string)
pretty_xml = parsed.toprettyxml(indent="  ")

with open('report.xml', 'w') as f:
    f.write(pretty_xml)

print("JUnit-compatible XML written to 'report.xml'")
