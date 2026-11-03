---
article_id: 360016129731
category: RH - 13º salário
content_hash: b851b0c64a99b53b1df1b3ce2ecec02f2761762a127a09874a27718cbd976cd1
fetched_at: '2026-06-28T22:44:01.632029+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não abate avos do 13º salário para funcionários
  que tiveram afastamentos
type: support-article
updated_at: '2025-08-13T11:17:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016129731-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-abate-avos-do-13%C2%BA-sal%C3%A1rio-para-funcion%C3%A1rios-que-tiveram-afastamentos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18725687608087)*****Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Sistema não abate avos do 13º salário para funcionários que tiveram afastamentos

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
1. Acesse: **Atualizações / Lançamentos / Ausências (GPEA240)**, selecione o funcionário e verifique qual tipo de ausência foi lançado para o mesmo:  
![](https://totvssuporte.zendesk.com/attachments/token/XBAlNfVb92CPYPLoIBAU0Cu5o/?name=inline-1138683576.png)

​​2. Em seguida, acesse: **Atualizações / Definições de Cálculo / Tipos de Ausência (GPEA430)** e selecione a ausência lançada para o funcionário e clique em Alterar:

![](https://totvssuporte.zendesk.com/attachments/token/bGQNWwD4gRgNXk5iaRn3evwBq/?name=inline1392435312.png)

​

3. Verifique o campo**Abat. Avos 13** (RCM\_DECIMO).  
Este campo define se será abatido ou não, avos do 13º salário de funcionários que tiveram afastamentos maiores que 15 dias em um mês.   
Para que o avo de 13º salário seja abatido, este campo deve estar configurado com Sim.

![](https://totvssuporte.zendesk.com/attachments/token/VOQJpStAypNN93RtBdlcNhgct/?name=inline-514226209.png)

4. Após realizar a alteração no tipo de ausência acesse: **Miscelânea / Cálculos / Por Roteiro (GPEM020)**, e reprocesse os cálculos de 13º salário para este funcionário.

**Saiba Mais**[RH - Linha Protheus - GPE - Cálculo de 13º Salario considerando avos a mais quando tem afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057495954-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-13%C2%BA-Salario-considerando-avos-a-mais-quando-tem-afastamento)  
[RH - Linha Protheus - GPE - Base FGTS 13º para funcionário afastado por Serviço Militar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052557233-RH-Linha-Protheus-GPE-Base-FGTS-13%C2%BA-para-funcion%C3%A1rio-afastado-por-Servi%C3%A7o-Militar)
