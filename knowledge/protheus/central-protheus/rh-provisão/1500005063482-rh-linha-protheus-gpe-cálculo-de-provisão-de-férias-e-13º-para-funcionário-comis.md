---
article_id: 1500005063482
category: RH - Provisão
content_hash: 26c0bf1adadf911a3a8885c4523b7e2e7952ada17db06b36fffafb358032888f
fetched_at: '2026-06-28T22:43:55.681745+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de provisão de férias e 13º para funcionário
  comissionado
type: support-article
updated_at: '2025-06-18T18:17:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005063482-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-para-funcion%C3%A1rio-comissionado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903205088791)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Cálculo de provisão de férias e 13º para funcionário comissionado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**Por padrão do sistema os valores referente a comissão serão apresentados na coluna adicionais.

Esses valores serão apresentados de formas diferentes de acordo com a definição do parâmetro **P\_MEDDIREN ([Utilização do Mnemônico P\_MEDDIREN (Antigo MV\_MEDDIRE)](https://tdn.totvs.com/pages/viewpage.action?pageId=224112471))**

Cadastro do funcionário com a categoria C e sem salário cadastrado;  
  
![](https://totvssuporte.zendesk.com/attachments/token/rfT2ouqPJUe6QkFAVrNx9zqsY/?name=inline1062387660.png)  
  
Cadastro da verba de comissão com **Id 0165**;  
  
![](https://totvssuporte.zendesk.com/attachments/token/tXcfVmsNyMO8apBk2cmOxBPpD/?name=inline2124893160.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/Z8fOCkxNMeZQjmkv1eDbwhv69/?name=inline-1485580348.png)  
  
Calculo da folha:  
  
![](https://totvssuporte.zendesk.com/attachments/token/oQBvgX0sNoWhYeJY8OVzVVjZu/?name=inline1422576426.png)  
  
Cálculo da provisão:  
  
![](https://totvssuporte.zendesk.com/attachments/token/FR5V8wZTpYhkV22nyQY2zCFU5/?name=inline2140092186.png)  
  
Se o parâmetro **P\_MEDDIREN** estiver definido com **"N"**, verifique que dessa forma o valor das **médias** são **divididos** por **12**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15777383011351)  
  
Demonstrativo de médias:  
  
![](https://totvssuporte.zendesk.com/attachments/token/XmrYqm8VBupdYm1ew9feafILg/?name=inline-937426851.png)​  
  
Relatório de provisão:  
  
![](https://totvssuporte.zendesk.com/attachments/token/KR1V73aU4w3z7yzJGIdC75dew/?name=inline-293792647.png)

Se o parâmetro **P\_MEDDIREN** estiver definido com **"S"**, verifique que dessa forma o valor das médias é apresentado integral

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15777409570199)

Demonstrativo de médias:  
  
![](https://totvssuporte.zendesk.com/attachments/token/unNdZtIx9aYUfSywiJDkYpweh/?name=inline2018383043.png)  
  
Cálculo da provisão e relatório:  
  
![](https://totvssuporte.zendesk.com/attachments/token/GaKklPbP7wLuGtqxWnyMsNDJO/?name=inline448921835.png)​  
  
Verifique que o valor da comissão é apresentado na coluna adicionais apenas:  
  
![](https://totvssuporte.zendesk.com/attachments/token/ah5EDjzK1mLrrha8pHYr3AFv1/?name=inline1677710110.png)

**Saiba Mais:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028833931-MP-GPE-C%C3%A1lculo-de-Folha-para-comissionado-puro?source=search>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659773-MP-GPE-Adicionais-de-Provis%C3%A3o-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio?source=search>
