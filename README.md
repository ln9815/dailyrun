# Daily Run tool
## How to install
colne to local, run it in venv.

    pip install -e .
    pip install build
    python -m build

then you can get dailyrun-0.1.0-py3-none-any.whl in folder dist. and install it with pip

    pip install dailyrun-0.1.0-py3-none-any.whl


## How to use
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
