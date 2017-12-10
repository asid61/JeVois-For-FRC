import libjevois as jevois
import cv2
import numpy as np

## Simple example of image processing using OpenCV in Python on JeVois
#
# This module is a basic FRC vision process.
#
# By default, it first gets an image, blurs it, extracts the green channel, thresholds that, and uses the threshold to place
# a mask over the initial image. It then runs an HSV filter on the masked image, erodes and dilates the result, and finally
# finds and filters the contours.
# You can find the constants for all of these using GRIP. Tune the program constants and generate Python code from GRIP. Then,
# paste those constants into the Constructor below. Custom code can also be inserted after all the GRIP process code.
#
# See http://jevois.org/tutorials for tutorials on getting started with programming JeVois in Python without having
# to install any development software on your host computer.
#
# @author Anand Rajamani
# 
# @videomapping YUYV 320 240 60.0 YUYV 320 240 60.0 JeVois PythonSandbox
# @email anand.rajamani@scu.edu
# @mainurl http://jevois.org
# @supporturl http://jevois.org/doc
# @otherurl http://iLab.usc.edu
# @license GPL v3
# @distribution Unrestricted
# @restrictions None
# @ingroup modules

class PythonSandbox:
    # ###################################################################################################
    ## Constructor
    def __init__(self):
        # Instantiate a JeVois Timer to measure our processing framerate:
        self.timer = jevois.Timer("sandbox", 100, jevois.LOG_INFO)

        #SPECIAL REPLACED BLUR CONSTANT
        self.__blur_type = 0
        
        #ALL CONSTANTS GO HERE (make sure to remove the self.__blur_type line)
        
        self.__blur_radius = 5.0229474757776655

        self.blur_output = None

        self.__cv_extractchannel_src = self.blur_output
        self.__cv_extractchannel_channel = 1.0

        self.cv_extractchannel_output = None

        self.__cv_threshold_src = self.cv_extractchannel_output
        self.__cv_threshold_thresh = 30.0
        self.__cv_threshold_maxval = 255.0
        self.__cv_threshold_type = cv2.THRESH_BINARY

        self.cv_threshold_output = None

        self.__mask_input = self.blur_output
        self.__mask_mask = self.cv_threshold_output

        self.mask_output = None

        self.__normalize_input = self.mask_output
        self.__normalize_type = cv2.NORM_MINMAX
        self.__normalize_alpha = 0.0
        self.__normalize_beta = 255.0

        self.normalize_output = None

        self.__hsv_threshold_input = self.normalize_output
        self.__hsv_threshold_hue = [66.36690647482014, 94.9130331623807]
        self.__hsv_threshold_saturation = [0.0, 255.0]
        self.__hsv_threshold_value = [41.384942893143105, 255.0]

        self.hsv_threshold_output = None

        self.__cv_erode_src = self.hsv_threshold_output
        self.__cv_erode_kernel = None
        self.__cv_erode_anchor = (-1, -1)
        self.__cv_erode_iterations = 2.0
        self.__cv_erode_bordertype = cv2.BORDER_CONSTANT
        self.__cv_erode_bordervalue = (-1)

        self.cv_erode_output = None

        self.__cv_dilate_src = self.cv_erode_output
        self.__cv_dilate_kernel = None
        self.__cv_dilate_anchor = (-1, -1)
        self.__cv_dilate_iterations = 1.0
        self.__cv_dilate_bordertype = cv2.BORDER_CONSTANT
        self.__cv_dilate_bordervalue = (-1)

        self.cv_dilate_output = None

        self.__find_contours_input = self.cv_dilate_output
        self.__find_contours_external_only = True

        self.find_contours_output = None

        self.__filter_contours_contours = self.find_contours_output
        self.__filter_contours_min_area = 25.0
        self.__filter_contours_min_perimeter = 0.0
        self.__filter_contours_min_width = 0.0
        self.__filter_contours_max_width = 1000.0
        self.__filter_contours_min_height = 0.0
        self.__filter_contours_max_height = 1000.0
        self.__filter_contours_solidity = [0.0, 100]
        self.__filter_contours_max_vertices = 1000000.0
        self.__filter_contours_min_vertices = 0.0
        self.__filter_contours_min_ratio = 0.3
        self.__filter_contours_max_ratio = 1.0

        self.filter_contours_output = None
        #END CONSTANTS
        
    # ###################################################################################################
    ## Process function with USB output
    def process(self, inframe, outframe):
        # Get the next camera image (may block until it is captured) and here convert it to OpenCV BGR by default. If
        # you need a grayscale image instead, just use getCvGRAY() instead of getCvBGR(). Also supported are getCvRGB()
        # and getCvRGBA():
        source0 = inimg = inframe.getCvBGR()
        outimg = inimg = inframe.getCvBGR()
        
        # Start measuring image processing time (NOTE: does not account for input conversion time):
        self.timer.start()

