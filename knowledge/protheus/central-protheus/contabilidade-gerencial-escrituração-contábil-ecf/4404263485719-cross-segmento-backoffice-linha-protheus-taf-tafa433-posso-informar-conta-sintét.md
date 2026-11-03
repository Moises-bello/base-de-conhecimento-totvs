---
article_id: 4404263485719
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 1b383dba930488cf99fc67f41c29a15a03bda035d51010613306670133fce397
fetched_at: '2026-06-28T22:40:48.952098+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF- TAFA433 - Posso informar
  conta sintética no evento tributário
type: support-article
updated_at: '2022-09-06T18:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404263485719-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Posso-informar-conta-sint%C3%A9tica-no-evento-tribut%C3%A1rio
---

**Dúvida**TAFA444 Atenção: Não foi possível encontrar os saldos contábeis no cadastro do bloco K da conta 3. Por isso o registro filho do M300 não foram gerados.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TAF - Todas as versões  
  
**Solução**

No cadastro de evento tributário (TAFA433) a composição da base de calculo do IRPJ e CSLL é feito através de conta contábil, lançamento manual e/ou parte B.

Para fins de apuração e simulação a conta sintética é considerada corretamente, porém após a apuração ao **exportar os dados para ECF (TAFA444)** a conta sintética não é validada devido ao cruzamento de saldos com o bloco K. Sendo assim, o correto é NÃO informar contas sintéticas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404288493847/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404280961047/mceclip1.png)

Não foi possível encontrar os saldos contábeis no cadastro do Bloco K da conta 3 , por isso os registros filhos do M300 não foram gerados

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404288549783/mceclip2.png)

Manual ECF:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404277555223/mceclip0.png)

**Saiba mais:**

Cadastro Evento tributário: [Evento Tributário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404225269527-Cross-Segmento-Backoffice-Linha-Protheus-TAF-TAFA433-Cadastro-do-Evento-tributario-BLOCO-M-e-BLOCO-N)
