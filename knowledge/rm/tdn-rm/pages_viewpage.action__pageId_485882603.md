---
content_hash: 3fc8e9bbb45e6f37e3b9d874dc881940fe8eb98ca49f3b1aae2cae82ffd98e0e
fetched_at: '2026-06-29T00:10:20.152369+00:00'
page_id: '485882603'
product: rm
source: tdn-rm
title: EDUCACIONAL01-9019 DT Mala direta – Tamanho limite do endereço de remetente
  autorizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485882603
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Parâmetro Geral de Secretaria |
| Função: | Mala direta |
| Ticket: | 5636786 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [EDUCACIONAL01-9019](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-9019) |

## **02. SITUAÇÃO/REQUISITO**

No parâmetro Educacional de secretaria, apresentava mensagem de erro "String or binary data would be truncated" ao preencher o campo “Mala Direta – Endereço de e-mails de remetentes autorizados” com mais de 500 caracteres.

## **03. SOLUÇÃO**

Otimização do parâmetro Educacional de Secretaria, no campo “Mala Direta – Endereço de e-mails de remetentes autorizados”, onde o sistema irá emitir mensagem avisando ao ultrapassar o limite de caracteres permitidos para este campo (500 caracteres).
