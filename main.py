import sys
import random  
from PySide6.QtGui import QMovie, QIcon, QPixmap, QPalette, QBrush
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QTextEdit, QHeaderView, QTextBrowser, QLabel, QTableWidgetItem, QMainWindow, QProgressBar, QDialog, QFormLayout, QTableWidget
) 
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer, Signal, Slot, Qt, QSize
import firebase_admin
from firebase_admin import credentials, firestore
from PySide6.QtWidgets import QWidget, QProgressBar
from ui_inicio import Ui_Forms 
from ui_master import Ui_Formmaster 
from ui_juego import Ui_MainWindow 
from ui_personajes import Ui_Formperso
from ui_cargando import Ui_Formcarga 
from ui_jugadores import Ui_Formjugadores

# Inicialización de Firebase con las credenciales proporcionadas
cred = credentials.Certificate("C:/Users/COP405L/Downloads/juegorol-6d13a-firebase-adminsdk-7pr5a-dc589389f3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class MainWindow(QWidget, Ui_Forms):
    """
    Ventana principal de la aplicación. 

    Esta clase gestiona las acciones de los botones en la ventana principal, abriendo diferentes ventanas según la opción seleccionada por el usuario.

    Métodos:
        __init__: Inicializa la ventana principal y configura las conexiones de los botones.
        abrir_master: Abre la ventana del master para gestionar misiones.
        abrir_jugador: Abre la ventana para gestionar personajes.
        abrir_registro: Abre la ventana para registrar nuevos personajes.
    """

    def __init__(self):
        """
        Inicializa la ventana principal y configura las conexiones de los botones.
        """
        super().__init__()
        self.setupUi(self)
        self.btn_master.clicked.connect(self.abrir_master)
        self.btn_jugador.clicked.connect(self.abrir_jugador)
        self.btn_registro.clicked.connect(self.abrir_registro)

    def abrir_master(self):
        """
        Abre la ventana del master para gestionar misiones.
        """
        self.master_window = MasterWindow()
        self.master_window.show()

    def abrir_jugador(self):
        """
        Abre la ventana para gestionar personajes.
        """
        self.master_window = jugadorWindow()
        self.master_window.show()

    def abrir_registro(self):
        """
        Abre la ventana para registrar nuevos personajes.
        """
        self.master_window = PersonajesWindow()
        self.master_window.show()


class jugadorWindow(QWidget, Ui_Formjugadores):
    """
    Ventana para gestionar y mostrar las estadísticas de los personajes.

    Esta clase permite al usuario buscar un personaje por nombre y muestra sus estadísticas y el historial de la bitácora.

    Métodos:
        __init__: Inicializa la ventana de gestión de personajes.
        show_character_stats: Muestra las estadísticas del personaje buscado.
        handle_sala_unida: Maneja la entrada a una sala y actualiza la bitácora.
    """

    def __init__(self):
        """
        Inicializa la ventana de gestión de personajes y configura el manejo del evento de búsqueda del personaje.
        """
        super(jugadorWindow, self).__init__()
        self.setupUi(self)
        self.line_pp.returnPressed.connect(self.show_character_stats)

    def show_character_stats(self):
        """
        Muestra las estadísticas del personaje buscado por el usuario.

        Busca el personaje en la base de datos usando el nombre proporcionado y muestra el nivel, raza, habilidades, poderes, equipamiento y estado. También muestra el historial de la bitácora asociado al personaje.
        """
        nombre_personaje = self.line_pp.text().strip()

        if not nombre_personaje:
            QMessageBox.warning(self, 'Error', 'Introduce el nombre del personaje.')
            return

        personajes_ref = db.collection('personajes').where('nombre', '==', nombre_personaje).limit(1).get()

        if not personajes_ref:
            QMessageBox.warning(self, 'Error', 'Personaje no encontrado.')
            return

        personaje = personajes_ref[0].to_dict()
        nivel = personaje.get('nivel', 'Desconocido')
        raza = personaje.get('raza', 'Desconocida')
        habilidades = personaje.get('habilidades', '')
        poderes = personaje.get('poderes', '')
        equipamiento = personaje.get('equipamiento', 'Ninguno')
        estado = personaje.get('estado', 'Desconocido')

        self.t_nivel.setText(f' {nivel}')
        self.t_raza.setText(f' {raza}')
        self.t_Ha.setPlainText(f' {habilidades}')
        self.t_PO.setPlainText(f' {poderes}')
        self.T_EQ.setText(f' {equipamiento}')
        self.t_estado.setText(f'{estado}')

        bitacora_ref = db.collection('bitacora').where('personajes', 'array_contains', nombre_personaje).get()
        historial = '\n'.join([doc.to_dict().get('texto', '') for doc in bitacora_ref])
        self.t_his.setPlainText(historial)

    @Slot(str)
    def handle_sala_unida(self, nombre_sala):
        """
        Maneja la entrada a una sala de juego y actualiza la bitácora de la sala con un mensaje de entrada del jugador.

        Args:
            nombre_sala (str): El nombre de la sala a la que el jugador se une.
        """
        try:
            sala_ref = db.collection('salas').document(nombre_sala)
            sala_doc = sala_ref.get()
            
            if not sala_doc.exists:
                QMessageBox.warning(self, 'Error', 'Sala no encontrada.')
                return
            bitacora_text = sala_doc.to_dict().get('bitacora', '')
            
            nuevo_mensaje = f'Jugador {self.nombre_jugador} se unió a la sala'
            if bitacora_text:
                bitacora_text += '\n' + nuevo_mensaje
            else:
                bitacora_text = nuevo_mensaje
            
            sala_ref.update({'bitacora': bitacora_text})
            
            self.bitacora_window = BitacoraWindow(nombre_sala)
            self.bitacora_window.show()
        except Exception as e:
            print(f"Error al manejar la sala unida: {e}")

class BitacoraWindow(QDialog):
    """
    Ventana de diálogo para mostrar la bitácora de una sala de juego.

    Esta clase crea una ventana de diálogo que muestra el historial de eventos en una sala específica. La ventana muestra los mensajes registrados en la bitácora de la sala.

    Métodos:
        __init__(nombre_sala): Inicializa la ventana de la bitácora con el historial de la sala especificada.

    Atributos:
        bitacora_text (QTextBrowser): Widget que muestra el texto de la bitácora de la sala.
    """

    def __init__(self, nombre_sala):
        """
        Inicializa la ventana de la bitácora con el historial de la sala especificada.

        Esta función establece el título de la ventana, define su tamaño, y carga el historial de eventos de la bitácora de la sala desde la base de datos de Firebase.

        Args:
            nombre_sala (str): El nombre de la sala cuya bitácora se mostrará en la ventana.
        """
        super().__init__()
        self.setWindowTitle('Bitácora de Sala')
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout(self)
        
        # Crea un QTextBrowser para mostrar el texto de la bitácora
        self.bitacora_text = QTextBrowser(self)
        self.bitacora_text.setOpenExternalLinks(True)  # Permite abrir enlaces externos en el QTextBrowser
        self.layout.addWidget(self.bitacora_text)
        
        # Obtiene la referencia a la colección 'salas' y el documento correspondiente a la sala especificada
        sala_ref = db.collection('salas').document(nombre_sala)
        sala_doc = sala_ref.get()
        
        # Obtiene el texto de la bitácora de la sala desde la base de datos
        bitacora_text = sala_doc.to_dict().get('bitacora', '')
        
        # Establece el texto de la bitácora en el QTextBrowser
        self.bitacora_text.setPlainText(bitacora_text)

class MasterWindow(QWidget, Ui_Formmaster):
    """
    Ventana principal para gestionar misiones y aventuras en el juego.

    Esta clase representa la ventana principal para los administradores de misiones en el juego. Permite al usuario continuar aventuras existentes, crear nuevas misiones y acceder a la pantalla de carga para avanzar en las aventuras.

    Métodos:
        __init__(self): Inicializa la ventana principal del master y configura los eventos de los botones.
        continuar_aventura(self): Cambia a la página para continuar una aventura existente.
        actualizar_referencia(self): Actualiza el contenido de la referencia de la sala basada en el nombre ingresado por el usuario.
        sigue_la_aventura(self): Muestra una ventana de carga y cambia a la pantalla del juego para una aventura existente.
        up_progress(self, nombre_sala): Actualiza el progreso de la barra de carga y abre la ventana del juego cuando el progreso alcanza el 100%.
        crear_nueva(self): Cambia a la página para crear una nueva misión.
        nueva_mission(self): Crea una nueva misión en la base de datos y muestra una ventana de carga mientras se actualiza el progreso.
        update_progress(self, nombre_sala): Actualiza el progreso de la barra de carga y abre la ventana del juego cuando el progreso alcanza el 100%.
        go_juego(self, nombre_sala): Cambia a la pantalla del juego para una nueva misión y actualiza el nombre de la sala actual.

    Atributos:
        btn_continuar (QPushButton): Botón para continuar una aventura existente.
        btn_nueva (QPushButton): Botón para crear una nueva misión.
        btn_crear (QPushButton): Botón para agregar una nueva misión en la base de datos.
        btn_inicio (QPushButton): Botón para iniciar una nueva aventura.
        nombre_sala (QLineEdit): Campo de texto para ingresar el nombre de la sala de juego.
        text_refe (QTextEdit): Área de texto para mostrar el contenido de la sala o los detalles de la referencia.
        tex_nuevo (QLineEdit): Campo de texto para ingresar el texto de la nueva misión.
        text_sala (QLineEdit): Campo de texto para ingresar el nombre de la sala para una nueva misión.
        stackedWidget (QStackedWidget): Widget de apilamiento para cambiar entre diferentes páginas de la ventana.
        page (QWidget): Página para la creación de nuevas misiones.
        page_2 (QWidget): Página para continuar una aventura existente.
        cargando_window (CargandoWindow): Ventana de carga mostrada mientras se actualiza el progreso.
        progress (int): Variable para almacenar el progreso de la barra de carga.
        timer (QTimer): Temporizador para actualizar la barra de carga.
        juego_window (JuegoWindow): Ventana de juego que se muestra cuando se continúa una aventura o se inicia una nueva misión.

    Excepciones:
        Captura errores de conexión o recuperación de datos de Firebase y muestra un mensaje de error adecuado al usuario.
    """

    def __init__(self):
        """
        Inicializa la ventana principal del master y configura los eventos de los botones.

        Configura los eventos de los botones para manejar las acciones de continuar aventuras, crear nuevas misiones y gestionar la carga de las misiones.
        """
        super(MasterWindow, self).__init__()
        self.setupUi(self)
        self.btn_continuar.clicked.connect(self.continuar_aventura)
        self.btn_nueva.clicked.connect(self.crear_nueva)
        self.btn_crear.clicked.connect(self.nueva_mission)
        self.btn_inicio.clicked.connect(self.sigue_la_aventura)  

        self.nombre_sala.returnPressed.connect(self.actualizar_referencia)

    def continuar_aventura(self):
        """
        Cambia a la página para continuar una aventura existente.

        Este método cambia el widget actual a la página para continuar una aventura existente, mostrando la interfaz para la gestión de aventuras.
        """
        self.stackedWidget.setCurrentWidget(self.page_2)

    def actualizar_referencia(self):
        """
        Actualiza el contenido de la referencia de la sala basada en el nombre ingresado por el usuario.

        Recupera los datos de la sala desde Firebase usando el nombre ingresado y muestra el último texto añadido, penalización y recompensa en el área de texto correspondiente.
        """
        nombre_sala = self.nombre_sala.text().strip()  
        if nombre_sala:
            sala_id = f'unico_{nombre_sala}'  
            doc_ref = db.collection('PUNTOGUARDADO').document(sala_id)  

            try:
                doc = doc_ref.get()  #
                if doc.exists:
                    data = doc.to_dict()  

                    textos = []
                    for key in data:
                        if key.startswith('texto'):
                            textos.append(data[key])
                 
                    if textos:
                        ultimo_texto = textos[-1]  
                        texto_mostrar = f"Último texto añadido:\n{ultimo_texto}\n\n"
                    else:
                        ultimo_texto = ''
                        texto_mostrar = "No hay textos añadidos.\n\n"
                  
                    penalizacion = data.get('penalizacion', '')
                    recompensa = data.get('recompensa', '')

                    if penalizacion or recompensa:
                        texto_mostrar += f"Penalización: {penalizacion}\n" if penalizacion else ""
                        texto_mostrar += f"Recompensa: {recompensa}\n" if recompensa else ""

                    self.text_refe.setPlainText(texto_mostrar)  
                    print(f"Último texto añadido: {ultimo_texto}") 
                    print(f"Penalización: {penalizacion}")  
                    print(f"Recompensa: {recompensa}")  
                else:
                    self.text_refe.setPlainText('La sala no existe.') 
                    print(f"La sala '{nombre_sala}' no existe.") 
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al recuperar los datos de la sala: {e}')
                print(f"Excepción al recuperar los datos de la sala: {e}") 
    
            print("Nombre de sala vacío.")  

    def sigue_la_aventura(self):
        """
        Muestra una ventana de carga y cambia a la pantalla del juego para una aventura existente.

        Muestra una ventana de carga mientras se actualiza el progreso, y luego cambia a la pantalla del juego para la sala especificada por el usuario.
        """
        self.cargando_window = CargandoWindow()
        self.cargando_window.show()
        self.progress = 0
        
        nombre_sala = self.nombre_sala.text().strip()  
        if nombre_sala:
            sala_id = f'unico_{nombre_sala}'  
            doc_ref = db.collection('PUNTOGUARDADO').document(sala_id)  
            
            try:
                doc = doc_ref.get()  
                if doc.exists:
                    data = doc.to_dict()  
                    texto_sala = data.get('contenido', '')  

                    self.text_refe.setPlainText(texto_sala)

                    self.timer = QTimer(self)
                    self.timer.timeout.connect(lambda: self.up_progress(nombre_sala)) 
                    self.timer.start(30)  
                else:
                    QMessageBox.warning(self, 'Error', 'La sala no existe.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al recuperar los datos de la sala: {e}')
        else:
            QMessageBox.warning(self, 'Error', 'Por favor, ingresa el nombre de la sala.')
        self.close()

    def up_progress(self, nombre_sala):
        """
        Actualiza el progreso de la barra de carga y abre la ventana del juego cuando el progreso alcanza el 100%.

        Este método aumenta el progreso de la barra de carga y, cuando llega al 100%, detiene el temporizador y abre la ventana del juego.
        """
        self.progress += 1
        if self.progress >= 100:
            self.timer.stop()
            self.cargando_window.close()
            
            self.juego_window = JuegoWindow(nombre_sala) 
            self.juego_window.sala_name.setText(f"Sala Actual: {nombre_sala}")  
            self.juego_window.show()  
        else:
            self.cargando_window.barra_cargado.setValue(self.progress)

    def crear_nueva(self):
        """
        Cambia a la página para crear una nueva misión.

        Este método cambia el widget actual a la página donde el usuario puede ingresar los detalles de una nueva misión.
        """
        self.stackedWidget.setCurrentWidget(self.page)

    def nueva_mission(self):
        """
        Crea una nueva misión en la base de datos y muestra una ventana de carga mientras se actualiza el progreso.

        Este método toma el texto de la nueva misión y el nombre de la sala, crea una nueva entrada en la base de datos y muestra una ventana de carga mientras se actualiza el progreso.
        """
        tex_nuevo = self.tex_nuevo.text().strip()
        nombre_sala = self.text_sala.text().strip()

        if not tex_nuevo or not nombre_sala:
            QMessageBox.warning(self, 'Error', 'Introduce el nombre de la sala y el texto de la nueva misión.')
            return

        salas_ref = db.collection('PUNTOGUARDADO')
        salas_ref.add({
            'nombre': nombre_sala,
            'contenido': tex_nuevo,
            'misiones': [], 
        })

        self.cargando_window = CargandoWindow()
        self.cargando_window.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_progress(nombre_sala)) 
        self.progress = 0
        self.timer.start(30)  
        self.close()

    def update_progress(self, nombre_sala):
        """
        Actualiza el progreso de la barra de carga y abre la ventana del juego cuando el progreso alcanza el 100%.

        Este método aumenta el progreso de la barra de carga y, cuando llega al 100%, detiene el temporizador y abre la ventana del juego.
        """
        self.progress += 1
        if self.progress >= 100:
            self.timer.stop()
            self.go_juego(nombre_sala)
        else:
            self.cargando_window.barra_cargado.setValue(self.progress)

    def go_juego(self, nombre_sala):
        """
        Cambia a la pantalla del juego para una nueva misión y actualiza el nombre de la sala actual.

        Este método cambia a la ventana de juego para la nueva misión creada y actualiza el nombre de la sala actual.
        """
        self.juego_window = JuegoWindow(nombre_sala)
        self.juego_window.sala_name.setText("Sala Actual: " + nombre_sala)
        self.juego_window.show()
        self.cargando_window.close()

