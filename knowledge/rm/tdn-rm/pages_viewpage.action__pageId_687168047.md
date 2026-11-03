---
content_hash: 2f7ba9c1711641a1c6c36d47c0ece1d26cd12f111ae13ae4cf168c6564023dce
fetched_at: '2026-06-29T00:11:20.664667+00:00'
page_id: '687168047'
product: rm
source: tdn-rm
title: FISCAL01-18061 - DT NFS-e Joinville - Geração da tag <CodigoPais>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687168047
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18054 |

## **02. SITUAÇÃO/REQUISITO**

          Conforme análise, o cliente está realizando a emissão da NFS-e para o município de Joinville/SC porém a Prefeitura está rejeitando o documento com a seguinte mensagem: <strong>Código({0}) IBGE do país não localizado. | Informe um país válido.</strong>

## **03. SOLUÇÃO**

         Inserir tag <codpais> dentro da tag <prestacao> quando o município que emite a NFS-e for Joinville.

Disponível a partir da biblioteca 12.1.34