##############################################################################################
        """
        Runs the pipeline and sets all outputs to new values.
        """
        # Step Blur0:
        self.__blur_input = source0
        (self.blur_output) = self.__blur(self.__blur_input, self.__blur_type, self.__blur_radius)

        # Step CV_extractChannel0:
        self.__cv_extractchannel_src = self.blur_output
        (self.cv_extractchannel_output) = self.__cv_extractchannel(self.__cv_extractchannel_src, self.__cv_extractchannel_channel)

        # Step CV_Threshold0:
        self.__cv_threshold_src = self.cv_extractchannel_output
        (self.cv_threshold_output) = self.__cv_threshold(self.__cv_threshold_src, self.__cv_threshold_thresh, self.__cv_threshold_maxval, self.__cv_threshold_type)

        # Step Mask0:
        self.__mask_input = self.blur_output
        self.__mask_mask = self.cv_threshold_output
        (self.mask_output) = self.__mask(self.__mask_input, self.__mask_mask)

        # Step Normalize0:
        self.__normalize_input = self.mask_output
        (self.normalize_output) = self.__normalize(self.__normalize_input, self.__normalize_type, self.__normalize_alpha, self.__normalize_beta)

        # Step HSV_Threshold0:
        self.__hsv_threshold_input = self.normalize_output
        (self.hsv_threshold_output) = self.__hsv_threshold(self.__hsv_threshold_input, self.__hsv_threshold_hue, self.__hsv_threshold_saturation, self.__hsv_threshold_value)

        # Step CV_erode0:
        self.__cv_erode_src = self.hsv_threshold_output
        (self.cv_erode_output) = self.__cv_erode(self.__cv_erode_src, self.__cv_erode_kernel, self.__cv_erode_anchor, self.__cv_erode_iterations, self.__cv_erode_bordertype, self.__cv_erode_bordervalue)

        # Step CV_dilate0:
        self.__cv_dilate_src = self.cv_erode_output
        (self.cv_dilate_output) = self.__cv_dilate(self.__cv_dilate_src, self.__cv_dilate_kernel, self.__cv_dilate_anchor, self.__cv_dilate_iterations, self.__cv_dilate_bordertype, self.__cv_dilate_bordervalue)

        # Step Find_Contours0:
        self.__find_contours_input = self.cv_dilate_output
        (self.find_contours_output) = self.__find_contours(self.__find_contours_input, self.__find_contours_external_only)

        # Step Filter_Contours0:
        self.__filter_contours_contours = self.find_contours_output
        (self.filter_contours_output) = self.__filter_contours(self.__filter_contours_contours, self.__filter_contours_min_area, self.__filter_contours_min_perimeter, self.__filter_contours_min_width, self.__filter_contours_max_width, self.__filter_contours_min_height, self.__filter_contours_max_height, self.__filter_contours_solidity, self.__filter_contours_max_vertices, self.__filter_contours_min_vertices, self.__filter_contours_min_ratio, self.__filter_contours_max_ratio)

#################################################################################################
        #END GRIP CODE

