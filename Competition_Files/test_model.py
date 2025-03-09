import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from tensorflow.keras.models import load_model


class Test:
    def get_bounds(IMG_SHAPE, X_CUT, Y_CUT):
        # get x and y bounds
        x_bounds = []
        y_bounds = []

        for i in range(X_CUT):
            x_bounds.append((int(i*IMG_SHAPE[1]/X_CUT), int((i+1)*IMG_SHAPE[1]/X_CUT)))
        for j in range(Y_CUT):
            y_bounds.append((int(j*IMG_SHAPE[0]/Y_CUT), int((j+1)*IMG_SHAPE[0]/Y_CUT)))

        return x_bounds, y_bounds


    def cut_image(IMG_SIZE, x_bounds, y_bounds, X_CUT, Y_CUT):
        # cut image into quadrants
        img_array = []

        for i in range(X_CUT):
            x_bb = x_bounds[i]
            for j in range(Y_CUT):
                y_bb = y_bounds[j]

                # split image and save into img_array
                cropped_img = full_img[y_bb[0]:y_bb[1], x_bb[0]:x_bb[1]]
                cropped_img_2 = cv2.resize(cropped_img, (IMG_SIZE, IMG_SIZE))
                
                img_array.append(cropped_img_2)
        return img_array


    def get_test_data(img_array):
        # make testing set
        X_test = np.array(img_array)
        X_test = X_test.reshape(-1, X_test.shape[1], X_test.shape[2], 1)
        
        return X_test.astype('float32') / 255.0

        




    ##################
    ### CODE BELOW ###
    ##################

    def CarsInTheSky(imageName):

        # # SPECIFIED CONSTANTS
        # X_CUT = 3
        # Y_CUT = 3

        # # given file path
        # # dir = './test_data'
        # dir = os.path.dirname(__file__)
        # model_name = 'thermal_detection_model.h5'
        # img_name = imageName     # GET FROM PI

        # # get image
        # full_img = cv2.imread(os.path.join(dir,img_name), cv2.IMREAD_GRAYSCALE)
        # IMG_SHAPE = full_img.shape

        # # load model from the saved file
        # model = load_model(os.path.join(dir,model_name))
        # IMG_SIZE = model.input_shape[1]


        # # get bounds
        # x_bounds, y_bounds = get_bounds(IMG_SHAPE, X_CUT, Y_CUT)
        # # cut image
        # img_array = cut_image(IMG_SIZE, x_bounds, y_bounds, X_CUT, Y_CUT)
        # # get X_test
        # X_test = get_test_data(img_array)

        # # predict using model
        # y_pred = model.predict(X_test)



        #-------------
        # FINAL BOSS 
        #-------------
        # string_of_strings = ''

        # # get info from y_pred
        # class_preds = [np.argmax(categories, axis=0) + 1 for categories in y_pred]
        # confidence = [np.amax(categories, axis=0) for categories in y_pred]

        # # set acceptable confidence range
        # MIN_CONFIDENCE = 0.97
        # MAX_CONFIDENCE = 1.0

        # for i in range(X_CUT):
        #     for j in range(Y_CUT):
        #         # iterate through all y_preds
        #         index = X_CUT*i + j
        #         # disregard all values with confidence levels outside limits
        #         if (confidence[index] >= MIN_CONFIDENCE) & (confidence[index] < MAX_CONFIDENCE):
        #             print(y_pred[index])
        #             # add to final txt string
        #             string_of_strings += f"{img_name} {class_preds[index]} {confidence[index]} {x_bounds[i][0]} {y_bounds[j][0]} {x_bounds[i][1]} {y_bounds[j][1]}\n"

        # return final output
        return null


