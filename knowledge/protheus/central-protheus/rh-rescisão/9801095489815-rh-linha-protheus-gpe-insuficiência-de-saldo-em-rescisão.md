---
article_id: 9801095489815
category: RH - Rescisão
content_hash: 3791852dc62235d639167470c70e22d2f187572e966d176dbcf8b1175af618e8
fetched_at: '2026-06-28T22:43:48.389857+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Insuficiência de saldo em rescisão
type: support-article
updated_at: '2025-09-11T01:00:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9801095489815-RH-Linha-Protheus-GPE-Insufici%C3%AAncia-de-saldo-em-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34844262321431) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**É possível criar verba separada de insuficiência de saldo em rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.  
  
**Solução**Não é possível criar verba separada de insuficiência de saldo em rescisão, pois pelo padrão o sistema possui os ids 0045 e 0046 para insuficiência de saldo nos cálculos de folha de pagamento e rescisão.

**Exemplo:**

**Cadastro Id 0045**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10059463500439)

**Rescisão**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10059479429143)

A rescisão ficou negativa no valor de 374,27 deste modo o sistema gera este valor no Id 0045 (verba provento) para zerar o cálculo e assim a rescisão não ficar negativa.

**Saiba mais**

[RH - Linha Protheus - GPE - Como gerar o desconto de insuficiência de saldo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034006853-MP-GPE-Como-gerar-o-desconto-de-insufici%C3%AAncia-de-saldo?source=search)
