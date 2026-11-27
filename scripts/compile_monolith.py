import os
import re

SECTIONS_CONFIG = [
    {
        "title": "0. PÓRTICO Y ARQUITECTURA DE NAVEGACIÓN GENERAL",
        "docs": [
            "docs/index.md",
            "docs/00_INICIO_Y_MOCS/HOME.md",
        ]
    },
    {
        "title": "1. MANUALES DE ROLES Y GOBERNANZA",
        "docs": [
            "docs/01_ROLES/Rol_Investigador.md",
            "docs/01_ROLES/Rol_Centro_Investigacion.md",
            "docs/01_ROLES/Rol_Vicerrectoria.md",
            "docs/01_ROLES/Ecosistema_Comites_Gobernanza.md",
            "docs/01_ROLES/Caso_Aplicado_Centro_Facultad.md",
        ]
    },
    {
        "title": "2. PROCESOS CLAVE DEL CICLO DE VIDA DEL SIIU",
        "docs": [
            "docs/02_PROCESOS_CLAVE/Matricula_Proyectos.md",
            "docs/02_PROCESOS_CLAVE/Evaluacion_y_Aval.md",
            "docs/02_PROCESOS_CLAVE/Convocatorias_y_Fondos_CODI.md",
            "docs/02_PROCESOS_CLAVE/Inicio_Formal.md",
            "docs/02_PROCESOS_CLAVE/Modificaciones_y_Tramites.md",
            "docs/02_PROCESOS_CLAVE/Gestion_Compromisos.md",
            "docs/02_PROCESOS_CLAVE/Programa_Joven_Investigador.md",
            "docs/02_PROCESOS_CLAVE/Cierre_y_Liquidacion.md",
            "docs/02_PROCESOS_CLAVE/Reportes_y_Certificaciones.md",
        ]
    },
    {
        "title": "3. GUÍAS RÁPIDAS Y REGLAS DE ORO",
        "docs": [
            "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Reglas_Oro_SIIU.md",
            "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/Catalogo_Formatos_Oficiales.md",
            "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Investigador.md",
            "docs/03_GUIAS_RAPIDAS_CHEAT_SHEETS/CheatSheet_Centro.md",
            "docs/inicio-rapido.md",
            "docs/faq.md",
        ]
    },
    {
        "title": "4. INVESTIGACIÓN CENTRAL UDEA — CODI Y VICERRECTORÍA",
        "docs": [
            "docs/07_INVESTIGACION_CENTRAL_UDEA/index.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/codi.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/catalogo_formatos_descargables.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/circulares_vicerrectoria.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/vicerrectoria.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/siu.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/siiu.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/comite_central_etica.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/convocatorias_codi.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/convocatorias_externas.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/fondos_investigacion.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/fondo_primer_proyecto.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/programa_jovenes_investigadores.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/procedimientos_formatos.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/reglamento_investigacion.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/propiedad_intelectual.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/acceso_abierto.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/conflicto_intereses_financieros.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/permisos_investigacion.md",
            "docs/07_INVESTIGACION_CENTRAL_UDEA/atencion_ciudadano.md",
        ]
    },
    {
        "title": "5. ECOSISTEMA FACULTAD DE CIENCIAS ECONÓMICAS Y CIC",
        "docs": [
            "docs/06_CIENCIAS_ECONOMICAS_CIC/index.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/Manual_Legal_Prorrogas_Plazos_Semaforo.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/arquitectura_funcional.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/centro_investigacion.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/departamentos.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/grupos_investigacion_activos.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/matriz_conformacion_comites.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/directorio_administrativo.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/asesorias_consultorias.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/centro_documentacion.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-administrativo.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-aseguramiento-calidad.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-asuntos-estudiantiles.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-carrera-departamento-ciencias-administrativas.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-carrera-departamento-economia.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-carrera.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-clima.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-curriculo.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-egresados.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-emergencias.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-evaluacion-profesoral.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-genero.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-investigaciones-departamento-ciencias-administrativas.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-investigaciones-departamento-ciencias-contables.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-posgrados.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-practicas.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-revistas-departamento-ciencias-contables.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comite-tecnico.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/comites-programas-posgrados-departamentos.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/comites/consejo-facultad.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/angelo-macroeconomia.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/comphor.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/financiero-gicco.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/gestor.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/imark.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/innovacion-fce-gicco.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/semilleros-general.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/sifi-gifi.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/semilleros/siles-gicco.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/borradores-departamento-economia.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/publicaciones-general.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-adversia.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-conexiones.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-contaduria.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-lecturas-economia.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-oikos.md",
            "docs/06_CIENCIAS_ECONOMICAS_CIC/publicaciones/revista-perfil-coyuntura.md",
        ]
    },
    {
        "title": "6. MAPAS DE CONTENIDO (MOC) Y CONCEPTOS",
        "docs": [
            "docs/00_INICIO_Y_MOCS/MOC_Ciclo_de_Vida_Proyectos.md",
            "docs/00_INICIO_Y_MOCS/MOC_Por_Roles.md",
            "docs/00_INICIO_Y_MOCS/MOC_Tramites_y_Solicitudes.md",
            "docs/00_INICIO_Y_MOCS/MOC_Reportes_y_Constancias.md",
            "docs/00_INICIO_Y_MOCS/MOC_Marco_Normativo.md",
            "docs/04_GLOSARIO_Y_CONCEPTOS/Glosario_Terminos_SIIU.md",
            "docs/04_GLOSARIO_Y_CONCEPTOS/Catalogo_Normativo_31_Docs.md",
        ]
    },
    {
        "title": "7. SÍNTESIS DEL MARCO NORMATIVO INSTITUCIONAL (21 NORMAS)",
        "docs": [
            "docs/05_MARCO_NORMATIVO/AS_01_1994_Estatuto_General.md",
            "docs/05_MARCO_NORMATIVO/AS_083_1996_Estatuto_Profesoral.md",
            "docs/05_MARCO_NORMATIVO/AS_086_1996_Profesores_Catedra_Proyectos.md",
            "docs/05_MARCO_NORMATIVO/AS_121_1997_Estatuto_Presupuestal.md",
            "docs/05_MARCO_NORMATIVO/AS_124_1997_Estatuto_Extension.md",
            "docs/05_MARCO_NORMATIVO/AS_204_2001_Sistema_Universitario_Investigacion.md",
            "docs/05_MARCO_NORMATIVO/AS_253_2003_Docentes_Catedra_Ocasionales.md",
            "docs/05_MARCO_NORMATIVO/AS_284_2004_Gestion_Tecnologica.md",
            "docs/05_MARCO_NORMATIVO/RR_21231_2005_Estatuto_Propiedad_Intelectual.md",
            "docs/05_MARCO_NORMATIVO/AS_350_2007_Estatuto_Financiero.md",
            "docs/05_MARCO_NORMATIVO/AS_418_2014_Politica_Practicas.md",
            "docs/05_MARCO_NORMATIVO/AS_419_2014_Estatuto_Contratacion.md",
            "docs/05_MARCO_NORMATIVO/RR_39475_2014_Reglamento_Contratacion.md",
            "docs/05_MARCO_NORMATIVO/RR_39477_2014_Referente_Etico.md",
            "docs/05_MARCO_NORMATIVO/DJ_MA_02_Manual_Interventoria.md",
            "docs/05_MARCO_NORMATIVO/Ley_1838_2017_Spinoffs.md",
            "docs/05_MARCO_NORMATIVO/AS_451_2018_Politica_Acceso_Abierto.md",
            "docs/05_MARCO_NORMATIVO/AS_466_2020_Estatuto_Financiero_Vigente.md",
            "docs/05_MARCO_NORMATIVO/RR_49544_2022_Nuevo_Estatuto_PI.md",
            "docs/05_MARCO_NORMATIVO/RR_51525_2024_Ajustes_SIIU.md",
            "docs/05_MARCO_NORMATIVO/RR_00968_2026_Modernizacion.md",
        ]
    },
    {
        "title": "8. ARCHIVO MAESTRO FIDEDIGNO: 35 GUÍAS, INSTRUCTIVOS OFICIALES, PROCEDIMIENTOS Y ACTAS DE INICIO",
        "docs": [
            "archivo_maestro/VI-GU-01.md",
            "archivo_maestro/VI-GU-04.md",
            "archivo_maestro/VI-GU-05.md",
            "archivo_maestro/VI-GU-06.md",
            "archivo_maestro/VI-GU-07.md",
            "archivo_maestro/VI-GU-08.md",
            "archivo_maestro/VI-GU-09.md",
            "archivo_maestro/VI-GU-10.md",
            "archivo_maestro/VI-GU-11.md",
            "archivo_maestro/VI-GU-12.md",
            "archivo_maestro/VI-GU-13.md",
            "archivo_maestro/VI-GU-14.md",
            "archivo_maestro/VI-GU-15.md",
            "archivo_maestro/VI-GU-16.md",
            "archivo_maestro/VI-GU-17.md",
            "archivo_maestro/VI-GU-18.md",
            "archivo_maestro/VI-GU-19.md",
            "archivo_maestro/VI-GU-20.md",
            "archivo_maestro/VI-GU-22.md",
            "archivo_maestro/VI-GU-23.md",
            "archivo_maestro/VI-GU-24.md",
            "archivo_maestro/VI-GU-25.md",
            "archivo_maestro/VI-IN-01.md",
            "archivo_maestro/VI-IN-02.md",
            "archivo_maestro/VI-IN-05.md",
            "archivo_maestro/VI-IN-06.md",
            "archivo_maestro/VI-IN-07.md",
            "archivo_maestro/VI-IN-08.md",
            "archivo_maestro/VI-IN-09.md",
            "archivo_maestro/VI-IN-10.md",
            "archivo_maestro/VI-IN-11.md",
            "archivo_maestro/VI-IN-12.md",
            "archivo_maestro/PROC-CODI-INSCRIPCION-SUI.md",
            "archivo_maestro/TR-CODI-ACTA-CONSOLIDACION-GRUPOS.md",
            "archivo_maestro/TR-CODI-833-Primer-Proyecto.md",
        ]
    },
    {
        "title": "9. ARCHIVO MAESTRO FIDEDIGNO: 22 NORMAS INSTITUCIONALES Y LINEAMIENTOS CODI COMPLETOS",
        "docs": [
            "archivo_maestro/legalidad/LEG-CODI-LINEAMIENTOS-GRUPOS-2025.md",
            "archivo_maestro/legalidad/LEG-AS-01-1994.md",
            "archivo_maestro/legalidad/LEG-AS-083-1996.md",
            "archivo_maestro/legalidad/LEG-AS-086-1996.md",
            "archivo_maestro/legalidad/LEG-AS-121-1997.md",
            "archivo_maestro/legalidad/LEG-AS-124-1997.md",
            "archivo_maestro/legalidad/LEG-AS-204-2001.md",
            "archivo_maestro/legalidad/LEG-AS-253-2003.md",
            "archivo_maestro/legalidad/LEG-AS-284-2004.md",
            "archivo_maestro/legalidad/LEG-AS-350-2007.md",
            "archivo_maestro/legalidad/LEG-AS-418-2014.md",
            "archivo_maestro/legalidad/LEG-AS-419-2014.md",
            "archivo_maestro/legalidad/LEG-AS-451-2018.md",
            "archivo_maestro/legalidad/LEG-AS-466-2020.md",
            "archivo_maestro/legalidad/LEG-DJ-MA-02.md",
            "archivo_maestro/legalidad/LEG-LEY-1838-2017.md",
            "archivo_maestro/legalidad/LEG-RR-00968-2026.md",
            "archivo_maestro/legalidad/LEG-RR-21231-2005.md",
            "archivo_maestro/legalidad/LEG-RR-39475-2014.md",
            "archivo_maestro/legalidad/LEG-RR-39477-2014.md",
            "archivo_maestro/legalidad/LEG-RR-49544-2022.md",
            "archivo_maestro/legalidad/LEG-RR-51525-2024.md",
        ]
    },
    {
        "title": "10. TÉRMINOS LEGALES, POLÍTICAS Y CUMPLIMIENTO",
        "docs": [
            "docs/legal/index.md",
            "docs/legal/politicas-y-aclaraciones.md",
            "docs/legal/terminos.md",
            "docs/legal/privacidad.md",
            "docs/legal/licencias.md",
            "docs/legal/cookies.md",
        ]
    }
]

