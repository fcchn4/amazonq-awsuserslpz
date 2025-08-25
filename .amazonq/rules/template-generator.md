# Regla: Generador de Templates de Proyecto

## Objetivo

Automatizar la creación de templates de proyecto y su implementación para demostrar capacidades de scaffolding de Amazon Q.

## Instrucciones para Templates

### 1. Creación de Templates YAML

Cuando se solicite crear un template de proyecto:

- **Estructura**: Usar formato YAML con metadata, parámetros y archivos
- **Versionado**: Especificar versiones exactas de herramientas y dependencias
- **Compatibilidad**: Verificar compatibilidad entre versiones de plugins
- **Completitud**: Incluir estructura completa (src, test, build, config)

### 2. Generación de Proyectos

Para generar proyectos desde templates:

- **Ruta estándar**: Crear en `amazonq/{tecnologia}-project/`
- **Estructura de directorios**: Seguir convenciones de la tecnología
- **Archivos de configuración**: Incluir todos los archivos necesarios
- **Scripts de ejecución**: Proporcionar comandos completos

### 3. Formato de Template YAML

```yaml
apiVersion: v1
kind: Template
metadata:
  name: {nombre-template}
  description: "Descripción del template"
spec:
  parameters:
    - name: PROJECT_NAME
      description: "Nombre del proyecto"
      value: "default-name"
  files:
    - path: "archivo.ext"
      content: |
        contenido del archivo
```

### 4. Comandos de Implementación

Siempre incluir:

- **Creación de estructura**: `mkdir -p` para directorios
- **Generación de archivos**: Usando `cat > archivo << 'EOF'`
- **Permisos ejecutables**: `chmod +x` cuando sea necesario
- **Comandos de build**: Específicos de la tecnología
- **Comandos de ejecución**: Para probar el resultado
- **Verificación**: Comandos para validar la configuración

### 5. Tecnologías Soportadas

Templates disponibles para:

- **Groovy**: Con Gradle, plugins específicos y Spock testing
- **Java**: Spring Boot, Maven/Gradle, JUnit
- **Python**: Flask/Django, pip, pytest
- **Node.js**: Express, npm/yarn, Jest
- **Docker**: Compose, Dockerfile, multi-stage builds

## Reglas Específicas

### Groovy Projects

- **Versión Groovy**: 4.0.26
- **Gradle**: 8.13
- **Plugins requeridos**: de.undercouch.download, nebula.ospackage
- **Testing**: Spock framework
- **Ruta**: `amazonq/groovy-project/`

### Estructura de Archivos

```
amazonq/{tecnologia}-project/
├── build.gradle / pom.xml / package.json
├── src/
│   ├── main/{lenguaje}/
│   └── test/{lenguaje}/
├── gradle/wrapper/ (si aplica)
└── README.md
```

## Prompt Sugerido para Testing

```
Usa el template YAML ubicado en .amazonq/rules/groovy-template.yaml para crear 
un proyecto Groovy en la ruta amazonq/groovy-project. El proyecto debe usar 
Groovy 4.0.26, Gradle 8.13, incluir los plugins de.undercouch.download y 
nebula.ospackage. Sigue los comandos en .amazonq/rules/comandos-groovy-template.md 
para generar y ejecutar el proyecto completo.
```