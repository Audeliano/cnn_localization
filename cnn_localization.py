#!/usr/bin/env python
'''cnn_localization ROS Node'''
# license removed for brevity
import os
import cv2
import sys
import rospy
from std_msgs.msg import String
from std_srvs.srv import *

def teste_imagem_label(imagem):
    #rospy.wait_for_service('find_possible_areas')
    #try:
        #COLOCAR GMAPPING PARA EXTRAIR LOCAL_MAP (COMANDO 1 E 3)
        #SALVAR O MAP (COMANDO 2)
        #USAR O COMANDO ARQUIVO PARA CLASSIFICAR A IMAGEM
        #COM A IMAGEM CLASSICADA, TRATAR O VALOR (DIVIDIR POR 1000 E POR 100 = X; POR 10 E POR 1 = Y)
        #PEGAR VALOR DE X E Y E PUBLICAR NO TÓPICO "initialpose (geometry_msgs/PoseWithCovarianceStamped)"
        
 
        endereco_atual = os.getcwd()
        print endereco_atual
        os.chdir('/home/au16/Code/rgbdslam_catkin_ws/src/cnn_localization' + '/tensorflow-for-poets-2/')
        arquivo = 'python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=tf_files/' + str(imagem) +'.jpg'
        print arquivo

        comando1 = 'rosparam set use_sim_time false'
        comando2 = 'rosrun map_server map_saver -f /home/au16/Code/rgbdslam_catkin_ws/src/cnn_localization/tensorflow-for-poets-2/tf_files/local_maps/local_map'
        comando3 = 'rosrun gmapping slam_gmapping scan:=base_scan _odom_frame:=odom_combined'
        
        
        #os.system(arquivo)
        return EmptyResponse()

def service_function():
    rospy.init_node('cnn_localization_server')
    s = rospy.Service('activateKidnapping', Empty, teste_imagem_label)
    print ("SERVICO!!!!!!!!")
    rospy.spin()
    

if __name__ == '__main__':
    service_function()

    endereco_atual = os.getcwd()
    print endereco_atual
    print os.path.dirname(os.path.realpath(__file__))
    print (os.path.dirname(os.path.realpath(__file__))+"/tratandoImagens")

    os.chdir('/home/au16/Code/rgbdslam_catkin_ws/src/cnn_localization' + '/tensorflow-for-poets-2/tf_files/')
    asdf = 'local_maps/local_map'
    #teste_imagem_label(asdf)
       


