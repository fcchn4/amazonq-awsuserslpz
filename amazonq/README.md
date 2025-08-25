# Amazon Q - Demostración de Capacidades

Repositorio completo para demostrar las capacidades de Amazon Q en automatización de desarrollo, análisis de código y generación de proyectos.

## Resumen Ejecutivo

**Objetivo**: Mostrar cómo Amazon Q puede reducir 70% el tiempo de documentación, identificar vulnerabilidades de seguridad y acelerar la modernización de aplicaciones legacy.

**Caso de uso**: Migración de aplicaciones legacy Java a arquitecturas modernas de microservicios.

**Resultados**: 6 reglas personalizadas, +150 ejemplos analizables, 1 proyecto funcional generado, 8 prompts efectivos documentados.

## Capacidades Principales

- **Análisis de código completo**: Revisión de seguridad, calidad, mejores prácticas
- **Generación y modificación de código**: Desde snippets hasta aplicaciones completas
- **Interacción con filesystem**: Lectura, escritura, navegación de proyectos
- **Ejecución de comandos**: Automatización de tareas del sistema
- **Comprensión contextual**: Entiende la estructura del proyecto y dependencias

## Funcionalidades Únicas

- **Reglas personalizadas**: Como la que creamos para auto-actualizar README
- **Contexto de workspace**: Usa `@workspace`, `@folder`, `@file` para incluir contexto específico
- **Modos de operación**: Agentic ON/OFF según necesidades de seguridad
- **Integración IDE**: Funciona directamente en el entorno de desarrollo

## Casos de Uso Prácticos

- Automatización de documentación (como nuestro ejemplo)
- Refactoring de código legacy
- Implementación de nuevas features
- Debugging y troubleshooting
- Code reviews automatizados

## Limitaciones Actuales

**Nota importante**: Al 27 de agosto de 2025, Amazon Q no tiene capacidad de análisis de imágenes (PNG, JPEG, GIF, SVG). Para diagramas de infraestructura, se recomienda proporcionar descripciones textuales complementarias.

## Repositorio de Ejemplos

### blog-ejemplos

Repositorio clonado con +150 ejemplos de código Java para demostrar las capacidades de análisis de Amazon Q.

**Cómo clonar**:

```bash
git clone git@github.com:picodotdev/blog-ejemplos.git
```

**Propósito**:

- Demostrar análisis de código legacy y moderno
- Mostrar capacidades de revisión de seguridad
- Ejemplos de modernización de aplicaciones
- Casos de uso reales para migración de arquitecturas

**Tecnologías incluidas**:

- Java (desde Java 8 hasta versiones modernas)
- Spring Boot, Spring Cloud, JavaEE
- Microservicios y arquitecturas distribuidas
- Docker, Kubernetes, Consul, Vault
- Bases de datos: MongoDB, Redis, PostgreSQL
- Frameworks web: React, Angular, JavaScript

### Ejemplos Seleccionados para Análisis

Para la demostración de capacidades de Amazon Q, utilizaremos estos tres proyectos específicos:

1. **NginxLoadBalancer** - Configuración de balanceador de carga con Docker
2. **SpringBoot** - Aplicación web moderna con Gradle y dependencias
3. **JavaLogging** - Implementación de logging con múltiples frameworks

Estos ejemplos demostrarán:
- Análisis de configuraciones de infraestructura
- Revisión de código Java moderno
- Identificación de mejores prácticas en logging
- Sugerencias de optimización y seguridad

## Proyectos Generados

### groovy-project

Proyecto Groovy funcional generado desde template YAML que demuestra las capacidades de scaffolding de Amazon Q.

**Características**:

- **Groovy 4.0.26** con Gradle 8.13
- **Plugin de.undercouch.download** integrado
- **Aplicación "Hola Mundo"** ejecutable
- **Estructura completa** de proyecto con src/main/groovy
- **Configuración Gradle** optimizada para compatibilidad
- **Resolución automática** de problemas de compatibilidad

**Proceso de generación**:

