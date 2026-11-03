---
article_id: 360026421891
category: Call Center - Dúvidas Gerais
content_hash: cda548ffe7a2875319bcdefc0fde1d1ce0420db022f5d1322056ab36aaa56f52
fetched_at: '2026-06-28T22:41:26.789384+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Tela de Status
  de discagem na agenda do operador
type: support-article
updated_at: '2021-11-30T11:37:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026421891-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Tela-de-Status-de-discagem-na-agenda-do-operador
---

**![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:2:00 min****

**Dúvida**

É possível incluir mais opções na tela de status de discagem?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025589431/mceclip0.png)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Todas as versões

**Solução**

Não é possível a inclusão via tabela, pois não se trata de uma tabela de cadastro existente em dicionário, a tela de status de discagem é um array definido direto na programação do fonte **Tmka380b** através da rotina **TK380Falha**e somente acionada na agenda do operador (**Tmka380**), caso o operador não consiga efetuar a ligação ao cliente e informe que não teve sucesso na ligação, mantendo o registro na agenda para posterior contato.

A gravação da informação de discagem fica gravada na tabela **SU8** - Histórico de Marketing:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414386236695/mceclip0.png)

Para saber a que atendimento se refere, basta pegar o código de lista da SU8 e verificá-la na **SU4**- lista de contatos, assim conseguirá validar o atendimento que teve o status de ocupado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414392093847/mceclip1.png)
