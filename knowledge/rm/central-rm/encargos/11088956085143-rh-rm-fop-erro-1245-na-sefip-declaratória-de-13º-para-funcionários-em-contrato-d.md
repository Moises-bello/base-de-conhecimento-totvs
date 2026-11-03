---
article_id: 11088956085143
category: Encargos
content_hash: b1ef9466bced9b8380eb4e6611bc125b7f4305c1e8b3a603f58f395fd1a5480e
fetched_at: '2026-06-28T22:46:52.123552+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Erro 1245 na Sefip declaratória de 13º para funcionários em
  contrato determinado
type: support-article
updated_at: '2025-01-16T20:38:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11088956085143-RH-RM-FOP-Erro-1245-na-Sefip-declarat%C3%B3ria-de-13%C2%BA-para-funcion%C3%A1rios-em-contrato-determinado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a correção do erro SEFIP 1245 - Base de cálculo 13º Salário da Previdência Social - referente a competência do movimento deve ser igual a remuneração 13º salário para categoria 04 sem movimentação R1, na validação do arquivo?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003119722/mceclip1.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Conforme layout, para a competência 13 não deve ser informado código de movimentação, esta é uma limitação do próprio SEFIP.  **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101998054/mceclip3.png)**

Deve ser informada a movimentação diretamente no validador da Sefip, pois dessa forma o erro não ocorre ao realizar a simulação:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11116096240663)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003161801/mceclip4.png)

**Importante**  
O sistema RM, gera o arquivo corretamente, e ao validar no Aplicativo do SEFIP o mesmo é importado. Mas o erro ocorre quando é transmitido para o SEFIP, pois o mesmo não esta preparado para entender a movimentação. Sendo assim, a solução é criar uma Nova movimentação com o código R1.
