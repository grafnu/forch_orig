#!/bin/bash -e

TMP_SH=/tmp/update_gmaster.sh
BASE=`git rev-parse --show-toplevel`
BASE_SH=$BASE/update_gmaster.sh
VTEMP=/tmp/GVERSION
date > $VTEMP
UPSTREAM=`git rev-parse --abbrev-ref gupdater@{upstream}`
REPO=${UPSTREAM%/*}
BASELINE=gmaster
FFILE=/tmp/FEATURES
cp $BASE/gutil/FEATURES $FFILE

name_line=`fgrep name= $BASE/setup.py`
name_line=${name_line#*\"}
PROJ=${name_line%\"*}
echo Mined project $PROJ from setup.py
VFILE=$BASE/$PROJ/GVERSION

if [ $0 != $TMP_SH ]; then
    echo Running out of $TMP_SH to mask local churn...
    cp $0 $TMP_SH
    $TMP_SH $*; false
fi

if [ "$1" == reset ]; then
    echo Reset to using master as baseline...
    BASELINE=master
fi

if [ "$1" == reset ]; then
    BASELINE=master
fi

branch=`git rev-parse --abbrev-ref HEAD`
if [ "$branch" != "gupdater" ]; then
    echo $0 should be run from the gupdater branch, not $branch.
    false
fi

files=`git status --porcelain`
if [ -n "$files" ]; then
    echo Local changes detected:
    echo $files
    echo Please resolve before updating.
    false
fi

ORIGIN=`git remote -v | egrep ^$REPO | fgrep fetch | awk '{print $2}'`
echo upstream $ORIGIN >> $VTEMP

echo Fetching remote repos...
git fetch $REPO

LOCAL=`git rev-parse gupdater`
echo gupdater $LOCAL >> $VTEMP
REMOTE=`git rev-parse $REPO/gupdater`
if [ "$LOCAL" != "$REMOTE" ]; then
    echo gupdater out of sync with upstream $REPO/gupdater
    #false
fi

echo Switching to gmaster branch...
git checkout gmaster

echo Creating clean base from origin/$BASELINE...
git reset --hard origin/$BASELINE
echo $BASELINE `git rev-parse HEAD`>> $VTEMP

echo Merging feature branches...
while read < $FFILE; do
    hash=$1
    branch=$2
    bhash=`git rev-parse $REPO/$branch`
    if [ "$bhash" != "$hash" ]; then
        echo Branch hash mismatch for $branch
        false
    fi
    echo Merging $REPO/$branch...
    git merge --no-edit $REPO/$branch
    echo $hash $branch >> $VTEMP
done

echo gmaster `git rev-parse HEAD` >> $VTEMP
cp $VTEMP $VFILE
git add $VFILE
git commit -m "Version assembled $(date)"

echo Done with clean gmaster merge.
echo Now time to validate and push!
