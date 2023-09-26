import bpy
import platform
import json
from datetime import datetime

class Blender_Test:
        
    def create_new_scene(self,x_resolution,y_resolution,scene_name="New scene"):
        # Create a new scene and link it to this file
        new_scene = bpy.data.scenes.new(scene_name)
        bpy.context.window.scene = new_scene
        
        #Check file type of resolution variables
        assert type(x_resolution)==int and type(y_resolution)==int,'Wrong data type for resolution'
        
        # Change resolution for this image
        new_scene.render.resolution_x = x_resolution
        new_scene.render.resolution_y = y_resolution
        
        # Create camera
        bpy.ops.object.camera_add(location=(0, 0, 0))
        new_camera = bpy.context.object
        new_scene.camera = new_camera
        
        print('New scene is successfully created')
    
    def set_lighting(self):
        #Set lighting
        light_data = bpy.data.lights.new(name="Light", type='POINT')
        light_object= bpy.data.objects.new(name='Light Object',object_data=light_data)
        bpy.context.collection.objects.link(light_object)
        light_object.location=(3,3,3)
        light_data.energy=3000
        
        print('Default light is set up')

    def night_light(self):
        # Add a point light source (simulating moonlight)
        bpy.ops.object.light_add(type='POINT', align='WORLD', location=(0, 0, 10))
        nightlight = bpy.context.active_object
        nightlight.data.energy = 500  # Adjust the intensity as needed 
        nightlight.location=(6,4,3)
        
        print('Night light is set up')

    def set_camera(self):
        #Set location of camera
        scene = bpy.context.scene
        scene.camera.location.x = 3
        scene.camera.location.y = 15
        scene.camera.location.z = 11
        
        #Set rotation of camera
        scene.camera.rotation_mode = 'XYZ'
        scene.camera.rotation_euler[0] = -662.163 * (3.14 / 180.0) 
        scene.camera.rotation_euler[1] = 2.21025 * (3.14 / 180.0)
        scene.camera.rotation_euler[2] = -1999.33 * (3.14 / 180.0) 
        
        print('Camera is placed')
             
    def render_image(self,output_path,image_name,x_resolution,y_resolution): 
        #Render image and save it
        bpy.context.scene.render.filepath = f"{output_path}\{image_name}.png"
        bpy.context.scene.render.image_settings.file_format = 'PNG' 
        bpy.ops.render.render(write_still=True) 
        print(f'Render of {image_name} is saved\nResults in: {output_path}\{image_name}.png')
    
    def export_json(self,output_path,test_name,test_start,test_end):
        #Get info about machine
        uname = platform.uname()
        #Create dict from which json file is gonna be created
        json_file={
        "TestName":test_name,
        "Test_Executed":test_start.strftime("%H:%M:%S.%f %d/%m/%Y"),
        "Test_Finished":test_end.strftime("%H:%M:%S.%f %d/%m/%Y"),
        "Test_Duration":str(test_end-test_start)[:-1],
        "Environment":{
            "CPU":str(uname.processor),
            "RAM":"32GB", #Made it fixed because to make it dynamic i need library psutil
            "OS":f"{platform.system()} {platform.release()} {platform.version()}"}
        }
        #convert dict to json format
        json_object = json.dumps(json_file, indent=4)
 
        #write json file in output folder with test_name.json as name
        with open(f"{output_path}\{test_name}.json", "w") as outfile:
            outfile.write(json_object)
        
        print(f'JSON report for {test_name} is created\nResults in: {output_path}\{test_name}.json')
        
    def create_cube_test(self,output_path,x_resolution,y_resolution):
        #Set up test environment
        print('First test started. Cube test is starting execution.')
        print()
        scene_name="cube_scene"
        test_start = datetime.now()
        self.create_new_scene(x_resolution,y_resolution,scene_name)
        self.set_lighting()
        self.set_camera()
        print()
        print('Environment is set up')
        # Create mesh and new object
        cube = bpy.data.meshes.new("Cube")
        cube_obj = bpy.data.objects.new("Cube Object", cube)
        print('Cube object is created')

        # Setthe object to new scene
        bpy.context.collection.objects.link(cube_obj)
    
        # Set cube as active object
        bpy.context.view_layer.objects.active = cube_obj
        # Make it editable
        bpy.ops.object.mode_set(mode="EDIT")

        # Create size and position
        bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
        # Exit editing
        bpy.ops.object.mode_set(mode="OBJECT")
        print('Cube object is edited and setup')
        test_end= datetime.now()
        
        print('Test is finished. Exporting results.')
        #Export test results
        self.export_json(output_path,'Cube_basic_ligthing_test' , test_start , test_end)
        self.render_image(output_path,"Cube_basic_ligthing_test", x_resolution , y_resolution)

        print('Cube_basic_ligthing_test Passed\nResults saved in Output folder.')
        print('='*50)
        print()

    def create_sphere_test_basic_light(self, output_path, x_resolution, y_resolution):
        #Set up test environment
        print('Second test started. Sphere colored test is starting execution.')
        print()
        scene_name = "sphere_scene"
        test_start = datetime.now()
        self.create_new_scene(x_resolution, y_resolution, scene_name)
        self.set_lighting()
        self.set_camera()
        print()
        print('Environment is set up')
        # Create a new mesh and object named "Sphere"
        sphere = bpy.data.meshes.new("Sphere")
        sphere_obj = bpy.data.objects.new("Sphere Object", sphere)
        print('Sphere object is created')

        # Set the object on new scene
        bpy.context.collection.objects.link(sphere_obj)
        
        # Set sphere as active object
        bpy.context.view_layer.objects.active = sphere_obj

        # Make sphere editable
        bpy.ops.object.mode_set(mode="EDIT")
        # Set size and position
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, 1))

        #Exit editing mode for sphere
        bpy.ops.object.mode_set(mode="OBJECT")

        #Create material and set the color
        material = bpy.data.materials.new("Sphere Material")
        material.diffuse_color = (1,0,0,0.8) 
        sphere_obj.data.materials.append(material)
        print('Sphere object is edited and setup. Material and color is added. Sphere is red.')
        # Record the end time of the test
        test_end = datetime.now()
        
        print('Test is finished. Exporting results.')
        # Export test result
        self.export_json(output_path, 'Basic_lighting_sphere_test', test_start, test_end)
        self.render_image(output_path, "Basic_lighting_sphere_test", x_resolution, y_resolution)

        print('Basic_lighting_sphere_test Passed\nResults saved in Output folder.')
        print('='*50)
        print()

    def create_sphere_test_night_light(self, output_path, x_resolution, y_resolution):
        #Set up test environment
        print('Third test started. Spehere low light test is starting execution.')
        print()
        scene_name = "sphere_scene_nightlight"
        test_start = datetime.now()
        self.create_new_scene(x_resolution, y_resolution, scene_name)
        self.night_light()
        self.set_camera()
        print()
        print('Environment is set up with low light')
        # Create a new mesh and object named "Sphere"
        sphere = bpy.data.meshes.new("Sphere")
        sphere_obj = bpy.data.objects.new("Sphere Object", sphere)
        print('Sphere object is created')

        # Set the object on new scene
        bpy.context.collection.objects.link(sphere_obj)
        
        # Set sphere as active object
        bpy.context.view_layer.objects.active = sphere_obj

        # Make sphere editable
        bpy.ops.object.mode_set(mode="EDIT")
        # Set size and position
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, 1))

        #Exit editing mode for sphere
        bpy.ops.object.mode_set(mode="OBJECT")

        #Create material and set the color
        material = bpy.data.materials.new("Sphere Material")
        material.diffuse_color = (1,0,0,0.8) 
        sphere_obj.data.materials.append(material)
        print('Sphere object is edited and setup. Material and color is added. Sphere is red.')
        # Record the end time of the test
        test_end = datetime.now()
        print('Test is finished. Exporting results.')
        # Export test result
        self.export_json(output_path, 'nightligh_sphere_test', test_start, test_end)
        self.render_image(output_path, "nightligh_sphere_test", x_resolution, y_resolution)
        print('Low_lighting_sphere_test Passed\nResults saved in Output folder.')
        print('='*50)
        print()

p=Blender_Test()

cube_test_renders_output='F:\PythonProjects\project_test_blender\output\cube_render_results'
sphere_test_renders_output='F:\PythonProjects\project_test_blender\output\sphere_render_results'
night_sphere_test_renders_output='F:\PythonProjects\project_test_blender\output\sphere_night_render_results'

p.create_cube_test(cube_test_renders_output,1920,1080)
p.create_sphere_test_basic_light(sphere_test_renders_output,1920,1080)
p.create_sphere_test_night_light(night_sphere_test_renders_output,1920,1080)