REM    Windows batch script to run a Python program within its virtual environment. This can be called from Windows Task Scheduler.

set venv_root_dir="D:\health_monitoring_python\scripts"

cd %venv_root_dir%

CALL activate_conda.bat

CALL start_app.bat


