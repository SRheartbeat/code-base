def RandomCut(img, mask,):

    height, width = img.shape[:2]
    center_height = int(height / 2.0)
    center_width = int(width / 2.0)
    Cut = np.random.choice(np.array([0, 1, 2, 3, 4, ]))
    if Cut == 0:
        _img = img[:512, :512, :]
        _mask = mask[:512, :512]
    elif Cut == 1:
        _img = img[:512, -512:, :]
        _mask = mask[:512, -512:]
    elif Cut == 2:
        _img = img[-512:, :512, :]
        _mask = mask[-512:, :512]
    elif Cut == 3:
        _img = img[-512:, -512:, :]
        _mask = mask[-512:, -512:]
    elif Cut == 4:
        _img = img[int(center_height-256):int(center_height+256), int(center_width-256):int(center_width+256), :]
        _mask = mask[int(center_height-256):int(center_height+256), int(center_width-256):int(center_width+256)]

    return _img, _mask


def RandomFlip(img, mask, ):
    Flip = np.random.choice(np.array([0, 1, -1, ]))
    if Flip == 0:
        _img = cv2.flip(img, 0)  
        _mask = cv2.flip(mask, 0)
    if Flip == 1:
        _img = cv2.flip(img, 1) 
        _mask = cv2.flip(mask, 1)
    if Flip == -1:
        _img = cv2.flip(img, -1)  
        _mask = cv2.flip(mask, -1)

    return _img, _mask

def RandomRotate(img, mask, border_mode=cv2.BORDER_CONSTANT, border_value=0):
    angle = np.random.choice(np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]))
    height, width = img.shape[:2]
    center = (width / 2.0, height / 2.0)
    rot = cv2.getRotationMatrix2D(center, angle, 1.0)

    # determine bounding rectangle
    boxpoints = cv2.boxPoints((center, (width, height), angle))
    bbox = cv2.boundingRect(boxpoints)  # x,y,width,height

    # adjust transformation matrix
    rot[0, 2] += bbox[2] / 2.0 - center[0]
    rot[1, 2] += bbox[3] / 2.0 - center[1]

    return cv2.warpAffine(img, rot, (bbox[2], bbox[3]), flags=cv2.INTER_CUBIC, borderMode=border_mode, borderValue=border_value), cv2.warpAffine(mask, rot, (bbox[2], bbox[3]), flags=cv2.INTER_NEAREST, borderMode=border_mode, borderValue=border_value)
