---
article_id: 5405666610967
category: Faturamento - Cenários de Venda
content_hash: 07cec6c13b2996bea01e462802b3a5b5869ba07b872e041a948fe69da1b07348
fetched_at: '2026-06-28T22:38:33.916705+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS BackOffice (Linha Protheus) - Faturamento (SIGAFAT)
  -  Configuração Nova Liberação MATA455
type: support-article
updated_at: '2022-04-12T18:30:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5405666610967-Cross-Segmento-TOTVS-BackOffice-Linha-Protheus-Faturamento-SIGAFAT-Configura%C3%A7%C3%A3o-Nova-Libera%C3%A7%C3%A3o-MATA455
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como podemos bloquear ás **três opções** de Liberação na tela de “**Nova Liberação**”:

**Ambiente**Cross Segmentos-TOTVS BackOffice (Linha Protheus)-Faturamento (SIGAFAT)-todas as versões.  
  
**Solução**

Existem **três opções** de Liberação na tela de “**Nova Liberação**”:

![](https://tdn.totvs.com/download/attachments/274312270/001.PNG?version=1&modificationDate=1594527658890&api=v2)

O parâmetro **MV\_OPLBEST** permite a definição da opção padrão de liberação, em que:  
**0** - permite que usuário **selecione** o tipo de liberação.  
**1** - traz marcada, como padrão, a opção **Libera reavaliando crédito e estoque**, não permitindo que o usuário selecione outra opção.  
**2** - traz marcada, como padrão, a opção **Libera reavaliando somente estoque**, não permitindo que o usuário selecione outra opção.  
**3** - traz marcada, como padrão, a opção **Libera sempre**, não permitindo que o usuário selecione outra opção.

Saiba mais: [Funcionamento da função "Nova Liberação" na rotina Liberação de Estoque (MATA455)](https://tdn.totvs.com/x/TqxZE)
