---
content_hash: 34d4c89848e5f3374e68802bc589d6e1cac70f6f5b7d589f5ea2065ce08bde82
fetched_at: '2026-06-29T00:11:53.946447+00:00'
page_id: '852325817'
product: rm
source: tdn-rm
title: FISCAL01-23351 - Alteração no Envio de NFS-e txt com TPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852325817
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Enviar NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | FISCAL01-23351 |

## **02. SITUAÇÃO/REQUISITO**

A emissão de NFS-e através da integração com o TPF sempre irá gerar um arquivo não sendo necessário as etapas de geração e importação de arquivo txt, assim devemos alterar este processo para seguir o mesmo fluxo da NFS-e (web Service) quando estiver configurado a integração com TPF.

## **03. SOLUÇÃO**

Alteração na transição de status da NFSE ao usar o TPF para envio.

No envio a nota deixa de passar para o Status de geração de txt pendente e passa direto para pendente.

Disponível a partir da biblioteca 12.1.2310
