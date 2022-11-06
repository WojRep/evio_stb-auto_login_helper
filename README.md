# Automatic login helper of Evio IPTV decoders like Z123

#### Wymagania

    - Zalecany Python >=3.6
    - Środowisko uruchomieniowe docker

#### Instalacja

`docker run -p 44444:5000 wrepinski/evio_stb-auto_login_helper`

#### Użytkowanie wywołania API:

Wywołanie: `http://hostname.domain:44444/Evio/<ip>/<mac_address>/login`
gdzie:
`<ip>` - to IP STB Evio
`<mac_address>` - to MAC STB Evio

Wynikiem jest przekierowanie z żądaniem zalogowania się do STB Evio.

Przetestowane z Z123.
