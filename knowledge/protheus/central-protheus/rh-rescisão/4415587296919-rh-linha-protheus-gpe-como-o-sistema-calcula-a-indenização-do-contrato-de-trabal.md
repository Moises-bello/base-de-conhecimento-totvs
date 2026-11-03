---
article_id: 4415587296919
category: RH - Rescisão
content_hash: 40e1f475a326095e86a9367fa1cbb838861c487414fb333128601dead16ef833
fetched_at: '2026-06-28T22:43:52.100122+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema calcula a Indenização do Contrato
  de Trabalho por prazo Determinado, lei 6.019/74
type: support-article
updated_at: '2025-04-16T18:34:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415587296919-RH-Linha-Protheus-GPE-Como-o-sistema-calcula-a-Indeniza%C3%A7%C3%A3o-do-Contrato-de-Trabalho-por-prazo-Determinado-lei-6-019-74
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26601611496343)***Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como o sistema calcula o indenização do contrato de trabalho por prazo determinado dos funcionários que se enquadram na lei 6.019/74?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Conforme Lei n° 6.019 de 03 de janeiro de 1974, artigo 12 alínea f, é devido uma indenização sobre rescisão de trabalhador temporário:

"*Art. 12 - Ficam assegurados ao trabalhador temporário os seguintes direitos:*  
*(...)*  
*f) indenização por dispensa sem justa causa ou término normal do contrato, correspondente a 1/12 (um doze avos) do pagamento recebido;*"

A verba será apurada de acordo com o líquido da rescisão (ID 0126), sendo gerado o valor correspondente a 1/12 avos, mas após a geração da indenização, o líquido será recalculado para considerar o valor da indenização.

A indenização será paga na verba de **ID 1880.**

**Composição do cálculo:**

Liquido da rescisão (ID 0126) 8.982,48 - Indenização (ID 1880) 690,96 = 8.291,52

Liquido Rescisão sem a indenização 8.291,52 / 12 = 690,96 Valor do Indenização do Contrato de Trabalho calculada na verba de ID 1880.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415572920599)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415572935447)

**Saiba Mais:**

**[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)**
