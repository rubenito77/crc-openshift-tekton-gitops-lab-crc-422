# CRC OpenShift Tekton GitOps Lab - OCP 4.22

Laboratorio practico de CI/CD sobre un cluster local OpenShift creado con CRC.

La solucion combina:

- Red Hat OpenShift Pipelines y Tekton para integracion continua.
- Red Hat OpenShift GitOps y Argo CD para despliegue continuo.
- Kustomize para administrar los manifiestos por ambiente.
- Registro interno de OpenShift para almacenar las imagenes.
- GitHub como fuente de verdad.

## Entorno

- Microsoft Windows con PowerShell
- CRC
- OpenShift Container Platform 4.22.1
- Red Hat OpenShift Pipelines 1.23.1
- Red Hat OpenShift GitOps 1.21.2
- Repositorio publico de GitHub

## Objetivo

Construir una aplicacion FastAPI y demostrar el siguiente flujo:

1. Clonar el repositorio.
2. Ejecutar pruebas unitarias con pytest.
3. Construir una imagen mediante Tekton.
4. Publicar la imagen con un tag inmutable.
5. Actualizar el manifiesto Kustomize en Git.
6. Permitir que Argo CD detecte el cambio.
7. Desplegar la nueva version en OpenShift.
8. Validar actualizaciones y rollback mediante Git.

## Separacion de responsabilidades

| Componente | Responsabilidad |
| --- | --- |
| Tekton | Clonar, probar, construir, publicar y actualizar Git |
| Argo CD | Sincronizar el estado declarado en Git con OpenShift |
| Kustomize | Renderizar los manifiestos del ambiente |
| GitHub | Mantener el codigo y el estado deseado |
| Registro interno | Almacenar las imagenes de la aplicacion |
| OpenShift | Ejecutar la aplicacion |

Tekton no desplegara directamente la aplicacion.

Argo CD sera el unico componente responsable de desplegar y reconciliar
los recursos de la aplicacion.

## Flujo previsto

```text
GitHub
  |
  v
Tekton Pipeline
  |
  +-- clone
  +-- test
  +-- build
  +-- push
  +-- update-git
          |
          v
        GitHub
          |
          v
        Argo CD
          |
          v
    tekton-demo-dev
```

## Namespaces

| Namespace | Uso |
| --- | --- |
| `openshift-pipelines` | Componentes administrados por el operador |
| `tekton-cicd` | Tasks, Pipelines, PipelineRuns y credenciales de CI |
| `tekton-demo-dev` | Aplicacion desplegada por Argo CD |
| `openshift-gitops` | Instancia de Argo CD |

## Estrategia de imagenes

Las imagenes utilizaran tags inmutables derivados del commit Git.

Ejemplo:

```text
image-registry.openshift-image-registry.svc:5000/tekton-demo-dev/app-demo:506d253
```

No se utilizara `latest` para promover versiones.

## Estrategia de implementacion

La POC se construira incrementalmente:

1. Instalacion declarativa de OpenShift Pipelines.
2. Aplicacion FastAPI y pruebas unitarias.
3. Containerfile.
4. Manifiestos Kustomize.
5. Application de Argo CD.
6. Tasks de Tekton.
7. Pipeline CI.
8. PipelineRun manual.
9. Actualizacion automatica de Git.
10. Triggers y webhook de GitHub.
11. Versionado y rollback.

## Estructura prevista

```text
crc-openshift-tekton-gitops-lab-crc-422/
|-- .gitattributes
|-- README.md
|-- VERSION
|-- app/
|-- tests/
|-- container/
|-- deploy/
|   |-- base/
|   `-- overlays/
|       `-- dev/
|-- tekton/
|   |-- rbac/
|   |-- tasks/
|   |-- pipelines/
|   |-- runs/
|   `-- triggers/
|-- argocd/
|-- operators/
|   `-- openshift-pipelines/
|-- scripts/
`-- docs/
```

## Estado

- [x] Repositorio GitHub creado.
- [x] Red Hat OpenShift GitOps disponible.
- [x] Red Hat OpenShift Pipelines instalado.
- [x] TektonConfig configurado con perfil `basic`.
- [ ] Aplicacion FastAPI.
- [ ] Pruebas unitarias.
- [ ] Construccion de imagen.
- [ ] Manifiestos Kustomize.
- [ ] Application de Argo CD.
- [ ] Pipeline CI.
- [ ] Primera ejecucion manual.
- [ ] Triggers y webhook.
- [ ] Prueba de rollback.
