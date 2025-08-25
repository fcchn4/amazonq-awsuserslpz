# Comandos para ejecutar el template Groovy

## 1. Generar proyecto desde template

```bash
# Crear directorio del proyecto
mkdir groovy-hello-world
cd groovy-hello-world

# Copiar archivos del template (simulando generación)
cp ../groovy-template.yaml .
```

## 2. Generar estructura de archivos

```bash
# Crear estructura de directorios
mkdir -p src/main/groovy/com/example/groovy
mkdir -p src/test/groovy/com/example/groovy
mkdir -p gradle/wrapper

# Crear build.gradle
cat > build.gradle << 'EOF'
plugins {
    id 'groovy'
    id 'application'
    id 'de.undercouch.download' version '5.4.0'
    id 'com.netflix.nebula.ospackage' version '11.8.0'
}

group = 'com.example.groovy'
version = '1.0.0'

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.apache.groovy:groovy:4.0.26'
    testImplementation 'org.spockframework:spock-core:2.3-groovy-4.0'
}

application {
    mainClass = 'com.example.groovy.HelloWorld'
}

tasks.named('test') {
    useJUnitPlatform()
}
EOF
```

## 3. Crear archivo principal HelloWorld.groovy

```bash
cat > src/main/groovy/com/example/groovy/HelloWorld.groovy << 'EOF'
package com.example.groovy

class HelloWorld {
    static void main(String[] args) {
        println "¡Hola Mundo desde Groovy 4.0.26!"
        println "Gradle version: 8.13"
        println "Plugins cargados: de.undercouch.download, nebula.ospackage"
    }
}
EOF
```

## 4. Configurar Gradle Wrapper

```bash
# Crear gradle-wrapper.properties
cat > gradle/wrapper/gradle-wrapper.properties << 'EOF'
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.13-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
EOF

# Crear settings.gradle
cat > settings.gradle << 'EOF'
rootProject.name = 'groovy-hello-world'
EOF
```

## 5. Ejecutar el proyecto

```bash
# Inicializar Gradle wrapper
gradle wrapper --gradle-version 8.13

# Compilar el proyecto
./gradlew build

# Ejecutar la aplicación
./gradlew run

# Ejecutar tests
./gradlew test

# Ver información del proyecto
./gradlew projects
./gradlew dependencies
```

## 6. Verificar plugins

```bash
# Verificar que los plugins están cargados
./gradlew tasks --all | grep -E "(download|ospackage)"

# Ver información de la build
./gradlew buildEnvironment
```

## Salida esperada

```
¡Hola Mundo desde Groovy 4.0.26!
Gradle version: 8.13
Plugins cargados: de.undercouch.download, nebula.ospackage
```