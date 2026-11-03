---
content_hash: 5f588baf66e59cb383be3ce91bd20eacc5458fb688059bbb2095f4c42cf95689
fetched_at: '2026-06-29T00:10:56.988433+00:00'
page_id: '593754811'
product: rm
source: tdn-rm
title: 9196175 FISCAL01-13646 - DT NFS-e - Gerar o código do cancelamento (Integração
  Neogrid)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593754811
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cancelamento de NFS-e |
| Ticket: | 9196175 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13646 |

## **02. SITUAÇÃO/REQUISITO**

Ao solicitar o cancelamento da NFS-e de Niterói (integração com Neogrid) ocorre rejeição de código do cancelamento inválido.

Atualmente o ERP não gera a tag <codmotcanc> e a Neogrid assume o valor padrão “c999”, fazendo com que o cancelamento da NFS-e seja rejeitado.

De acordo com a equipe da Neogrid será necessário o ERP enviar o código do cancelamento

## **03. SOLUÇÃO**

Foi alterado no Wizard do cancelamento da NFS-e o campo código motivo de cancelamento, se tornando um campo livre invés de ser um combo-box.

Também foi alterado para que o formulário sempre exiba se existir notas a ser canceladas em uma Filial com integração ao TOTVS Colaboração