##################################################################################################
        #PUT CUSTOM CODE HERE

        def getArea(con): #Gets the area of the contour
            return cv2.contourArea(con)

        def getYcoord(con): #Gets the Y coordinate of the contour
            M = cv2.moments(con)
            cy = int(M['m01']/M['m00'])
            return cy

        def findClosestY(conts): #Finds the contours that are closest in their Y coordinates and have reasonably close area
            contourNum = len(conts) #Gets number of contours
            sortedBy = sorted(conts, key=getYcoord) #sortedBy now has all the contours sorted by y-coordinate
            delta = []
            index = 1
            for i in range(1, contourNum): #for loop through all the contours
                delta.append(getYcoord(sortedBy[i]) - getYcoord(sortedBy[i-1])) #Find the difference in ycoord
                if i > 1:
                    #if delta is smaller than the last delta (closer ycoord) and areas are within 1/0.3 of each other
                    if (delta[i-1] < delta[i-2]) and abs(getArea(sortedBy[i]) - getArea(sortedBy[i-1]) < getArea(sortedBy[i])*0.3): 
                        index = i #store the index
            newContours = [conts[index], conts[index-1]] #make a new array of contours
            return newContours

        def findLargestArea(conts): #Finds the contours with the largest area
            contourNum = len(conts) #Gets number of contours
            sortedBy = sorted(conts, key=getArea) #sortedBy now has all the contours sorted by area
            if contourNum >= 2: #if there are 2 or more contours
                newContours = [sortedBy[contourNum-1], sortedBy[contourNum-2]] #make a new array of contours
            else:
                newContours = sortedBy
            return newContours

        #cv2.drawContours(outimg, self.filter_contours_output, -1, (255, 0, 0), 1) #Draws all contours on original image in blue
                               
        contourNum = len(self.filter_contours_output) #Gets number of contours
        if contourNum > 1: #if more than a single contour
            newContours = findLargestArea(self.filter_contours_output) #find 2 largest areas
            cv2.drawContours(outimg, newContours, -1, (0, 0, 255), 1) #Draw the two contours closest in ycoord in red
                
        elif contourNum == 1:
            cv2.drawContours(outimg, self.filter_contours_output, -1, (0, 0, 255), 1) #Draw the contour in red            
        
                
        #jevois.sendSerial("DONE frame {}".format(self.frame))
