def myimages(imdir):
    import os
    # imdir = '.\\..\\ImageAssets\\Juicy\\'
    files = os.listdir(imdir)
    image_paths = list(
        map(lambda filename: imdir+filename, 
            filter(
                lambda filename: filename.endswith(('.jpg','.JPG')), files)
            )
        )
    
    return image_paths


