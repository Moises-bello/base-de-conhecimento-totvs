---
article_id: 4413007316759
category: Financeiro - Compensação entre Carteiras
content_hash: f8fac3091e1125ca78e9d74b0bd61e00c0d49e1b6e0507203a5cd92b05b5a683
fetched_at: '2026-06-28T22:37:26.961688+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmento -  Backofficce Linha Protheus - FINA450 - Ao efetuar a contabilização
  do LP 594 está duplicando o registro
type: support-article
updated_at: '2026-02-09T16:57:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413007316759-Cross-Segmento-Backofficce-Linha-Protheus-FINA450-Ao-efetuar-a-contabiliza%C3%A7%C3%A3o-do-LP-594-est%C3%A1-duplicando-o-registro
---

**Dúvida**  
Ao efetuar a contabilização do LP 594 está duplicando o registro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA450 - Todas as versões  
  
**Solução**  
Para evitar a duplicidade de lançamentos, é necessário que a pergunta **“Aglut. Lançamentos?”**, no parâmetro **F12**, esteja configurada com o valor **“Não”**.

![](https://totvssuporte.zendesk.com/attachments/token/ziEovpB6t1zJTJVGsSADXII1d/?name=inline1471046923.png)

**Importante**

Por padrão, o LP 594 gera duas linhas de lançamentos contábeis, referentes aos movimentos de contas a pagar e contas a receber que foram compensados entre si.  
Para identificar a qual movimento cada linha pertence, deve-se utilizar a função **STRLCTPAD** no campo de histórico do LP (**CT5\_HIST**).

**Saiba mais**

[Cross Segmento - Backofficce Linha Protheus - FINA450 - Como contabilizar a compensação entre carteiras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37677808178967-Cross-Segmento-Backofficce-Linha-Protheus-FINA450-Como-contabilizar-a-compensa%C3%A7%C3%A3o-entre-carteiras)

[Compensação entre Carteiras](https://centraldeatendimento.totvs.com/hc/pt-br/sections/35058659965079-Financeiro-Compensa%C3%A7%C3%A3o-entre-Carteiras)
