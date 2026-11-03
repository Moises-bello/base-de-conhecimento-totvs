---
content_hash: 8e566337057c701bd8098bb47bcfa2379ea344a0dd040f764a08c1cd2f21ce3b
fetched_at: '2026-06-29T00:12:16.197661+00:00'
page_id: '982918520'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Nome Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982918520
version: 7
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Nome Social |
| País: | Brasil |
| Story: | [DRHROTRM-14896](http://DRHROTRM-14896) |

## **02.** **RELEASES**

* 12.1.2410.295
* 12.1.2502.198
* 12.1.2506.140 e superiores

## **03. SITUAÇÃO/REQUISITO**

Implementar o envio do nome social existente no cadastro do colaborador para o Ponto Web.

## **04. SOLUÇÃO**

Foi implementada a tratativa para envio do nome social existente no cadastro do colaborador para o Ponto Web (Ahgora).

Para colaboradores que possuem **Nome Social**, o json será gerado conforme o detalhamento abaixo:

* "nome": "NOME SOCIAL",
* "checkbox\_nome\_social": true,
* "nome\_registro": "NOME"

**🔄 Exemplo:**

Cadastro do Colaborador.

Json gerado na integração.

Registro do colaborador no Ponto Web.

## **05****. DOCUMENTAÇÃO**