def clean_frontmatter(content):
    if content.startswith("---"):
        end_idx = content.find("---", 3)
        if end_idx != -1:
            return content[end_idx + 3:].lstrip("\r\n")
    return content

def compile():
    total_docs = sum(len(sec["docs"]) for sec in SECTIONS_CONFIG)
    print(f"Total documents configured to compile: {total_docs}")

    # Check for duplicates or missing
    seen = set()
    for sec in SECTIONS_CONFIG:
        for p in sec["docs"]:
            if p in seen:
                raise ValueError(f"Duplicate path in config: {p}")
            seen.add(p)
            if not os.path.exists(p):
                raise FileNotFoundError(f"Missing file: {p}")
    print("All files exist and are unique on disk.")

    parts = []

    header = """# COMPENDIO TOTAL Y CANÓNICO DE LA WIKI SIIU Y ECOSISTEMA DE INVESTIGACIÓN UDEA
## Sistema de Información para la Investigación Universitaria — Universidad de Antioquia

> **Documento Consolidado Monolítico (All-in-One)**  
> **Propósito:** Archivo único diseñado para ingesta directa de contexto completo por Agentes Inteligentes (Gemini, Claude, GPT), modelos LLM locales, auditoría documental exhaustiva y lectura offline sin dependencias externas.  
> **Contenido Integrado:** Manuales de roles, 9 macroprocesos operativos, 35 guías, instructivos oficiales, actas de consolidación y términos CODI fidedignos transcritos íntegramente (incluyendo VI-GU-05 con 51 figuras), 22 normas institucionales y lineamientos CODI 2025 (síntesis didáctica y textos íntegros), Manual Legal de Prórrogas y Plazos para SCMP, gobernanza CODI y Cronograma 2026, catálogo de 18 formatos descargables, 66 circulares oficiales de la Vicerrectoría, arquitectura de la Facultad de Ciencias Económicas y CIC con sus 9 grupos MinCiencias, 20 comités, semilleros y revistas científicas.

---

"""
    parts.append(header)

    doc_counter = 0

    for sec in SECTIONS_CONFIG:
        sec_title = sec["title"]
        sec_divider = f"""

================================================================================
# {sec_title}
================================================================================

"""
        parts.append(sec_divider)

        for doc_path in sec["docs"]:
            doc_counter += 1
            file_name = os.path.basename(doc_path)
            with open(doc_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
            cleaned = clean_frontmatter(raw_content).strip()

            doc_block = f"""

------------------------------------------------------------
## [DOCUMENTO]: {file_name}
*Ruta canónica original: `{doc_path}`*
------------------------------------------------------------

{cleaned}
"""
            parts.append(doc_block)

    full_text = "".join(parts).lstrip("\r\n")

    with open("WIKI_COMPLETA_SIIU_UDEA.md", "w", encoding="utf-8") as out:
        out.write(full_text)

    print(f"Successfully compiled {doc_counter} documents into WIKI_COMPLETA_SIIU_UDEA.md")
    print(f"New file size: {len(full_text.encode('utf-8')) / (1024*1024):.2f} MB ({len(full_text.splitlines())} lines)")

if __name__ == "__main__":
    compile()