class JuegoWindow(QMainWindow, Ui_MainWindow):
    """
    Ventana principal del juego que gestiona la interfaz del usuario y las interacciones del juego.

    Hereda de QMainWindow y Ui_MainWindow para proporcionar la funcionalidad de una ventana principal
    y usar el diseño definido en Ui_MainWindow.

    Atributos:
    ----------
    nombre_sala : QLabel
        Etiqueta que muestra el nombre de la sala actual del juego.
    contador_giros : int
        Contador para llevar la cuenta de las acciones realizadas en el juego.
    animations : dict
        Diccionario que mapea índices a rutas de imágenes para diferentes fondos de pantalla.
    tabla_personajes_agregada : bool
        Bandera para verificar si la tabla de personajes ha sido agregada a la interfaz.

    Métodos:
    --------
    __init__(self, nombre_sala, parent=None):
        Inicializa la ventana principal del juego y configura la interfaz de usuario.

    ventana_dados(self):
        Abre una nueva ventana para lanzar dados.

    mision_seleccionada(self):
        Busca una misión por su nombre en la base de datos y muestra el resultado.

    mostrar_mision_resultado(self, snapshot):
        Muestra los detalles de la misión encontrada en la búsqueda.

    manejar_error_mision(self, error):
        Muestra un mensaje de error si ocurre un problema durante la búsqueda de una misión.
    """

    def __init__(self, nombre_sala, parent=None):
        """
        Inicializa la ventana principal del juego y configura la interfaz de usuario.

        Parámetros:
        -----------
        nombre_sala : str
            El nombre de la sala actual del juego que se mostrará en la interfaz.
        parent : QWidget, opcional
            El widget padre para esta ventana. Por defecto es None.

        Configura los botones, conexiones de señales y otros elementos de la interfaz de usuario.
        """
        super(JuegoWindow, self).__init__(parent)
        self.setupUi(self)

        self.nombre_sala = QLabel(nombre_sala, self)  
        self.setWindowTitle(f'Juego - Sala: {self.nombre_sala.text()}')  
        self.sala_name.setText(f"Sala Actual: {self.nombre_sala.text()}")  

        self.btn_envio_2.clicked.connect(self.send_text_to_vita)
        self.btn_guardado.clicked.connect(self.save_bitacora)
        self.btn_his.clicked.connect(self.open_bitacora_history)
        self.btn_dados.clicked.connect(self.ventana_dados)

        self.btn_aleatorio.clicked.connect(self.mision_aleatoria)

        self.btn_m.clicked.connect(self.show_pagina_1)
        self.btn_crear.clicked.connect(self.show_pagina_2)
        self.btn_tpa.clicked.connect(self.show_pagina_3)
        self.btn_md.clicked.connect(self.show_pagina_4)
        self.btn_pp.clicked.connect(self.show_pagina_5)

        self.b_ms.returnPressed.connect(self.mision_seleccionada)
        self.btn_mison.clicked.connect(self.mision_seleccionada)

        self.contador_giros = 0

        self.animations = {
            0: "fondos/fantasia.jpg",
            1: "fondos/mundo flotante.jpg",
            2: "fondos/mundo funki.jpg",
            3: "fondos/reino desconocido.jpg",
            4: "fondos/jefe.webp",
            5: "fondos/jefe dragon.jpg",
            6: "fondos/cosmo.jpg",
        }
    
        self.comboBox_2.currentIndexChanged.connect(self.cambio_etapa)

        self.sala_name.setText("Sala Actual: " + self.sala_name.text())
        self.tabla_personajes_agregada = False

    def ventana_dados(self):
        """
        Abre una nueva ventana para lanzar dados.

        Crea una instancia de DiceWindow y la muestra al usuario.
        """
        self.dice_window = DiceWindow()
        self.dice_window.show()

    def mision_seleccionada(self):
        """
        Busca una misión por su nombre en la base de datos y muestra el resultado.

        Recupera el nombre de la misión desde un campo de texto, realiza una búsqueda en la colección de eventos
        en la base de datos y llama a `mostrar_mision_resultado` para mostrar los detalles de la misión encontrada.

        Si no se ingresa un nombre de misión o hay un error en la consulta, muestra un mensaje de advertencia o error.
        """
        nombre_mision = self.b_ms.text().strip()

        if not nombre_mision:
            QMessageBox.warning(self, 'Campo Vacío', 'Por favor, ingresa el nombre de la misión que deseas buscar.')
            return

        eventos_ref = db.collection('evento')
        query = eventos_ref.where('nombre', '==', nombre_mision).limit(1)
        
        try:
            snapshot = query.get()
            self.mostrar_mision_resultado(snapshot)
        except Exception as e:
            self.manejar_error_mision(e)

    def mostrar_mision_resultado(self, snapshot):
        """
        Muestra los detalles de la misión encontrada en la búsqueda.

        Parámetros:
        -----------
        snapshot : list
            Lista de documentos de misión obtenidos de la búsqueda en la base de datos.

        Si se encuentra una misión, extrae los detalles como nombre, descripción, condiciones y recompensa, 
        y llama a `mostrar_ventana_mision_selec` para mostrar esos detalles al usuario.

        Si no se encuentra ninguna misión, muestra un mensaje de advertencia.
        """
        if not snapshot:
            QMessageBox.warning(self, 'Misión No Encontrada', 'No se encontró ninguna misión con el nombre proporcionado.')
            return

        mision = snapshot[0].to_dict()
        nombre = mision.get('nombre')
        descripcion = mision.get('descripcion')
        condiciones = mision.get('condiciones')
        recompensa = mision.get('recompensa')

        self.mostrar_ventana_mision_selec(nombre, descripcion, condiciones, recompensa)

    def manejar_error_mision(self, error):
        """
        Muestra un mensaje de error si ocurre un problema durante la búsqueda de una misión.

        Parámetros:
        -----------
        error : Exception
            La excepción capturada durante la búsqueda de la misión.

        Muestra un mensaje crítico con detalles sobre el error.
        """
        QMessageBox.critical(self, 'Error de Consulta', f'Ocurrió un error al buscar la misión: {error}')


    def mostrar_ventana_mision_selec(self, nombre, descripcion, condiciones, recompensa):
        """
        Muestra una ventana de misión con opciones de victoria o derrota.

        Parámetros:
        -----------
        nombre : str
            El nombre de la misión a mostrar.
        descripcion : str
            La descripción detallada de la misión.
        condiciones : str
            Las condiciones necesarias para completar la misión.
        recompensa : str
            La recompensa ofrecida por completar la misión.

        Esta función crea una ventana emergente (`QWidget`) que muestra la información de la misión actual, 
        incluyendo su nombre, descripción, condiciones y recompensa. También proporciona dos botones para 
        manejar el resultado de la misión: "Victoria" y "Derrota".

        El botón "Victoria" llama a `victoria_mision_selec` con el nombre de la misión y la recompensa, 
        mientras que el botón "Derrota" llama a `derrota_mision_selec`.

        La ventana se diseña con un fondo de pergamino y un estilo que recuerda al papel antiguo.

        Ejemplos:
        ---------
        >>> self.mostrar_ventana_mision_selec("Misión de Prueba", "Descripción de la misión", "Condiciones necesarias", "Recompensa obtenida")
        """
        mision_dialog = QWidget()
        mision_dialog.setWindowTitle("Misión")
        mision_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  
        layout.setSpacing(15)  

        sala_text = QLabel(f": {self.sala_name.text()}", self)
        evento_info = QLabel(f"Nombre: {nombre}\nDescripción:\n {descripcion}\nCondiciones:\n{condiciones}\nRecompensa:\n {recompensa}", self)
        evento_info.setWordWrap(True)  
        layout.addWidget(evento_info)

        btn_victoria = QPushButton("Victoria", self)
        btn_victoria.setStyleSheet("background-color: green; color: white;")
        btn_derrota = QPushButton("Derrota", self)
        btn_derrota.setStyleSheet("background-color: red; color: white;")

        layout.addWidget(btn_victoria)
        layout.addWidget(btn_derrota)

        mision_dialog.setLayout(layout)
        mision_dialog.show()

        btn_victoria.clicked.connect(lambda: self.victoria_mision_selec(nombre, recompensa, mision_dialog))
        btn_derrota.clicked.connect(lambda: self.derrota_mision_selec(mision_dialog))

    def victoria_mision_selec(self, nombre, recompensa, dialog):
        """
        Maneja la victoria en la misión y guarda la recompensa.

        Parámetros:
        -----------
        nombre : str
            El nombre de la misión ganada.
        recompensa : str
            La recompensa obtenida por completar la misión.
        dialog : QWidget
            La ventana de misión que se debe cerrar después de manejar la victoria.

        Esta función cierra la ventana de misión (`dialog`) y llama a `guardar_recompensa` para registrar 
        la recompensa de la misión ganada.

        Ejemplos:
        ---------
        >>> self.victoria_mision_selec("Misión de Prueba", "1000 Oro", mision_dialog)
        """
        dialog.close()
        
        self.guardar_recompensa(nombre, recompensa)

    def derrota_mision_selec(self, dialog):
        """
        Maneja la derrota en la misión y muestra la ventana de penalización.

        Parámetros:
        -----------
        dialog : QWidget
            La ventana de misión que se debe cerrar después de manejar la derrota.

        Esta función cierra la ventana de misión (`dialog`) y llama a `mostrar_penalizacion_selec` 
        para mostrar la ventana de penalización al jugador.

        Ejemplos:
        ---------
        >>> self.derrota_mision_selec(mision_dialog)
        """
        dialog.close()
        
        self.mostrar_penalizacion_selec()

    def mostrar_penalizacion_selec(self):
        """
        Muestra una ventana de ruleta para elegir una penalización.

        Esta función crea una ventana emergente (`QWidget`) que muestra una penalización aleatoria 
        obtenida de la base de datos. La ventana muestra el nombre, descripción, efecto y el lanzamiento 
        de dado asociado a la penalización.

        La ventana se diseña con un fondo de pergamino y un estilo que recuerda al papel antiguo. 
        También proporciona un botón para cerrar la ventana.

        Ejemplos:
        ---------
        >>> self.mostrar_penalizacion_selec()
        """
        penalizacion_dialog = QWidget()
        penalizacion_dialog.setWindowTitle("Penalización")
        penalizacion_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  
        layout.setSpacing(15) 

        sala_text = QLabel(f"Sala Actual: {self.sala_name.text()}", self)
        layout.addWidget(sala_text)

        penalizaciones_ref = db.collection('penalizaciones')
        penalizaciones = penalizaciones_ref.stream()
        penalizacion_list = [penalizacion.to_dict() for penalizacion in penalizaciones]

        if not penalizacion_list:
            QMessageBox.warning(self, 'Sin Penalizaciones', 'No hay penalizaciones disponibles en la base de datos.')
            return

        penalizacion = random.choice(penalizacion_list)
        penalizacion_info = QLabel(f"Nombre: {penalizacion['nombre']}\nDescripción: {penalizacion['descripcion']}\nEfecto: {penalizacion['efecto']}\nLanzamiento Dado: {penalizacion['lanzamiento_dado']}", self)
        penalizacion_info.setWordWrap(True)  
        layout.addWidget(penalizacion_info)

        btn_cerrar = QPushButton("Cerrar", self)
        btn_cerrar.setStyleSheet("background-color: red; color: white;")

        layout.addWidget(btn_cerrar)

        penalizacion_dialog.setLayout(layout)
        penalizacion_dialog.show()

        btn_cerrar.clicked.connect(lambda: self.guardar_penalizacion_selec(penalizacion, penalizacion_dialog))
    def guardar_penalizacion_selec(self, penalizacion, dialog):
        """
        Guarda la penalización en la base de datos.

        Parámetros:
        -----------
        penalizacion : dict
            Diccionario con los detalles de la penalización. Debe contener al menos la clave 'descripcion' con la descripción de la penalización.
        dialog : QWidget
            La ventana de penalización que se debe cerrar después de manejar la penalización.

        Esta función cierra la ventana de penalización (`dialog`) y actualiza el documento de la sala actual en 
        la colección `PUNTOGUARDADO` con la descripción de la penalización. Si la actualización es exitosa, se 
        muestra un mensaje de información; si ocurre un error, se muestra un mensaje de error.

        Ejemplos:
        ---------
        >>> self.guardar_penalizacion_selec({'descripcion': 'Pierdes 100 Oro'}, penalizacion_dialog)
        """
        dialog.close()
        sala = self.sala_name.text().replace('Sala Actual: ', '')
        doc_id = f'unico_{sala}'

        try:
            doc_ref = db.collection('PUNTOGUARDADO').document(doc_id)
            doc_ref.update({
                'penalizacion': penalizacion['descripcion']
            })
            QMessageBox.information(self, 'Penalización', f'Penalización: {penalizacion["descripcion"]}')
        except Exception as e:
            QMessageBox.critical(self, 'Error de Actualización', f'Ocurrió un error al guardar la penalización: {e}')


    def guardar_recompensa(self, nombre, recompensa):
        """
        Guarda la recompensa en la base de datos.

        Parámetros:
        -----------
        nombre : str
            El nombre de la misión ganada.
        recompensa : str
            La recompensa obtenida por completar la misión.

        Esta función actualiza el documento de la sala actual en la colección `PUNTOGUARDADO` con la recompensa 
        obtenida por completar una misión. Si la actualización es exitosa, se muestra un mensaje de victoria; 
        si ocurre un error, se muestra un mensaje de error.

        Ejemplos:
        ---------
        >>> self.guardar_recompensa("Misión de Prueba", "1000 Oro")
        """
        sala = self.sala_name.text().replace('Sala Actual: ', '')
        doc_id = f'unico_{sala}'

        try:
            doc_ref = db.collection('PUNTOGUARDADO').document(doc_id)
            doc_ref.update({
                'recompensa': recompensa
            })
            QMessageBox.information(self, 'Victoria', f'¡Has ganado! Recompensa: {recompensa}')
        except Exception as e:
            QMessageBox.critical(self, 'Error de Actualización', f'Ocurrió un error al guardar la recompensa: {e}')


    def mision_aleatoria(self):
        """
        Selecciona una misión al azar de la base de datos y muestra la ruleta.

        Esta función obtiene una lista de eventos de la colección `evento` en la base de datos, elige uno al azar 
        y llama al método `mostrar_ruleta` para presentar una ventana de ruleta con opciones de aceptar, rechazar 
        o girar otra vez la ruleta.

        Ejemplos:
        ---------
        >>> self.mision_aleatoria()
        """
        eventos_ref = db.collection('evento')
        eventos = eventos_ref.stream()
        evento_list = [evento.to_dict() for evento in eventos]

        if not evento_list:
            QMessageBox.warning(self, 'Sin Eventos', 'No hay eventos disponibles en la base de datos.')
            return

        self.evento_list = evento_list
        evento = random.choice(evento_list)
        self.mostrar_ruleta(evento)


    def mostrar_ruleta(self, evento):
        """
        Muestra una ventana de ruleta con opciones de aceptar, rechazar o girar otra vez.

        Parámetros:
        -----------
        evento : dict
            Diccionario con los detalles del evento. Debe contener las claves 'nombre', 'descripcion', 'condiciones', 
            y 'recompensa' con la información de la misión.

        Esta función crea una ventana de diálogo que muestra los detalles del evento actual, incluyendo su nombre, 
        descripción, condiciones y recompensa. También proporciona tres botones para manejar el evento: "Aceptar", 
        "Rechazar" y "Girar Otra Vez". El botón "Girar Otra Vez" solo está habilitado si el número de giros es menor que 2.

        Ejemplos:
        ---------
        >>> self.mostrar_ruleta({'nombre': 'Misión de Prueba', 'descripcion': 'Descripción de la misión', 'condiciones': 'Condiciones necesarias', 'recompensa': 'Recompensa obtenida'})
        """
        ruleta_dialog = QWidget()
        ruleta_dialog.setWindowTitle("Ruleta de Eventos")
        ruleta_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        """)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Agregar márgenes
        layout.setSpacing(15)  # Agregar espaciado

        sala_text = QLabel(f"Sala Actual: {self.sala_name.text()}", self)
        evento_info = QLabel(f"Nombre: {evento['nombre']}\nDescripción:\n {evento['descripcion']}\nCondiciones:\n {evento['condiciones']}\nRecompensa:\n {evento['recompensa']}", self)
        evento_info.setWordWrap(True)  # Habilitar el ajuste de línea
        layout.addWidget(sala_text)
        layout.addWidget(evento_info)

        btn_aceptar = QPushButton("Aceptar", self)
        btn_aceptar.setStyleSheet("background-color: green; color: white;")
        btn_rechazar = QPushButton("Rechazar", self)
        btn_rechazar.setStyleSheet("background-color: red; color: white;")
        btn_girar = QPushButton("Girar Otra Vez", self)
        btn_girar.setStyleSheet("background-color: purple; color: white;")
        btn_girar.setEnabled(self.contador_giros < 2)

        layout.addWidget(btn_aceptar)
        layout.addWidget(btn_rechazar)
        layout.addWidget(btn_girar)

        ruleta_dialog.setLayout(layout)
        ruleta_dialog.show()

        btn_aceptar.clicked.connect(lambda: self.aceptar_mision(evento, ruleta_dialog))
        btn_rechazar.clicked.connect(lambda: self.rechazar_mision(ruleta_dialog))
        btn_girar.clicked.connect(lambda: self.girar_otra_vez(btn_girar, ruleta_dialog))

    def aceptar_mision(self, evento, dialog):
        """
        Acepta la misión y muestra la ventana de victoria o derrota.

        Este método cierra el diálogo actual y llama a `mostrar_ventana_mision` para mostrar una nueva ventana 
        con las opciones de victoria o derrota basadas en el evento de la misión aceptada.

        Parámetros:
        -----------
        evento : dict
            Diccionario con los detalles del evento. Debe contener las claves 'nombre', 'descripcion', 'condiciones', 
            y 'recompensa' con la información de la misión.
        dialog : QWidget
            La ventana de la ruleta que se debe cerrar después de aceptar la misión.

        Ejemplos:
        ---------
        >>> self.aceptar_mision({'nombre': 'Misión de Prueba', 'descripcion': 'Descripción de la misión', 'condiciones': 'Condiciones necesarias', 'recompensa': 'Recompensa obtenida'}, ruleta_dialog)
        """
        dialog.close()
        self.mostrar_ventana_mision(evento)


    def rechazar_mision(self, dialog):
        """
        Rechaza la misión y muestra la ventana de penalización.

        Este método cierra el diálogo actual y llama a `mostrar_penalizacion` para mostrar una nueva ventana 
        donde se puede definir una penalización por rechazar la misión.

        Parámetros:
        -----------
        dialog : QWidget
            La ventana de la ruleta que se debe cerrar después de rechazar la misión.

        Ejemplos:
        ---------
        >>> self.rechazar_mision(ruleta_dialog)
        """
        dialog.close()
        self.mostrar_penalizacion()


    def girar_otra_vez(self, btn_girar, dialog):
        """
        Permite girar la ruleta otra vez, con un máximo de 2 giros.

        Este método incrementa el contador de giros y selecciona un nuevo evento de la lista de eventos. Si el número 
        de giros alcanza 2, deshabilita el botón para girar nuevamente.

        Parámetros:
        -----------
        btn_girar : QPushButton
            El botón para girar la ruleta que se deshabilitará si se alcanza el límite de giros.
        dialog : QWidget
            La ventana de la ruleta que se debe cerrar después de girar nuevamente.

        Ejemplos:
        ---------
        >>> self.girar_otra_vez(btn_girar, ruleta_dialog)
        """
        self.contador_giros += 1
        if self.contador_giros >= 2:
            btn_girar.setEnabled(False)

        evento = random.choice(self.evento_list)  # Seleccionar un nuevo evento
        dialog.close()
        self.mostrar_ruleta(evento)


    def mostrar_ventana_mision(self, evento):
        """
        Muestra la ventana de misión con opciones de victoria o derrota.

        Este método crea una ventana de diálogo que muestra los detalles de la misión actual, incluyendo su nombre, 
        descripción, condiciones y recompensa. También proporciona botones para aceptar la victoria o la derrota en 
        la misión.

        Parámetros:
        -----------
        evento : dict
            Diccionario con los detalles del evento. Debe contener las claves 'nombre', 'descripcion', 'condiciones', 
            y 'recompensa' con la información de la misión.

        Ejemplos:
        ---------
        >>> self.mostrar_ventana_mision({'nombre': 'Misión de Prueba', 'descripcion': 'Descripción de la misión', 'condiciones': 'Condiciones necesarias', 'recompensa': 'Recompensa obtenida'})
        """
        mision_dialog = QWidget()
        mision_dialog.setWindowTitle("Misión")
        mision_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Agregar márgenes
        layout.setSpacing(15)  # Agregar espaciado

        sala_text = QLabel(f" {self.sala_name.text()}", self)
        evento_info = QLabel(f"Nombre: {evento['nombre']}\nDescripción:\n {evento['descripcion']}\nCondiciones:\n {evento['condiciones']}\nRecompensa:\n {evento['recompensa']}", self)
        evento_info.setWordWrap(True)  # Habilitar el ajuste de línea
        layout.addWidget(sala_text)
        layout.addWidget(evento_info)

        btn_victoria = QPushButton("Victoria", self)
        btn_victoria.setStyleSheet("""
            background-color: green; 
            color: white; 
            border: 2px solid #003300; /* Borde verde oscuro */
            border-radius: 5px; 
            padding: 12px 20px; 
            font-weight: bold; 
            min-width: 120px; 
            text-align: center; 
        """)
        btn_derrota = QPushButton("Derrota", self)
        btn_derrota.setStyleSheet("""
            background-color: red; 
            color: white; 
            border: 2px solid #660000; /* Borde rojo oscuro */
            border-radius: 5px; 
            padding: 12px 20px; 
            font-weight: bold; 
            min-width: 120px; 
            text-align: center; 
        """)

        layout.addWidget(btn_victoria)
        layout.addWidget(btn_derrota)

        mision_dialog.setLayout(layout)
        mision_dialog.show()

        btn_victoria.clicked.connect(lambda: self.victoria_mision(evento, mision_dialog))
        btn_derrota.clicked.connect(lambda: self.derrota_mision(evento, mision_dialog))

        # Estilo para tabla_personajes
        self.tabla_personajes.setStyleSheet("""
            background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
            QTableWidget {
                border: 2px solid red; /* Borde exterior rojo */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 5px; /* Espaciado interno */
            }
            QHeaderView::section {
                background-color: #DCE8F5; /* Color de fondo de las cabeceras */
                color: #000000; /* Color del texto en las cabeceras */
                padding: 10px; /* Espaciado interno de las cabeceras */
                border: 1px solid #a0a0a0; /* Borde de las cabeceras */
            }
            QPushButton {
                background-color: #FFD700; /* Color de fondo dorado */
                color: #000000; /* Color del texto */
                border: 2px solid #DAA520; /* Borde dorado oscuro */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 12px 20px; /* Espaciado interno del botón */
                font-weight: bold; /* Texto en negrita */
                min-width: 120px; /* Ancho mínimo del botón */
                text-align: center; /* Alinear el texto al centro */
            }
            QPushButton:hover {
                background-color: #FFC107; /* Color de fondo dorado al pasar el ratón */
            }
            QPushButton:pressed {
                background-color: #FFA000; /* Color de fondo dorado oscuro al presionar */
            }
        """)

    def victoria_mision(self, evento, dialog):
        """
        Maneja la victoria en la misión y guarda la recompensa en la base de datos.

        Este método se llama cuando el jugador completa exitosamente una misión. 
        Actualiza el documento correspondiente en la colección `PUNTOGUARDADO` 
        con la recompensa obtenida por el jugador. Luego, muestra un mensaje 
        de victoria con la recompensa.

        **Parametros**:
        - `evento` (dict): Un diccionario con los detalles del evento de la misión ganada. 
          Ejemplo:
          ```python
          evento = {
              'nombre': 'Rescatar al aldeano',
              'descripcion': 'Has rescatado al aldeano perdido en el bosque.',
              'condiciones': 'Debes tener al menos 100 puntos de vida.',
              'recompensa': '1000 monedas de oro'
          }
          ```
        - `dialog` (QWidget): La ventana de diálogo actual de la misión que se va a cerrar.

        **Ejemplo de uso**:
        ```python
        self.victoria_mision(evento, mision_dialog)
        ```

        **Exceptions**:
        - Lanza `Exception` si ocurre un error al actualizar el documento en Firestore.
        """
        dialog.close()  # Cierra el diálogo de misión
        recompensa = evento['recompensa']
        sala = self.sala_name.text().replace('Sala Actual: ', '')
        doc_id = f'unico_{sala}'  # Nombre único del documento basado en la sala

        try:
            # Actualiza el documento existente en la colección PUNTOGUARDADO
            doc_ref = db.collection('PUNTOGUARDADO').document(doc_id)
            doc_ref.update({
                'recompensa': recompensa
            })
            QMessageBox.information(self, 'Victoria', f'¡Has ganado! Recompensa: {recompensa}')
        except Exception as e:
            QMessageBox.critical(self, 'Error de Actualización', f'Ocurrió un error al guardar la recompensa: {e}')

    def derrota_mision(self, evento, dialog):
        """
        Maneja la derrota en la misión y muestra la ventana de penalización.

        Este método se llama cuando el jugador falla en una misión. Cierra el diálogo
        actual de la misión y muestra una ventana para seleccionar una penalización.

        **Parametros**:
        - `evento` (dict): Un diccionario con los detalles del evento de la misión fallida. 
          Ejemplo:
          ```python
          evento = {
              'nombre': 'Rescatar al aldeano',
              'descripcion': 'No lograste rescatar al aldeano perdido en el bosque.',
              'condiciones': 'Debes tener al menos 100 puntos de vida.',
              'recompensa': '1000 monedas de oro'
          }
          ```
        - `dialog` (QWidget): La ventana de diálogo actual de la misión que se va a cerrar.

        **Ejemplo de uso**:
        ```python
        self.derrota_mision(evento, mision_dialog)
        ```

        **Exceptions**:
        - No se esperan excepciones, pero puede ocurrir un error en la carga de la penalización.
        """
        dialog.close()  # Cierra el diálogo de misión
        self.mostrar_penalizacion()  # Muestra la ventana de penalización

    def mostrar_penalizacion(self):
        """
        Muestra una ventana de penalización con una opción para seleccionar una penalización aleatoria.

        Este método crea una ventana de diálogo que presenta una penalización aleatoria 
        de la base de datos. El jugador puede cerrar la ventana para guardar la penalización 
        en la base de datos.

        **Ejemplo de uso**:
        ```python
        self.mostrar_penalizacion()
        ```

        **Exceptions**:
        - Lanza `QMessageBox.warning` si no hay penalizaciones disponibles en la base de datos.
        """
        penalizacion_dialog = QWidget()
        penalizacion_dialog.setWindowTitle("Penalización")
        penalizacion_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
    """)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Agregar márgenes
        layout.setSpacing(15)  # Agregar espaciado

        sala_text = QLabel(f"Sala Actual: {self.sala_name.text()}", self)
        layout.addWidget(sala_text)

        # Rescatar las penalizaciones de la base de datos
        penalizaciones_ref = db.collection('penalizaciones')
        penalizaciones = penalizaciones_ref.stream()
        penalizacion_list = [penalizacion.to_dict() for penalizacion in penalizaciones]

        if not penalizacion_list:
            QMessageBox.warning(self, 'Sin Penalizaciones', 'No hay penalizaciones disponibles en la base de datos.')
            return

        penalizacion = random.choice(penalizacion_list)
        penalizacion_info = QLabel(f"Nombre: {penalizacion['nombre']}\nDescripción: {penalizacion['descripcion']}\nEfecto: {penalizacion['efecto']}\nLanzamiento Dado: {penalizacion['lanzamiento_dado']}", self)
        penalizacion_info.setWordWrap(True)  # Habilitar el ajuste de línea
        layout.addWidget(penalizacion_info)

        btn_cerrar = QPushButton("Cerrar", self)
        btn_cerrar.setStyleSheet("background-color: red; color: white;")

        layout.addWidget(btn_cerrar)

        penalizacion_dialog.setLayout(layout)
        penalizacion_dialog.show()

        btn_cerrar.clicked.connect(lambda: self.guardar_penalizacion(penalizacion, penalizacion_dialog))

    def guardar_penalizacion(self, penalizacion, dialog):
        """
        Guarda la penalización seleccionada en la base de datos.

        Este método actualiza el documento de `PUNTOGUARDADO` con la penalización seleccionada por el jugador.

        **Parametros**:
        - `penalizacion` (dict): Un diccionario con los detalles de la penalización seleccionada. 
          Ejemplo:
          ```python
          penalizacion = {
              'nombre': 'Reducción de Puntos de Vida',
              'descripcion': 'Pierdes 50 puntos de vida.',
              'efecto': 'Reducir puntos de vida',
              'lanzamiento_dado': '1d6'
          }
          ```
        - `dialog` (QWidget): La ventana de diálogo actual de penalización que se va a cerrar.

        **Ejemplo de uso**:
        ```python
        self.guardar_penalizacion(penalizacion, penalizacion_dialog)
        ```

        **Exceptions**:
        - Lanza `Exception` si ocurre un error al actualizar el documento en Firestore.
        """
        dialog.close()
        sala = self.sala_name.text().replace('Sala Actual: ', '')
        doc_id = f'unico_{sala}'  # Nombre único del documento basado en la sala

        try:
            # Actualiza el documento existente en la colección PUNTOGUARDADO
            doc_ref = db.collection('PUNTOGUARDADO').document(doc_id)
            doc_ref.update({
                'penalizacion': penalizacion['descripcion']
            })
            QMessageBox.information(self, 'Penalización', f'Penalización: {penalizacion["descripcion"]}')
        except Exception as e:
            QMessageBox.critical(self, 'Error de Actualización', f'Ocurrió un error al guardar la penalización: {e}')

    def send_text_to_vita(self):
        """
        Envía el texto del campo `game_edit` al `tex_vita` y limpia el campo de texto.

        Este método toma el texto escrito en el campo `game_edit`, lo añade al `tex_vita`, 
        y luego limpia `game_edit` para permitir la entrada de nuevo texto.

        **Ejemplo de uso**:
        ```python
        self.send_text_to_vita()
        ```

        **Exceptions**:
        - No se esperan excepciones en este método.
        """
        text = self.game_edit.toPlainText()
        self.tex_vita.append(text)
        self.game_edit.clear()
    

    def save_bitacora(self):
        """
        Guarda una nueva entrada en la bitácora y añade campos adicionales si ya existe.

        Este método guarda el texto actual de la bitácora en la base de datos. Si el documento
        ya existe en la colección `PUNTOGUARDADO`, agrega un nuevo campo de texto numerado 
        (`texto1`, `texto2`, etc.). Si el documento no existe, crea uno nuevo con el primer campo 
        de texto llamado `texto`.

        **Pasos del método**:
        1. Obtiene el nombre de la sala desde el widget `sala_name`.
        2. Obtiene el texto de la bitácora desde el widget `tex_vita`.
        3. Construye un ID único para el documento basado en el nombre de la sala.
        4. Intenta recuperar el documento desde Firestore.
        5. Si el documento existe, cuenta los campos existentes que comienzan con 'texto' y añade un nuevo campo `textoN+1`.
        6. Si el documento no existe, crea un nuevo campo llamado `texto`.
        7. Muestra un mensaje de éxito al usuario y guarda el ID del documento para uso futuro.
        8. Maneja cualquier excepción que pueda ocurrir durante el proceso de actualización.

        **Ejemplo de uso**:
        ```python
        self.save_bitacora()
        ```

        **Exceptions**:
        - Lanza `Exception` si ocurre un error al actualizar el documento en Firestore.
        """
        sala = self.sala_name.text().replace('Sala Actual: ', '')
        bitacora_text = self.tex_vita.toPlainText()
        doc_id = f'unico_{sala}'  # Nombre único del documento basado en la sala

        try:
            # Referencia al documento específico
            doc_ref = db.collection('PUNTOGUARDADO').document(doc_id)
            
            # Recuperar el documento existente
            doc = doc_ref.get()

            if doc.exists:
                # Documento existe, contar los campos existentes de 'texto'
                data = doc.to_dict()
                texto_count = sum(1 for key in data.keys() if key.startswith('texto'))
                nuevo_campo = f'texto{texto_count + 1}'
            else:
                # Documento no existe, usar 'texto' como primer campo
                nuevo_campo = 'texto'
            
            # Actualizar el documento con el nuevo campo
            doc_ref.set({
                'sala': sala,
                nuevo_campo: bitacora_text
            }, merge=True)  # merge=True para no sobrescribir otros campos
            
            # Muestra un mensaje de éxito
            QMessageBox.information(self, 'Éxito', f'Bitácora guardada exitosamente. Campo añadido: {nuevo_campo}')
            
            # Imprime el ID del documento en la consola
            print(f'ID del documento: {doc_id}')
            
            # Guarda el ID del documento para su uso futuro (opcional)
            self.last_doc_id = doc_id

        except Exception as e:
            # Manejo de errores en caso de que ocurra una excepción
            QMessageBox.critical(self, 'Error', f'No se pudo guardar la bitácora: {str(e)}')
            print(f'Error al guardar la bitácora: {str(e)}')


    def open_bitacora_history(self):
        """
        Abre una ventana con el historial de bitácoras.

        Este método muestra un diálogo con el historial de bitácoras para la sala actual. 
        Recupera la información del documento correspondiente en la colección `PUNTOGUARDADO` 
        y muestra los campos de texto almacenados en el documento, así como la recompensa 
        y la penalización. Si no hay bitácora disponible o ocurre un error, muestra un 
        mensaje de advertencia o error, respectivamente.

        **Pasos del método**:
        1. Crea una nueva ventana de diálogo para mostrar el historial de bitácoras.
        2. Configura el estilo del diálogo para imitar un pergamino antiguo.
        3. Obtiene el nombre de la sala desde el widget `sala_name`.
        4. Construye el ID del documento basado en el nombre de la sala.
        5. Intenta recuperar el documento desde Firestore.
        6. Si el documento existe, extrae y muestra la recompensa, penalización y los campos de texto.
        7. Si el documento no existe, muestra un mensaje de advertencia y cierra el diálogo.
        8. Maneja cualquier excepción que pueda ocurrir durante el proceso de recuperación.
        9. Configura un botón para cerrar el diálogo.

        **Ejemplo de uso**:
        ```python
        self.open_bitacora_history()
        ```

        **Exceptions**:
        - Lanza `QMessageBox.warning` si no hay bitácora disponible para la sala actual.
        - Lanza `QMessageBox.critical` si ocurre un error al recuperar la bitácora desde Firestore.
        """
        historial_dialog = QWidget()
        historial_dialog.setWindowTitle("Historial de Bitácora")

        # Estilos para el diálogo
        historial_dialog.setStyleSheet("""
        background-color: #f5f5dc; /* Color de fondo en caso de que la imagen no se cargue */
        color: #3e3e3e; /* Color del texto oscuro para buen contraste */
        border: 2px solid #8b4513; /* Borde marrón oscuro, como el pergamino envejecido */
        border-radius: 10px; /* Bordes redondeados */
        font-family: 'Times New Roman', serif; /* Fuente clásica que recuerda al papel antiguo */
        padding: 10px;
        background-image: url('fondos/31254.jpg');  /* Imagen de fondo de pergamino */
        background-repeat: repeat;  /* Repetir la imagen de fondo */
        background-size: cover;  /* Asegura que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
    """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Obtener el nombre de la sala del QLabel
        nombre_sala = self.sala_name.text().replace("Sala Actual: ", "").strip()  # Obtener el texto del QLabel
        print(f"Nombre de la sala: {nombre_sala}")  # Mensaje de depuración

        # Construir el ID único del documento
        unique_nombre_sala = f'unico_{nombre_sala}'  # Asumiendo que el ID es único_ + nombre_sala
        print(f"ID del documento: {unique_nombre_sala}")  # Mensaje de depuración

        sala_text = QLabel(f"Sala Actual: {nombre_sala}", self)
        sala_text.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(sala_text)

        try:
            # Recuperar el documento usando `unique_nombre_sala` como ID
            bitacora_doc_ref = db.collection('PUNTOGUARDADO').document(unique_nombre_sala)
            bitacora_doc = bitacora_doc_ref.get()
            print(f"Documento recuperado: {bitacora_doc}")  # Mensaje de depuración

            if bitacora_doc.exists:
                bitacora_data = bitacora_doc.to_dict()
                print(f"Datos del documento: {bitacora_data}")  # Mensaje de depuración
                
                recompensa = bitacora_data.get('recompensa', 'N/A')
                penalizacion = bitacora_data.get('penalizacion', 'N/A')
                textos = [bitacora_data.get(f'texto{i}', '') for i in range(1, 8)]  # Recupera texto1 a texto7

                bitacora_texts = [
                    f"Recompensa: {recompensa}\n",
                    f"Penalización: {penalizacion}\n",
                    "\n".join(textos)  # Muestra todos los textos
                ]

                historial_info = QLabel("\n".join(bitacora_texts), self)
                historial_info.setWordWrap(True)
                historial_info.setStyleSheet("font-size: 16px;")  # Tamaño de fuente para el texto
                layout.addWidget(historial_info)
            else:
                QMessageBox.warning(self, 'Sin Bitácora', 'No hay bitácora disponible para esta sala en la base de datos.')
                historial_dialog.close()  # Cierra el diálogo si no hay bitácora
                return
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Ocurrió un error al recuperar la bitácora: {str(e)}')
            historial_dialog.close()  # Cierra el diálogo en caso de error
            return

        btn_cerrar = QPushButton("Cerrar", self)
        btn_cerrar.setStyleSheet("""
            background-color: #8b4513; /* Color marrón oscuro */
            color: #f5f5dc; /* Color beige claro para el texto */
            font-size: 14px; /* Tamaño de fuente del botón */
            border: 2px solid #6a3e2f; /* Borde del botón */
            border-radius: 5px; /* Bordes redondeados del botón */
        """)
        layout.addWidget(btn_cerrar)

        historial_dialog.setLayout(layout)
        historial_dialog.resize(600, 400)  # Establecer un tamaño inicial para el diálogo

        # Mensaje de depuración para verificar antes de mostrar el diálogo
        print("Mostrando el diálogo de historial")

        historial_dialog.show()

        btn_cerrar.clicked.connect(lambda: print("Botón Cerrar clickeado") or historial_dialog.close())


    def show_pagina_1(self):
        """
        Muestra la `pagina_1` en el `QStackedWidget`.

        Este método cambia la vista actual del `QStackedWidget` a la página de índice `pagina_1`.

        **Ejemplo de uso**:
        ```python
        self.show_pagina_1()
        ```

        **Notas**:
        - Este método no recibe parámetros ni retorna valores.
        - Asegúrate de que `pagina_1` esté correctamente añadida al `QStackedWidget` para que este método funcione.

        **Errores Comunes**:
        - `pagina_1` debe ser una de las páginas añadidas al `QStackedWidget`.
        """
        self.stackedWidget.setCurrentWidget(self.pagina_1)


    def show_pagina_2(self):
        """
        Muestra la `pagina_2` en el `QStackedWidget` y conecta el botón `btn_crearM` al método `crear_nueva_mision`.

        Este método cambia la vista actual del `QStackedWidget` a la página de índice `pagina_2` y configura el botón 
        `btn_crearM` para que llame al método `crear_nueva_mision` cuando se haga clic en él.

        **Ejemplo de uso**:
        ```python
        self.show_pagina_2()
        ```

        **Notas**:
        - Este método configura el evento de clic para `btn_crearM` para crear una nueva misión.
        - Asegúrate de que `btn_crearM` y `crear_nueva_mision` estén definidos y configurados correctamente.

        **Errores Comunes**:
        - `btn_crearM` debe ser un botón válido en `pagina_2`.
        """
        self.stackedWidget.setCurrentWidget(self.pagina_2)
        self.btn_crearM.clicked.connect(self.crear_nueva_mision)


    def crear_nueva_mision(self):
        """
        Crea una nueva misión y la guarda en la colección `evento` en Firestore.

        Este método toma los datos de los campos de texto de la misión, los valida, y los guarda en la colección `evento`.
        Luego, limpia los campos de entrada y muestra un mensaje de éxito.

        **Ejemplo de uso**:
        ```python
        self.crear_nueva_mision()
        ```

        **Manejo de Errores**:
        - Muestra un mensaje de advertencia si algún campo está vacío.
        - Muestra un mensaje de éxito cuando la misión se crea y se guarda correctamente.
        - Maneja errores durante la adición de la misión a Firestore y muestra un mensaje de error si ocurre una excepción.

        **Notas**:
        - `name_m`, `descrip_m`, `tex_condi`, y `recom_m` deben ser `QTextEdit` o widgets similares con texto que no esté vacío.
        """
        nombre = self.name_m.toPlainText()
        descripcion = self.descrip_m.toPlainText()
        condiciones = self.tex_condi.toPlainText()
        recompensa = self.recom_m.toPlainText()

        if not nombre or not descripcion or not condiciones or not recompensa:
            QMessageBox.warning(self, 'Campos Vacíos', 'Por favor, completa todos los campos.')
            return

        nueva_mision = {
            'nombre': nombre,
            'descripcion': descripcion,
            'condiciones': condiciones,
            'recompensa': recompensa
        }

        try:
            eventos_ref = db.collection('evento')
            eventos_ref.add(nueva_mision)
            self.name_m.clear()
            self.descrip_m.clear()
            self.tex_condi.clear()
            self.recom_m.clear()
            QMessageBox.information(self, 'Misión Creada', 'La nueva misión ha sido creada y guardada en la base de datos.')
        except Exception as e:
            QMessageBox.critical(self, 'Error al Crear Misión', f'No se pudo crear la misión: {str(e)}')


            nueva_mision = {
                'nombre': nombre,
                'descripcion': descripcion,
                'condiciones': condiciones,
                'recompensa': recompensa
            }

            
            eventos_ref = db.collection('evento')
            eventos_ref.add(nueva_mision)

            
            self.name_m.clear()
            self.descrip_m.clear()
            self.tex_condi.clear()
            self.recom_m.clear()

        
            QMessageBox.information(self, 'Misión Creada', 'La nueva misión ha sido creada y guardada en la base de datos.')
        

    def show_pagina_4(self):
        """
        Muestra la `pagina_4` en el `QStackedWidget` y agrega una tabla de personajes si no está agregada.

        Este método cambia la vista actual del `QStackedWidget` a la página de índice `pagina_4` y agrega la tabla de 
        personajes solo si aún no se ha agregado.

        **Ejemplo de uso**:
        ```python
        self.show_pagina_4()
        ```

        **Notas**:
        - Asegúrate de que `pagina_4` esté correctamente añadida al `QStackedWidget`.
        - `self.tabla_personajes_agregada` debe ser un atributo booleano inicializado en `False`.

        **Errores Comunes**:
        - La tabla de personajes debe ser añadida a un diseño de `pagina_4`.
        """
        self.stackedWidget.setCurrentWidget(self.pagina_4)

        if not self.tabla_personajes_agregada:
            self.agregar_tabla_personajes()
            self.tabla_personajes_agregada = True


    def show_pagina_3(self):
        """
        Muestra la `pagina_3` en el `QStackedWidget` y llama al método `cambio_etapa`.

        Este método cambia la vista actual del `QStackedWidget` a la página de índice `pagina_3` y realiza una 
        actualización basada en la selección del `comboBox_2`.

        **Ejemplo de uso**:
        ```python
        self.show_pagina_3()
        ```

        **Notas**:
        - Asegúrate de que `pagina_3` esté correctamente añadida al `QStackedWidget`.
        - `cambio_etapa` debe ser un método definido en la clase para manejar la selección del `comboBox_2`.

        **Errores Comunes**:
        - `comboBox_2` debe ser un widget `QComboBox` válido en `pagina_3`.
        """
        self.stackedWidget.setCurrentWidget(self.pagina_3)
        self.cambio_etapa()

    def cambio_etapa(self):
        """
        Actualiza la animación del QLabel `inicio_p` basado en la selección del `comboBox_2`.

        Este método obtiene el índice seleccionado en `comboBox_2`, detiene cualquier animación actual en `inicio_p`,
        y establece una nueva animación basada en el índice seleccionado.

        **Ejemplo de uso**:
        ```python
        self.cambio_etapa()
        ```

        **Notas**:
        - `comboBox_2` debe ser un widget `QComboBox` con varias opciones.
        - `self.animations` debe ser un diccionario que mapea índices de `comboBox_2` a rutas de archivos GIF.

        **Errores Comunes**:
        - Asegúrate de que `self.animations` esté correctamente configurado con rutas válidas de archivos GIF.
        """
        index = self.comboBox_2.currentIndex()
        print(f"ComboBox index changed to: {index}")  # Mensaje de depuración

        # Detiene cualquier animación actual en el QLabel
        if hasattr(self, 'movie') and self.movie:
            self.movie.stop()
        
        # Establece el nuevo GIF basado en la selección del QComboBox_2
        gif_path = self.animations.get(index)
        if gif_path:
            print(f"Loading GIF: {gif_path}")  # Mensaje de depuración
            self.movie = QMovie(gif_path)
            self.inicio_p.setMovie(self.movie)
            self.movie.start()
        else:
            self.inicio_p.clear()

    def show_pagina_5(self):
        """
        Muestra la `pagina_5` en el `QStackedWidget`.

        Este método cambia la vista actual del `QStackedWidget` a la página de índice `pagina_5`.

        **Ejemplo de uso**:
        ```python
        self.show_pagina_5()
        ```

        **Notas**:
        - Asegúrate de que `pagina_5` esté correctamente añadida al `QStackedWidget`.
        """
        self.stackedWidget.setCurrentWidget(self.pagina_5)

        
    def agregar_tabla_personajes(self):
        """
        Crea y agrega una tabla de personajes a `pagina_4`.

        Este método crea un `QTableWidget` con 7 columnas para mostrar detalles de personajes y los agrega a `pagina_4`.
        También aplica un estilo a la tabla para que coincida con el diseño visual del resto de la aplicación.

        **Ejemplo de uso**:
        ```python
        self.agregar_tabla_personajes()
        ```

        **Notas**:
        - Asegúrate de que `pagina_4` tenga un diseño adecuado para contener la tabla de personajes.
        - `self.tabla_personajes_agregada` debe ser un atributo booleano inicializado en `False`.

        **Errores Comunes**:
        - `self.tabla_personajes` debe ser una instancia de `QTableWidget`.
        - Asegúrate de que `self.tabla_personajes` se haya configurado correctamente antes de añadirlo a `pagina_4`.
        """
        self.tabla_personajes = QTableWidget()
        self.tabla_personajes.setColumnCount(7)
        self.tabla_personajes.setHorizontalHeaderLabels(["Nombre", "Nivel", "Raza", "Habilidades", "Poderes", "Equipamiento", "Modificar"])
        self.actualizar_tabla_personajes()

        # Estilo para la tabla
        self.tabla_personajes.setStyleSheet("""
            QTableWidget {
                border: 2px solid red; /* Borde exterior rojo */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 5px; /* Espaciado interno */
            }
            QHeaderView::section {
                background-color: #DCE8F5; /* Color de fondo de las cabeceras */
                color: #000000; /* Color del texto en las cabeceras */
                padding: 10px; /* Espaciado interno de las cabeceras */
                border: 1px solid #a0a0a0; /* Borde de las cabeceras */
            }
            QPushButton {
                background-color: #FFD700; /* Color de fondo dorado */
                color: #000000; /* Color del texto */
                border: 2px solid #DAA520; /* Borde dorado oscuro */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 12px 20px; /* Espaciado interno del botón */
                font-weight: bold; /* Texto en negrita */
                min-width: 120px; /* Ancho mínimo del botón */
                text-align: center; /* Alinear el texto al centro */
            }
            QPushButton:hover {
                background-color: #FFC107; /* Color de fondo dorado al pasar el ratón */
            }
            QPushButton:pressed {
                background-color: #FFA000; /* Color de fondo dorado oscuro al presionar */
            }
        """)

        layout = self.pagina_4.layout()
        if layout is None:
            layout = QVBoxLayout(self.pagina_4)
            self.pagina_4.setLayout(layout)
        
        if isinstance(layout, QVBoxLayout):
            layout.addWidget(self.tabla_personajes)


    def actualizar_tabla_personajes(self):
        """
        Actualiza la tabla de personajes en `pagina_4` con datos de la colección `personajes` en Firestore.

        Este método recupera los datos de todos los personajes, los muestra en una tabla, y agrega un botón de modificación a cada fila.

        **Ejemplo de uso**:
        ```python
        self.actualizar_tabla_personajes()
        ```

        **Notas**:
        - `self.tabla_personajes` debe ser un `QTableWidget` con 7 columnas: Nombre, Nivel, Raza, Habilidades, Poderes, Equipamiento, Modificar.
        - El campo `habilidades` se convierte de un diccionario a una cadena de texto en el formato `"Habilidad: valor\n"`.
        - El campo `poderes` también se convierte de un diccionario a una cadena de texto en el mismo formato.

        **Errores Comunes**:
        - Asegúrate de que `self.tabla_personajes` esté correctamente inicializado antes de llamar a este método.
        - Verifica que los datos en Firestore estén en el formato correcto.

        **Modificaciones**:
        - Asegúrate de que las habilidades y poderes estén en el formato adecuado para mostrarse en la tabla.
        """
        personajes = self.recuperar_personajes()
        self.tabla_personajes.setRowCount(len(personajes))
        for i, personaje in enumerate(personajes):
            self.tabla_personajes.setItem(i, 0, QTableWidgetItem(str(personaje.get("nombre", ""))))
            self.tabla_personajes.setItem(i, 1, QTableWidgetItem(str(personaje.get("nivel", ""))))
            self.tabla_personajes.setItem(i, 2, QTableWidgetItem(str(personaje.get("raza", ""))))
            
            # Mostrar habilidades como una cadena concatenada
            habilidades = personaje.get("habilidades", {})
            if isinstance(habilidades, dict):
                habilidades_texto = "\n".join(f"{k}: {v}" for k, v in habilidades.items())
            else:
                habilidades_texto = habilidades  # Asumimos que es una cadena ya formateada
            self.tabla_personajes.setItem(i, 3, QTableWidgetItem(habilidades_texto))
            
            # Mostrar poderes como una cadena concatenada
            poderes = personaje.get("poderes", {})
            if isinstance(poderes, dict):
                poderes_texto = "\n".join(f"{k}: {v}" for k, v in poderes.items())
            else:
                poderes_texto = poderes  # Asumimos que es una cadena ya formateada
            self.tabla_personajes.setItem(i, 4, QTableWidgetItem(poderes_texto))
            
            self.tabla_personajes.setItem(i, 5, QTableWidgetItem(str(personaje.get("equipamiento", ""))))
            
            # Añadir botón de modificar
            btn_modificar = QPushButton("Modificar")
            btn_modificar.setStyleSheet("""
                QPushButton {
                    background-color: #FFD700; /* Color de fondo dorado */
                    color: #000000; /* Color del texto */
                    border: 2px solid #DAA520; /* Borde dorado oscuro */
                    border-radius: 5px; /* Esquinas redondeadas */
                    padding: 12px 20px; /* Espaciado interno del botón */
                    font-weight: bold; /* Texto en negrita */
                    min-width: 120px; /* Ancho mínimo del botón */
                    text-align: center; /* Alinear el texto al centro */
                }
                QPushButton:hover {
                    background-color: #FFC107; /* Color de fondo dorado al pasar el ratón */
                }
                QPushButton:pressed {
                    background-color: #FFA000; /* Color de fondo dorado oscuro al presionar */
                }
            """)
            btn_modificar.clicked.connect(lambda _, row=i: self.modificar_personaje(row))
            self.tabla_personajes.setCellWidget(i, 6, btn_modificar)
            self.tabla_personajes.setRowHeight(i, 50)  # Asegúrate de que haya suficiente altura para el botón

        self.tabla_personajes.resizeColumnsToContents()
        self.tabla_personajes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



    def recuperar_personajes(self):
        """
        Recupera todos los personajes de la colección `personajes` en Firestore.

        Este método recupera los documentos de personajes y devuelve una lista de diccionarios que representan los personajes.

        **Ejemplo de uso**:
        ```python
        personajes = self.recuperar_personajes()
        ```

        **Notas**:
        - Cada diccionario incluye el ID del documento (`personaje['id']`) para futuras referencias.
        - Asegúrate de que la colección `personajes` exista en Firestore y contenga documentos válidos.

        **Errores Comunes**:
        - Verifica la conexión a Firestore y que la colección `personajes` esté correctamente configurada.
        """
        personajes = []
        docs = db.collection("personajes").stream()
        for doc in docs:
            personaje = doc.to_dict()
            personaje['id'] = doc.id  # Agregar el ID del documento para futuras referencias
            personajes.append(personaje)
        return personajes

    
    def modificar_personaje(self, row):
        """
        Modifica los datos del personaje en la fila seleccionada de la tabla y actualiza la base de datos.

        Este método obtiene los datos de la fila seleccionada, actualiza el personaje correspondiente en Firestore, 
        y muestra un mensaje de éxito.

        **Parámetros**:
        - `row`: El índice de la fila seleccionada en la tabla de personajes.

        **Ejemplo de uso**:
        ```python
        self.modificar_personaje(row)
        ```

        **Notas**:
        - Asegúrate de que la fila seleccionada corresponda a un personaje válido.
        - Actualiza los campos `nombre`, `nivel`, `raza`, `habilidades`, `poderes` y `equipamiento` en Firestore.

        **Errores Comunes**:
        - Verifica que `self.tabla_personajes` tenga datos válidos en la fila seleccionada.
        - Asegúrate de que los datos en la base de datos estén en el formato correcto.
        """
        personaje_id = self.recuperar_personajes()[row]['id']  # Obtener el ID del personaje de la fila seleccionada
        nombre = self.tabla_personajes.item(row, 0).text()
        nivel = self.tabla_personajes.item(row, 1).text()
        raza = self.tabla_personajes.item(row, 2).text()
        habilidades = self.tabla_personajes.item(row, 3).text()
        poderes = self.tabla_personajes.item(row, 4).text()
        equipamiento = self.tabla_personajes.item(row, 5).text()
        
        # Actualizar los datos en la base de datos
        db.collection("personajes").document(personaje_id).update({
            "nombre": nombre,
            "nivel": nivel,
            "raza": raza,
            "habilidades": habilidades,
            "poderes": poderes,
            "equipamiento": equipamiento
        })

        QMessageBox.information(self, 'Éxito', 'Personaje modificado exitosamente.')

    
    
    
    def load_mission(self):
        """
        Carga una misión de la colección 'Mision' en Firestore y muestra los detalles en `tex_vita`.

        Este método busca una misión basada en el nombre proporcionado en `b_ms`, y si se encuentra, muestra los detalles en `tex_vita`.

        **Notas**:
        - `self.b_ms` es un `QLineEdit` donde el usuario introduce el nombre de la misión.
        - `self.tex_vita` es un `QTextBrowser` donde se muestran los detalles de la misión.
        - Asegúrate de que `b_ms` tenga el nombre de una misión existente.

        **Errores Comunes**:
        - Verifica que `self.b_ms.text().strip()` no esté vacío.
        - Asegúrate de que `tex_vita` esté correctamente inicializado y visible en la interfaz.
        """
        mission_name = self.b_ms.text().strip()

        if not mission_name:
            QMessageBox.warning(self, 'Error', 'Introduce el nombre de la misión.')
            return

        misiones_ref = db.collection('Mision')
        query = misiones_ref.where('nombre', '==', mission_name).limit(1)
        results = query.stream()

        mission_found = False  # Bandera para verificar si encontramos la misión
        for doc in results:
            mision = doc.to_dict()
            evento_texto = f'''
                <b>Misión:</b> {mision["nombre"]}
                <br><b>Descripción:</b> {mision["descripcion"]}
                <br><b>Recompensa:</b> {mision["recompensa"]}
            '''
            self.tex_vita.setHtml(evento_texto)  # Usar setHtml para formato mejorado
            mission_found = True
            break  # Salir del bucle después de encontrar la misión

        if not mission_found:
            QMessageBox.warning(self, 'Error', 'Misión no encontrada.')


class DiceWindow(QWidget):
    """
    Ventana de la aplicación para lanzar dados de diferentes tipos.

    Esta clase define una ventana con botones para lanzar dados de varios tipos (D4, D6, D10, D12, D20) y muestra el resultado del lanzamiento en una etiqueta.

    **Atributos**:
    - `title_label`: `QLabel` que muestra el título de la ventana.
    - `label_result`: `QLabel` que muestra el resultado del lanzamiento del dado.
    - `button_layout`: `QHBoxLayout` que organiza los botones para lanzar los dados.
    - `btn_roll_d4`, `btn_roll_d6`, `btn_roll_d10`, `btn_roll_d12`, `btn_roll_d20`: `QPushButton` para lanzar dados de 4, 6, 10, 12 y 20 caras, respectivamente.
    - `background_label`: `QLabel` que se utiliza para mostrar la imagen de fondo de la ventana.

    **Ejemplo de Uso**:
    ```python
    app = QApplication([])
    dice_window = DiceWindow()
    dice_window.show()
    app.exec()
    ```

    **Notas**:
    - Asegúrate de tener las imágenes `dice_icon.png` y las imágenes de los dados en la carpeta correcta.
    - La imagen de fondo debe estar en `fondos/31254.jpg`. Asegúrate de que el archivo exista en esa ruta.

    **Métodos**:

    - `__init__(self)`: Constructor de la clase. Configura la ventana, el diseño, los botones, y conecta las señales de los botones al método `roll_dice`.

        **Descripción**:
        Inicializa la ventana principal de la aplicación de dados. Configura el título de la ventana, la geometría, el ícono y el fondo. Añade una etiqueta de título, una etiqueta para mostrar los resultados de los dados, y botones para lanzar los dados.

        **Ejemplo de Uso**:
        No es necesario llamar a este método directamente. Se invoca automáticamente cuando se crea una instancia de `DiceWindow`.

    - `set_background(self, image_path)`: Configura una imagen de fondo para el widget.

        **Descripción**:
        Configura una imagen de fondo en la ventana utilizando la ruta proporcionada. Ajusta la imagen para que cubra toda la ventana.

        **Parámetros**:
        - `image_path` (`str`): Ruta de la imagen de fondo.

        **Ejemplo de Uso**:
        ```python
        self.set_background('fondos/31254.jpg')
        ```

    - `resizeEvent(self, event)`: Ajusta el tamaño del fondo cuando la ventana cambia de tamaño.

        **Descripción**:
        Maneja el evento de cambio de tamaño de la ventana para asegurarse de que la imagen de fondo se redimensiona correctamente.

        **Parámetros**:
        - `event` (`QResizeEvent`): El evento de cambio de tamaño.

        **Ejemplo de Uso**:
        Este método se llama automáticamente cuando la ventana cambia de tamaño, no es necesario invocar este método directamente.

    - `roll_dice(self, sides)`: Lanza un dado con el número de caras especificado y muestra el resultado.

        **Descripción**:
        Lanza un dado con un número de caras dado (4, 6, 10, 12, o 20) y actualiza `label_result` con el número obtenido. Cambia el color del texto del resultado a azul (#007BFF).

        **Parámetros**:
        - `sides` (`int`): Número de caras del dado (4, 6, 10, 12, 20).

        **Ejemplo de Uso**:
        Este método se llama cuando se hace clic en uno de los botones de dados. No es necesario invocar este método directamente.

        **Ejemplo de Uso**:
        ```python
        self.roll_dice(6)  # Lanza un dado de 6 caras
        ```

    """

    def __init__(self):
        super(DiceWindow, self).__init__()
        self.setWindowTitle('¿SUERTE?')
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon('dice_icon.png'))  # Agregar un icono para la ventana
        
        # Configurar el fondo
        self.set_background('fondos/31254.jpg')  # Asegúrate de tener una imagen de fondo llamada 'fondos/31254.jpg'
        
        self.layout = QVBoxLayout()
        
        # Título de la ventana
        self.title_label = QLabel('¿MIEDO?')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet('font-size: 20px; font-weight: bold; color: #007BFF;')
        self.layout.addWidget(self.title_label)
        
        # Etiqueta de Resultado
        self.label_result = QLabel('DEBERIAS TENERLO: ')
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_result.setStyleSheet('font-size: 18px; color: #333333;')
        self.layout.addWidget(self.label_result)
        
        # Diseño de Botones
        self.button_layout = QHBoxLayout()
        
        # Botones de Dados
        self.btn_roll_d4 = QPushButton('Roll D4')
        self.btn_roll_d6 = QPushButton('Roll D6')
        self.btn_roll_d10 = QPushButton('Roll D10')
        self.btn_roll_d12 = QPushButton('Roll D12')
        self.btn_roll_d20 = QPushButton('Roll D20')
        
        # Agregar iconos a los botones
        self.btn_roll_d4.setIcon(QIcon('iconos/dados (1).png'))
        self.btn_roll_d6.setIcon(QIcon('iconos/dados.png'))
        self.btn_roll_d10.setIcon(QIcon('iconos/dado (3).png'))
        self.btn_roll_d12.setIcon(QIcon('iconos/juego-de-rol (1).png'))
        self.btn_roll_d20.setIcon(QIcon('iconos/dados-d20.png'))
        
        self.btn_roll_d4.setIconSize(QSize(32, 32))
        self.btn_roll_d6.setIconSize(QSize(32, 32))
        self.btn_roll_d10.setIconSize(QSize(32, 32))
        self.btn_roll_d12.setIconSize(QSize(32, 32))
        self.btn_roll_d20.setIconSize(QSize(32, 32))
        
        # Estilos para los botones
        self.btn_roll_d4.setStyleSheet('background-color: #5BC0EB; color: white; font-size: 14px; border-radius: 8px; padding: 10px;')
        self.btn_roll_d6.setStyleSheet('background-color: #51CF66; color: white; font-size: 14px; border-radius: 8px; padding: 10px;')
        self.btn_roll_d10.setStyleSheet('background-color: #FFC107; color: white; font-size: 14px; border-radius: 8px; padding: 10px;')
        self.btn_roll_d12.setStyleSheet('background-color: #6F42C1; color: white; font-size: 14px; border-radius: 8px; padding: 10px;')
        self.btn_roll_d20.setStyleSheet('background-color: #FF6B6B; color: white; font-size: 14px; border-radius: 8px; padding: 10px;')
        
        self.button_layout.addWidget(self.btn_roll_d4)
        self.button_layout.addWidget(self.btn_roll_d6)
        self.button_layout.addWidget(self.btn_roll_d10)
        self.button_layout.addWidget(self.btn_roll_d12)
        self.button_layout.addWidget(self.btn_roll_d20)
        
        self.layout.addLayout(self.button_layout)
        
        # Conectar botones con el método roll_dice
        self.btn_roll_d4.clicked.connect(lambda: self.roll_dice(4))
        self.btn_roll_d6.clicked.connect(lambda: self.roll_dice(6))
        self.btn_roll_d10.clicked.connect(lambda: self.roll_dice(10))
        self.btn_roll_d12.clicked.connect(lambda: self.roll_dice(12))
        self.btn_roll_d20.clicked.connect(lambda: self.roll_dice(20))
        
        self.setLayout(self.layout)
    
    def set_background(self, image_path):
        """
        Configura una imagen de fondo para el widget.

        **Parámetros**:
        - `image_path` (`str`): Ruta de la imagen de fondo que se mostrará en la ventana.

        **Descripción**:
        Crea un `QLabel` para mostrar una imagen de fondo en el widget. La imagen se ajusta al tamaño de la ventana y se coloca detrás de todos los demás widgets.

        **Ejemplo de Uso**:
        ```python
        self.set_background('fondos/31254.jpg')
        ```

        **Errores Comunes**:
        - Verifica que el archivo de imagen exista en la ruta proporcionada.
        - Asegúrate de que `image_path` sea una cadena de texto válida.
        """
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(image_path))
        self.background_label.setScaledContents(True)
        self.background_label.resize(self.size())
        self.background_label.lower()

    def resizeEvent(self, event):
        """
        Ajusta el tamaño del fondo cuando la ventana cambia de tamaño.

        **Parámetros**:
        - `event` (`QResizeEvent`): El evento de cambio de tamaño que indica cómo ha cambiado el tamaño de la ventana.

        **Descripción**:
        Este método maneja el evento de cambio de tamaño para asegurarse de que la imagen de fondo se redimensione de acuerdo con el tamaño de la ventana.

        **Ejemplo de Uso**:
        Este método es llamado automáticamente por el sistema cuando la ventana cambia de tamaño.
        """
        self.background_label.resize(self.size())
        super(DiceWindow, self).resizeEvent(event)

    def roll_dice(self, sides):
        """
        Lanza un dado con el número de caras especificado y muestra el resultado.

        **Parámetros**:
        - `sides` (`int`): Número de caras del dado (4, 6, 10, 12, 20).

        **Descripción**:
        Genera un número aleatorio entre 1 y el número de caras del dado. Actualiza el texto de `label_result` para mostrar el resultado del lanzamiento.

        **Ejemplo de Uso**:
        Este método es llamado cuando se hace clic en uno de los botones de dados.

        **Errores Comunes**:
        - Asegúrate de que `sides` sea uno de los valores válidos (4, 6, 10, 12, 20).
        """
        result = random.randint(1, sides)
        self.label_result.setText(f'Numero: {result}')
        self.label_result.setStyleSheet('font-size: 18px; color: #007BFF;')  # Cambio de color para el texto

