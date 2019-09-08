#! /usr/bin/bash

TESTDIR="./testProject"

rm -r $TESTDIR
mkdir $TESTDIR
cd $TESTDIR

echo "Testing INIT"
../project --init

echo "Created in $TESTDIR:"
ls -la

