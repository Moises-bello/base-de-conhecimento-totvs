---
content_hash: 8a67244cca92fa9a40a85ffb0867cebffaf95b7befe669e17acd1c7cfd7c7e9c
fetched_at: '2026-06-29T00:12:07.387926+00:00'
page_id: '925340318'
product: rm
source: tdn-rm
title: Template de Criação de Quantitativos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925340318
version: 6
---

Regras utilizadas para extrair as quantidades das tarefas no processo de geração de EAP:

* **Entidade:**Objeto a ser utilizado.
* **Propriedade:**A propriedade a ser utilizada para extrair quantitativos.
  + **Observação**: Caso a propriedade não seja encontrada no objeto filho, o sistema deve buscar a propriedade no objeto pai na seguinte prioridade:
    - andar (IfcBuildingStorey)
    - construção (IfcBuilding)
    - terreno (IfcSite)
    - projeto (IfcProject)
* ****Fórmula de Extração de Quantitativos:**** Ao utilizar fórmula RM, não pode ser selecionada uma propriedade, nem a opção de Unidade automática.

A fórmula deve permitir utilizar a função de buscar uma propriedade do elemento do IFC.

Exemplo de fórmula para extrair a área da porta e multiplicar por 0,5:

* **Etapa Pai (EAP Manual) :** Informar a etapa correspondente a esta entidade, quando o tipo de  for EAP Manual.
* **Filtrar propriedades do modelo:**Filtra somente as propriedades se um modelo associado ao template.
* **Unidade:** Unidade de Medida da Propriedade.
* **Formatação do Nome:** Formatação customizada pelo usuário.
* **Multiplicador:** Multiplicador para quantidade.
* **Associar ao Recurso**: Indica se deve associar um recurso específico (Composição ou Insumo) automaticamente na geração da EAP.

Observação

Ao utilizar essa funcionalidade, as regras de tarefa serão ignoradas.

* + - **Tipo de Recurso**: Indica o tipo de recurso: Composição ou Insumo.
    - **Utilizar nome do recurso**: Indica que deve utilizar o nome do recurso como nome da tarefa.

* + - A associação poderá ser feita de duas formas:
      * + **Código do Recurso Fixo**: Código da composição ou insumo que deve ser associado a tarefa.
        + **Propriedade do arquivo IFC**: Propriedade do arquivo IFC que contém o código do recurso a ser associado a tarefa.
          - * **Campo de pesquisa**: Indica qual o campo que deve ser utilizado para pesquisar o recurso: chave primária ou campo complementar.

Observação:

Ao selecionar o filtro através de um modelo, será filtrado também pelo tipo de entidade.

Veja também:
