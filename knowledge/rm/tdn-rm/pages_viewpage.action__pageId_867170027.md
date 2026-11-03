---
content_hash: 6c538972524b03a4530ff963669563628291a0a7e111506b6e48df3a7e2066ae
fetched_at: '2026-06-29T00:11:56.606505+00:00'
page_id: '867170027'
product: rm
source: tdn-rm
title: FISCAL01-23852 - Alterar o Processo de Emissão da NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867170027
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Estoque, Compras e Faturamento |
| Função: | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23852 |

## **02. SITUAÇÃO/REQUISITO**

Modificar o processo de emissão da NFS-e modelo nacional para que, sempre que o regime tributário da Filial estiver configurado como "Imunidade" (tribISSQN = 2), o campo tpImunidade seja gerado no XML da nota com base no valor informado no cadastro da Filial.

## **03. SOLUÇÃO**

Foi implementado geração da tag <tpImunidade> no grupo tribMun do XML da NFS-e. A tag será gerada com base no valor informado no campo Tipo Imunidade localizado no cadastro da Filial, aba Tributos .

Disponível à partir da biblioteca 12.1.2310
