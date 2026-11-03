---
article_id: 360021777592
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 123093b9cbf745b69f7df5bbc563be0c4815a37d357d9e5bc744406e988c89cc
fetched_at: '2026-06-28T22:38:58.639452+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Validação do Campo C2_TPPR (rotina MATA650)
type: support-article
updated_at: '2021-04-28T15:45:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021777592-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-Campo-C2-TPPR-rotina-MATA650
---

**Dúvida**Quais são as validações do campo **C2\_TPPR** na rotina de Ordem de Produção (MATA650)?

**Ambiente**Microsiga Protheus – Estoque – A partir da versão 11.80

**Solução**

As validações do campo C2\_TPPR são:

OP's que foram produzidas em sua empresa I = Interna

OP's que NÃO foram produzidas em sua empresa E = Externa

OP's que NÃO é para o bloco K considerar O = Outros

![c2_tppr.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360018724291/c2_tppr.PNG)

Se utilizar uma OP com tipo E (Externa), será necessário, através da rotina **MATA037**, apontar de qual terceiro é esta Produção para antes de gerar o Bloco K.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000755601/mceclip0.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
