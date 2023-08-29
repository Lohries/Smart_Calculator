
import pygame
import pygame.camera
import time
  

pygame.camera.init()
  

camlist = pygame.camera.list_cameras()
  

if camlist:
    time.sleep(20)
    cam = pygame.camera.Camera(camlist[0], (640, 480))
  
    
    cam.start()

  
    image = cam.get_image()
  

    pygame.image.save(image, "filename.jpg")
  

else:
    print("No camera on current device")