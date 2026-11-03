---
article_id: 36572308581399
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f6d6bb78c5ee5e5f79debc0d5ea9ed11e1e1eb104226d276402db20947214d67
fetched_at: '2026-06-28T22:38:54.119083+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Movimentos Internos
  (MATA241) campo de Controle de Numeração D3_DOC incorreto após confirmar o Movimento
type: support-article
updated_at: '2026-05-28T21:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36572308581399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Movimentos-Internos-MATA241-campo-de-Controle-de-Numera%C3%A7%C3%A3o-D3-DOC-incorreto-ap%C3%B3s-confirmar-o-Movimento
---

O sistema TOTVS Protheus apresenta um problema na rotina MOVIMENTAÇÕES MÚLTIPLAS (MATA241), onde o campo Documento (D3\_DOC) não respeita o Controle de Numeração após confirmação, incrementando o número sem gravar corretamente na SD3. A solução é aplicar os pacotes indicados para as versões 12.1.2310, 12.1.2410 e 12.1.2510, testando antes em ambiente de homologação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36572280900247) Tempo aproximado para leitura: **00:03:20 min**  
  
**Ocorrência**

Na rotina MOVIMENTAÇÕES MÚLTIPLAS (MATA241) ao informar o campo **Documento (D3\_DOC)** preenchido corretamente, **após a confirmação** não respeita o Controle de Numeração digitado pelo usuário. O Controle de Numeração incrementa o número, como se estivesse sendo utilizado, mas não grava corretamente na SD3.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse incidente foi identificado na ISSUE de MANUTENÇÃO DMANMAT01-46656 conforme [esse link](https://tdn.totvs.com/x/Q62kP).  
  
**Solução**

Para solucionar essa ocorrência, aplicar o pacote do link abaixo, recomendamos primeirametne em ambiente de Homologação e testar antes de sua base de Produção:

***12.1.2310:***[***https://r.totvs.io/p/1225744***](https://r.totvs.io/p/1225744)***;***

***12.1.2410:***[***https://r.totvs.io/p/1225742***](https://r.totvs.io/p/1225742)***;***

***12.1.2510:***[***https://r.totvs.io/p/1225745***](https://r.totvs.io/p/1225745)***;***

Saiba Mais:

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
