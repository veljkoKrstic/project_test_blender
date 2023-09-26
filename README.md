# Description
This project is build on purpose of testing Blender rendering software.
I have successfully created class called Blender_Test which successfully tests 3 functions of Blender software.
Documentation of Blender Python API is really basic and there is not much information, and updates on the API are often so the functions that were working on Blender 2.8 are not working on newer versions etc.

# Comment
I am new to Blender, never used it before, so i am have a lot of questions regarding how objects, scenes, camera and lighting works. I tried to create render of my object without setting lighting and camera but all i got back were black images so i was not quite sure if there was any other way to solve this without adding materials to the object. Also i created new scene for every object so they are the only object on the render.
Also i was not sure if data for json file regarding environment are needed to be fixed or dynamic based on where the test was executed so i did them dinamically but i was not able to do that for RAM because i needed "psutil" library and ,because i am not familiar with blender, i was not sure how external libraries are handled inside blender.
Also i was not able to export render logs inside code using any bpy function, because all of existing ones were deleted. But i created script the way that if you run it in the way explained below there is log file created.
Also i could create class with fields for blender_path and output_path  but that would not go with the task, as well as to create one function that gets another function as argument, sets up scene, camera and lighting, executes function from argument and export all necessary files, but that as well would not go with given task, so i kept it simple but not as optimized as i could make it. If needed i could do that too.

# Structure of code
Structure is designed this way and could not be made any other way because when blender runs command it changes location in system and I could not target test_module.py file from there.
I did tasks object oriented, created Blender_Test class which has next methods:
## 1.create_new_scene()
## 2.set_lighting()
## 3.set_camera()
## 4.render_image()
## 5.export_json()
## 6.create_cube_test()

# Functions that were necessary for executing tasks properly
## 1.create_new_scene()
Used this function to create a new scene for each object for each task.
## 2.set_lighting()
Used this function to set basic lighting, because if i didn't i would get black picture after render
## 3.night_light()
Used this function to set night lighting, so the lighting can be different for third task
## 4.set_camera()
Used this function to set the angle and position of camera to get better render picture
## 5.render_image()
Used this function to export render as image
## 6.export_json()
Used this function to export all necessary data about test to json file

# Functions that are fulfilling the give tasks
## 1.create_cube_test()
This function calls almost all other functions and in between creates cube object.

## 2.create_sphere_test_basic_light()
This function calls almost all other functions and in between creates red colored sphere object .

## 3.create_sphere_test_night_light()
This function calls almost all other functions and in between creates red colored sphere object in lower light for the third task.

# How to Run
## !!!Change output path in luxsoft_test_script.py in the end of the file, so all the files can be saved in correct output folder!!!
## python <<path_to_execution.py_python_file>>
## Then provide all needed information which will be asked for in terminal