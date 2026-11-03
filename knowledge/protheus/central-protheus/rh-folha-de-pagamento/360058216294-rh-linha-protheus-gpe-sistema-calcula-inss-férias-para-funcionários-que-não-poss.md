---
article_id: 360058216294
category: RH - Folha de Pagamento
content_hash: 70371d068f5bd07b742fecaf0e22b1b0840eb07cf6d9dd132e6b8eff3742c9a1
fetched_at: '2026-06-28T22:44:16.353876+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema calcula INSS Férias para funcionários que
  não possuem cálculo de férias na folha de pagamento
type: support-article
updated_at: '2025-06-13T19:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058216294-RH-Linha-Protheus-GPE-Sistema-calcula-INSS-F%C3%A9rias-para-funcion%C3%A1rios-que-n%C3%A3o-possuem-c%C3%A1lculo-de-f%C3%A9rias-na-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19221151886231)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Sistema calcula INSS Férias para funcionários que não possuem cálculo de férias na folha de pagamento e não estão de férias.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 11.80.  
  
**Solução**O sistema efetua o cálculo do INSS de férias quando alguma verba que foi calculada para o funcionário está configurada como **Refere-se a Férias = SIM**.  
Verificar o cadastro de verba, aba funcionais, campo **Ref. a Ferias (RV\_REFFER)**, alterar para **"NÃO"** e calcular a folha do funcionário novamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100857493)

**Após novo cálculo folha de pagamento, todo valor de INSS desconto funcionário é calculado na verba de INSS ID 0064.**

**ID 0064.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221189750167)**

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-DINSSFM?source=search)
