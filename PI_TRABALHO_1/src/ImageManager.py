'''
Created on 17/08/2010

@author: matheus
'''
from __future__ import division
from math import sqrt
import Image
import CairoPlot

class ImageManager():
    
    
    #Construtor da classe ImageManager
    def __init__(self):
        pass



    #Metodo que gera outra imagem em escala de cinza
    def escala_cinza(self, file_path):
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
                
            #Percorre todos os pixels da imagem pegando os valores RGB e dividindo por 3 (media)
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x, y))
                    media = int((pixel[0] + pixel[1] + pixel[2]) / 3)
                    img_result.putpixel((x, y), (media, media, media))
        except :
            #Caso a imagem nao tenha RGB, nao e necessario efetuar a media, pois a imagem gerada e igual a imagem origem
            pass
        
        img_result.save("../img/modificada_escala_cinza.png")



    #Metodo que gera um histograma referentes a escala de cinza da imagem
    def histograma_escala_cinza (self, file_path):
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
        except :
            #Caso a imagem nao tenha RGB
            #Percorre todos os pixels da imagem incrementando uma vez na posicao do valor do pixel
            #img[0] X e img[1] Y
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    escala_cinza[pixel] += 1
        
        #Plotagem do grafico
        h_labels = ["10", "40", "70", "100", "130", "160", "190", "220", "250"]
        CairoPlot.bar_plot("../img/histograma_escala_cinza.png", escala_cinza, 300, 250, border = 20, grid = True, h_labels = h_labels, colors = colors)



    #Metodo que gera tres histogramas referentes ao rgb da imagem
    def histograma_rgb (self, file_path):
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
        except :
            #Caso a imagem nao tenha RGB
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
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)

            #Percorre todos os pixels da imagem e compara com o limiar t
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    if (img.getpixel((x,y))[0] > int(limiar_t)):
                        valor = 0 
                    else:
                        valor = 255
                    img_result.putpixel((x,y), (valor, valor, valor))
        except :
            #Caso a imagem nao tenha RGB
            #Percorre todos os pixels da imagem e compara com o limiar t
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    if (img.getpixel((x,y)) > int(limiar_t)):
                        valor = 0 
                    else:
                        valor = 255
                    img_result.putpixel((x,y), valor, valor, valor)
        
        img_result.save("../img/modificada_limiarizacao.png")
    
    
    
    #Metodo que efetua a limiarizacao baseado em diversas varias
    def limiarizacao_diversas_variaveis(self, file_path, limiar_t, valor_rgb):
        img = Image.open(file_path)
        img.load()
        img_result = img.copy()
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            #Percorre todos os pixels da imagem e compara com o limiar t
            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    pixel = img.getpixel((x,y))
                    distancia = sqrt(pow(valor_rgb[0] - pixel[0], 2) + 
                                     pow(valor_rgb[1] - pixel[1], 2) +
                                     pow(valor_rgb[2] - pixel[2], 2))
                    if (distancia > limiar_t):
                        img_result.putpixel((x,y), (0, 0, 0))
                        
        except :
            #Caso a imagem nao tenha RGB, nao se pode fazer diversas variaveis, pois deve ser uma imagem colorida
            pass
        
        img_result.save("../img/modificada_limiarizacao.png")
    
    
    
    #Metodo que efetua a operacao aritmetica ADICAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_adicao(self, file_path1, file_path2):
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
        except :
            #Caso no minimo uma das imagens nao tenha RGB
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
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
            except :
                #Caso no minimo uma das imagens nao tenha RGB
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
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
                except :
                    #Caso no minimo de as duas nao terem vao RGB
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 + pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 510, 0)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))

        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
    #Metodo que efetua a operacao aritmetica SUBTRACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_subtracao(self, file_path1, file_path2):
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
        except :
            #Caso no minimo uma das imagens nao tenha RGB
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
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
            except :
                #Caso no minimo uma das imagens nao tenha RGB
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
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
                except :
                    #Caso no minimo de as duas nao terem vao RGB
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 - pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 255, -255)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))

        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
    #Metodo que efetua a operacao aritmetica MULTIPLICACAO entre duas imagens gerando uma terceira imagem
    def operacao_aritmetica_multiplicacao(self, file_path1, file_path2):
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
        except :
            #Caso no minimo uma das imagens nao tenha RGB
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
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
            except :
                #Caso no minimo uma das imagens nao tenha RGB
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
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
                except :
                    #Caso no minimo de as duas nao terem vao RGB
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            pixel1 = img1.getpixel((x,y))
                            pixel2 = img2.getpixel((x,y))
                            
                            valor = pixel1 * pixel2
                            
                            #Reescalonamento de valores
                            valor = self.reescalonamento_de_valores(valor, 65025, 0)
                            
                            img_result.putpixel((x,y), (valor, valor, valor))

        img_result.save("../img/modificada_operacao_aritmetica.png")
    
    
    
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
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == 255 and img2.getpixel((x,y))[0] == 255):
                        valor = 255
                    else :
                        valor = 0
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == 255 and img2.getpixel((x,y)) == 255):
                            valor = 255
                        else :
                            valor = 0
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 255 and img2.getpixel((x,y))[0] == 255):
                                valor = 255
                            else :
                                valor = 0
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except :
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 255 and img2.getpixel((x,y)) == 255):
                                valor = 255
                            else :
                                valor = 0
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
    
        img_result.save("../img/modificada_operacao_logica.png")
    
    
    
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
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == 0 and img2.getpixel((x,y))[0] == 0):
                        valor = 0
                    else :
                        valor = 255
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == 0 and img2.getpixel((x,y)) == 0):
                            valor = 0
                        else :
                            valor = 255
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 0 and img2.getpixel((x,y))[0] == 0):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except :
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == 0 and img2.getpixel((x,y)) == 0):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
    
        img_result.save("../img/modificada_operacao_logica.png")
    
    
    
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
            
        img_result = Image.new("RGB", (tamanho_x, tamanho_y))

        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel1 = img1.getpixel((0, 0))
        pixel2 = img2.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel1)
            len(pixel2)
            
            for x in range(tamanho_x):
                for y in range(tamanho_y):
                    if (img1.getpixel((x,y))[0] == img2.getpixel((x,y))[0]):
                        valor = 0
                    else :
                        valor = 255
                            
                    img_result.putpixel((x,y), (valor, valor, valor))
        except :
            try :
                #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                len(pixel1)
                
                for x in range(tamanho_x):
                    for y in range(tamanho_y):
                        if (img1.getpixel((x,y))[0] == img2.getpixel((x,y))):
                            valor = 0
                        else :
                            valor = 255
                                
                        img_result.putpixel((x,y), (valor, valor, valor))
            except :
                try :
                    #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
                    len(pixel2)
                    
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == img2.getpixel((x,y))[0]):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
                except :
                    for x in range(tamanho_x):
                        for y in range(tamanho_y):
                            if (img1.getpixel((x,y)) == img2.getpixel((x,y))):
                                valor = 0
                            else :
                                valor = 255
                                    
                            img_result.putpixel((x,y), (valor, valor, valor))
    
        img_result.save("../img/modificada_operacao_logica.png")
        
        
        
    #Metodo que gera outra imagem filtrado com passa alta basico
    def filtro_passa_alta_basico(self, file_path, tamanho_matriz):
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa a matriz
        matriz = []
        for i in range(tamanho_matriz):
            matriz.append([])
            for j in range(tamanho_matriz):
                matriz[i].append(-1)
        
        variacao = int(tamanho_matriz / 2)
        matriz[variacao][variacao] = 8
        divisor = tamanho_matriz * tamanho_matriz;
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r = 0
                    somador_g = 0
                    somador_b = 0
                    
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
        except :
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador = 0
                    
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador += pixel * matriz[x + variacao][y + variacao]
                    
                    somador = int(somador/divisor)
                    
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com a media
    def filtro_media(self, file_path, tamanho_matriz):
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))
        
        #Inicializa a matriz
        matriz = []
        for i in range(tamanho_matriz):
            matriz.append([])
            for j in range(tamanho_matriz):
                matriz[i].append(1)
        
        divisor = tamanho_matriz * tamanho_matriz;
        variacao = int(tamanho_matriz / 2)
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador_r = 0
                    somador_g = 0
                    somador_b = 0
                    
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = (0, 0, 0)
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador_r += pixel[0] * matriz[x + 1][y+ 1]
                            somador_g += pixel[1] * matriz[x + 1][y+ 1]
                            somador_b += pixel[2] * matriz[x + 1][y+ 1]
                    
                    somador_r = int(somador_r/divisor)
                    somador_g = int(somador_g/divisor)
                    somador_b = int(somador_b/divisor)
                    
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
        except :
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    somador = 0
                    
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                pixel = 0
                            else :
                                pixel = img.getpixel((i + x, j + y))
                            
                            somador += pixel * matriz[x + 1][y+ 1]
                    
                    somador = int(somador/divisor)
                    
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com mediana
    def filtro_mediana(self, file_path, tamanho_matriz):
        img = Image.open(file_path)
        img.load()
        img_result = Image.new("RGB", (img.size[0], img.size[1]))

        variacao = int(tamanho_matriz / 2)
        
        #Verifica qual o tipo de codec utilizado na criacao da imagem
        pixel = img.getpixel((0, 0))
        try :
            #Verifica se a imagem tem valores de RGB atraves da verificacao do tamanho da List
            len(pixel)
            
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    valores_r = []
                    valores_g = []
                    valores_b = []
                    
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
                    
                    valores_r.sort()
                    valores_g.sort()
                    valores_b.sort()
                    
                    posicao_meio = int((tamanho_matriz * tamanho_matriz) / 2) 
                    somador_r = valores_r[posicao_meio]
                    somador_g = valores_b[posicao_meio] 
                    somador_b = valores_g[posicao_meio]
                    
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
        except :
            for i in range(0, img.size[0]):
                for j in range(0, img.size[1]):
                    valores = []
                    
                    for x in range(-variacao, variacao + 1):
                        for y in range(-variacao, variacao + 1):
                            if ((i + x < 0) or (i + x > img.size[0]-1) or (j + y < 0) or (j + y > img.size[1]-1)) :
                                valores.append(0)
                            else :
                                valores.append(img.getpixel((i + x, j + y)))
                            
                    valores.sort()
                    
                    posicao_meio = int((tamanho_matriz * tamanho_matriz) / 2) 
                    somador = valores[posicao_meio]
                    
                    if (somador < 0) :
                        somador = 0
                    elif (somador > 255) :
                        somador = 255
                    
                    img_result.putpixel((i, j), (somador, somador, somador))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com high boost
    def filtro_high_boost(self, file_path):
        img = Image.open(file_path)
        img.load()
        img_result = img
        
        #Percorre todos os pixels da imagem
        for x in range(1, img.size[0] - 1):
            for y in range(1, img.size[1] - 1):
                
                media_r = 0
                media_g = 0
                media_b = 0
                for z in range(x - 1, x + 2):
                    for w in range(y - 1, y + 2):
                        media_r = media_r + img.getpixel((z,w))[0]
                        media_g = media_g + img.getpixel((z,w))[1]
                        media_b = media_b + img.getpixel((z,w))[2]
                        
                img_result.putpixel((x,y), (int(img.getpixel((x,y))[0] - (media_r / 9)),
                                     int(img.getpixel((x,y))[1] - (media_g / 9)),
                                     int(img.getpixel((x,y))[2] - (media_b / 9))))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Sobel
    def filtro_sobel(self, file_path):
        img = Image.open(file_path)
        img.load()
        img_result = img
        
        #Percorre todos os pixels da imagem
        for x in range(1, img.size[0] - 1):
            for y in range(1, img.size[1] - 1):
                
                media_r = 0
                media_g = 0
                media_b = 0
                for z in range(x - 1, x + 2):
                    for w in range(y - 1, y + 2):
                        media_r = media_r + img.getpixel((z,w))[0]
                        media_g = media_g + img.getpixel((z,w))[1]
                        media_b = media_b + img.getpixel((z,w))[2]
                        
                img_result.putpixel((x,y), (int(img.getpixel((x,y))[0] - (media_r / 9)),
                                     int(img.getpixel((x,y))[1] - (media_g / 9)),
                                     int(img.getpixel((x,y))[2] - (media_b / 9))))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Roberts
    def filtro_roberts(self, file_path):
        img = Image.open(file_path)
        img.load()
        img_result = img
        
        #Percorre todos os pixels da imagem
        for x in range(1, img.size[0] - 1):
            for y in range(1, img.size[1] - 1):
                
                media_r = 0
                media_g = 0
                media_b = 0
                for z in range(x - 1, x + 2):
                    for w in range(y - 1, y + 2):
                        media_r = media_r + img.getpixel((z,w))[0]
                        media_g = media_g + img.getpixel((z,w))[1]
                        media_b = media_b + img.getpixel((z,w))[2]
                        
                img_result.putpixel((x,y), (int(img.getpixel((x,y))[0] - (media_r / 9)),
                                     int(img.getpixel((x,y))[1] - (media_g / 9)),
                                     int(img.getpixel((x,y))[2] - (media_b / 9))))
        
        img_result.save("../img/modificada_filtro.png")
        
        
        
    #Metodo que gera outra imagem filtrado com Prewitt
    def filtro_prewitt(self, file_path):
        img = Image.open(file_path)
        img.load()
        img_result = img
        
        #Percorre todos os pixels da imagem
        for x in range(1, img.size[0] - 1):
            for y in range(1, img.size[1] - 1):
                
                media_r = 0
                media_g = 0
                media_b = 0
                for z in range(x - 1, x + 2):
                    for w in range(y - 1, y + 2):
                        media_r = media_r + img.getpixel((z,w))[0]
                        media_g = media_g + img.getpixel((z,w))[1]
                        media_b = media_b + img.getpixel((z,w))[2]
                        
                img_result.putpixel((x,y), (int(img.getpixel((x,y))[0] - (media_r / 9)),
                                     int(img.getpixel((x,y))[1] - (media_g / 9)),
                                     int(img.getpixel((x,y))[2] - (media_b / 9))))
        
        img_result.save("../img/modificada_filtro.png")