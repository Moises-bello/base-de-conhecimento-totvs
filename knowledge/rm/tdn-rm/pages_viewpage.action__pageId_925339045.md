---
content_hash: 7675a7d4c57d636ff12435f418ab89902746caa4d43c42992defb3b6310575f6
fetched_at: '2026-06-29T00:12:07.380547+00:00'
page_id: '925339045'
product: rm
source: tdn-rm
title: Nível do Template
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925339045
version: 2
---

Regras utilizadas para gerar as etapas no processo de geração da EAP:

* **Tipo de Nível:** indica o tipo de nível que será usado para geração da EAP, que pode ser importado da estrutura do arquivo IFC ou através da criação de uma .
* **Nível:** indica o nível da etapa/tarefa começando do nível 1.

Observação: 

A quantidade de níveis deve estar de acordo com configuração da máscara de código da tarefa. Exemplo: a máscara de código da tarefa "###.##.##" possui apenas 3 níveis.

* **Entidade:** indica a entidade que será utilizada para representar a etapa.
  + **Projeto (IfcProject):** Extrai informações do projeto do arquivo IFC para gerar no nome da etapa.
  + **Local (IfcSite):** Extrai informações do terreno do arquivo IFC para gerar no nome da etapa.
  + **Construção (IfcBuilding):** Extrai informações da construção do arquivo IFC para gerar no nome da etapa.
  + **Andar (IfcBuildingStorey):** Extrai informações do andar do arquivo IFC para gerar no nome da etapa.
  + **Entidade**: Gera a etapa agrupando por tipo de objeto: IfcDoor, IfcWindow, IfcWall...
  + **Disciplina do Modelo**: Gera a etapa pegando o nome da disciplina informada no cadastro de modelo.
  + **Tipo de Objeto**: Gera a etapa agrupando por tipo de objeto.
  + **Nome do arquivo IFC**: Gera a etapa com o nome do arquivo IFC.

* **Propriedade:**indica a propriedade do objeto que será utilizada para representar a etapa.

* **Ordem da propriedade no nível:**caso o objeto/propriedade não exista no arquivo IFC, será utilizado a próxima configuração conforme a prioridade.
* **Valor default:**caso o nome do objeto esteja vazio, será utilizado este valor default.
* **Formatação do nome:** Formatação customizada pelo usuário.
