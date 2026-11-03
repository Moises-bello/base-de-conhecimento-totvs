---
article_id: 4406265299479
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7e7fb105ec1b7eb1ad8e897e83b5e6e5580f6dea3785ec01a74abf3e19eca7be
fetched_at: '2026-06-28T22:38:38.518604+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Finalidade com
  campo C5_CLIREM
type: support-article
updated_at: '2021-08-18T14:36:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406265299479-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Finalidade-com-campo-C5-CLIREM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Finalidade do campo **C5\_CLIREM**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Versão 12

**Solução**

Conforme a documentação fiscal, **[5715507 DSERFIS1-13059 DT Conversão de CFOP para tratamento de TAGS de entrega no XML e DANFE](https://tdn.totvs.com/x/Pkn6Hg)**, o campo **C5\_CLIREM**foi criado para uso no tratamento de conversão de CFOP para as tasg de entrega  do xml e do Danfe, a ideia é realizar operação fiscal triangular, onde os endereços de faturamento e entrega sejam diferentes e caso estes sejam situados em Estados distintos, que o sistema aceite o CFOP de operação interestadual sem alterar automaticamente para CFOP de operação interna.

Com isso, se o campo em questão estiver preenchido com o código de cliente para remessa , o mesmo será considerado no preenchimento das informações do Local de Entrega no DANFE e nas *tags* de entrega no XML.

**Saiba Mais:**

**[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as TAGS entrega e retirada no XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-entrega-e-retirada-no-XML-)**
