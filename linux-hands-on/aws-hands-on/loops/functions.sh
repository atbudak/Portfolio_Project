#!/bin/bash

Welcome () {
	    echo "Welcome to Linux Lessons $1 $2 $3"
	    return 1
    }

Welcome $1 $2 $3
echo $?
