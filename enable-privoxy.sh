#!/bin/sh
# $1 is the password
[ -n "$1" ] || {
    echo "Provide a password for your tor control port"
    exit 1
}

hash="$(tor --hash-password "$1")"

backup() { # backup $1 with a timestamp
    cp "$1" "$1-$(date "+%y%m%d-%a-%H%M%S").bak"
}

replace_or_append() { # $1 replace query; $2: replacee; $3: file
    if ! sed "/$1"'/{s//'"$2"'/;h};${x;/./{x;q0};x;q1}' "$3"; then
        sed "\$a$2" /etc/tor/torrc
    fi
}

backup "/etc/tor/torrc"
replace_or_append "#\s*ControlPort.*" "ControlPort 9051" "/etc/tor/torrc"
replace_or_append "#\s*HashedControlPassword.*" "HashedControlPassword $hash" "/etc/tor/torrc"

backup "/etc/privoxy/config"
sed -i '$aforward-socks5t / 127.0.0.1:9050 .\nkeep-alive-timeout 600\ndefault-server-timeout 600\nsocket-timeout 600' "/etc/privoxy/config"

echo "$hash"
