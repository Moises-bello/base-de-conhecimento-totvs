---
content_hash: 74d5b833be25ca7cb58a26328c382a393a7baaad8079832116bb74fefd47cded
fetched_at: '2026-06-29T00:12:09.208989+00:00'
page_id: '943108738'
product: rm
source: tdn-rm
title: 'FISCAL01-25752 RM - NFS-e: Nenhuma NFS-e foi consultada. Erro: Referência
  de objeto não definida para uma instância de um objeto'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=943108738
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Estoque |
| Função: | NFS-e -  Consultar Autorização/Cancelamento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25752 |

## **02. SITUAÇÃO/REQUISITO**

Ao consultar a autorização da NFS-e para o município de Barueri/SP, consultando 50 notas simultaneamente, a seguinte mensagem de erro é apresentada:  
*“Nenhuma NFS-e foi consultada. Erro: Referência de objeto não definida para uma instância de um objeto.”*

## **03. SOLUÇÃO**

O erro era causado pela forma como o serviço de monitor de notas do TSS estava sendo chamado. O serviço recebe uma lista de notas a serem consultadas, cada nota deve mapear para um movimento no RM. O serviço estava sendo chamado com a lista de notas e com um range de ids, este range compreendia o primeiro e último ids da lista de notas, no entanto, como a lista de ids pode ter descontinuidades isso fazia com que o TSS consultasse notas que não estavam na lista e, portanto, não estavam também no RM, gerando o erro quando o retorno era mapeado para um movimento existente no sistema.

Foi corrigida a chamada do serviço para não mais passar os ids iniciais e finais. Somente a lista de ids é passada.

Disponível a partir da biblioteca 12.1.2406