class PersonajesWindow(QWidget, Ui_Formperso):
    """
    Ventana para la gestión de personajes en el juego de rol.

    Esta clase define una ventana con un formulario para crear personajes. Permite ingresar información como el nombre del personaje, raza, habilidades, poderes, y equipamiento, y guarda estos datos en la colección 'personajes' en Firestore.

    **Atributos**:
    - `name_id`: `QLineEdit` para ingresar el nombre del personaje.
    - `raza_box`: `QComboBox` para seleccionar la raza del personaje.
    - `text_hb`: `QTextEdit` para ingresar las habilidades del personaje en formato 'Habilidad: valor'.
    - `tx_pd`: `QTextEdit` para ingresar los poderes del personaje en formato 'Poder: valor'.
    - `cc_eq`: `QComboBox` para seleccionar el equipamiento del personaje.
    - `raza_line`: `QLineEdit` para ingresar una raza personalizada si la opción es seleccionada en `raza_box`.
    - `li_equi`: `QLineEdit` para ingresar un equipamiento personalizado si la opción es seleccionada en `cc_eq`.
    - `btn_guarp`: `QPushButton` para guardar el personaje.
    - `btn_otro`: `QPushButton` para limpiar los campos del formulario.

    **Ejemplo de Uso**:
    ```python
    app = QApplication([])
    personajes_window = PersonajesWindow()
    personajes_window.show()
    app.exec()
    ```

    **Métodos**:

    - `__init__(self)`: Constructor de la clase. Configura el formulario y conecta los botones a los métodos correspondientes.

        **Descripción**:
        Inicializa la ventana del formulario de personajes. Configura los botones para guardar el personaje y limpiar los campos del formulario.

        **Ejemplo de Uso**:
        No es necesario llamar a este método directamente. Se invoca automáticamente cuando se crea una instancia de `PersonajesWindow`.

    - `validacion_campos(self, text, label)`: Valida que se ingrese un valor para un campo específico.

        **Descripción**:
        Verifica que el campo de texto no esté vacío. Si está vacío, muestra un mensaje de advertencia.

        **Parámetros**:
        - `text` (`str`): El texto ingresado en el campo.
        - `label` (`str`): El nombre del campo para mostrar en el mensaje de advertencia.

        **Retorno**:
        - `bool`: `True` si el campo no está vacío, `False` si está vacío.

        **Ejemplo de Uso**:
        ```python
        if not self.validacion_campos(self.name_id.text(), 'Nombre'):
            return
        ```

    - `validar_habilidades(self, habilidades_text)`: Valida que se introduzcan dos habilidades válidas en formato 'Habilidad: valor'.

        **Descripción**:
        Valida que el texto de habilidades contenga exactamente dos habilidades en el formato correcto.

        **Parámetros**:
        - `habilidades_text` (`str`): Texto con las habilidades en formato 'Habilidad: valor'.

        **Retorno**:
        - `dict` o `bool`: Un diccionario con habilidades si son válidas, `False` si no lo son.

        **Ejemplo de Uso**:
        ```python
        habilidades = self.validar_habilidades(self.text_hb.toPlainText())
        if not habilidades:
            QMessageBox.warning(self, 'Error', 'Introduce dos habilidades válidas.')
            return
        ```

    - `validar_poderes(self, poderes_text)`: Valida que se introduzcan dos poderes válidos en formato 'Poder: valor'.

        **Descripción**:
        Valida que el texto de poderes contenga exactamente dos poderes en el formato correcto.

        **Parámetros**:
        - `poderes_text` (`str`): Texto con los poderes en formato 'Poder: valor'.

        **Retorno**:
        - `dict` o `bool`: Un diccionario con poderes si son válidos, `False` si no lo son.

        **Ejemplo de Uso**:
        ```python
        poderes = self.validar_poderes(self.tx_pd.toPlainText())
        if not poderes:
            QMessageBox.warning(self, 'Error', 'Introduce dos poderes válidos.')
            return
        ```

    - `guardar_p(self)`: Guarda los datos del personaje en Firestore y limpia los campos.

        **Descripción**:
        Recolecta los datos del formulario, valida la información, y guarda el personaje en la colección 'personajes' en Firestore. Luego, limpia los campos del formulario.

        **Ejemplo de Uso**:
        Este método se llama cuando se hace clic en el botón de guardar.

        **Ejemplo de Uso**:
        ```python
        self.guardar_p()
        ```

    - `limpiar_p(self)`: Limpia todos los campos del formulario para ingresar un nuevo personaje.

        **Descripción**:
        Borra el contenido de todos los campos del formulario para preparar la ventana para ingresar un nuevo personaje.

        **Ejemplo de Uso**:
        Este método se llama cuando se hace clic en el botón de limpiar.

        **Ejemplo de Uso**:
        ```python
        self.limpiar_p()
        ```

    """

    def __init__(self):
        super(PersonajesWindow, self).__init__()
        self.setupUi(self)
        self.btn_guarp.clicked.connect(self.guardar_p)
        self.btn_otro.clicked.connect(self.limpiar_p)
    
    def validacion_campos(self, text, label):
        """Validar que se ingrese un valor para un campo específico."""
        if not text:
            QMessageBox.warning(self, 'Error', f'Introduce un valor para {label}.')
            return False
        return True
    
    def validar_habilidades(self, habilidades_text):
        """Validar que se introduzcan dos habilidades válidas en formato 'Habilidad: valor'."""
        habilidades = habilidades_text.split('\n')
        if len(habilidades) != 2:
            return False
        habilidades_dict = {}
        for habilidad in habilidades:
            if ':' not in habilidad:
                return False
            name, value = habilidad.split(':')
            if name in habilidades_dict:
                return False
            habilidades_dict[name] = value
        return habilidades_dict if len(habilidades_dict) == 2 else False
    
    def validar_poderes(self, poderes_text):
        """Validar que se introduzcan dos poderes válidos en formato 'Poder: valor'."""
        poderes = poderes_text.split('\n')
        if len(poderes) != 2:
            return False
        poderes_dict = {}
        for poder in poderes:
            if ':' not in poder:
                return False
            name, value = poder.split(':')
            if name in poderes_dict:
                return False
            poderes_dict[name] = value
        return poderes_dict if len(poderes_dict) == 2 else False
    
    def guardar_p(self):
        """Guardar los datos del personaje en Firestore y limpiar los campos."""
        nombre = self.name_id.text().strip()
        raza = self.raza_box.currentText().strip()
        habilidades_text = self.text_hb.toPlainText().strip()
        poderes_text = self.tx_pd.toPlainText().strip()
        equipamiento = self.cc_eq.currentText().strip()
        raza_custom = self.raza_line.text().strip()
        equipo_custom = self.li_equi.text().strip()
        
        if not self.validacion_campos(nombre, 'Nombre') or not self.validacion_campos(raza, 'Raza'):
            return

        habilidades = self.validar_habilidades(habilidades_text)
        if not habilidades:
            QMessageBox.warning(self, 'Error', 'Introduce dos habilidades válidas.')
            return

        poderes = self.validar_poderes(poderes_text)
        if not poderes:
            QMessageBox.warning(self, 'Error', 'Introduce dos poderes válidos.')
            return
        
        if raza_custom:
            raza = raza_custom
        
        if equipo_custom:
            equipamiento = equipo_custom

        data = {
            'nombre': nombre,
            'nivel': 1,
            'raza': raza,
            'habilidades': habilidades,
            'poderes': poderes,
            'equipamiento': equipamiento,
            'estado': 'vivo'
        }

        # Guardar los datos en la colección 'personajes'
        db.collection('personajes').add(data)
        QMessageBox.information(self, 'Éxito', 'Personaje guardado exitosamente.')
        self.limpiar_p()  # Llamar al método de limpiar campos

    def limpiar_p(self):
        """Limpiar todos los campos del formulario para ingresar un nuevo personaje."""
        self.name_id.clear()
        self.raza_box.setCurrentIndex(0)
        self.text_hb.clear()
        self.tx_pd.clear()
        self.cc_eq.setCurrentIndex(0)
        self.raza_line.clear()
        self.li_equi.clear()

