# Utils karton service

Analyse Utils from files with Karton.

**Author**: cocoapuck

**Maintainers**: cocoapuck

## Usage

### Build local pip


`python3 setup.py bdist_wheel`


### Create service


`sudo nano /usr/lib/systemd/system/mwdb-karton-utils.service`


### Contents of /usr/lib/systemd/system/mwdb-karton-utils.service


```
[Unit]
Description=Karton System
After=network.target

[Service]
User=sadmin
Group=sadmin
WorkingDirectory=/opt/karton
Environment="PATH=/opt/karton/.karton/bin"
ExecStart=/opt/karton/.karton/bin/karton-utils
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```


### Systemd commands


`sudo systemctl daemon-reload`
`sudo systemctl enable mwdb-karton-utils`
`sudo systemctl start mwdb-karton-utils`