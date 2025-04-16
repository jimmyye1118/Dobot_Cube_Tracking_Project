import roboflow

rf=roboflow.Roboflow(api_key="48TrqHbazjT2kcISiJpD")

project = rf.workspace().project("cube-color-gzmh4")
version = project.version(8)
model_dir = "C:/Users/jimmy/Desktop/Dobot_Cube_Tracking_Project/Cube_Color_4_Model/V7_4_Color_Training1/weights"
version.deploy("yolov11", model_dir, "best.pt")
