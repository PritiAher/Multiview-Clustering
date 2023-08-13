
import os
import random
import cv2
import NMF
import TrainedWeightFusion
import Fuzzy
import collections
import matplotlib.pyplot as plt
import operator
import gradio as gr
import gradio.components

target_folder = "INPUT IMAGES//INPUT"



def multiview_clustering(inp1, inp2):
    inputdatapath = "INPUT IMAGES//INPUT"
    outputfolder = "MULTI-VIEW CLUSTER RESULTS"

    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    dir_list = os.listdir(inputdatapath)
    noi = len(dir_list)
    rangefactor = int(noi / 2)
    print("Range Factor ", rangefactor)

    clusterlist = []
    label1 = ""
    label2 = ""

    for i in range(rangefactor):
        current_images = 2
        print("Remaining_images: ", current_images)

        while True:
            ran_img1 = random.randint(0, (current_images - 1))
            imagename1 = dir_list[ran_img1]
            imgpath1 = inputdatapath + "//" + imagename1

            ran_img2 = random.randint(0, (current_images - 1))
            imagename2 = dir_list[ran_img2]
            imgpath2 = inputdatapath + "//" + imagename2

            if imgpath1 != imgpath2:
                optimage1 = "Optimized1.jpg"
                val1 = NMF.formNMFParameterOptimzedImage(imgpath1, optimage1, imgpath2)
                optimage2 = "Optimized2.jpg"
                val2 = NMF.formNMFParameterOptimzedImage(imgpath2, optimage2, imgpath1)

                if val1 == 1 and val2 == 1:
                    index1 = TrainedWeightFusion.getFusionScore(optimage1)
                    index2 = TrainedWeightFusion.getFusionScore(optimage2)
                    stageclustername1 = Fuzzy.getStage(index1)
                    clusterlist.append(stageclustername1)

                    stageclustername2 = Fuzzy.getStage(index2)
                    clusterlist.append(stageclustername2)

                    os.remove(optimage1)
                    os.remove(optimage2)
                    dir_list.remove(imagename1)
                    dir_list.remove(imagename2)

                    label1 = stageclustername1
                    label2 = stageclustername2
                    
                  
                
                

                break

        print("\n----------------------------------------\n")

    frequency = collections.Counter(clusterlist)
    stagefreq = dict(frequency)
    sorted_d = sorted(stagefreq.items(), key=operator.itemgetter(1))

    names = list(stagefreq.keys())
    values = list(stagefreq.values())

    plt.bar(range(len(stagefreq)), values, tick_label=names)
    plt.show()

    return label1, label2


def image_clustering_interface(image1, image2):
    # Save the uploaded images to the target folder
    image1_path = os.path.join(target_folder, "image1.jpg")
    image2_path = os.path.join(target_folder, "image2.jpg")
    cv2.imwrite(image1_path, image1)
    cv2.imwrite(image2_path, image2)

    # Perform multiview clustering and obtain the labels
    label1, label2 = multiview_clustering(image1_path, image2_path)

    # Create the Gradio output components with dynamic labels
    output_label1 = gr.components.Label(label=label1)
    output_label2 = gr.components.Label(label=label2)

    return [label1, label2]




iface = gr.Interface(
    fn=image_clustering_interface,
    inputs=[
        gr.components.Image(label="Image 1", description="Upload the first image"),
        gr.components.Image(label="Image 2",  description="Upload the second image"),
    ],
    outputs=[
        gr.components.Label(label="First Image Stage"),
        gr.components.Label(label="Second Image Stage")
    ],
)

iface.launch()