class CargandoWindow(QWidget, Ui_Formcarga):
    """
    Ventana para mostrar una barra de progreso durante el proceso de carga.

    Esta clase define una ventana con una barra de progreso para mostrar el estado de carga.

    **Atributos**:
    - `barra_cargado`: `QProgressBar` que muestra el progreso de la carga.

    **Ejemplo de Uso**:
    ```python
    app = QApplication([])
    cargando_window = CargandoWindow()
    cargando_window.show()
    app.exec()
    ```

    **Métodos**:

    - `__init__(self)`: Constructor de la clase. Configura la barra de progreso y verifica que exista en la UI.

        **Descripción**:
        Inicializa la ventana de carga y asegura que la barra de progreso esté correctamente configurada.

        **Ejemplo de Uso**:
        No es necesario llamar a este método directamente. Se invoca automáticamente cuando se crea una instancia de `CargandoWindow`.

        **Errores Comunes**:
        - Asegúrate de que `barra_cargado` esté presente en el archivo de UI y se llame correctamente.
    """

    def __init__(self):
        super(CargandoWindow, self).__init__()
        self.setupUi(self)
        self.barra_cargado = self.findChild(QProgressBar, 'barra_cargado')
        if self.barra_cargado is None:
            raise AttributeError("QProgressBar 'barra_cargado' no se encontró en la UI.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
