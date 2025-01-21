# import xml.etree.ElementTree as ET
# from xml.dom import minidom
#
# root = ET.Element("testsuites")
#
# LOG_ARRAY = []
#
# with open('mylog.log', 'r') as log_file:
#     for index, line in enumerate(log_file):
#         if index <=4:
#             LOG_ARRAY.append(f"{index}: {line.strip()}")
#
#
#
# for i in range(5):
#     ele1 = ET.Element("testsuite")
#     ele2 = ET.Element('testcase')
#     ele3 = ET.Element("build-info")
#     ele2.text = f"Test-{i}"
#     ele3.text = LOG_ARRAY[i]
#     ele1.append(ele2)
#     ele1.append(ele3)
#     root.append(ele1)
#
# rough_string = ET.tostring(root, 'utf-8')
#
# parsed = minidom.parseString(rough_string)
# pretty_xml = parsed.toprettyxml(indent="    ")
#
# with open('report.xml', 'w') as f:
#     f.write(pretty_xml)
#
# print("Formatted XML written to 'report.xml'")


import xml.etree.ElementTree as ET
from xml.dom import minidom

root = ET.Element("testsuites")

LOG_ARRAY = []

with open('mylog.log', 'r') as log_file:
    for index, line in enumerate(log_file):
        if index <=3:
            LOG_ARRAY.append(f"{index}: {line.strip()}")

for i in range(4):
    if i%2 == 0:
        testsuite = ET.Element("testsuite", {
            "name": f"Suite-{i}",
            "tests": "1",
            "failures": "0",
            "errors": "0",
            "skipped": "0",
            "time": "0.123"
        })
    else:
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

    testsuite.append(testcase)
    root.append(testsuite)

rough_string = ET.tostring(root, 'utf-8')

parsed = minidom.parseString(rough_string)
pretty_xml = parsed.toprettyxml(indent="  ")

with open('report.xml', 'w') as f:
    f.write(pretty_xml)

print("JUnit-compatible XML written to 'report.xml'")
