#!/usr/bin/bash

this_file_path=`readlink -f $0`
this_dir_path=`dirname $this_file_path`

echo $this_dir_path
cd $this_dir_path

docker build -f Dockerfile -t mytest:1.0.0 .


cd -