# Regla: Actualizador Automático de README

## Objetivo

Mantener el README.md principal actualizado automáticamente con la estructura de carpetas y contenido del repositorio.

## Instrucciones

Cuando se creen nuevas carpetas o archivos en la raíz del repositorio:

1. **Actualizar README.md** con:

   - Estructura de directorios usando formato tree
   - Descripción de cada carpeta nueva como un tópico
   - Mantener formato consistente

2. **Formato del README.md principal**:

   ```markdown
   # Examples for Demonstrations

   Este repositorio contiene ejemplos para demostraciones de Amazon Q.

   ## Estructura del Proyecto

   ```
   [INSERTAR SALIDA DEL COMANDO tree AQUÍ]
   ```

   ## Tópicos Disponibles

   ### [Nombre de Carpeta](./nombre-carpeta/)

   Descripción breve del contenido.
   ```

3. **Formato de README secundarios**:

   - Cada carpeta debe tener su propio README.md con detalles completos
   - Incluir información técnica, limitaciones y casos de uso
   - Mantener el README principal simple y enfocado en navegación

4. **Reglas de formato markdown**:

   - Agregar línea en blanco después de cada título (###)
   - Usar espacios consistentes en listas y sublistas
   - Mantener líneas en blanco entre secciones
   - Verificar que los bloques de código tengan formato correcto
   - Aplicar formato consistente en todas las reglas nuevas o actualizadas
   - Revisar espaciado en subtítulos en negrita (**texto**)

5. **Reglas específicas**:

   - Cada carpeta en la raíz = un nuevo tópico
   - Generar descripción basada en el contenido de la carpeta
   - Mantener orden alfabético de tópicos
   - Incluir tree completo hasta 2 niveles de profundidad

6. **Ejecutar automáticamente** cuando:

   - Se cree una nueva carpeta en la raíz
   - Se modifique contenido significativo
   - Se solicite explícitamente actualizar documentación
   - Se genere o actualice cualquier regla de Amazon Q
   - Se requiera explicar contexto del proyecto a nuevos colaboradores
