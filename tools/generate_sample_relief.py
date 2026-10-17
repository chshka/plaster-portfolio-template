import bpy,math,sys
from pathlib import Path
from mathutils import Vector
import numpy as np
out=Path(__file__).resolve().parents[1]/'site/assets';out.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def height(x,y):
 # Original procedural relief: rounded frame, floral medallions and stems.
 h=.025
 edge=min(1-abs(x),1-abs(y));h+=.20*math.exp(-((edge-.07)/.018)**2)+.1*math.exp(-((edge-.13)/.014)**2)
 for cy in [-.67,0,.67]:
  yy=(y-cy)*2.5;r=math.hypot(x,yy);a=math.atan2(yy,x)
  petals=(.37+.09*math.cos(6*a));h+=.45*math.exp(-((r-petals)/.10)**2)+.30*math.exp(-(r/.16)**2)
  h+=.10*math.exp(-((r-.63)/.025)**2)
 for side in [-1,1]:
  stem=side*(.73+.065*math.sin(y*14));h+=.13*math.exp(-((x-stem)/.025)**2)
  for cy in [-.83,-.49,-.16,.16,.49,.83]:
   dx=x-side*.72;dy=(y-cy)*2.5;ang=side*.7;u=dx*math.cos(ang)+dy*math.sin(ang);v=-dx*math.sin(ang)+dy*math.cos(ang)
   h+=.15*math.exp(-((u/.14)**2+(v/.045)**2))
 return min(.95,h)
w,h=512,1280;pix=np.zeros((h,w,4),dtype=np.float32)
for j in range(h):
 for i in range(w):pix[j,i,:3]=height(i/(w-1)*2-1,j/(h-1)*2-1)
pix[:,:,3]=1
im=bpy.data.images.new('Linear sample height',width=w,height=h);im.colorspace_settings.name='Non-Color';im.pixels.foreach_set(pix.ravel());im.filepath_raw=str(out/'sample-height.png');im.file_format='PNG';im.save()
cols,rows=100,250;verts=[];faces=[]
for j in range(rows+1):
 for i in range(cols+1):
  x=i/cols*2-1;y=j/rows*2-1;verts.append((x,y*2.5,height(x,y)*.26))
for j in range(rows):
 for i in range(cols):
  a=j*(cols+1)+i;faces.extend([(a,a+1,a+cols+2),(a,a+cols+2,a+cols+1)])
mesh=bpy.data.meshes.new('Sample floral relief');mesh.from_pydata(verts,[],faces);mesh.update();obj=bpy.data.objects.new('Sample plaster relief',mesh);bpy.context.collection.objects.link(obj)
for f in mesh.polygons:f.use_smooth=True
mat=bpy.data.materials.new('Matte white plaster');mat.diffuse_color=(.87,.87,.87,1);mat.use_nodes=True;bs=mat.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(.87,.87,.87,1);bs.inputs['Roughness'].default_value=.9;obj.data.materials.append(mat)
bpy.context.view_layer.objects.active=obj;obj.select_set(True);bpy.ops.export_scene.gltf(filepath=str(out/'sample-relief.glb'),export_format='GLB',use_selection=True)
bpy.ops.object.camera_add(location=(0,0,7));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=5;cam.rotation_euler=(Vector((0,0,0))-cam.location).to_track_quat('-Z','Y').to_euler();scene=bpy.context.scene;scene.camera=cam
bpy.ops.object.light_add(type='AREA',location=(-3,4,6));light=bpy.context.object;light.data.energy=500;light.data.shape='DISK';light.data.size=4;light.rotation_euler=(Vector((0,0,0))-light.location).to_track_quat('-Z','Y').to_euler()
scene.world.color=(.4,.4,.4);scene.render.engine='CYCLES';scene.cycles.samples=16;scene.render.resolution_x=512;scene.render.resolution_y=1280;scene.render.resolution_percentage=100;scene.render.filepath=str(out/'sample-relief.png');bpy.ops.wm.save_as_mainfile(filepath=str(out/'sample-relief.blend'));bpy.ops.render.render(write_still=True)
