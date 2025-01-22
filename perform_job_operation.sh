# Performing operations like changing values of variables(read_delay, write_delay),
# printing value of variables (in_checks),
# replacing value of <assignedNode> tag with new value "TenIvp - Dummy",
# Adding network configurations after "${WORKSPACE}/change_network.cfg"
# finding files that are modified less than 5 days and listing only .xml files.

file=$(cat job_list.txt)
for line in $file; do
  # 1. Performing a sed operation change the values of read_delay and write_delay
  sed -i 's/read_delay = 100/read_delay = 150/' "$line.xml"
  sed -i 's/write_delay = 10/write-delay = 50/' "$line.xml"

  # 2.  Print the values of in_checks variable from the .xml files
  # It will print value of in_checks from all the files.
  awk '/export in_checks=/{flag=1} flag && /\\/{printf "%s\n", $0} flag && !/\\/ {print $0; flag=0}' "$line.xml"
  echo

  # 3. Perform a sed operation to replace the value of <assignedNode> with "TenIvp - Dummy"
  sed -i 's/<assignedNode>.*<\/assignedNode>/<assignedNode>TenIvp - Dummy<\/assignedNode>/' "$line.xml"

  # 4. Adding network configuration below of "${WORKSPACE}/change_network.cfg"
  sed -i "/${WORKSPACE}\/change_network.cfg/a \[extraXNNCargs.TinyBert_ONNX] \n--mapper_extra == -enable-index-placeholder=true" "$line.xml"

  # 5. Find files that are modified less than 5 days ago and display only .xml files using grep command
  find ./ -type f -mtime -5 | grep "\.xml$"
done