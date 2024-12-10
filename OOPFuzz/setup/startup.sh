#!/bin/bash
cd ..
swi_1="mutate"
swi_2="validate"
swi_3="complete"
if [ $1 = $swi_1 ]
then 
    #echo "swi_1"
    rm *_*.cpp
    python3 ./setup/spread.py
    python3 ./setup/run3.py
elif [ $1 = $swi_2 ]
then
    #echo "swi_2"
    export LANG=EN_US
    python3 ./setup/main.py
elif [ $1 = $swi_3 ]
then
    #echo "swi_3"
    rm *_*.cpp
    python3 ./setup/spread.py
    python3 ./setup/run3.py
    export LANG=EN_US
    python3 ./setup/main.py
else
    echo "no matched operation : $@"
fi