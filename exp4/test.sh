#!usr/bin/env Bash

echo "Start testing";
cd ./code;
python IndexFiles.py;
python SearchFiles.py;
cd ..;
echo "Finish testing";
