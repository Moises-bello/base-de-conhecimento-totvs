---
article_id: 360004020232
category: esocial - Periódicos
content_hash: c034dceedd0b64d2a01b451cedc7e4a8d42b15b0e9de986c1fd37b53829d8765
fetched_at: '2026-06-28T22:47:09.526384+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RM - eSocial - Diferença entre o evento S-1200 e o evento S-1210
type: support-article
updated_at: '2025-12-23T13:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004020232-RM-eSocial-Diferen%C3%A7a-entre-o-evento-S-1200-e-o-evento-S-1210
---

**Dúvida**  
Qual a diferença entre o evento S-1200 e o evento S-1210?

**Ambiente**  
RM – eSocial – Todas as versões

**Solução**  
Tanto os eventos S-1200 quanto S-1210 tem suas informações montadas a partir dos valores lançados no envelope de pagamento (ficha financeira/PFFINANC).

S-1200- Leva em consideração competência

* Proventos;
* Descontos (incluindo o desconto de INSS);
* Base de cálculo.

Leva em consideração a data em que o eventos foi lançado.

S-1210- Regime de caixa

* Valor efetivamente pago ao funcionário (Líquido);
* Desconto de IRRF;
* Valores relativos a Pensão Alimentícia;
* PLR;
* Plano de Saúde

Leva em consideração o caixa em que o pagamento foi feito.  
Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360005010971)

Lavando em consideração o envelope acima, entendendo que a competência é 5 e o caixa é 6:

Eventos no S-1200:

* 0002
* 0009
* 0003
* 0032
* 0203
* 0221

Como o 0004 é o IR, o mesmo só entrará na geração do S-1210 no mês de pagamento, ou seja, no mês 6.

* **Importante:**  
  1-As verbas rescisórias são lançadas no S-2299.  
  2-Os valores referente a IRRF de verbas rescisórias são lançados no S-1210.  
  3-Os valores referentes as férias são (afastamento temporário S-2230) são retornados do recibo de férias.
