# MCP Server - Star Wars API Demo

Servidor MCP funcional que demuestra integración con API externa usando FastMCP y httpx.

## Descripción del Proyecto

Este proyecto implementa un servidor MCP (Model Context Protocol) que se conecta a la API de Star Wars (SWAPI) para obtener información de personajes. Demuestra:

- **Servidor MCP funcional** con FastMCP
- **Integración con API externa** (https://www.swapi.tech/)
- **Manejo de errores HTTP** y validación
- **Funciones asíncronas** para llamadas a API
- **Tools disponibles** para inspección

## Tools Implementadas

### 1. `connection()`
- **Descripción**: Test básico de conexión al servidor MCP
- **Retorna**: Mensaje de confirmación "Github MCP server is running!"

### 2. `get_api_url()`
- **Descripción**: Obtiene la URL base de la API
- **Retorna**: URL de la API de Star Wars (https://www.swapi.tech/api/people)

### 3. `get_people(people_number: int)`
- **Descripción**: Obtiene información de un personaje específico de Star Wars
- **Parámetro**: `people_number` - ID del personaje (ej: 1 para Luke Skywalker)
- **Retorna**: JSON con datos del personaje o mensaje de error
- **Ejemplo**: `get_people(1)` retorna información de Luke Skywalker

## Requisitos

- **NodeJS 22+** para el inspector MCP
- **Python 3.12+** para el servidor
- **UV** para gestión de dependencias

## Comandos UV

### 1. Configurar proyecto

```bash
# Navegar al directorio
cd mcp-server

# Crear entorno virtual
uv venv
source .venv/bin/activate

# Instalar dependencias
uv sync
```

### 2. Ejecutar servidor MCP

```bash
# Ejecutar con inspector MCP
npx @modelcontextprotocol/inspector python poc.py

# Ejecutar directamente
uv run python poc.py
```

### 3. Retomar el proyecto

```bash
# Si no existe el entorno virtual
uv venv

# Activar el entorno virtual
source .venv/bin/activate

# Sincronizar entorno
uv sync

# Si es necesario volver a instalar las dependencias
uv add "mcp[cli]" httpx
```

## Uso del Inspector MCP

1. Ejecutar: `npx @modelcontextprotocol/inspector python poc.py`
2. Abrir navegador en la URL mostrada
3. Probar las tools disponibles:
   - `connection` - Test de conexión
   - `get_api_url` - Ver URL de la API
   - `get_people` - Obtener personaje (usar números 1-83)

## Ejemplos de Uso

```bash
# Obtener Luke Skywalker (ID: 1)
get_people(1)

# Obtener Darth Vader (ID: 4)
get_people(4)

# Obtener Leia Organa (ID: 5)
get_people(5)
```

## Estructura del Código

- **FastMCP**: Framework para crear servidores MCP
- **httpx**: Cliente HTTP asíncrono para llamadas a API
- **Error handling**: Manejo de errores HTTP y de red
- **Type hints**: Tipado completo para mejor desarrollo