######################### ########################################################################
        #END CUSTOM CODE
        
        # Write a title:
        cv2.putText(outimg, "Anand's JeVois Code", (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),
                    1, cv2.LINE_AA)
        
        # Write frames/s info from our timer into the edge map (NOTE: does not account for output conversion time):
        fps = self.timer.stop()
        #height, width, channels = outimg.shape # if outimg is grayscale, change to: height, width = outimg.shape
        height, width, channels = outimg.shape
        cv2.putText(outimg, fps, (3, height - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

        # Convert our BGR output image to video output format and send to host over USB. If your output image is not
        # BGR, you can use sendCvGRAY(), sendCvRGB(), or sendCvRGBA() as appropriate:
        outframe.sendCvBGR(outimg)
        #outframe.sendCvGRAY(outimg)

###################################################################################################
        #FUNCTIONS GO HERE (Anything that starts with "@staticmethod")
        
    @staticmethod
    def __blur(src, type, radius):
        """Softens an image using one of several filters.
        Args:
            src: The source mat (numpy.ndarray).
            type: The blurType to perform represented as an int.
            radius: The radius for the blur as a float.
        Returns:
            A numpy.ndarray that has been blurred.
        """
        ksize = int(2 * round(radius) + 1)
        return cv2.blur(src, (ksize, ksize))


    @staticmethod
    def __cv_extractchannel(src, channel):
        """Extracts given channel from an image.
        Args:
            src: A numpy.ndarray.
            channel: Zero indexed channel number to extract.
        Returns:
             The result as a numpy.ndarray.
        """
        return cv2.extractChannel(src, (int) (channel + 0.5))

    @staticmethod
    def __cv_threshold(src, thresh, max_val, type):
        """Apply a fixed-level threshold to each array element in an image
        Args:
            src: A numpy.ndarray.
            thresh: Threshold value.
            max_val: Maximum value for THRES_BINARY and THRES_BINARY_INV.
            type: Opencv enum.
        Returns:
            A black and white numpy.ndarray.
        """
        return cv2.threshold(src, thresh, max_val, type)[1]

    @staticmethod
    def __mask(input, mask):
        """Filter out an area of an image using a binary mask.
        Args:
            input: A three channel numpy.ndarray.
            mask: A black and white numpy.ndarray.
        Returns:
            A three channel numpy.ndarray.
        """
        return cv2.bitwise_and(input, input, mask=mask)

    @staticmethod
    def __normalize(input, type, a, b):
        """Normalizes or remaps the values of pixels in an image.
        Args:
            input: A numpy.ndarray.
            type: Opencv enum.
            a: The minimum value.
            b: The maximum value.
        Returns:
            A numpy.ndarray of the same type as the input.
        """
        return cv2.normalize(input, None, a, b, type)

    @staticmethod
    def __hsv_threshold(input, hue, sat, val):
        """Segment an image based on hue, saturation, and value ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max value.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
        return cv2.inRange(out, (hue[0], sat[0], val[0]),  (hue[1], sat[1], val[1]))

    @staticmethod
    def __cv_erode(src, kernel, anchor, iterations, border_type, border_value):
        """Expands area of lower value in an image.
        Args:
           src: A numpy.ndarray.
           kernel: The kernel for erosion. A numpy.ndarray.
           iterations: the number of times to erode.
           border_type: Opencv enum that represents a border type.
           border_value: value to be used for a constant border.
        Returns:
            A numpy.ndarray after erosion.
        """
        return cv2.erode(src, kernel, anchor, iterations = (int) (iterations +0.5),
                            borderType = border_type, borderValue = border_value)

    @staticmethod
    def __cv_dilate(src, kernel, anchor, iterations, border_type, border_value):
        """Expands area of higher value in an image.
        Args:
           src: A numpy.ndarray.
           kernel: The kernel for dilation. A numpy.ndarray.
           iterations: the number of times to dilate.
           border_type: Opencv enum that represents a border type.
           border_value: value to be used for a constant border.
        Returns:
            A numpy.ndarray after dilation.
        """
        return cv2.dilate(src, kernel, anchor, iterations = (int) (iterations +0.5),
                            borderType = border_type, borderValue = border_value)

    @staticmethod
    def __find_contours(input, external_only):
        """Sets the values of pixels in a binary image to their distance to the nearest black pixel.
        Args:
            input: A numpy.ndarray.
            external_only: A boolean. If true only external contours are found.
        Return:
            A list of numpy.ndarray where each one represents a contour.
        """
        if(external_only):
            mode = cv2.RETR_EXTERNAL
        else:
            mode = cv2.RETR_LIST
        method = cv2.CHAIN_APPROX_SIMPLE
        im2, contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        return contours

    @staticmethod
    def __filter_contours(input_contours, min_area, min_perimeter, min_width, max_width,
                        min_height, max_height, solidity, max_vertex_count, min_vertex_count,
                        min_ratio, max_ratio):
        """Filters out contours that do not meet certain criteria.
        Args:
            input_contours: Contours as a list of numpy.ndarray.
            min_area: The minimum area of a contour that will be kept.
            min_perimeter: The minimum perimeter of a contour that will be kept.
            min_width: Minimum width of a contour.
            max_width: MaxWidth maximum width.
            min_height: Minimum height.
            max_height: Maximimum height.
            solidity: The minimum and maximum solidity of a contour.
            min_vertex_count: Minimum vertex Count of the contours.
            max_vertex_count: Maximum vertex Count.
            min_ratio: Minimum ratio of width to height.
            max_ratio: Maximum ratio of width to height.
        Returns:
            Contours as a list of numpy.ndarray.
        """
        output = []
        for contour in input_contours:
            x,y,w,h = cv2.boundingRect(contour)
            if (w < min_width or w > max_width):
                continue
            if (h < min_height or h > max_height):
                continue
            area = cv2.contourArea(contour)
            if (area < min_area):
                continue
            if (cv2.arcLength(contour, True) < min_perimeter):
                continue
            hull = cv2.convexHull(contour)
            solid = 100 * area / cv2.contourArea(hull)
            if (solid < solidity[0] or solid > solidity[1]):
                continue
            if (len(contour) < min_vertex_count or len(contour) > max_vertex_count):
                continue
            ratio = (float)(w) / h
            if (ratio < min_ratio or ratio > max_ratio):
                continue
            output.append(contour)
        return output


#BlurType = Enum('BlurType', 'Box_Blur Gaussian_Blur Median_Filter Bilateral_Filter')

