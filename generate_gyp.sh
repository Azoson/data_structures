#!/bin/bash
scriptpath=`cd $(dirname $0) && pwd`

gyp -f ninja --depth . ${scriptpath}/build/data-structures.gyp
