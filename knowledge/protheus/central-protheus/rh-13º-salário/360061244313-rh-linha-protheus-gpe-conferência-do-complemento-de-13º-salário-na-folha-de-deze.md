---
article_id: 360061244313
category: RH - 13º salário
content_hash: 0b89dec721b33fe281c5e0b2a36ea3f0f1421e8493f640945451268a6c828683
fetched_at: '2026-06-28T22:44:00.746375+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Conferência do Complemento de 13º Salário na Folha
  de Dezembro
type: support-article
updated_at: '2025-08-13T14:02:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061244313-RH-Linha-Protheus-GPE-Confer%C3%AAncia-do-Complemento-de-13%C2%BA-Sal%C3%A1rio-na-Folha-de-Dezembro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19055975006871) Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como conferir o valor de Diferença de 13º Salário gerado no cálculo da Folha de Dezembro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Basicamente, o cálculo é a diferença entre o Total de Médias gerado no Relatório de Médias Antes do Cálculo da Folha e o Total de Médias gerado no Relatório de Médias após o Cálculo da Folha.   
  
O ponto de Configuração que influencia na Conferência e resultado do cálculo, são as perguntas **Data de Referência** e **Considera Mês Atual** do **Cálculo e do Relatório**, ambas devem ser iguais.  
Abaixo exemplo passo a passo desde o cálculo do 13º até o Cálculo da Folha. Observe que no primeiro Cálculo, no cálculo do 13º, foi usada Referência 31/12/2020 e Considera mês Atual = Não tanto no cálculo quanto no Relatório de MédiasDepois, no cálculo da Folha, usada data de Referência 31/12/2020 e Considera Mês Atual - Sim no cálculo, e Referência 31/12/2020 e Considera Mês Atual - Mensal no Relatório de Médias.

Parâmetros de Cálculo do 13º Segunda Parcela  
  
![](https://totvssuporte.zendesk.com/attachments/token/lAeu67hYUDF3ri6viWq5Ih4sz/?name=inline647938648.png)​

Cálculo do 13º Mês 12/2020

![](https://totvssuporte.zendesk.com/attachments/token/aNiaKbJtksMhmLEnUslNyO3Qb/?name=inline1967437036.png)​

**Média Valor - 20,00****Média Horas - 141,67****Total de Média Pago - 161,67**

Relatório de Médias Emitido antes do Cálculo da Folha, **com referência 31/12/2020 e Mês Atual = Não**

![](https://totvssuporte.zendesk.com/attachments/token/cBf2rHBkNfnl9RP8ddqGFg8h3/?name=inline519704398.png)​

![](https://totvssuporte.zendesk.com/attachments/token/lwXvpOVxZBERlk20jMHukVc1z/?name=inline1459377119.png)​

![](https://totvssuporte.zendesk.com/attachments/token/Vrq3AK85VCDVawFdPusi4HmAI/?name=inline-671792338.png)​

![](https://totvssuporte.zendesk.com/attachments/token/FQyPJVcfjPGAjlskLCCorvBmk/?name=inline770094954.png)​

**Total de Média Gerado - 161,67 - Confere com o Cálculo Efetuado no roteiro 132, somando as Médias Valor e Médias Horas**

Fechamento do roteiro 132

![](https://totvssuporte.zendesk.com/attachments/token/ZUxnAnA8zi3HTvfdl6Z0iL2Mt/?name=inline1351733680.png)​

![](https://totvssuporte.zendesk.com/attachments/token/Bzv5UjZxl9ksLmQgtld6T2xZ5/?name=inline1807027714.png)​

Feito Lançamento de Horas Extras no mês 12/2020 roteiro FOL, que incide média de 13º.

![](https://totvssuporte.zendesk.com/attachments/token/zVMMNTmCI54GCsXhOj0jML149/?name=inline1683034453.png)​

Feito o Cálculo da Folha do mês 12/2020 agora com considera mês atual - Sim

![](https://totvssuporte.zendesk.com/attachments/token/QGpDEiAGw4altvdNr7N11R4rS/?name=inline-1673912890.png)​

Cálculo Efetuado - Folha 12/2020.

Diferença de 13º Gerada - **38,27**

![](https://totvssuporte.zendesk.com/attachments/token/pPPxviHVmMPZfuWUXTSN7eOyu/?name=inline-1848661380.png)​

Relatório de Médias Emitido após o Cálculo da Folha, com referência 31/12/2020 e Mês Atual = Sim

![](https://totvssuporte.zendesk.com/attachments/token/0meauH6Z4phKGeFfI1qo0HN2V/?name=inline-2054247369.png)​

![](https://totvssuporte.zendesk.com/attachments/token/oPpjMTlmO5FHRTXZZTgC3sqL0/?name=inline691298212.png)​

![](https://totvssuporte.zendesk.com/attachments/token/ZuY5m6S0I6NuTpXXjEDLK5108/?name=inline-292362162.png)​

![](https://totvssuporte.zendesk.com/attachments/token/hjxfgGDV83qkLeJexY0uUDkzF/?name=inline360945440.png)​

**Dica:** O Relatório de Médias também pode ser emitido pela rotina de Consulta de Cálculo por Funcionário, Selecionando a opção Outras Ações > Médias.  
![](https://lh7-us.googleusercontent.com/UTlkodB6TYqln3uZrQqQW7vQOsmUFd3MRpB66cUGCgQV-dJga9e4-Oh1wzHxRBjKUZFehwAczPuHmKhh_qd51OlKuyXRg-sz00mTJylcB_qVYg9NcCcah0klGCzBzDiUReOM7gCievNCqT3ocGsLR6RWoQ=s2048)

**Total de Média Gerado - 199,94**

**Conferência:**Considere a Média do Relatório Antes do Cálculo - **161,67**

Considere a Média do Relatório Após o Cálculo - **199,94**

Diferença - **38,27**

**Valor Gerado na Folha - 38,27**

**Saiba Mais**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
