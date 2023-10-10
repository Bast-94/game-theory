#!/bin/sh
pusher() {
    echo $(git status --porcelain  | awk 'match($1, ""){print $2}' )
    for file in $(git status --porcelain  | awk 'match($1, ""){print $2}' );
        do
            git add $file 2> /dev/null
            echo "Commiting $file"
            read msg
            git commit -m "UPDATE($file): $msg"
        done
}

pusher

