---
article_id: 360020800552
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 58592d050ae421878caad5af81fccef5541a6286b1fd7997406e1506726c680c
fetched_at: '2026-06-28T22:39:09.750142+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do campo
  F5_VAL
type: support-article
updated_at: '2025-03-12T11:43:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020800552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-campo-F5-VAL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503584461079)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Qual validação o campo F5\_VAL realiza no *Protheus*?  
  
**Ambiente**Microsiga Protheus - Estoque/Custo – A partir da versão 11.80

**Solução**

No cadastro de Tipo de Movimentação, este campo irá identificar se o processo será valorizado pelo Custo Atual do estoque quando o campo estiver com conteúdo "**NÃO**".

Ou se será informado um custo especifico para a movimentação, quando o campo estiver como "**SIM**".

Caso o campo seja configurado com conteúdo "**NÃO**", o campo Custo (D3\_CUSTO1) na tela de Movimentações Internas apresentará o HELP abaixo e o movimento não terá custo informado, somente na confirmação do tipo de Movimentação DE/RE que o campo será preenchido com o custo total do movimento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100234714)

Caso esteja configurado como conteúdo "**Sim**", o campo Custo (D3\_CUSTO1) permitirá alteração e o movimento receberá um novo custo a ser informado diretamente no movimento, se tratando de um acerto de custo.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque)

**Saiba mais:**

*[MP - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
