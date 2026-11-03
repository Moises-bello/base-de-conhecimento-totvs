---
article_id: 4402644388119
category: SIGAEST - PODER DE TERCEIROS
content_hash: a361867e95b461b233b7d08d89df7a031daad1f5c46ec897e9d000bffda9f26b
fetched_at: '2026-06-28T22:39:03.268407+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do parâmetro
  MV_LIBESB6
type: support-article
updated_at: '2021-06-14T12:00:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402644388119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-LIBESB6
---

**Dúvida**Qual a utilidade do parâmetro MV\_LIBESB6 no controle e baixa de Poder de Terceiros?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Este parâmetro tem por objetivo permitir a baixa de Poder de Terceiros via Documento de Entrada quando o valor financeiro da devolução **não atinge** o valor da remessa (e normalmente gera o Help: A103SLDPD3.

Para isso foi disponibilizado o parâmetro **MV\_LIBESB6** na rotina Documento de Entrada (MATA103) que permite incluir uma nota com as seguintes características:

* TES configurado com os campos abaixo:

Campo "Atu. Estoque" (F4\_ESTOQUE) com conteúdo igual a ‘S’;  
Campo: "Poder Terc." (F4\_PODER3) com conteúdo igual a ‘D’.

* O valor informado no campo Quantidade (D1\_QUANT) deve zerar o saldo total em quantidade do controle de poder de terceiros, ou seja, a inclusão desse item encerra o controle de poder de terceiros;
* O valor informado no campo Vlr.Total (D1\_TOTAL) **não zera** o saldo total em valor do controle de poder de terceiros;

Dentro deste cenário acima, considere deixar o parâmetro **MV\_LIBESB6 = .T. e MV\_BLOQSB6 = .F.** para conseguir concluir a baixa do Poder de Terceiros.

**Saiba mais:**

*[MP - SIGAEST - MATA103 - HELP A103SLDPD3 ao fazer retorno (devolução) de Remessa em Poder de Terceiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004786181)*

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
