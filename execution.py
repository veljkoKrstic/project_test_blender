import os

blender_path=input('Insert path to your blender.exe file: ')
#C:\Program Files\Blender Foundation\Blender 3.6
os.chdir(f'{blender_path}')
python_script_path=input('Insert path to your python script: ')
#F:\PythonProjects\project_test_blender\luxsoft_test_script.py
log_output_path=input('Insert path to output your render log: ')
#F:\PythonProjects\project_test_blender\Output\RenderLogs

os.system(f'cmd /c "blender -b -P {python_script_path} > {log_output_path}\log.txt"')