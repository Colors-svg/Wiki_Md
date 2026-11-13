# Documentación y Base de Conocimiento del SIIU
### Vicerrectoría de Investigación — Universidad de Antioquia

Portal técnico y operativo del **Sistema de Información para la Investigación Universitaria (SIIU)**, diseñado para la consulta integral de procesos, convocatorias, trámites administrativos y normatividad vigente.

> **Acceso a la Wiki Interactiva en Línea:**  
> Navegue por la documentación estructurada con buscador integrado, diagramas de proceso y barra lateral de navegación en:  
> **[https://colors-svg.github.io/Wiki/](https://colors-svg.github.io/Wiki/)**

---

## Estructura de la Documentación

### 1. Manuales Operativos por Perfil
- **Investigador Principal / Tutor:** Formulación, radicación, gestión de compromisos académicos, cupos de Joven Investigador y trámites administrativos.
- **Centro de Investigación / Extensión:** Evaluación técnica formal, devoluciones para ajustes, emisión de avales institucionales y aprobación de trámites.
- **Vicerrectoría de Investigación:** Parametrización del sistema, gestión de convocatorias, asignación de evaluadores pares, trámites en instancias centrales (CODI) y liquidación de proyectos.

### 2. Procesos Clave del Ciclo de Vida
- **Matrícula e Inscripción:** Proyectos en convocatoria interna, proyectos inscritos con financiación externa y primer proyecto.
- **Evaluación y Aval:** Criterios de evaluación técnica de Centro, protocolo de subsanación y asignación de pares evaluadores.
- **Inicio Formal:** Verificación de pólizas, contratos, centros de costo y formalización de acta de inicio.
- **Modificaciones Administrativas:** Prórrogas de ejecución, traslados presupuestales (cambio de rubro) y modificaciones en el equipo de trabajo.
- **Compromisos y Seguimiento:** Carga de informes parciales, finales, productos y solicitudes de plazo.
- **Programa Joven Investigador:** Matrícula de cupos asignados, verificación de requisitos bancarios y solicitudes de prórroga.
- **Cierre y Liquidación:** Emisión de paz y salvos técnicos, acta de cierre y liquidación financiera.
- **Reportes y Certificaciones:** Emisión de certificados de participación, constancias de evaluación y reportes consolidados.

### 3. Normativa Institucional y Archivo Maestro
- **Archivo Maestro de Procesos (31 Documentos):** Transcripción fidedigna de las 21 guías de proceso (`VI-GU-*`) y 10 instructivos técnicos (`VI-IN-*`).
- **Archivo Maestro de Legalidad (21 Documentos):** Transcripción íntegra de las 21 leyes, acuerdos superiores y resoluciones rectorales que rigen la investigación en la UdeA (`archivo_maestro/legalidad/`).
- **Marco Normativo Wiki (21 Fichas Didácticas):** Fichas operativas con diagramas Mermaid, tablas de impacto y enlaces cruzados hacia el SIIU (`wiki/05_MARCO_NORMATIVO/`).
- **Matriz de Concordancia Normativa:** Mapa central de contenido que articula trámites del SIIU con normas habilitantes (`wiki/00_INICIO_Y_MOCS/MOC_Marco_Normativo.md`).

---

## Organización del Repositorio

```text
├── mkdocs.yml                      # Configuración de compilación para GitHub Pages
├── docs/                          # Directorio fuente de la documentación web
├── wiki/                          # Base de conocimiento modular y didáctica
│   ├── 00_INICIO_Y_MOCS/          # Mapas de contenido (Ciclo, Roles, Trámites, Marco Normativo)
│   ├── 01_ROLES/                  # Manuales por rol operativo (Investigador, Centro, Vicerrectoría)
│   ├── 02_PROCESOS_CLAVE/         # Procedimientos secuenciales detallados
│   ├── 03_GUIAS_RAPIDAS_CHEAT_SHEETS/ # Resúmenes ejecutivos y reglas de oro
│   ├── 04_GLOSARIO_Y_CONCEPTOS/   # Glosario oficial y catálogo de 31 docs
│   └── 05_MARCO_NORMATIVO/        # 21 fichas didácticas del marco legal UdeA
├── archivo_maestro/               # Transcripciones fidedignas 1 a 1
│   ├── VI-GU-* / VI-IN-*          # 31 documentos de guías e instructivos
│   └── legalidad/                 # 21 documentos normativos íntegros (Leyes, CSU, Resoluciones)
├── fuentes_pdf/                   # Documentos PDF originales de la Vicerrectoría
└── Legalidad/                     # Normativa legal original en PDF de la Universidad
```


## 📚 Mapa Estructurado de Lectura Rápida para Agentes IA y LLMs

Para consultar cualquier procedimiento sin ambigüedades, utiliza las siguientes rutas directas en texto plano:

### 1. Procesos Clave del Ciclo de Vida del SIIU
- **Matrícula e Inscripción de Proyectos:** [docs/02_PROCESOS_CLAVE/Matricula_Proyectos.md](docs/02_PROCESOS_CLAVE/Matricula_Proyectos.md)
  *(Convocatoria Interna CODI, Proyectos Inscritos con financiación externa Minciencias/SGR y Primer Proyecto)*.
- **Evaluación Técnica y Aval Institucional:** [docs/02_PROCESOS_CLAVE/Evaluacion_y_Aval.md](docs/02_PROCESOS_CLAVE/Evaluacion_y_Aval.md)
  *(Revisión formal de Centro, devolución para ajustes, asignación de evaluadores pares y aval)*.
- **Inicio Formal de Proyectos:** [docs/02_PROCESOS_CLAVE/Inicio_Formal.md](docs/02_PROCESOS_CLAVE/Inicio_Formal.md)
  *(Contratos, pólizas de garantía, centro de costos institucional y generación de acta de inicio)*.
- **Modificaciones, Novedades y Trámites:** [docs/02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md](docs/02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md)
  *(Prórrogas de proyecto, traslados y cambios de rubro presupuestal, cambios de participantes e IP)*.
- **Gestión de Compromisos:** [docs/02_PROCESOS_CLAVE/Gestion_Compromisos.md](docs/02_PROCESOS_CLAVE/Gestion_Compromisos.md)
  *(Informes de avance, informes finales, productos académicos y prórrogas de entrega)*.
- **Programa Joven Investigador:** [docs/02_PROCESOS_CLAVE/Programa_Joven_Investigador.md](docs/02_PROCESOS_CLAVE/Programa_Joven_Investigador.md)
  *(Matrícula de cupos, vinculación de hoja de vida y cuentas bancarias permitidas)*.
- **Cierre y Liquidación:** [docs/02_PROCESOS_CLAVE/Cierre_y_Liquidacion.md](docs/02_PROCESOS_CLAVE/Cierre_y_Liquidacion.md)
  *(Aprobación técnica de compromisos, acta de cierre y paz y salvo presupuestal)*.
- **Reportes y Certificaciones:** [docs/02_PROCESOS_CLAVE/Reportes_y_Certificaciones.md](docs/02_PROCESOS_CLAVE/Reportes_y_Certificaciones.md)
  *(Constancias de participación en proyectos, constancia de evaluador e historial)*.

### 2. Manuales de Operación por Rol y Gobernanza
- **Investigador Principal y Tutor:** [docs/01_ROLES/Rol_Investigador.md](docs/01_ROLES/Rol_Investigador.md)
- **Centro de Investigación / Extensión:** [docs/01_ROLES/Rol_Centro_Investigacion.md](docs/01_ROLES/Rol_Centro_Investigacion.md)
- **Vicerrectoría de Investigación:** [docs/01_ROLES/Rol_Vicerrectoria.md](docs/01_ROLES/Rol_Vicerrectoria.md)
- **Ecosistema de Comités y Gobernanza:** [docs/01_ROLES/Ecosistema_Comites_Gobernanza.md](docs/01_ROLES/Ecosistema_Comites_Gobernanza.md)

### 3. Fichas de Referencia Rápida
- **Reglas de Oro del SIIU:** [docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Reglas_Oro_SIIU.md](docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Reglas_Oro_SIIU.md)
- **Ficha Rápida Investigador:** [docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Investigador.md](docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Investigador.md)
- **Ficha Rápida Centro:** [docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Centro.md](docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Centro.md)
- **Glosario Canónico:** [docs/04_GLOSARIO_Y_CONCEPTOS/Glosario_Terminos_SIIU.md](docs/04_GLOSARIO_Y_CONCEPTOS/Glosario_Terminos_SIIU.md)

### 4. Transcripciones Maestras y Normativa
- **31 Guías e Instructivos Oficiales:** [rchivo_maestro/](archivo_maestro/)
- **21 Normas Institucionales UdeA:** [rchivo_maestro/legalidad/](archivo_maestro/legalidad/)
