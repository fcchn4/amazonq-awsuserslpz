# Examples for Demonstrations

Repositorio de demostración para charla técnica sobre Amazon Q, mostrando capacidades reales de análisis de código, generación automática de documentación, scaffolding de proyectos y automatización de tareas de desarrollo.

## Estructura del Proyecto

```
amazonq-awsuserslpz/
|-- .amazonq/
|   `-- rules/
|       |-- auto-readme-updater.md
|       |-- comandos-groovy-template.md
|       |-- groovy-template.yaml
|       |-- project-context.md
|       |-- project-status.md
|       `-- template-generator.md
|-- amazonq/
|   `-- README.md
|-- mcp-server/
|   |-- poc.py
|   |-- pyproject.toml
|   `-- README.md
|-- .gitignore
|-- LICENSE.md
`-- README.md
```

## Tópicos Disponibles

### [amazonq](./amazonq/)

Plantillas, ejemplos y proyectos generados para Amazon Q. Incluye documentación completa de capacidades y casos de uso prácticos.

**Contenido**:

- **README.md**: Documentación detallada con prompts y casos de uso
- **Ejemplos de análisis**: NginxLoadBalancer, SpringBoot, JavaLogging
- **Templates de scaffolding**: Groovy, Java, Python

### [mcp-server](./mcp-server/)

Servidor MCP (Model Context Protocol) funcional que demuestra integración con API externa de Star Wars.

**Características**:

- **FastMCP**: Framework para servidores MCP
- **API Integration**: Conexión a SWAPI (Star Wars API)
- **Tools implementadas**: connection, get_api_url, get_people
- **Manejo asíncrono**: Funciones async para llamadas HTTP
- **Error handling**: Validación y manejo de errores

**Tecnologías**:

- Python 3.12+ con UV
- FastMCP + httpx
- Inspector MCP para testing

**Métricas actuales**:

- 6 reglas personalizadas implementadas
- 8 prompts efectivos documentados
- 1 servidor MCP funcional
- 3 tools MCP implementadas

## Referencias

1. [Model Context Protocol - Server Quickstart](https://modelcontextprotocol.io/quickstart/server)
2. [DrawIO MCP Server - Community Example](https://mcp.so/server/drawio-mcp-server/lgazo?tab=comments)
3. [DrawIO MCP Server - Implementation Example](https://github.com/lgazo/drawio-mcp-server/blob/main/docs/examples/example1.md)
4. [Amazon Q Developer - Official Documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/)
5. [Amazon Q Developer - IDE Integration Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/ide-integration.html)
6. [Amazon Q Developer - Code Generation Best Practices](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-generation.html)
7. [Amazon Q Developer - Security Scanning](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-scans.html)
