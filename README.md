# Daily Run tool
## How to use it
this script will run the specified command at the specified time points every day.
Used as following:

        Usage: dailyrun [OPTIONS]

        Options:
        -c, --cmd TEXT    command to run.  [required]
        -t, --times TEXT  times to run command. valid format is HH:MM(:SS) and
                            combined with &  [required]
        --help            Show this message and exit.

## Example
Run command 'dir' and 10:00 and 11：00 every day.

    dailyrun -c dir -t 10:00&11:00
    dailyrun -cmd 'ls -l' -times '10:00&11:00'
