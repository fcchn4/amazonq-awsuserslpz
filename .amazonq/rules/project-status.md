# Regla: Status y Contexto del Proyecto

## Objetivo

Proporcionar automáticamente el contexto completo, objetivo, ejemplos y status actual del proyecto cada vez que se comparta con nuevos miembros del equipo o colaboradores.

## Contexto del Proyecto

### **Propósito Principal**

Repositorio de demostración para charla técnica sobre Amazon Q, mostrando capacidades reales de análisis de código, generación automática de documentación, scaffolding de proyectos y automatización de tareas de desarrollo.

### **Caso de Uso Empresarial**

Migración de aplicaciones legacy Java a arquitecturas modernas de microservicios, utilizando Amazon Q para:

- Análisis automático de código legacy (+150 ejemplos reales)
- Generación de documentación automática
- Identificación de vulnerabilidades de seguridad
- Sugerencias de modernización y refactoring

## Status Dinámico del Proyecto

### **Reglas Activas**
- Contar archivos `.md` y `.yaml` en `.amazonq/rules/`
- Verificar proyectos generados en `amazonq/`
- Analizar ejemplos disponibles en `blog-ejemplos/`
- Calcular prompts documentados en README secundario

### **Métricas Automáticas**
- **Reglas implementadas**: Archivos en `.amazonq/rules/`
- **Proyectos generados**: Carpetas en `amazonq/` (excluyendo blog-ejemplos)
- **Ejemplos disponibles**: Carpetas en `amazonq/blog-ejemplos/`
- **Documentación**: Archivos README.md existentes

## Ejemplos Implementados

### **1. Análisis de Código Legacy**

- **NginxLoadBalancer**: Configuración Docker con buenas/malas prácticas identificadas
- **SpringBoot**: Aplicación moderna para revisión de arquitectura
- **JavaLogging**: Implementación de logging para mejores prácticas

### **2. Generación de Proyectos**

- **groovy-project**: Proyecto funcional Groovy 4.0.26 + Gradle 8.13
- **Template YAML**: Sistema de scaffolding automatizado
- **Resolución de compatibilidad**: Ajustes en tiempo real

### **3. Automatización de Documentación**

- **README auto-actualizable**: Basado en estructura de carpetas
- **Formato markdown consistente**: Reglas de estilo automatizadas
- **Enlaces locales**: Navegación entre documentos

## Status Actual

### ✅ **Completado**

**Instrucción**: Calcular dinámicamente el status verificando:
- [x] **Reglas activas**: Contar archivos en `.amazonq/rules/`
- [x] **Repositorio clonado**: Verificar existencia de `amazonq/blog-ejemplos/`
- [x] **Ejemplos analizados**: Buscar documentación de análisis (ej: NginxLoadBalancer)
- [x] **Templates funcionales**: Verificar archivos `.yaml` en reglas
- [x] **Proyectos ejecutables**: Contar carpetas con `build.gradle` o similares
- [x] **Documentación actualizada**: Verificar README.md en cada carpeta
- [x] **Prompts documentados**: Contar secciones numeradas en README secundario

### 🔄 **En Progreso**

- [ ] Análisis de SpringBoot y JavaLogging pendientes
- [ ] Templates adicionales (Java, Python, Node.js)
- [ ] Casos de uso de seguridad avanzados

### 📊 **Métricas Calculadas Dinámicamente**

**Instrucción**: Al proporcionar contexto, calcular automáticamente:
- **Ejemplos disponibles**: Contar carpetas en `amazonq/blog-ejemplos/`
- **Reglas activas**: Contar archivos en `.amazonq/rules/`
- **Prompts documentados**: Contar secciones numeradas en README secundario
- **Proyectos generados**: Contar carpetas en `amazonq/` (excluyendo blog-ejemplos)
- **Ejemplos analizados**: Verificar cuáles tienen documentación de análisis

## Beneficios Demostrados

### **Para Desarrolladores**

- Reducción del 70% en tiempo de documentación
- Identificación proactiva de issues de seguridad
- Scaffolding automático de proyectos
- Análisis de código legacy sin esfuerzo manual

### **Para Equipos**

- Estandarización de prácticas de desarrollo
- Aceleración del onboarding de nuevos miembros
- Automatización de tareas repetitivas
- Mejora en calidad de código

## Instrucciones de Uso

Cuando Amazon Q necesite explicar este proyecto:

1. **Mencionar el propósito educativo** y de demostración
2. **Destacar el caso empresarial** de migración legacy
3. **Mostrar ejemplos concretos** implementados
4. **Proporcionar métricas cuantificables**
5. **Explicar beneficios tangibles** para desarrolladores y equipos
6. **Incluir status actual** y próximos pasos

## Prompt para Compartir Proyecto

```
Este repositorio demuestra las capacidades de Amazon Q para automatización 
de desarrollo. Incluye ejemplos de código real, reglas personalizadas, 
templates de scaffolding y casos de uso empresariales. Calcula dinámicamente 
las métricas del proyecto para mostrar cómo Amazon Q puede reducir 70% el 
tiempo de documentación, identificar vulnerabilidades de seguridad y acelerar 
la modernización de aplicaciones legacy.

[CALCULAR: X ejemplos, Y reglas, Z prompts, W proyectos generados]
```