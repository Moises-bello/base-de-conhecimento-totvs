---
article_id: 360021560132
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b97b31314c50f8be7bcd12ddd1a28d732f7373402d9bdbb9e85f81d606b1fd03
fetched_at: '2026-06-28T22:38:55.383003+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como não preencher
  o campo D3_CC mesmo com B1_CC preenchido?
type: support-article
updated_at: '2025-03-12T12:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021560132-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-n%C3%A3o-preencher-o-campo-D3-CC-mesmo-com-B1-CC-preenchido
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807517515543)*** Tempo aproximado para leitura: **00:05:00 min****Dúvida**  
Como não gatilhar no campo D3\_CC nas movimentações internas mesmo com B1\_CC preenchido?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A forma de não **gatilhar** o **centro de custo** que esta no campo **B1\_CC** do cadastro do produto no campo **D3\_CC** da rotina de **movimentações internas** é **criar** um **gatilho**.  
  
O gatilho deverá gatilhar em branco o campo **D3\_CC**.

Servirá para que mesmo que o campo B1\_CC não esteja em branco, o sistema não considere essa informação devido a regra do gatilho.

**Exemplo:**

**if(xFilial("SD3")="01".AND.Alltrim(funName())$"MATA240/MATA241","",SB1->B1\_CONTA)**

**Atenção:** Isso é apenas um exemplo, a regra e tratamento efetivo, deve-se avaliar pontualmente com o seu analista Desenvolvedor.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

[*MP - SIGAEST - Reavaliação do Custo Médio MATA338*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015649031-MP-SIGAEST-Reavalia%C3%A7%C3%A3o-do-Custo-M%C3%A9dio-MATA338)
