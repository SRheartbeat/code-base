def readIndex(index_path, shuffle=False,mode=str):
    _list = []
    if mode == 'train':
        name_list = [os.path.basename(name).split('.')[0]
                     for name in glob(os.path.join(index_path,'train', 'img', '*'))]
        for i in range(len(name_list)):
            name = name_list[i]
            img_path = os.path.normcase(os.path.join(index_path,'train','img', name + '.jpg'))
            seg_path = os.path.normcase(os.path.join(index_path,'train','mask', name + '.bmp'))
            _list.append([img_path,seg_path])
    elif mode == 'val':
        name_list = [os.path.basename(name).split('.')[0]
                     for name in glob(os.path.join(index_path,'val','img', '*'))]
        for i in range(len(name_list)):
            name = name_list[i]
            img_path = os.path.normcase(os.path.join(index_path,'val','img', name + '.JPG'))
            seg_path = os.path.normcase(os.path.join(index_path,'val','mask', name + '.bmp'))
            _list.append([img_path,seg_path])
    elif mode == 'test':
        name_list = [os.path.basename(name).split('.')[0]
                     for name in glob(os.path.join(index_path,'img', '*'))]
        for i in range(len(name_list)):
            name = name_list[i]
            img_path = os.path.normcase(os.path.join(index_path,'img', name + '.jpg'))
            seg_path = os.path.normcase(os.path.join(index_path,'mask', name + '.bmp'))
            _list.append([img_path,seg_path])

    if shuffle is True:
        random.shuffle(_list)
    return _list
