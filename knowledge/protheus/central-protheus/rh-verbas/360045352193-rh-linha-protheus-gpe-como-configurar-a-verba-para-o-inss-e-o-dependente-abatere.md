---
article_id: 360045352193
category: 'RH - Verbas '
content_hash: 9df1822063043d95bf0aaa30a53832fac0258f700eb2773c029b01447f1e42b0
fetched_at: '2026-06-28T22:43:19.937515+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar a verba para o INSS e o Dependente
  abaterem da composição da base de IR
type: support-article
updated_at: '2025-09-12T17:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045352193-RH-Linha-Protheus-GPE-Como-configurar-a-verba-para-o-INSS-e-o-Dependente-abaterem-da-composi%C3%A7%C3%A3o-da-base-de-IR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26301004535831) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como configurar a verba para o INSS e o Dependente abaterem da composição da base de IR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Para que o valor do INSS seja abatido da base de IR, ou a verba de ID 0064 ou a verba de ID 0167 devem ficar com SIM no campo IR na aba Incidências no cadastro da verba, para isso, entre na rotina **Verbas** pelo caminho **>Atualizações >Definições cálculos >Verbas**;  
  
2. Deixe o campo IR com SIM para somente uma as verbas (ou ID 0064 ou ID 0167)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062594373)  
  
3. Altere a incidência para IR da verba de ID 0059 para SIM

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061684394)![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062593913)  
  
**IMPORTANTE:** Somente um dos IDs 0064 ou 0167 devem ter incidência de IR, pois se deixar as duas verbas, a dedução de INSS na base de IR será dobrada.

**Saiba Mais**[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)  
[RH - Linha Protheus - GPE - Como configurar verbas de férias mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941171-RH-Linha-Protheus-GPE-Como-configurar-verbas-de-f%C3%A9rias-m%C3%AAs-seguinte)  
[RH - Linha Protheus - GPE - Valor da verba Base de IR de férias com Id de cálculo 0016 apresenta valores diferentes para funcionários que possuem desconto de IR dos que não tem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15309469010199-RH-Linha-Protheus-GPE-Valor-da-verba-Base-de-IR-de-f%C3%A9rias-com-Id-de-c%C3%A1lculo-0016-apresenta-valores-diferentes-para-funcion%C3%A1rios-que-possuem-desconto-de-IR-dos-que-n%C3%A3o-tem)
