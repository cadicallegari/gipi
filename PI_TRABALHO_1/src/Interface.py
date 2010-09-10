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
        self.hsLimiarizacao = gui.get_widget("lim_hscale");
        self.txtLimiarizacaoR = gui.get_widget("lim_txt_r");
        self.txtLimiarizacaoG = gui.get_widget("lim_txt_g");
        self.txtLimiarizacaoB = gui.get_widget("lim_txt_b");
        
        
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
        
        self.main_window.show_all()
        self.loop()


    def actImprimir(self, widget):
        print 1

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
            imageManager.operacao_aritmetica_adicao(self.fcOpAritmeticaOrigem1.get_filename(), self.fcOpAritmeticaOrigem2.get_filename())
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