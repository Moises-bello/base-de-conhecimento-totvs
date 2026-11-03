---
content_hash: 1235de5636afc445d87f94f740614168e05bac25faa7bf7908e1a20c669a4955
fetched_at: '2026-06-29T00:11:26.632833+00:00'
page_id: '718435339'
product: rm
source: tdn-rm
title: 'FISCAL01-18817 - Ticket #15389219 - DT - Ajuste geração das tags Discrdedu,
  dJustificaDeducao, grupo Deduções e Base de Cálculo, para o Totvs Colaboração'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=718435339
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Nota Fiscal Eletrônica (Nfs-e) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18859 |

## **02. SITUAÇÃO/REQUISITO**

O cliente Telemont esta gerando NFS-e para o município de Varginha através da integração com o TOTVS Colaboração 2.0 e para este município existe a necessidade de gerar a discriminação referente ao valor da dedução.

Hoje esta discriminação é gerada para o TSS através do campo Discrdedu, porém para a Neogrid esta mesma informação deve ser gerada no campo dJustificaDeducao dentro do grupo valores logo abaixo do campo Pis.

## **03. SOLUÇÃO**

Realizadas as seguintes alterações:

* Retirada a geração do campo DISCRDEDU para a geração da NFS-e com o TOTVS Colaboração, geração mantida para o TSS.

* Implementada a geração da discriminação da dedução no campo RPS/VALORES/djustificadeducao apenas para o TOTVS Colaboração.

* Grupo de deduções do Totvs Colaboração passa a considerar também as deduções de materiais, mesmo comportamento do TSS.

* Alteração para Geração da Base de cálculo do grupo valores que passar a ser igual a base de cálculo do grupo Serviços quando se tratar de Totvs Colaboração.

Disponível a partir da biblioteca 12.1.2205
