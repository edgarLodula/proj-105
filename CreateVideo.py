import cv2

path="Images"

images=[]

for verificaFile in os.listdir(path):
     name, ext = os.path.splitext(file)

     if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

        count = len(images) 

        frame=cv2.imread(images [0])

        height,width,canais=frame.shape
        size=(width,height)

        out=cv2.VideoWriter("Nascsol.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,size)

        for i in range(0,count-1):
            frame=cv2.imread(images[i])
            out.write(frame)
       
        print("concluido")