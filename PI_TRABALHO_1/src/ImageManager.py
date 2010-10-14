'''
Created on 17/08/2010

@author: matheus
'''
#Bibliotecas necessarias
from __future__ import division
from math import sqrt
import Image
import CairoPlot

#Classe que implementa todos os algoritmo des Gerenciamento de Imagens
class ImageManager():
    
    
    
    #Construtor da classe ImageManager
    def __init__(self):
        pass



    #Metodo que gera outra imagem em escala de cinza
    def escala_cinza(self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
                
            #Percorre todos os pixels da imagem efetuando a media entre os valores RGB
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x, y))
                    media = int((pixel[0] + pixel[1] + pixel[2]) / 3)
                    img_result.putpixel((x, y), (media, media, media))
        #Caso a imagem nao tenha RGB
        except TypeError :
            img_result = img
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_escala_cinza.png")



    #Metodo que gera um histograma referente a uma imagem em escala de cinza
    def histograma_escala_cinza (self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        
        #Inicializa arrays de 256 posicoes para contagem de cores e para cores do grafico
        escala_cinza = []
        colors = []
        for x in range(256):
            escala_cinza.append(0)
            colors.append((0, 0, 0))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    escala_cinza[pixel[0]] += 1
        #Caso a imagem nao tenha RGB
        except TypeError :
            #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    escala_cinza[pixel] += 1
        
        #Plotagem do grafico
        h_labels = ["10", "40", "70", "100", "130", "160", "190", "220", "250"]
        CairoPlot.bar_plot("../img/histograma_escala_cinza.png", escala_cinza, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors)



    #Metodo que gera tres histogramas referente a imagem com rgb
    def histograma_rgb (self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        
        #Inicializa arrays de 256 posicoes para contagem de cores e para cores do grafico
        red = []
        green = []
        blue = []
        colors_red = []
        colors_green = []
        colors_blue = []
        for x in range(256):
            red.append(0)
            green.append(0)
            blue.append(0)
            colors_red.append((1, 0, 0))
            colors_green.append((0, 1, 0))
            colors_blue.append((0, 0, 1))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    red[pixel[0]] += 1
                    green[pixel[1]] += 1
                    blue[pixel[2]] += 1
        #Caso a imagem nao tenha RGB
        except TypeError :
            #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    red[pixel] += 1
                    green[pixel] += 1
                    blue[pixel] += 1
        
        #Plotagem do grafico
        h_labels = ["10", "40", "70", "100", "130", "160", "190", "220", "250"]
        CairoPlot.bar_plot("../img/histograma_red.png", red, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_red)
        CairoPlot.bar_plot("../img/histograma_green.png", green, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_green)
        CairoPlot.bar_plot("../img/histograma_blue.png", blue, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_blue)
   
   

    #Metodo que efetua a limiarizacao global simples    
    def limiarizacao_global_simples(self, file_path, limiar_t):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre todos os pixels da imagem e compara com o limiar t
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    if (img.getpixel((x,y))[0] > int(limiar_t)):
                        valor = 0
                    else:
                        valor = 255
                    img_result.putpixel((x,y), (valor, valor, valor))
        except TypeError :
            #Caso a imagem nao tenha RGB
            #Percorre todos os pixels da imagem e compara com o limiar t
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    if (img.getpixel((x,y)) > int(limiar_t)):
                        valor = 0
                    else:
                        valor = 255
                    img_result.putpixel((x,y), valor, valor, valor)
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_limiarizacao.png")
    
    
    
    #Metodo que efetua a limiarizacao baseado em diversas varias
    def limiarizacao_diversas_variaveis(self, file_path, limiar_t, valor_rgb):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = img.copy()
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #Percorre todos os pixels da imagem e compara com o limiar T utilizando distancia euclidiana
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    #Calculo da distancia euclidiana
                    distancia = sqrt(pow(valor_rgb[0] - pixel[0], 2) + 
                                     pow(valor_rgb[1] - pixel[1], 2) +
                                     pow(valor_rgb[2] - pixel[2], 2))
                    if (distancia > limiar_t):
                        img_result.putpixel((x,y), (0, 0, 0))
        
        #Caso a imagem nao tenha RGB, nao se pode fazer diversas variaveis, pois deve ser uma imagem colorida            
        except TypeError :
            pass
        
        img_result.save("../img/modificada_limiarizacao.png")
    
    
    
    #Metodo que efetua a operacao aritmetica ADICAO entre duas imagens gerando uma terceira imagem com reescalonamento
    def operacao_aritmetica_adicao_reescalonamento(self, file_path1, file_path2):
        #Efetua o load das imagens passadas os caminhos como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()
        
        #Verifica o menor tamanho das imagens em X e Y
        #img[0] X e img[1] Y
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
        
        #Instancia nova variavel imagem com o tamanho X e Y
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #Percorre todos os pixels das imagens efetuando a soma dos valores e reescalonando
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    pixel1 = img1.getpixel((x,y))
                    pixel2 = img2.getpixel((x,y))
                    
                    valor_r = pixel1[0] + pixel2[0]
                    valor_g = pixel1[1] + pixel2[1]
                    valor_b = pixel1[2] + pixel2[2]
                    
                    #Reescalonamento de valores
                    valor_r = self.reescalonamento_de_valores(valor_r, 510, 0)
                    valor_g = self.reescalonamento_de_valores(valor_g, 510, 0)
                    valor_b = self.reescalonamento_de_valores(valor_b, 510, 0)
                    
                    img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
        
        #Caso no minimo uma das imagens nao tenha RGB
        except TypeError :
            try :
                #Verifica se a imagem1 tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #Caso a imagem2 nao tenha valores RGB
                #Percorre todos os pixels das imagens efetuando a soma dos valores e reescalonando
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        pixel1 = img1.getpixel((x,y))
                        pixel2 = img2.getpixel((x,y))
                        
                        valor_r = pixel1[0] + pixel2
                        valor_g = pixel1[1] + pixel2
                        valor_b = pixel1[2] + pixel2
                        
                        #Reescalonamento de valores
                        valor_r = self.reescalonamento_de_valores(valor_r, 510, 0)
                        valor_g = self.reescalonamento_de_valores(valor_g, 510, 0)
                        valor_b = self.reescalonamento_de_valores(valor_b, 510, 0)
                        
                        img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
            
            #Caso no minimo uma das imagens nao tenha RGB
            except TypeError :
                try :
                    #Verifica se a imagem2 tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #Caso a imagem1 nao tenha valores RGB
                    #Percorre todos os pixels das imagens efetuando a soma dos valores e reescalonando
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor_r = pixel1 + pixel2[0]
                            valor_g = pixel1 + pixel2[1]
                            valor_b = pixel1 + pixel2[2]
                            
                            #Reescalonamento de valores
                            valor_r = self.reescalonamento_de_valores(valor_r, 510, 0)
                            valor_g = self.reescalonamento_de_valores(valor_g, 510, 0)
                            valor_b = self.reescalonamento_de_valores(valor_b, 510, 0)
                            
                            img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
                
                #Caso nenhuma das imagens tenha valores RGB
                except TypeError :
                    #Percorre todos os pixels das imagens efetuando a soma dos valores e reescalonando
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 + pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 510, 0)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))
                                
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
    #Metodo que efetua a operacao aritmetica ADICAO entre duas imagens gerando uma terceira imagem com truncamento
    def operacao_aritmetica_adicao_truncamento(self, file_path1, file_path2):
        #Efetua o load das imagens passadas os caminhos como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()
        
        #Verifica o menor tamanho das imagens em X e Y
        #img[0] X e img[1] Y
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
        
        #Instancia nova variavel imagem com o tamanho X e Y
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #Percorre todos os pixels das imagens efetuando a soma dos valores e efetua truncamento de valores
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    pixel1 = img1.getpixel((x,y))
                    pixel2 = img2.getpixel((x,y))
                    
                    valor_r = pixel1[0] + pixel2[0]
                    valor_g = pixel1[1] + pixel2[1]
                    valor_b = pixel1[2] + pixel2[2]
                    
                    #Trucamento de valores
                    if (valor_r > 255) :
                        valor_r = 255
                    elif (valor_r < 0) :
                        valor_r = 0
                    if (valor_g > 255) :
                        valor_g = 255
                    elif (valor_g < 0) :
                        valor_g = 0
                    if (valor_b > 255) :
                        valor_b = 255
                    elif (valor_b < 0) :
                        valor_b = 0
                    
                    img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
        
        #Caso no minimo uma das imagens nao tenha RGB
        except TypeError :
            try :
                #Verifica se a imagem1 tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #Caso a imagem2 nao tenha valores RGB
                #Percorre todos os pixels das imagens efetuando a soma dos valores e efetua truncamento de valores
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        pixel1 = img1.getpixel((x,y))
                        pixel2 = img2.getpixel((x,y))
                        
                        valor_r = pixel1[0] + pixel2
                        valor_g = pixel1[1] + pixel2
                        valor_b = pixel1[2] + pixel2
                        
                        #Trucamento de valores
                        if (valor_r > 255) :
                            valor_r = 255
                        elif (valor_r < 0) :
                            valor_r = 0
                        if (valor_g > 255) :
                            valor_g = 255
                        elif (valor_g < 0) :
                            valor_g = 0
                        if (valor_b > 255) :
                            valor_b = 255
                        elif (valor_b < 0) :
                            valor_b = 0
                        
                        img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
            
            #Caso no minimo uma das imagens nao tenha RGB
            except TypeError :
                try :
                    #Verifica se a imagem2 tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #Caso a imagem1 nao tenha valores RGB
                    #Percorre todos os pixels das imagens efetuando a soma dos valores e efetua truncamento de valores
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor_r = pixel1 + pixel2[0]
                            valor_g = pixel1 + pixel2[1]
                            valor_b = pixel1 + pixel2[2]
                            
                            #Trucamento de valores
                            if (valor_r > 255) :
                                valor_r = 255
                            elif (valor_r < 0) :
                                valor_r = 0
                            if (valor_g > 255) :
                                valor_g = 255
                            elif (valor_g < 0) :
                                valor_g = 0
                            if (valor_b > 255) :
                                valor_b = 255
                            elif (valor_b < 0) :
                                valor_b = 0
                            
                            img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
                
                #Caso nenhuma das imagens tenha valores RGB
                except TypeError :
                    #Percorre todos os pixels das imagens efetuando a soma dos valores e efetua truncamento de valores
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 + pixel2
                            
                            #Trucamento de valores
                            if (valor > 255) :
                                valor = 255
                            elif (valor < 0) :
                                valor = 0
                            
                            img_result.putpixel((x,y), (valor, valor, valor))
                                
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_aritmetica.png")
        
        
        
    #Metodo que efetua a operacao aritmetica SUBTRACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_subtracao(self, file_path1, file_path2):
        #Efetua o load das imagens passadas os caminhos como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()
        
        #Verifica o tamanho menor das imagens em x e em y
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
        
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    pixel1 = img1.getpixel((x,y))
                    pixel2 = img2.getpixel((x,y))
                    
                    valor_r = pixel1[0] - pixel2[0]
                    valor_g = pixel1[1] - pixel2[1]
                    valor_b = pixel1[2] - pixel2[2]
                    
                    #Reescalonamento de valores
                    valor_r = self.reescalonamento_de_valores(valor_r, 255, -255)
                    valor_g = self.reescalonamento_de_valores(valor_g, 255, -255)
                    valor_b = self.reescalonamento_de_valores(valor_b, 255, -255)
                    
                    img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
        except TypeError :
            #Caso no minimo uma das imagens nao tenha RGB
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        pixel1 = img1.getpixel((x,y))
                        pixel2 = img2.getpixel((x,y))
                        
                        valor_r = pixel1[0] - pixel2
                        valor_g = pixel1[1] - pixel2
                        valor_b = pixel1[2] - pixel2
                        
                        #Reescalonamento de valores
                        valor_r = self.reescalonamento_de_valores(valor_r, 255, -255)
                        valor_g = self.reescalonamento_de_valores(valor_g, 255, -255)
                        valor_b = self.reescalonamento_de_valores(valor_b, 255, -255)
                        
                        img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
            except TypeError :
                #Caso no minimo uma das imagens nao tenha RGB
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor_r = pixel1 - pixel2[0]
                            valor_g = pixel1 - pixel2[1]
                            valor_b = pixel1 - pixel2[2]
                            
                            #Reescalonamento de valores
                            valor_r = self.reescalonamento_de_valores(valor_r, 255, -255)
                            valor_g = self.reescalonamento_de_valores(valor_g, 255, -255)
                            valor_b = self.reescalonamento_de_valores(valor_b, 255, -255)
                            
                            img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
                except TypeError :
                    #Caso no minimo de as duas nao terem vao RGB
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 - pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 255, -255)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
    #Metodo que efetua a operacao aritmetica MULTIPLICACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_multiplicacao(self, file_path1, file_path2):
        #Efetua o load das imagens passadas os caminhos como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()
        
        #Verifica o tamanho menor das imagens em x e em y
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
        
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    pixel1 = img1.getpixel((x,y))
                    pixel2 = img2.getpixel((x,y))
                    
                    valor_r = pixel1[0] * pixel2[0]
                    valor_g = pixel1[1] * pixel2[1]
                    valor_b = pixel1[2] * pixel2[2]
                    
                    #Reescalonamento de valores
                    valor_r = self.reescalonamento_de_valores(valor_r, 65025, 0)
                    valor_g = self.reescalonamento_de_valores(valor_g, 65025, 0)
                    valor_b = self.reescalonamento_de_valores(valor_b, 65025, 0)
                    
                    img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
        except TypeError :
            #Caso no minimo uma das imagens nao tenha RGB
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        pixel1 = img1.getpixel((x,y))
                        pixel2 = img2.getpixel((x,y))
                        
                        valor_r = pixel1[0] * pixel2
                        valor_g = pixel1[1] * pixel2
                        valor_b = pixel1[2] * pixel2
                        
                        #Reescalonamento de valores
                        valor_r = self.reescalonamento_de_valores(valor_r, 65025, 0)
                        valor_g = self.reescalonamento_de_valores(valor_g, 65025, 0)
                        valor_b = self.reescalonamento_de_valores(valor_b, 65025, 0)
                        
                        img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
            except TypeError :
                #Caso no minimo uma das imagens nao tenha RGB
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor_r = pixel1 * pixel2[0]
                            valor_g = pixel1 * pixel2[1]
                            valor_b = pixel1 * pixel2[2]
                            
                            #Reescalonamento de valores
                            valor_r = self.reescalonamento_de_valores(valor_r, 65025, 0)
                            valor_g = self.reescalonamento_de_valores(valor_g, 65025, 0)
                            valor_b = self.reescalonamento_de_valores(valor_b, 65025, 0)
                            
                            img_result.putpixel((x,y), (valor_r, valor_g, valor_b))
                except TypeError :
                    #Caso no minimo de as duas nao terem vao RGB
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 * pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 65025, 0)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))

        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
    #Metodo que efetua o reescalonamento de valores para a escala 0 a 255 do rgb
    def reescalonamento_de_valores(self, valor, tmax, tmin):
        return int((255 / (tmax - tmin)) * (valor - tmin))
    
    
    
    #Metodo que efetua a operacao logica AND entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_and(self, file_path1, file_path2):
        #Efetua o load da imagem passada o caminho como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e comparando,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == 255 and img2.getpixel((x,y))[0] == 255):
                        valor = 255
                    else :
                        valor = 0
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except TypeError :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == 255 and img2.getpixel((x,y)) == 255):
                            valor = 255
                        else :
                            valor = 0
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except TypeError :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 255 and img2.getpixel((x,y))[0] == 255):
                                valor = 255
                            else :
                                valor = 0
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except TypeError :
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 255 and img2.getpixel((x,y)) == 255):
                                valor = 255
                            else :
                                valor = 0
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
    
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_logica.png")
    
    
    
    #Metodo que efetua a operacao logica OR entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_or(self, file_path1, file_path2):
        #Efetua o load das imagens passadas os caminhos como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e comparando,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == 0 and img2.getpixel((x,y))[0] == 0):
                        valor = 0
                    else :
                        valor = 255
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except TypeError :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == 0 and img2.getpixel((x,y)) == 0):
                            valor = 0
                        else :
                            valor = 255
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except TypeError :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 0 and img2.getpixel((x,y))[0] == 0):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except TypeError :
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 0 and img2.getpixel((x,y)) == 0):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_logica.png")
    
    
    
    #Metodo que efetua a operacao logica XOR entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_xor(self, file_path1, file_path2):
        #Efetua o load da imagem passada o caminho como parametro
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e comparando,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            #img[0] X e img[1] Y
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == img2.getpixel((x,y))[0]):
                        valor = 0
                    else :
                        valor = 255
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except TypeError :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                #img[0] X e img[1] Y
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == img2.getpixel((x,y))):
                            valor = 0
                        else :
                            valor = 255
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except TypeError :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == img2.getpixel((x,y))[0]):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except TypeError :
                    #img[0] X e img[1] Y
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == img2.getpixel((x,y))):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
    
        #Salva a imagem resultante
        img_result.save("../img/modificada_operacao_logica.png")
        
        
        
    #Metodo que gera outra imagem filtrado com passa alta basico
    def filtro_passa_alta_basico(self, file_path, tamanho_matriz):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa a matriz (mascara)
        matriz = []
        for i in range(tamanho_matriz):
            matriz.append([])
            for j in range(tamanho_matriz):
                matriz[i].append(-1)
        #Inicializa variaveis necessarias para a manipulacao do matriz (mascara)
        variacao = int(tamanho_matriz / 2)
        divisor = tamanho_matriz * tamanho_matriz
        matriz[variacao][variacao] = divisor - 1
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r = 0
                    somador_g = 0
                    somador_b = 0
                    
                    #Percorre a matriz (mascara) fazendo a multiplicacao dos valores com os valores da imagem 
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r += pixel[0] * matriz[x + variacao][y + variacao]
                            somador_g += pixel[1] * matriz[x + variacao][y + variacao]
                            somador_b += pixel[2] * matriz[x + variacao][y + variacao]
                    
                    somador_r = int(somador_r/divisor)
                    somador_g = int(somador_g/divisor)
                    somador_b = int(somador_b/divisor)
                    
                    #Trucamento de valores
                    if (somador_r < 0) :
                        somador_r = 0
                    elif (somador_r > 255) :
                        somador_r = 255
                            
                    if (somador_g < 0) :
                        somador_g = 0
                    elif (somador_g > 255) :
                        somador_g = 255
    
                    if (somador_b < 0) :
                        somador_b = 0
                    elif (somador_b > 255) :
                        somador_b = 255
                    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
        
        #Caso a imagem nao possua RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador = 0
                    
                    #Percorre a matriz (mascara) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador += pixel * matriz[x + variacao][y + variacao]
                    
                    somador = int(somador/divisor)
                    
                    #Trucamento de valores
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com a media
    def filtro_media(self, file_path, tamanho_matriz):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa a matriz
        matriz = []
        for i in range(tamanho_matriz):
            matriz.append([])
            for j in range(tamanho_matriz):
                matriz[i].append(1)
        #Inicializa variaveis necessarias para a manipulacao do matriz (mascara)
        variacao = int(tamanho_matriz / 2)
        divisor = tamanho_matriz * tamanho_matriz
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r = 0
                    somador_g = 0
                    somador_b = 0
                    
                    #Percorre a matriz (mascara) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r += pixel[0] * matriz[x + variacao][y + variacao]
                            somador_g += pixel[1] * matriz[x + variacao][y + variacao]
                            somador_b += pixel[2] * matriz[x + variacao][y + variacao]
                    
                    somador_r = int(somador_r/divisor)
                    somador_g = int(somador_g/divisor)
                    somador_b = int(somador_b/divisor)
                    
                    #Truncamento de valores
                    if (somador_r < 0) :
                        somador_r = 0
                    elif (somador_r > 255) :
                        somador_r = 255
                            
                    if (somador_g < 0) :
                        somador_g = 0
                    elif (somador_g > 255) :
                        somador_g = 255
    
                    if (somador_b < 0) :
                        somador_b = 0
                    elif (somador_b > 255) :
                        somador_b = 255
    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
        #Caso a imagem nao tenha RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador = 0
                    #Percorre a matriz (mascara) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador += pixel * matriz[x + variacao][y + variacao]
                    
                    somador = int(somador/divisor)
                    
                    #Truncamento de valores
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com mediana
    def filtro_mediana(self, file_path, tamanho_matriz):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        #Inicializa variaveis necessarias para a manipulacao da mascara
        variacao = int(tamanho_matriz / 2)
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    valores_r = []
                    valores_g = []
                    valores_b = []
                    
                    #Percorre a imagem adicionando nas litas os valores pertencentes a mascara
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                valores_r.append(0)
                                valores_g.append(0)
                                valores_b.append(0)
                            else :
                                valores_r.append(img.getpixel((i + x, j + y))[0])
                                valores_g.append(img.getpixel((i + x, j + y))[1])
                                valores_b.append(img.getpixel((i + x, j + y))[2])
                    
                    #Ordena as listas        
                    valores_r.sort()
                    valores_g.sort()
                    valores_b.sort()
                    
                    posicao_meio = int((tamanho_matriz * tamanho_matriz) / 2) 
                    somador_r = valores_r[posicao_meio]
                    somador_g = valores_g[posicao_meio] 
                    somador_b = valores_b[posicao_meio]
                    
                    #Truncamento de valores
                    if (somador_r < 0) :
                        somador_r = 0
                    elif (somador_r > 255) :
                        somador_r = 255
                            
                    if (somador_g < 0) :
                        somador_g = 0
                    elif (somador_g > 255) :
                        somador_g = 255
    
                    if (somador_b < 0) :
                        somador_b = 0
                    elif (somador_b > 255) :
                        somador_b = 255
                    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
        #Caso a imagem nao tenha RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    valores = []
                    
                    #Percorre a imagem adicionando na lita os valores pertencentes a mascara
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                valores.append(0)
                            else :
                                valores.append(img.getpixel((i + x, j + y)))
                            
                    #Ordena a lsita
                    valores.sort()
                    
                    posicao_meio = int((tamanho_matriz * tamanho_matriz) / 2) 
                    somador = valores[posicao_meio]
                    
                    #Truncamento de valores
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com high boost
    def filtro_high_boost(self, file_path, tamanho_matriz, valor_a):
        #Gera a imagem com Passa Alta Basico    
        self.filtro_passa_alta_basico(file_path, tamanho_matriz)
        
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_amplificado = Image.new("RGB", (img.size[0], img.size[1]))
        #Valor de amplificacao
        valor_a = valor_a - 1 
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre a imagem efetuando a multiplicacao dos pixels pelo valor de aplificacao
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    pixel = img.getpixel((i, j))
                    
                    pixel[0] = int(pixel[0] * valor_a)
                    pixel[1] = int(pixel[1] * valor_a)
                    pixel[2] = int(pixel[2] * valor_a)
                    
                    img_amplificado.putpixel((i, j), pixel)
        #Caso a imagem nao tenha RGB
        except TypeError :
            #Percorre a imagem efetuando a multiplicacao dos pixels pelo valor de aplificacao
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    pixel = img.getpixel((i, j))
                    
                    pixel = int(pixel * valor_a)
                    
                    img_amplificado.putpixel((i, j), (pixel, pixel, pixel))
        
        #Salva a imagem resultante da amplificacao       
        img_amplificado.save("../img/modificada_amplificado.png")
        #Efetua a soma da imagem amplificada com a imagem passa alta basico
        self.operacao_aritmetica_adicao_truncamento("../img/modificada_filtro.png", "../img/modificada_amplificado.png")
        
        #Efetua o load da imagem resultante da soma
        img = Image.open("../img/modificada_operacao_aritmetica.png")
        img.load()
        #Salva a imagem resultante
        img.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Sobel
    def filtro_sobel(self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        #Inicializa as tres variaveis de imagens
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_h = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_v = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa as matrizes horizontal e vertical
        matriz_h = []
        matriz_v = []
        for i in range(3):
            matriz_h.append([])
            matriz_v.append([])
            for j in range(3):
                matriz_h[i].append(0)
                matriz_v[i].append(0)
        
        #Atribui os pesos necessarios as matrizes horizontal e vertical
        matriz_h[0][0] = -1
        matriz_h[0][1] = -2
        matriz_h[0][2] = -1
        matriz_h[2][0] = 1
        matriz_h[2][1] = 2
        matriz_h[2][2] = 1
        
        matriz_v[0][0] = -1
        matriz_v[1][0] = -2
        matriz_v[2][0] = -1
        matriz_v[0][2] = 1
        matriz_v[1][2] = 2
        matriz_v[2][2] = 1
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r_h = 0
                    somador_g_h = 0
                    somador_b_h = 0
                    
                    somador_r_v = 0
                    somador_g_v = 0
                    somador_b_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r_h += pixel[0] * matriz_h[x + 1][y + 1]
                            somador_g_h += pixel[1] * matriz_h[x + 1][y + 1]
                            somador_b_h += pixel[2] * matriz_h[x + 1][y + 1]
                            
                            somador_r_v += pixel[0] * matriz_v[x + 1][y + 1]
                            somador_g_v += pixel[1] * matriz_v[x + 1][y + 1]
                            somador_b_v += pixel[2] * matriz_v[x + 1][y + 1]
                    
                    somador_r = abs(somador_r_h) + abs(somador_r_v)
                    somador_g = abs(somador_g_h) + abs(somador_g_v)
                    somador_b = abs(somador_b_h) + abs(somador_b_v)    
                    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
                    img_result_h.putpixel((i, j), (somador_r_h, somador_g_h, somador_b_h))
                    img_result_v.putpixel((i, j), (somador_r_v, somador_g_v, somador_b_v))
        #Caso a imagem nao tenha RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_h = 0
                    somador_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_h += pixel * matriz_h[x + 1][y + 1]
                            somador_v += pixel * matriz_v[x + 1][y + 1]
                            
                    somador = abs(somador_h) + abs(somador_v)
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
                    img_result_h.putpixel((i, j), (somador_h, somador_h, somador_h))
                    img_result_v.putpixel((i, j), (somador_v, somador_v, somador_v))
        
        #Salva as imagens resultantes
        img_result.save("../img/modificada_filtro.png")
        img_result_h.save("../img/modificada_filtro_h.png")
        img_result_v.save("../img/modificada_filtro_v.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Roberts
    def filtro_roberts(self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        #Inicializa as tres variaveis de imagens
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_h = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_v = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa as matrizes horizontal e vertical
        matriz_h = []
        matriz_v = []
        for i in range(2):
            matriz_h.append([])
            matriz_v.append([])
            for j in range(2):
                matriz_h[i].append(0)
                matriz_v[i].append(0)
        
        #Atribui os pesos necessarios as matrizes horizontal e vertical
        matriz_h[0][0] = 1
        matriz_h[1][1] = -1
        
        matriz_v[0][1] = 1
        matriz_v[1][0] = -1
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r_h = 0
                    somador_g_h = 0
                    somador_b_h = 0
                    
                    somador_r_v = 0
                    somador_g_v = 0
                    somador_b_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(0, 2):
                        for y in range(0, 2):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r_h += pixel[0] * matriz_h[x][y]
                            somador_g_h += pixel[1] * matriz_h[x][y]
                            somador_b_h += pixel[2] * matriz_h[x][y]
                            
                            somador_r_v += pixel[0] * matriz_v[x][y]
                            somador_g_v += pixel[1] * matriz_v[x][y]
                            somador_b_v += pixel[2] * matriz_v[x][y]
                    
                    somador_r = abs(somador_r_h) + abs(somador_r_v)
                    somador_g = abs(somador_g_h) + abs(somador_g_v)
                    somador_b = abs(somador_b_h) + abs(somador_b_v)    
                    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
                    img_result_h.putpixel((i, j), (somador_r_h, somador_g_h, somador_b_h))
                    img_result_v.putpixel((i, j), (somador_r_v, somador_g_v, somador_b_v))
        #Caso a imagem nao tenha RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_h = 0
                    somador_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(0, 2):
                        for y in range(0, 2):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_h += pixel * matriz_h[x][y]
                            somador_v += pixel * matriz_v[x][y]
                            
                    somador = abs(somador_h) + abs(somador_v)
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
                    img_result_h.putpixel((i, j), (somador_h, somador_h, somador_h))
                    img_result_v.putpixel((i, j), (somador_v, somador_v, somador_v))
        
        #Salva as imagens resultantes
        img_result.save("../img/modificada_filtro.png")
        img_result_h.save("../img/modificada_filtro_h.png")
        img_result_v.save("../img/modificada_filtro_v.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Prewitt
    def filtro_prewitt(self, file_path):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        #Inicializa as tres variaveis de imagens
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_h = Image.new("RGB", (img.size[0], img.size[1]))
        img_result_v = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa as matrizes horizontal e vertical
        matriz_h = []
        matriz_v = []
        for i in range(3):
            matriz_h.append([])
            matriz_v.append([])
            for j in range(3):
                matriz_h[i].append(0)
                matriz_v[i].append(0)
        
        #Atribui os pesos necessarios as matrizes horizontal e vertical
        matriz_h[0][0] = -1
        matriz_h[0][1] = -1
        matriz_h[0][2] = -1
        matriz_h[2][0] = 1
        matriz_h[2][1] = 1
        matriz_h[2][2] = 1
        
        matriz_v[0][0] = -1
        matriz_v[1][0] = -1
        matriz_v[2][0] = -1
        matriz_v[0][2] = 1
        matriz_v[1][2] = 1
        matriz_v[2][2] = 1
        
        variacao = 1
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r_h = 0
                    somador_g_h = 0
                    somador_b_h = 0
                    
                    somador_r_v = 0
                    somador_g_v = 0
                    somador_b_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r_h += pixel[0] * matriz_h[x + variacao][y + variacao]
                            somador_g_h += pixel[1] * matriz_h[x + variacao][y + variacao]
                            somador_b_h += pixel[2] * matriz_h[x + variacao][y + variacao]
                            
                            somador_r_v += pixel[0] * matriz_v[x + variacao][y + variacao]
                            somador_g_v += pixel[1] * matriz_v[x + variacao][y + variacao]
                            somador_b_v += pixel[2] * matriz_v[x + variacao][y + variacao]
                    
                    somador_r = abs(somador_r_h) + abs(somador_r_v)
                    somador_g = abs(somador_g_h) + abs(somador_g_v)
                    somador_b = abs(somador_b_h) + abs(somador_b_v)    
                    
                    img_result.putpixel((i, j), (somador_r, somador_g, somador_b))
                    img_result_h.putpixel((i, j), (somador_r_h, somador_g_h, somador_b_h))
                    img_result_v.putpixel((i, j), (somador_r_v, somador_g_v, somador_b_v))
        #Caso a imagem nao tenha RGB
        except TypeError :
            #img[0] X e img[1] Y
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_h = 0
                    somador_v = 0
                    
                    #Percorre as matrizes (mascaras) fazendo a multiplicacao dos valores com os valores da imagem
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_h += pixel * matriz_h[x + variacao][y + variacao]
                            somador_v += pixel * matriz_v[x + variacao][y + variacao]
                            
                    somador = abs(somador_h) + abs(somador_v)
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
                    img_result_h.putpixel((i, j), (somador_h, somador_h, somador_h))
                    img_result_v.putpixel((i, j), (somador_v, somador_v, somador_v))
        
        #Salva as imagens resultantes
        img_result.save("../img/modificada_filtro.png")
        img_result_h.save("../img/modificada_filtro_h.png")
        img_result_v.save("../img/modificada_filtro_v.png")


    
    #Metodo que efetua o crescimento de regioes
    def outros_crescimento_regioes(self, file_path, limiar_t, pixel):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = img.copy()
        
        #Inicializa a matriz de vizinhos visitados
        pixels_visitados = []
        for x in range(img.size[0]):
            pixels_visitados.append([])
            for y in range(img.size[1]):
                pixels_visitados[x].append(0)
        #Inicializa o variavevl com o numero de pixels da regiao
        qtde_pixels_regiao = 0
            
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        teste = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(teste)
            
            #Seta o pixel Semente como visitado
            pixels_visitados[pixel[0]][pixel[1]] = 1
            
            #Pilha dos vizinhos que ainda necessita visitar
            pilha = []
            pilha.append([pixel[0], pixel[1]])
            
            #Instancia uma variavel com a cor do pixel Semente
            rgb = img.getpixel((pixel[0], pixel[1]))
            
            #Executa enquanto existir vizinhos que necessita visitar
            while (len(pilha) > 0) :
                #Desempilha o pixel a ser visitado
                ponto = pilha.pop(0)
                #Instancia uma variavel com a cor do pixel visitado
                ponto_rgb = img.getpixel((ponto[0], ponto[1]))
                
                x = ponto[0]
                y = ponto[1]
             
                #Verifica a similaridade entre os dois pontos
                if (sqrt(pow(rgb[0] - ponto_rgb[0], 2) + 
                         pow(rgb[1] - ponto_rgb[1], 2) +
                         pow(rgb[2] - ponto_rgb[2], 2)) < limiar_t) :
                    
                    img_result.putpixel((ponto), (0, 0, 0))
                    qtde_pixels_regiao += 1
                    
                    #Verifica para o vizinho com X - 1 e Y
                    if (x - 1 >= 0) :
                        if (pixels_visitados[x-1][y] == 0) :
                            pilha.append([x-1,y])
                            pixels_visitados[x-1][y] = 1
                            
                        if (y+1 < img.size[1]) :
                            if (pixels_visitados[x-1][y+1] == 0) :
                                pilha.append([x-1,y+1])
                                pixels_visitados[x-1][y+1] = 1
                    
                    if (y - 1 >= 0) :
                        if (pixels_visitados[x][y-1] == 0) :
                            pilha.append([x,y-1])
                            pixels_visitados[x][y-1] = 1
                            
                        if (x+1 < img.size[0]) :
                            if (pixels_visitados[x+1][y-1] == 0) :
                                pilha.append([x+1,y-1])
                                pixels_visitados[x+1][y-1] = 1
                
                    if (y-1 >= 0 and x-1 >= 0) :
                        if (pixels_visitados[x-1][y-1] == 0) :
                            pilha.append([x-1,y-1])
                            pixels_visitados[x-1][y-1] = 1
                    
                    if (y+1 < img.size[1]) :
                        if (pixels_visitados[x][y+1] == 0) :
                            pilha.append([x,y+1])
                            pixels_visitados[x][y+1] = 1
                    
                    if (x+1 < img.size[0]) :
                        if (pixels_visitados[x+1][y] == 0) :
                            pilha.append([x+1,y])
                            pixels_visitados[x+1][y] = 1
                            
                    if (x+1 < img.size[0] and y+1 < img.size[1]) :
                        if (pixels_visitados[x+1][y+1] == 0) :
                            pilha.append([x+1,y+1])
                            pixels_visitados[x+1][y+1] = 1
        
        except TypeError :
            #Caso a imagem nao tenha RGB
            
            #Comeca a percorrer os vizinhos
            pixels_visitados[pixel[0]][pixel[1]] = 1
            
            pilha = []
            pilha.append([pixel[0], pixel[1]])
            
            rgb = img.getpixel((pixel[0], pixel[1]))
                               
            while (len(pilha) > 0) :
                
                ponto = pilha.pop(0)
                ponto_rgb = img.getpixel((ponto[0], ponto[1]))
                x = ponto[0]
                y = ponto[1]
             
                if (sqrt(pow(rgb - ponto_rgb, 2)) < limiar_t) :
                    
                    img_result.putpixel((ponto), 0)
                    qtde_pixels_regiao += 1
                    
                    if (x - 1 >= 0) :
                        if (pixels_visitados[x-1][y] == 0) :
                            pilha.append([x-1,y])
                            pixels_visitados[x-1][y] = 1
                            
                        if (y+1 < img.size[1]) :
                            if (pixels_visitados[x-1][y+1] == 0) :
                                pilha.append([x-1,y+1])
                                pixels_visitados[x-1][y+1] = 1
                    
                    if (y - 1 >= 0) :
                        if (pixels_visitados[x][y-1] == 0) :
                            pilha.append([x,y-1])
                            pixels_visitados[x][y-1] = 1
                            
                        if (x+1 < img.size[0]) :
                            if (pixels_visitados[x+1][y-1] == 0) :
                                pilha.append([x+1,y-1])
                                pixels_visitados[x+1][y-1] = 1
                
                    if (y-1 >= 0 and x-1 >= 0) :
                        if (pixels_visitados[x-1][y-1] == 0) :
                            pilha.append([x-1,y-1])
                            pixels_visitados[x-1][y-1] = 1
                    
                    if (y+1 < img.size[1]) :
                        if (pixels_visitados[x][y+1] == 0) :
                            pilha.append([x,y+1])
                            pixels_visitados[x][y+1] = 1
                    
                    if (x+1 < img.size[0]) :
                        if (pixels_visitados[x+1][y] == 0) :
                            pilha.append([x+1,y])
                            pixels_visitados[x+1][y] = 1
                            
                    if (x+1 < img.size[0] and y+1 < img.size[1]) :
                        if (pixels_visitados[x+1][y+1] == 0) :
                            pilha.append([x+1,y+1])
                            pixels_visitados[x+1][y+1] = 1
            
        img_result.save("../img/modificada_outros.png")        
        
        
            
    #Metodo que efetua o crescimento de regioes
    def outros_deteccao_de_bordas(self, file_path, limiar_t):
        #Efetua o load da imagem passada o caminho como parametro
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre todos os pixels da imagem, efetua o calculo da distancia euclidiana entre dois pixels e compara com o limiar t
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    
                    if (y + 1 < img.size[1]) :
                        pixel_y = img.getpixel((x,y + 1))
                        distancia_y = sqrt(pow(pixel[0] - pixel_y[0], 2) + 
                                           pow(pixel[1] - pixel_y[1], 2) +
                                           pow(pixel[2] - pixel_y[2], 2))
                    else :
                        distancia_y = 0
                        
                    if (x + 1 < img.size[0]) :
                        pixel_x = img.getpixel((x + 1,y))
                        distancia_x = sqrt(pow(pixel[0] - pixel_x[0], 2) + 
                                           pow(pixel[1] - pixel_x[1], 2) +
                                           pow(pixel[2] - pixel_x[2], 2))
                    else :
                        distancia_x = 0
                        
                    if ((distancia_x > int(limiar_t)) or (distancia_y > int(limiar_t))):
                        valor = 255
                    else:
                        valor = 0 
                    img_result.putpixel((x,y), (valor, valor, valor))
        #Caso a imagem nao tenha RGB        
        except TypeError :
            #Percorre todos os pixels da imagem, efetua o calculo da distancia euclidiana entre dois pixels e compara com o limiar t
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    
                    if (y + 1 < img.size[1]) :
                        pixel_y = img.getpixel((x,y + 1))
                        distancia_y = sqrt(pow(pixel - pixel_y, 2))
                    else :
                        distancia_y = 0
                        
                    if (x + 1 < img.size[0]) :
                        pixel_x = img.getpixel((x + 1,y))
                        distancia_x = sqrt(pow(pixel - pixel_x, 2))
                    else :
                        distancia_x = 0
                        
                    if ((distancia_x > int(limiar_t)) or (distancia_y > int(limiar_t))):
                        valor = 255
                    else:
                        valor = 0 
                    img_result.putpixel((x,y), (valor, valor, valor))
        
        #Salva a imagem resultante
        img_result.save("../img/modificada_outros.png")