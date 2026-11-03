---
content_hash: 0740d984fce5e00b41ad31ca3f3432c99bc8de56133e2586d04f7d117dd106cf
fetched_at: '2026-06-29T00:12:07.383419+00:00'
page_id: '925339093'
product: rm
source: tdn-rm
title: Template de Criação de Tarefas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925339093
version: 2
---

Regra utilizadas para gerar o nome das tarefas no processo de geração de EAP:

* **Tipo de Objeto:**Objeto a ser utilizado.
* **Propriedade:**A propriedade a ser utilizada para compor o nome e a descrição da tarefa.
  + **Observação**: Caso a propriedade não seja encontrada no objeto filho, o sistema deve buscar a propriedade no objeto pai na seguinte prioridade:
    - andar (IfcBuildingStorey)
    - construção (IfcBuilding)
    - terreno (IfcSite)
    - projeto (IfcProject)
* **Ordem da propriedade no nível:**caso o objeto/propriedade não exista no arquivo IFC, será utilizado a próxima configuração conforme a prioridade.
* **Formatação do nome:** Formatação customizada pelo usuário.
