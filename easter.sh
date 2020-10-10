#!/bin/bash

fetch_ascii_art(){
    rm -f .ascii-art && touch .ascii-art
    echo "" > .ascii-art
    curl -s \
    'https://ssfy.sh/dev/text-to-ascii-art@d9d0510c/textToAsciiArt?text=FastAPI%20API&font=Doom' >> .ascii-art
    echo -e "\nBy: Aris Ripandi\n" >> .ascii-art
}

prolado(){
    cat .ascii-art
    echo "[RUNNING] http://localhost:5000/docs"
    echo "[CTRL-C] to exit or wait.."
}

prooutro(){
    cat .ascii-art
    echo "[RUNNING] http://localhost:5000/docs"
    echo "[CTRL-C] to exit or wait..."
}

if [[ ! -e .ascii-art ]]; then
    fetch_ascii_art
fi

egg="$(python -c 'print("clear ; prolado ; sleep 1 ; clear ; prooutro; sleep 1;" * (0xDEADBEAF - (0xDEADBEAF - 42)))')"
eval $egg
