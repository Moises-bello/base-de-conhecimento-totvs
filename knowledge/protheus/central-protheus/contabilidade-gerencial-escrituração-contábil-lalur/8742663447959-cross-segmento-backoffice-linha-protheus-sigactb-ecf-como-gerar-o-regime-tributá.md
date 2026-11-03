---
article_id: 8742663447959
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: a497d546eecac2faef21b7e39b5cc9ebc725dae2a61932614d5aa7661fb36aad
fetched_at: '2026-06-28T22:40:40.298717+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF – Como gerar o Regime
  tributário Lucro Real /Lucro Exploração?
type: support-article
updated_at: '2022-09-09T18:28:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8742663447959-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Lucro-Explora%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como gerar o Regime tributário Lucro Real /Lucro Exploração?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Criar um evento tributário 00005 (Lucro de exploração)

Exemplo:  
Aba Receita liquida conta: 3010101001 = 1000,00   
Tipo de atividade: Isenção   
Prouni: SIM  
  
Aba Dedução:  
Conta: 401010998= R$ 100,00

![](https://totvssuporte.zendesk.com/attachments/token/0BdJRBMTt5VFZLMWXW3NYER6R/?name=image.png)

2. Criar outro evento tributário com o código do tributo= 000001 (Lucro Real)  
Lançamento manual, receita operacional de 9 mil reais   
Aba Receita Operacional 2010101001= 820,00   
Aba Dedução 1010101010 = 300,00

Criar outro evento tributário com o código do tributo= 000001 (Lucro Real)  
Lançamento manual, receita operacional de 9 mil reais   
Aba Receita Operacional 2010101001= 820,00   
Aba Dedução 1010101010 = 300,00

3. Simular o evento tributário 000001 (Lucro real)

![](https://totvssuporte.zendesk.com/attachments/token/SV0GRXfRspQL8fAbQ7OuZgN1P/?name=image.png)

4.Alterar o evento tributário com o tributo 000001 (lucro real) e adicionar a aba de Dedução uma linha com a Origem Evento tributário, e relacionar o evento do Lucro de Exploração.

![](https://totvssuporte.zendesk.com/attachments/token/Tb21GIuz5tawBQsFeg1D1b9yw/?name=image.png)
