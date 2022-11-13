# YouFlix &copy; 

**YouFLix** nacio como un proyecto de la asignatura Ingenieria Web. Pretende ser una plataforma donde cualquier usuario pueda subir videos y al mismo tiempo reproducirlos como si de YouTube se tratase. Asi mismo, cada usuario puede filtrar y categorizar los video de manera sencilla. Tambien, si un video te ha gustado, puedes dejar un me gusta o incluso un comentario para apoyar al creador.

##DownLoad	:fa-cloud-download:
Hay **dos** maneras sencillas de poder lanzar esta pagina:

####1. Clonacion del repositorio de GitHub		:fa-github-alt: 
`$ git clone https://github.com/imanoldt/django_project_iWeb.git`

Una vez clonado, se nos creara una carpeta llamada `django_project_iWeb`
####2. Descargar .ZIP		:fa-download:
Para descargar el ZIP es tan sencillo como acceder al [**Repositorio**](https://github.com/imanoldt/django_project_iWeb.git "Repositorio") y descargar como .**zip**

##Installation/Run	:fa-file-code-o:	:fa-html5:

Abrir una terminal en la ruta donde se ha descargado el proyecto y lanzar el siguiente comando: 

`$ pip install -r requirements.txt`

Este comando instalara todas las librerias necesarias para el mejor funcionamiento del mismo. 

Si desea ver las librerias instaladas ejecute `$ pip freeze` o abra el archivo `requirements.txt` con un su editor de texto favorito.

> NOTA: Para usuarios Mac OS puede que de algun tipo de fallo por incompatibilidad con algunas librerias. Ponerse en contacto con el desarrollador.


##Views	:fa-terminal:

| VIEW  |  PATH |
| ------------ | ------------ |
|  Videos | app_1/base/videos  |
| Profile |  app_1/base2/profile  |
|  Log-In| app_1/   |
|  Google|  accounts/google/login/   |
|  Upload|  app_1/upload/   |
|  Player|  /player/ `<slug:titulo_video> ` |


##Models :fa-space-shuttle:

```python
class Video(models.Model): #MODIFICADO
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True)
    thumnail = models.CharField(max_length=2000, null=True) #MINIATURA DE IMAGEN PARA MEJOR OPTIMIZACION DE LA PAGINA
    length = models.IntegerField(null=True) #DURACION DEL VIDEO ENTERO
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    cathegory = models.CharField(max_length=300, null=True, choices = VIDEO_CATHEGORY)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self): #DEVUELVE STRING DE LO QUE QUEREMOS VISUALIZAR / TOSTRING() _ JAVA
        return self.title
        
```
```python
class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```

```python
class Comment(models.Model):#MODIFICADO
 title = models.CharField(max_length=50, blank=False, null=False)

```

##API	:fa-toggle-on: :fa-jsfiddle:
En esta Web hemos implementado la** API de Google** que te permite iniciar sesion con tu cuenta de **Google** en dos simples click's. La API gestiona tu informacion, protegue toda tu privacidad permite el encriptado de lado a lado gracias a su interfaz.



## Integrantes
- Imanol Duran
- Irene Gonzalez
- Maria Mardones
