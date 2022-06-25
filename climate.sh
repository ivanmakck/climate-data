#!/bin/bash

mkdir -p logs;
exec > >(tee "logs/output_log_`date +"%F"`") 2>&1;

DIR=`mktemp --directory`;

for year in {2020..2022};
do wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year=${year}&Month=2&Day=14&timeframe=1&submit= Download+Data" -P $DIR;
done;

EC1=$?;
if [ $EC1 -ne 0 ];
then exit 1;
fi;

mv $DIR/* ./data;

python3 climate.py;

EC2=$?;
if [ $EC2 -ne 0 ];
then exit 1;
fi;
