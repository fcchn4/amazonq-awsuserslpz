# MCP Server - Desarrollo Local con Python

Comandos UV para crear el espacio de trabajo de desarrollo para un MCP server local.

## Requisitos Importantes

- NodeJS 22 o superior.
- Python 3.12 o superior.

## Comandos UV

### 1. Crear proyecto MCP y Configurar entorno virtual

```bash
# Crear y/o ingresar a la carpeta mcp-server
mkdir mcp-server
cd mcp-server

# Dentro de la carpeta mcp-server
uv init

# Crear entorno virtual y activar
uv venv
source .venv/bin/activate

# Instalar dependencias importantes
uv add "mcp[cli]" httpx

# Crear el archivo mcp.py
touch mcp.py
```

### 2. Ejecutar servidor MCP

```bash
# Ejecutar servidor local
npx @modelcontextprotocol/inspector python mcp.py

# Otra forma de ejecución
npx @modelcontextprotocol/inspector uvx mcp-server

# Otra forma
npx @modelcontextprotocol/inspector uvx .
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
