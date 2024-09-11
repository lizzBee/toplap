# lizzys midi proj
## some examples of midi messages
>lp control_change channel=0 control=1 value=127 time=0
>AKAI control_change channel=0 control=5 value=29 time=0
>AKAI control_change channel=0 control=5 value=30 time=0
>AKAI control_change channel=0 control=5 value=31 time=0
>AKAI control_change channel=0 control=5 value=32 time=0
>AKAI control_change channel=0 control=5 value=33 time=0
>AKAI control_change channel=0 control=5 value=34 time=0
>lp control_change channel=1 control=1 value=127 time=0

## Channel mappings
| Channel | Action              |
|---------|---------------------|
| 0       | spinnys~sfx         |
| 1       | record              |
| 2       | re-record (on top)  |
| 3       | mute                |
| 4       | solo                |
| 5       | freeplay (on)       |