1. Template YAML en `.amazonq/rules/groovy-template.yaml`
2. Comandos automatizados en `.amazonq/rules/comandos-groovy-template.md`
3. Generación de estructura completa de directorios
4. Ajustes de compatibilidad en tiempo real
5. Compilación y ejecución exitosa

**Ejecución**:

```bash
cd amazonq/groovy-project
gradle run
```

**Salida esperada**:

```
¡Hola Mundo desde Groovy 4.0.26!
Gradle version: 8.13
Plugins cargados: de.undercouch.download, nebula.ospackage
```

**Lecciones aprendidas**:

- Plugin `nebula.ospackage` incompatible con Gradle 8.13
- `toolchain` reemplazado por `sourceCompatibility/targetCompatibility`
- Importancia de ajustes dinámicos durante la generación

## Prompts Útiles para Amazon Q

### Prompts Efectivos

1. **Creación de reglas automatizadas**:

   ```
   Crea una regla para generar y actualizar automáticamente el archivo README.md 
   basado en la estructura de carpetas del repositorio. Cada carpeta nueva en la 
   raíz debe convertirse en un nuevo tópico con estructura tree.
   ```

2. **Organización de documentación**:

   ```
   Reorganiza la documentación: README principal solo con lista de tópicos, 
   README secundarios en cada carpeta con detalles completos. Agrega enlaces 
   locales para navegación directa entre documentos.
   ```

3. **Clonado y análisis de repositorios**:

   ```
   Ejecuta git clone git@github.com:picodotdev/blog-ejemplos.git para clonar 
   el repositorio dentro de la carpeta amazonq, analiza el repositorio 
   blog-ejemplos y busca ejemplos con Java, Python, Docker y tecnologías relacionadas.
   ```

4. **Búsqueda y selección de ejemplos**:

   ```
   Busca en la carpeta amazonq/blog-ejemplos ejemplos que contengan Java, Docker, 
   y Spring. Selecciona los más representativos para demostrar capacidades de 
   análisis de código legacy, configuración de infraestructura y mejores prácticas.
   ```

5. **Análisis detallado de código**:

   ```
   Analiza el ejemplo NginxLoadBalancer: describe qué realiza, qué variables 
   necesita, identifica buenas y malas prácticas, riesgos de seguridad y 
   sugerencias de modernización.
   ```

6. **Generación de templates de proyecto**:

   ```
   Usa el template YAML ubicado en .amazonq/rules/groovy-template.yaml para crear 
   un proyecto Groovy en la ruta amazonq/groovy-project. El proyecto debe usar 
   Groovy 4.0.26, Gradle 8.13, incluir los plugins de.undercouch.download y 
   nebula.ospackage. Sigue los comandos en .amazonq/rules/comandos-groovy-template.md 
   para generar y ejecutar el proyecto completo.
   ```

7. **Resolución de problemas de compatibilidad**:

   ```
   Al generar el proyecto Groovy, si encuentras errores de compatibilidad con 
   plugins o configuración Java, ajusta las versiones y configuraciones en tiempo 
   real. Reemplaza toolchain por sourceCompatibility/targetCompatibility si es necesario.
   ```

8. **Contexto completo del proyecto**:

   ```
   Soy nuevo en el proyecto, dame el contexto completo del proyecto por favor
   ```

9. **Cálculo dinámico de métricas**:

   ```
   Calcula las métricas actuales del proyecto: cuántas reglas hay en .amazonq/rules/, 
   cuántos ejemplos en blog-ejemplos/, cuántos proyectos generados y cuántos 
   prompts documentados en este README.
   ```

### Mejores Prácticas para Prompts

- **Se específico**: Define claramente el objetivo y el resultado esperado
- **Incluye contexto**: Menciona archivos, carpetas o estructura relevante
- **Solicita formato**: Especifica si necesitas markdown, código, o documentación
- **Itera gradualmente**: Haz mejoras incrementales en lugar de cambios masivos

### Prompts Menos Efectivos

- Solicitudes vagas como "mejora esto" sin contexto específico
- Cambios múltiples sin priorizar qué es más importante
- Instrucciones contradictorias en el mismo prompt