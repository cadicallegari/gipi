'''
Created on 17/08/2010

@author: matheus
'''
from __future__ import division
from math import sqrt
import Image
import CairoPlot

class ImageManager():
    
    def __init__(self):
        pass



    #Metodo que gera outra imagem em escala de cinza
    def escala_cinza(self, file_path):
        img = Image.open(file_path)
        img.load()
        
        #Percorre todos os pixels da imagem pegando os valores RGB e dividindo por 3 (media)
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                valor = int((img.getpixel((x,y))[0] 
                                 + img.getpixel((x,y))[1]
                                 + img.getpixel((x,y))[2]) / 3)
                img.putpixel((x,y), (valor,valor,valor))
        
        img.save("../img/modificada_escala_cinza.png")


    
    #Metodo que gera um histograma referentes a escala de cinza da imagem
    def histograma_escala_cinza (self, file_path):
        img = Image.open(file_path)
        img.load()
        
        #Inicializa o array de 256 posicoes
        escala_cinza = []
        for x in range(256):
            escala_cinza.append(0)
        
        #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
        #img[0] X e img[1] Y
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                posicao = int(img.getpixel((x,y))[0])
                escala_cinza[posicao] += 1
        
        #Array de cores do grafico
        colors = []
        for x in range(256):
            colors.append((0, 0, 0))
        
        #Plotagem do grafico
        h_labels = ["10", "40", "70", "100", "130", "160", "190", "220", "250"]
        CairoPlot.bar_plot("../img/histograma_escala_cinza.png", escala_cinza, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors)
    
    #Metodo que gera tres histogramas referentes ao rgb da imagem
    def histograma_rgb (self, file_path):
        img = Image.open(file_path)
        img.load()
        
        #Inicializa os tres vetores de 256 posicoes
        red = []
        green = []
        blue = []
        for x in range(256):
            red.append(0)
            green.append(0)
            blue.append(0)
        
        #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
        #img[0] X e img[1] Y
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                #Cor Red
                posicao = int(img.getpixel((x,y))[0])
                red[posicao] += 1
                #Cor Green
                posicao = int(img.getpixel((x,y))[1])
                green[posicao] += 1
                #Cor Blue
                posicao = int(img.getpixel((x,y))[2])
                blue[posicao] += 1
        
        #Arrays de cores dos graficos
        colors_red = []
        colors_green = []
        colors_blue = []
        for x in range(256):
            colors_red.append((1, 0, 0))
            colors_green.append((0, 1, 0))
            colors_blue.append((0, 0, 1))
        
        #Plotagem do grafico
        h_labels = ["10", "40", "70", "100", "130", "160", "190", "220", "250"]
        CairoPlot.bar_plot("../img/histograma_red.png", red, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_red)
        CairoPlot.bar_plot("../img/histograma_green.png", green, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_green)
        CairoPlot.bar_plot("../img/histograma_blue.png", blue, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors_blue)
    
    #Metodo que efetua a limiarizacao global simples    
    def limiarizacao_global_simples(self, file_path, limiar_t):
        img = Image.open(file_path)
        img.load()
        
        #Percorre todos os pixels da imagem e compara com o limiar t
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if (img.getpixel((x,y))[0] > int(limiar_t)):
                    valor = 0 
                else:
                    valor = 255
                img.putpixel((x,y), (valor,valor,valor))
        
        img.save("../img/modificada_limiarizacao.png")
    
    #Metodo que efetua a limiarizacao baseado em diversas varias
    def limiarizacao_diversas_variaveis(self, file_path, limiar_t, valor_rgb):
        img = Image.open(file_path)
        img.load()
        
        #Percorre todos os pixels da imagem e compara com o limiar t
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                distancia = sqrt(pow(valor_rgb[0] - img.getpixel((x,y))[0], 2) + 
                                 pow(valor_rgb[1] - img.getpixel((x,y))[1], 2) +
                                 pow(valor_rgb[2] - img.getpixel((x,y))[2], 2))
                if (distancia > limiar_t):
                    img.putpixel((x,y), (0, 0, 0))
                
        
        img.save("../img/modificada_limiarizacao.png")
        
    #Metodo que efetua a operacao aritmetica ADICAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_adicao(self, file_path1, file_path2):
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e adiciona,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                valor_r = img1.getpixel((x,y))[0] + img2.getpixel((x,y))[0]
                valor_g = img1.getpixel((x,y))[1] + img2.getpixel((x,y))[1]
                valor_b = img1.getpixel((x,y))[2] + img2.getpixel((x,y))[2]
                
                #Reescalonamento de valores
                valor_r = self.reescalonamento_de_valores(valor_r, 510, 0)
                valor_g = self.reescalonamento_de_valores(valor_g, 510, 0)
                valor_b = self.reescalonamento_de_valores(valor_b, 510, 0)
                    
                img1.putpixel((x,y), (valor_r,valor_g,valor_b))

        img1.save("../img/modificada_operacao_aritmetica.png")
    
    #Metodo que efetua a operacao aritmetica SUBTRACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_subtracao(self, file_path1, file_path2):
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e subtraindo,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                valor_r = img1.getpixel((x,y))[0] - img2.getpixel((x,y))[0]
                valor_g = img1.getpixel((x,y))[1] - img2.getpixel((x,y))[1]
                valor_b = img1.getpixel((x,y))[2] - img2.getpixel((x,y))[2]
                
                #Reescalonamento de valores
                valor_r = self.reescalonamento_de_valores(valor_r, 255, -255)
                valor_g = self.reescalonamento_de_valores(valor_g, 255, -255)
                valor_b = self.reescalonamento_de_valores(valor_b, 255, -255)

                img1.putpixel((x,y), (valor_r,valor_g,valor_b))
    
        img1.save("../img/modificada_operacao_aritmetica.png")
    
    #Metodo que efetua a operacao aritmetica MULTIPLICACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_multiplicacao(self, file_path1, file_path2):
        img1 = Image.open(file_path1)
        img2 = Image.open(file_path2)
        img1.load()
        img2.load()    
        
        #Percorre todos os pixels da imagem pegando os valores dos pixels das duas imagens e multiplicando,
        #gerando uma terceira imagem
        if (img1.size[0] > img2.size[0]):
            tamanho_x = img2.size[0]
        else:
            tamanho_x = img1.size[0]
        
        if (img1.size[1] > img2.size[1]):
            tamanho_y = img2.size[1]
        else:
            tamanho_y = img1.size[1]

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                valor_r = img1.getpixel((x,y))[0] * img2.getpixel((x,y))[0]
                valor_g = img1.getpixel((x,y))[1] * img2.getpixel((x,y))[1]
                valor_b = img1.getpixel((x,y))[2] * img2.getpixel((x,y))[2]
                
                #Reescalonamento de valores
                valor_r = self.reescalonamento_de_valores(valor_r, 65025, 0)
                valor_g = self.reescalonamento_de_valores(valor_g, 65025, 0)
                valor_b = self.reescalonamento_de_valores(valor_b, 65025, 0)
                    
                img1.putpixel((x,y), (valor_r,valor_g,valor_b))
    
        img1.save("../img/modificada_operacao_aritmetica.png")
    
    #Metodo que efetua o reescalonamento de valores para a escala 0 a 255 do rgb
    def reescalonamento_de_valores(self, valor, tmax, tmin):
        return int((255 / (tmax - tmin)) * (valor - tmin))
    
    #Metodo que efetua a operacao logica AND entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_and(self, file_path1, file_path2):
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

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                if (img1.getpixel((x,y))[0] == 255 and img2.getpixel((x,y))[0] == 255):
                    valor = 255
                else :
                    valor = 0
                        
                img1.putpixel((x,y), (valor,valor,valor))
    
        img1.save("../img/modificada_operacao_logica.png")
    
    #Metodo que efetua a operacao logica OR entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_or(self, file_path1, file_path2):
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

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                if (img1.getpixel((x,y))[0] == 0 and img2.getpixel((x,y))[0] == 0):
                    valor = 0
                else :
                    valor = 255
                    
                img1.putpixel((x,y), (valor,valor,valor))

        img1.save("../img/modificada_operacao_logica.png")
    
    #Metodo que efetua a operacao logica XOR entre duas imagens binarias gerando uma terceira imagem
    def operacao_logica_xor(self, file_path1, file_path2):
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

        for x in range(tamanho_x):
            for y in range(tamanho_y):
                if (img1.getpixel((x,y))[0] == img2.getpixel((x,y))[0]):
                    valor = 0
                else :
                    valor = 255

                img1.putpixel((x,y), (valor,valor,valor))

        img1.save("../img/modificada_operacao_logica.png")