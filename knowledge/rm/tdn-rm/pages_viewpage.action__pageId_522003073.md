---
content_hash: 9114710d3540e6b378d127cbbb966eac999f9de06511cdc9a155c21cc7fc52fe
fetched_at: '2026-06-29T00:10:31.747358+00:00'
page_id: '522003073'
product: rm
source: tdn-rm
title: EDUCACIONAL01-12054 DT Geração de Usuário - Responsável Acadêmico e Responsável
  Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522003073
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Geração de Usuário |
| Ticket: | #7505691 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-12054 |

## **02. SITUAÇÃO/REQUISITO**

Processo de geração de usuário para responsáveis do aluno não gerava as permissões definidas para o responsável financeiro para o usuário gerado quando o responsável acadêmico era o mesmo que o financeiro. O usuário era gerado apenas com as permissões do responsável acadêmico.

## **03. SOLUÇÃO**

Alteração do processo de geração de usuário para geração correta dos perfis do usuário quando o responsável acadêmico é a mesma pessoa relacionada ao cliente/fornecedor do responsável financeiro. O usuário gerado irá conter os perfis definidos tanto para o responsável acadêmico quanto os definidos para o responsável financeiro.
