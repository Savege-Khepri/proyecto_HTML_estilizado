# Guía de instalación con Vite + Sass

1. Instalar Node versión 22.12
2. npm create vite@latest sass-vite-template
3. cd sass-vite-template
4. npm i
5. npm i sass --save-dev
6. Crear fichero de configuración vite.config.js para conseguir que los enlaces de los archivos sean relativos





# comandos para usar vite

//crea una platilla de vite con index y todo, donde realizaremos el proyecto=

npm create vite 

//se selecciona la opcion vanilla

cd nombre-del-proyecto

//para crear una platilla de sass

npm add -D sass

//para activar el servidor vite (se tiene que estar en el directorio raiz del proyecto)

npm run dev

//para abrir el servidor en el navegador

o + enter

# comandos para usar Sass

//para instalar Sass

npm install -g sass

//comprobamos que se halla instalado correctamente corrobrando la version

sass --version

//para compilar ficheros con el preprocesador Sass
//donde .scss es el archivo compilador y .css el ya compilado

sass archivo.scss archivo.css

//ahora, podemos configurar que estos archivos esten enlazados pendiente de los cambios que se realizen en cualquiera de los ficheros.

sass --watch archivo.scss archivo.css

//tambien se pueden comprimir los documentos .css ya compilados de modo que se emplee en el servidor directamente

sass --style=compressed archivo.scss archivo.css