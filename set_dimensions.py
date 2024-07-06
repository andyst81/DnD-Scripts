import easygui

def set_aspects(width, height):
    # find largest dimension and set other dimension relative to it
    if (width > height):
        main_dimension = "width"
        aspect_ratio = width/height
    else:
        main_dimension = "height"
        aspect_ratio = height/width
    return (main_dimension, aspect_ratio)

def resize_values(main_dimension, aspect_ratio, standard):
    # generate image new dimensions based on creature size
    if main_dimension == "height":
        new_size = (int(standard/aspect_ratio), standard)
    else:
        new_size = (standard, int(standard/aspect_ratio))
    return new_size

def get_new_size(image_size, input):
    # resize image based on pixel sizes of creature sizes
    if image_size == "Tiny":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=75)
        return new_size
    elif image_size == "Small":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=94)
        return new_size
    elif image_size == "Medium":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=113)
        return new_size
    elif image_size == "Large":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=189)
        return new_size
    elif image_size == "Huge":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=283)
        return new_size
    elif image_size == "Gargantuan":
        main_dimension, aspect_ratio = set_aspects(input.width, input.height)
        new_size = resize_values(main_dimension, aspect_ratio, standard=378)
        return new_size
    else:
        easygui.msgbox("Error!", title="error")
        return