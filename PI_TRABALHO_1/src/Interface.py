'''
Created on 17/08/2010

@author: matheus
'''
#Importacoes
import pygtk
from ImageManager import ImageManager
import Image
pygtk.require('2.0')
import gtk.glade

#Classe que gerencia a interface
class Gui():


    #Construtor da classe
    def __init__(self):
        
        
        #Nome do arquivo Glade
        self.__glade_file = "../xml/principal.glade"
        gui = gtk.glade.XML(self.__glade_file)
        self.gui = gui
        
        self.main_window = gui.get_widget("janela_principal")
        self.main_window.connect("destroy", gtk.main_quit)
        
        
        #Associa os controles
        
        #Controles do menu
        self.btSair = gui.get_widget("sair_menuitem")
        self.btSobre = gui.get_widget("sobre_menuitem")
        
        
        #Controles da aba ESCALA DE CINZA
        self.fcEscalaOrigem = gui.get_widget("escala_filechooserbutton_origem")
        self.fcEscalaDestino = gui.get_widget("escala_filechooserbutton_destino")
        self.btEscalaExecutar = gui.get_widget("escala_button_executar")
        self.btEscalaSalvar = gui.get_widget("escala_button_salvar")
        
        
        #Controles da aba HISTOGRAMA
        self.fcHistogramaOrigem = gui.get_widget("hist_filechooserbutton_origem")
        self.btHistogramaExecutar = gui.get_widget("hist_button_executar")
        
        
        #Controles da aba LIMIARIZACAO
        self.fcLimiarizacaoOrigem = gui.get_widget("lim_filechooserbutton_origem")
        self.fcLimiarizacaoDestino = gui.get_widget("lim_filechooserbutton_destino")
        self.btLimiarizacaoSalvar = gui.get_widget("lim_button_salvar")
        self.rbLimiarizacaoGlobal = gui.get_widget("lim_radiobutton_global")
        self.rbLimiarizacaoVariaveis = gui.get_widget("lim_radiobutton_variaveis")
        self.evLimiarizacao = gui.get_widget("lim_eventos")
        self.hsLimiarizacao = gui.get_widget("lim_hscale")
        self.txtLimiarizacaoR = gui.get_widget("lim_txt_r")
        self.txtLimiarizacaoG = gui.get_widget("lim_txt_g")
        self.txtLimiarizacaoB = gui.get_widget("lim_txt_b")
        
        
        #Controles da aba OPERACOES ARITMETICAS
        self.fcOpAritmeticaOrigem1 = gui.get_widget("op_arit_filechooserbutton1")
        self.fcOpAritmeticaOrigem2 = gui.get_widget("op_arit_filechooserbutton2")
        self.fcOpAritmeticaDestino = gui.get_widget("op_arit_filechooserbutton_destino")
        self.btOpAritmeticaExecutar = gui.get_widget("op_arit_button_executar")
        self.btOpAritmeticaSalvar = gui.get_widget("op_arit_button_salvar")
        self.rbOpAritmeticaAdicao = gui.get_widget("op_arit_radiobutton_adicao")
        self.rbOpAritmeticaSubtracao = gui.get_widget("op_arit_radiobutton_subtracao")
        self.rbOpAritmeticaMultiplicacao = gui.get_widget("op_arit_radiobutton_multiplicacao")
        
        
        #Controles da aba OPERACOES LOGICAS
        self.fcOpLogicaOrigem1 = gui.get_widget("op_log_filechooserbutton1")
        self.fcOpLogicaOrigem2 = gui.get_widget("op_log_filechooserbutton2")
        self.fcOpLogicaDestino = gui.get_widget("op_log_filechooserbutton_destino")
        self.btOpLogicaExecutar = gui.get_widget("op_log_button_executar")
        self.btOpLogicaSalvar = gui.get_widget("op_log_button_salvar")
        self.rbOpLogicaAnd = gui.get_widget("op_log_radiobutton_and")
        self.rbOpLogicaOr = gui.get_widget("op_log_radiobutton_or")
        self.rbOpLogicaXor = gui.get_widget("op_log_radiobutton_xor")
        
        
        #Controles da aba FILTROS DINAMICOS
        self.fcFiltroDinOrigem = gui.get_widget("filtro_din_filechooserbutton_origem")
        self.fcFiltroDinDestino = gui.get_widget("filtro_din_filechooserbutton_destino")
        self.rbFiltroDinPassaAlta = gui.get_widget("filtro_din_radiobutton_passa_alta")
        self.rbFiltroDinMedia = gui.get_widget("filtro_din_radiobutton_media")
        self.rbFiltroDinMediana = gui.get_widget("filtro_din_radiobutton_mediana")
        self.rbFiltroDinHighBoost = gui.get_widget("filtro_din_radiobutton_highboost")
        self.cbFiltroDin = gui.get_widget("filtro_din_combobox")
        self.sbFiltroDin = gui.get_widget("filtro_din_spinbutton")
        self.btFiltroDinExecutar = gui.get_widget("filtro_din_button_executar")
        self.btFiltroDinSalvar = gui.get_widget("filtro_din_button_salvar")
        
        
        #Controles da aba FILTROS
        self.fcFiltroOrigem = gui.get_widget("filtro_filechooserbutton_origem")
        self.fcFiltroDestino = gui.get_widget("filtro_filechooserbutton_destino")
        self.fcFiltroDestino_h = gui.get_widget("filtro_filechooserbutton_destino_h")
        self.fcFiltroDestino_v = gui.get_widget("filtro_filechooserbutton_destino_v")
        self.rbFiltroSobel = gui.get_widget("filtro_radiobutton_sobel")
        self.rbFiltroRoberts = gui.get_widget("filtro_radiobutton_roberts")
        self.rbFiltroPrewitt = gui.get_widget("filtro_radiobutton_prewitt")
        self.btFiltroExecutar = gui.get_widget("filtro_button_executar")
        self.btFiltroSalvar = gui.get_widget("filtro_button_salvar")
        self.btFiltroSalvar_h = gui.get_widget("filtro_button_salvar_h")
        self.btFiltroSalvar_v = gui.get_widget("filtro_button_salvar_v")


        #Controles da aba OUTROS
        self.fcOutrosOrigem = gui.get_widget("out_filechooserbutton_origem")
        self.fcOutrosDestino = gui.get_widget("out_filechooserbutton_destino")
        self.btOutrosSalvar = gui.get_widget("out_button_salvar")
        self.rbOutrosCrescimento = gui.get_widget("out_radiobutton_crescimento")
        self.rbOutrosDeteccao = gui.get_widget("out_radiobutton_deteccao")
        self.evOutros = gui.get_widget("out_eventos")
        self.hsOutros = gui.get_widget("out_hscale")
        self.txtOutrosVizinhos = gui.get_widget("out_txt_visitados")
                
        
        
        #Associa os eventos aos controles
        
        #Eventos do menu
        self.btSair.connect("activate", self.actSair)
        self.btSobre.connect("activate", self.actSobre)
        
        
        #Eventos da aba ESCALA DE CINZA
        self.fcEscalaOrigem.connect("file-set", self.actEscalaCinzaCarregaImagem)
        self.btEscalaExecutar.connect("clicked", self.actEscalaCinzaExecutar)
        self.btEscalaSalvar.connect("clicked", self.actEscalaCinzaSalvar)
        
        
        #Eventos da aba HISTOGRAMA
        self.fcHistogramaOrigem.connect("file-set", self.actHistogramaCarregaImagem)
        self.btHistogramaExecutar.connect("clicked", self.actHistogramaExecutar)
        
        
        #Eventos da aba LIMIARIZACAO
        self.fcLimiarizacaoOrigem.connect("file-set", self.actLimiarizacaoCarregaImagem)
        self.btLimiarizacaoSalvar.connect("clicked", self.actLimiarizacaoSalvar)
        self.evLimiarizacao.connect("button-press-event", self.actLimiarizacaoPreencherRgb)
        self.hsLimiarizacao.connect("button-release-event", self.actLimiarizacaoExecutar)
        
        
        #Eventos da aba OPERACOES ARITMETICAS
        self.fcOpAritmeticaOrigem1.connect("file-set", self.actOpAritmeticaCarregaImagem1)
        self.fcOpAritmeticaOrigem2.connect("file-set", self.actOpAritmeticaCarregaImagem2)
        self.btOpAritmeticaExecutar.connect("clicked", self.actOpAritmeticaExecutar)
        self.btOpAritmeticaSalvar.connect("clicked", self.actOpAritmeticaSalvar)
        
        
        #Eventos da aba OPERACOES LOGICAS
        self.fcOpLogicaOrigem1.connect("file-set", self.actOpLogicaCarregaImagem1)
        self.fcOpLogicaOrigem2.connect("file-set", self.actOpLogicaCarregaImagem2)
        self.btOpLogicaExecutar.connect("clicked", self.actOpLogicaExecutar)
        self.btOpLogicaSalvar.connect("clicked", self.actOpLogicaSalvar)
        
        
        #Eventos da aba FILTROS DINAMICOS
        self.fcFiltroDinOrigem.connect("file-set", self.actFiltroDinCarregaImagem)
        self.btFiltroDinExecutar.connect("clicked", self.actFiltroDinExecutar)
        self.btFiltroDinSalvar.connect("clicked", self.actFiltroDinSalvar)
        
        
        #Eventos da aba FILTROS
        self.fcFiltroOrigem.connect("file-set", self.actFiltroCarregaImagem)
        self.btFiltroExecutar.connect("clicked", self.actFiltroExecutar)
        self.btFiltroSalvar.connect("clicked", self.actFiltroSalvar)
        self.btFiltroSalvar_h.connect("clicked", self.actFiltroSalvarHorizontal)
        self.btFiltroSalvar_v.connect("clicked", self.actFiltroSalvarVertical)
        
        
        #Eventos da aba OUTROS
        self.fcOutrosOrigem.connect("file-set", self.actOutrosCarregaImagem)
        self.btOutrosSalvar.connect("clicked", self.actOutrosSalvar)
        self.evOutros.connect("button-press-event", self.actOutrosPreencherPosicaoPixel)
        self.hsOutros.connect("button-release-event", self.actOutrosExecutar)
        
        
        self.main_window.show_all()
        self.loop()


    #Metodo da GTK
    def loop(self):
        gtk.main()


    #Metodo que fecha o programa
    def actSair(self, widget):
        gtk.main_quit()
        
        
    #Metodo que abre a janela Sobre
    def actSobre(self, widget):
        Sobre()
    
    
    
    #Metodos de ESCALA DE CINZA
    
    #Metodo que carrega a imagem no widget de escala de cinza
    def actEscalaCinzaCarregaImagem(self, widget):
        imagem = self.gui.get_widget('escala_image_origem')
        imagem.set_from_file(self.fcEscalaOrigem.get_filename())
        imagem.show()


    #Metodo que gera a imagem em escala de cinza
    def actEscalaCinzaExecutar(self, widget):
        imageManager = ImageManager()
        imageManager.escala_cinza(self.fcEscalaOrigem.get_filename())
        imagem = self.gui.get_widget('escala_image_gerada')
        imagem.set_from_file("../img/modificada_escala_cinza.png")
        imagem.show()
    
    
    #Metodo que salva a imagem em escala de cinza
    def actEscalaCinzaSalvar(self, widget):
        img = Image.open("../img/modificada_escala_cinza.png")
        file = self.fcEscalaOrigem.get_filename().split("/")
        img.save(self.fcEscalaDestino.get_filename() + "/escala-cinza-" + file[len(file) - 1])



    #Metodos de HISTOGRAMAS
    
    #Metodo que carrega a imagem no widget de histograma
    def actHistogramaCarregaImagem(self, widget):
        imagem = self.gui.get_widget('hist_image_origem')
        imagem.set_from_file(self.fcHistogramaOrigem.get_filename())
        imagem.show()


    #Metodo que gera os histogramas
    def actHistogramaExecutar(self, widget):
        imageManager = ImageManager()
        #Gera histograma escala de cinza
        imageManager.escala_cinza(self.fcHistogramaOrigem.get_filename())
        imageManager.histograma_escala_cinza("../img/modificada_escala_cinza.png")
        imageManager.histograma_rgb(self.fcHistogramaOrigem.get_filename())
        imagem = self.gui.get_widget('hist_image_cinza')
        imagem.set_from_file("../img/histograma_escala_cinza.png")
        imagem.show()
        #Gera histograma banda red
        imagem = self.gui.get_widget('hist_image_r')
        imagem.set_from_file("../img/histograma_red.png")
        imagem.show()
        #Gera histograma banda green
        imagem = self.gui.get_widget('hist_image_g')
        imagem.set_from_file("../img/histograma_green.png")
        imagem.show()
        #Gera histograma banda blue
        imagem = self.gui.get_widget('hist_image_b')
        imagem.set_from_file("../img/histograma_blue.png")
        imagem.show()



    #Metodos de LIMIARIZACAO
    
    #Metodo que carrega a imagem no widget de limiarizacao
    def actLimiarizacaoCarregaImagem(self, widget):
        imagem = self.gui.get_widget('lim_image_origem')
        imagem.set_from_file(self.fcLimiarizacaoOrigem.get_filename())
        imagem.show()
        
    #Metodo que preenche o valor RGB do pixel clicado na imagem
    def actLimiarizacaoPreencherRgb(self, widget, event):
        img = Image.open(self.fcLimiarizacaoOrigem.get_filename())
        img.load()
        
        #Efetua os calculos do ponto X e Y clicado na tela
        if (img.size[0] < 610 and img.size[1] < 481) :
            pixel_x = event.get_coords()[0] - int((625 - img.size[0]) / 2)
            pixel_y = event.get_coords()[1] - int((480 - img.size[1]) / 2)
        elif (img.size[0] < 610) :
            pixel_x = event.get_coords()[0] - int((625 - img.size[0]) / 2)
            pixel_y = event.get_coords()[1]
        elif (img.size[1] < 481) :
            pixel_x = event.get_coords()[0]
            pixel_y = event.get_coords()[1] - int((480 - img.size[1]) / 2)
        else :
            pixel_x = event.get_coords()[0]
            pixel_y = event.get_coords()[1]
        
        if (pixel_x > 0 and pixel_x < img.size[0] and pixel_y > 0 and pixel_y < img.size[1]) :
            pixel = img.getpixel((pixel_x, pixel_y))
            try :
                self.txtLimiarizacaoR.set_text(str(pixel[0]))
                self.txtLimiarizacaoG.set_text(str(pixel[1]))
                self.txtLimiarizacaoB.set_text(str(pixel[2]))
            except : 
                self.txtLimiarizacaoR.set_text(str(pixel))
                self.txtLimiarizacaoG.set_text(str(pixel))
                self.txtLimiarizacaoB.set_text(str(pixel))
 
    #Metodo que gera a imagem limiarizada
    def actLimiarizacaoExecutar(self, widget, arg):
        imageManager = ImageManager()
        #Caso a opcao seJA GLOBAL SIMPLES
        if (self.rbLimiarizacaoGlobal.get_active()):
            imageManager.limiarizacao_global_simples(self.fcLimiarizacaoOrigem.get_filename(), self.hsLimiarizacao.get_value())
        #Caso a opcao seja DIVERSAS VARIAVEIS
        else:
            imageManager.limiarizacao_diversas_variaveis(self.fcLimiarizacaoOrigem.get_filename(), self.hsLimiarizacao.get_value(), [int(self.txtLimiarizacaoR.get_text()), int(self.txtLimiarizacaoG.get_text()), int(self.txtLimiarizacaoB.get_text())])
            
        imagem = self.gui.get_widget('lim_image_gerada')
        imagem.set_from_file("../img/modificada_limiarizacao.png")
        imagem.show()
    
    
    #Metodo que salva a imagem limiarizada
    def actLimiarizacaoSalvar(self, widget):
        img = Image.open("../img/modificada_limiarizacao.png")
        file = self.fcLimiarizacaoOrigem.get_filename().split("/")
        img.save(self.fcLimiarizacaoDestino.get_filename() + "/limiarizacao-" + file[len(file) - 1])
        


    #Metodos de OPERACOES ARITMETICAS
    
    #Metodo que carrega a imagem no widget de operacoes aritmeticas
    def actOpAritmeticaCarregaImagem1(self, widget):
        imagem = self.gui.get_widget('op_arit_image1')
        imagem.set_from_file(self.fcOpAritmeticaOrigem1.get_filename())
        imagem.show()
        
        
    #Metodo que carrega a imagem no widget de operacoes aritmeticas
    def actOpAritmeticaCarregaImagem2(self, widget):
        imagem = self.gui.get_widget('op_arit_image2')
        imagem.set_from_file(self.fcOpAritmeticaOrigem2.get_filename())
        imagem.show()


    #Metodo que gera a imagem apos ser executado a operacao aritmetica
    def actOpAritmeticaExecutar(self, widget):
        imageManager = ImageManager()
        #Caso a operacao seja de ADICAO
        if (self.rbOpAritmeticaAdicao.get_active()):
            imageManager.operacao_aritmetica_adicao_reescalonamento(self.fcOpAritmeticaOrigem1.get_filename(), self.fcOpAritmeticaOrigem2.get_filename())
        else:
            #Caso a operacao seja de SUBTRACAO
            if (self.rbOpAritmeticaSubtracao.get_active()):
                imageManager.operacao_aritmetica_subtracao(self.fcOpAritmeticaOrigem1.get_filename(), self.fcOpAritmeticaOrigem2.get_filename())
            #Caso a operacao seja de MULTIPLICACAO
            else:
                imageManager.operacao_aritmetica_multiplicacao(self.fcOpAritmeticaOrigem1.get_filename(), self.fcOpAritmeticaOrigem2.get_filename())
                
        imagem = self.gui.get_widget('op_arit_imagem_gerada')
        imagem.set_from_file("../img/modificada_operacao_aritmetica.png")
        imagem.show()
    
    
    #Metodo que salva a imagem apos ser executado a operacao aritmetica
    def actOpAritmeticaSalvar(self, widget):
        img = Image.open("../img/modificada_operacao_aritmetica.png")
        file = self.fcOpAritmeticaOrigem1.get_filename().split("/")
        img.save(self.fcOpAritmeticaDestino.get_filename() + "/operacao-aritmetica-" + file[len(file) - 1])
        
        
        
    #Metodos de OPERACOES LOGICAS
    
    #Metodo que carrega a imagem no widget de operacoes logicas
    def actOpLogicaCarregaImagem1(self, widget):
        imagem = self.gui.get_widget('op_log_image1')
        imagem.set_from_file(self.fcOpLogicaOrigem1.get_filename())
        imagem.show()
        
        
    #Metodo que carrega a imagem no widget de operacoes logicas
    def actOpLogicaCarregaImagem2(self, widget):
        imagem = self.gui.get_widget('op_log_image2')
        imagem.set_from_file(self.fcOpLogicaOrigem2.get_filename())
        imagem.show()


    #Metodo que gera a imagem apos ser executado a operacao logicas
    def actOpLogicaExecutar(self, widget):
        imageManager = ImageManager()
        #Caso a operacao seja de AND
        if (self.rbOpLogicaAnd.get_active()):
            imageManager.operacao_logica_and(self.fcOpLogicaOrigem1.get_filename(), self.fcOpLogicaOrigem2.get_filename())
        else:
            #Caso a operacao seja de OR
            if (self.rbOpLogicaOr.get_active()):
                imageManager.operacao_logica_or(self.fcOpLogicaOrigem1.get_filename(), self.fcOpLogicaOrigem2.get_filename())
            #Caso a operacao seja de XOR
            else:
                imageManager.operacao_logica_xor(self.fcOpLogicaOrigem1.get_filename(), self.fcOpLogicaOrigem2.get_filename())
                
        imagem = self.gui.get_widget('op_log_imagem_gerada')
        imagem.set_from_file("../img/modificada_operacao_logica.png")
        imagem.show()
    
    
    #Metodo que salva a imagem apos ser executado a operacao logicas
    def actOpLogicaSalvar(self, widget):
        img = Image.open("../img/modificada_operacao_logica.png")
        file = self.fcOpLogicaOrigem1.get_filename().split("/")
        img.save(self.fcOpLogicaDestino.get_filename() + "/operacao-logica-" + file[len(file) - 1])



    #Metodos de FILTROS DINAMICOS
    
    #Metodo que carrega a imagem no widget de filtro
    def actFiltroDinCarregaImagem(self, widget):
        imagem = self.gui.get_widget('filtro_din_image_origem')
        imagem.set_from_file(self.fcFiltroDinOrigem.get_filename())
        imagem.show()


    #Metodo que gera a imagem filtrada
    def actFiltroDinExecutar(self, widget):
        imageManager = ImageManager()
        index = self.cbFiltroDin.get_active()
        
        #Verifica qual sera o tamanho da mascara
        if (index == 2) :
            tamanho_matriz = 7
        elif (index == 1) :
            tamanho_matriz = 5
        else :
            tamanho_matriz = 3

        if (self.rbFiltroDinPassaAlta.get_active()):
            imageManager.filtro_passa_alta_basico(self.fcFiltroDinOrigem.get_filename(), tamanho_matriz)
        elif (self.rbFiltroDinMedia.get_active()):
            imageManager.filtro_media(self.fcFiltroDinOrigem.get_filename(), tamanho_matriz)
        elif (self.rbFiltroDinMediana.get_active()):
            imageManager.filtro_mediana(self.fcFiltroDinOrigem.get_filename(), tamanho_matriz)
        else :
            valor_a = self.sbFiltroDin.get_value()
            imageManager.filtro_high_boost(self.fcFiltroDinOrigem.get_filename(), tamanho_matriz, valor_a)
                                
        imagem = self.gui.get_widget('filtro_din_image_gerada')
        imagem.set_from_file("../img/modificada_filtro.png")
        imagem.show()
    
    
    #Metodo que salva a imagem filtrada
    def actFiltroDinSalvar(self, widget):
        img = Image.open("../img/modificada_filtro.png")
        file = self.fcFiltroDinOrigem.get_filename().split("/")
        img.save(self.fcFiltroDinDestino.get_filename() + "/filtro-" + file[len(file) - 1])



    #Metodos de FILTROS 
    
    #Metodo que carrega a imagem no widget de filtro
    def actFiltroCarregaImagem(self, widget):
        imagem = self.gui.get_widget('filtro_image_origem')
        imagem.set_from_file(self.fcFiltroOrigem.get_filename())
        imagem.show()


    #Metodo que gera a imagem filtrada
    def actFiltroExecutar(self, widget):
        imageManager = ImageManager()

        if (self.rbFiltroSobel.get_active()):
            imageManager.filtro_sobel(self.fcFiltroOrigem.get_filename())
        elif (self.rbFiltroRoberts.get_active()):
            imageManager.filtro_roberts(self.fcFiltroOrigem.get_filename())
        else :
            imageManager.filtro_prewitt(self.fcFiltroOrigem.get_filename())
                                
        imagem = self.gui.get_widget('filtro_image_gerada')
        imagem.set_from_file("../img/modificada_filtro.png")
        imagem.show()
        imagem_h = self.gui.get_widget('filtro_image_gerada_h')
        imagem_h.set_from_file("../img/modificada_filtro_h.png")
        imagem_h.show()
        imagem_v = self.gui.get_widget('filtro_image_gerada_v')
        imagem_v.set_from_file("../img/modificada_filtro_v.png")
        imagem_v.show()
    
    
    #Metodo que salva a imagem filtrada
    def actFiltroSalvar(self, widget):
        img = Image.open("../img/modificada_filtro.png")
        file = self.fcFiltroOrigem.get_filename().split("/")
        img.save(self.fcFiltroDestino.get_filename() + "/filtro-" + file[len(file) - 1])


    #Metodo que salva a imagem filtrada
    def actFiltroSalvarHorizontal(self, widget):
        img = Image.open("../img/modificada_filtro_h.png")
        file = self.fcFiltroOrigem.get_filename().split("/")
        img.save(self.fcFiltroDestino_h.get_filename() + "/filtro_h-" + file[len(file) - 1])


    #Metodo que salva a imagem filtrada
    def actFiltroSalvarVertical(self, widget):
        img = Image.open("../img/modificada_filtro_v.png")
        file = self.fcFiltroOrigem.get_filename().split("/")
        img.save(self.fcFiltroDestino_v.get_filename() + "/filtro_v-" + file[len(file) - 1])
        
        
        
    #Metodos de OUTROS
    
    #Metodo que carrega a imagem no widget de outros
    def actOutrosCarregaImagem(self, widget):
        imagem = self.gui.get_widget('out_image_origem')
        imagem.set_from_file(self.fcOutrosOrigem.get_filename())
        imagem.show()
        
    #Metodo que preenche a posicao do pixel clicado na imagem
    def actOutrosPreencherPosicaoPixel(self, widget, event):
        img = Image.open(self.fcOutrosOrigem.get_filename())
        img.load()
        
        if (img.size[0] < 610 and img.size[1] < 481) :
            pixel_x = event.get_coords()[0] - int((625 - img.size[0]) / 2)
            pixel_y = event.get_coords()[1] - int((480 - img.size[1]) / 2)
        elif (img.size[0] < 610) :
            pixel_x = event.get_coords()[0] - int((625 - img.size[0]) / 2)
            pixel_y = event.get_coords()[1]
        elif (img.size[1] < 481) :
            pixel_x = event.get_coords()[0]
            pixel_y = event.get_coords()[1] - int((480 - img.size[1]) / 2)
        else :
            pixel_x = event.get_coords()[0]
            pixel_y = event.get_coords()[1]
        
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        
 
    #Metodo que gera a imagem outros
    def actOutrosExecutar(self, widget, arg):
        imageManager = ImageManager()
        #Caso a opcao seja CRESCIMENTO DE REGIOES
        if (self.rbOutrosCrescimento.get_active()):
            self.txtOutrosVizinhos.set_text(imageManager.outros_crescimento_regioes(self.fcOutrosOrigem.get_filename(), self.hsOutros.get_value(), [int(self.pixel_x), int(self.pixel_y)]))
        #Caso a opcao seja DETECCAO DE BORDAS
        else:
            imageManager.outros_deteccao_de_bordas(self.fcOutrosOrigem.get_filename(), self.hsOutros.get_value())
            
        imagem = self.gui.get_widget('out_image_gerada')
        imagem.set_from_file("../img/modificada_outros.png")
        imagem.show()
    
    
    #Metodo que salva a imagem limiarizada
    def actOutrosSalvar(self, widget):
        img = Image.open("../img/modificada_outros.png")
        file = self.fcOutrosOrigem.get_filename().split("/")
        img.save(self.fcOutrosDestino.get_filename() + "/outros-" + file[len(file) - 1])
        
        
        
#Classe que gerencia a janela Sobre
class Sobre():
    
    
    #Construtor da classe
    def __init__(self):
        
        #Nome do arquivo Glade
        self.__glade_file_sobre = "../xml/sobre.glade"
        gui_sobre = gtk.glade.XML(self.__glade_file_sobre)
        self.gui_sobre = gui_sobre
        
        self.sobre_window = gui_sobre.get_widget("janela_sobre")
        self.sobre_window.connect("destroy", gtk.main_quit)
        
        gui_sobre.get_widget("sobre_fechar").connect("clicked", self.sair)
        
        self.sobre_window.show_all()
        self.loop()
        
        
    #Metodo que fecha o programa
    def sair(self, widget):
        self.sobre_window.destroy()
        
        
    #Metodo da GTK
    def loop(self):
        gtk.main()