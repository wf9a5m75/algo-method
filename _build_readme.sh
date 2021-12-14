#!/bin/bash

OUTPUT=./README.md
echo "# アルゴメソッド " > $OUTPUT
now=$(date)
echo "### last update: ${now}" >> $OUTPUT


echo "" > /tmp/README.md

for file_path in $(find . -name "README.md")
do
  if [ "$file_path" != "./README.md" ]; then
    info=$(head -n 1 "${file_path}")
    name=$(echo ${info} | cut -d '#' -f 2)
    modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" ${file_path})
    modified_sort=$(stat -f "%Sm" -t "%Y%m%d%H%M" ${file_path})
    dir_path=$(dirname $file_path)

    echo "${modified_sort}@| [${name}]($dir_path/) | ${modified} | " >> /tmp/README.md
  fi
done
echo "## questions" >> $OUTPUT
echo "| problem | last modified |" >> $OUTPUT
echo "|-|-|" >> $OUTPUT

sort -t'@' -k1 -nr /tmp/README.md  | cut -d'@' -f 2 >> $OUTPUT
rm /tmp/README.md
