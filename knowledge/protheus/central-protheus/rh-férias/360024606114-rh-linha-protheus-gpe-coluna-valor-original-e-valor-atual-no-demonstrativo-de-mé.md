---
article_id: 360024606114
category: RH - Férias
content_hash: 0e747af840e4fc67934050fc4b6ed82c3f676189aa0bbccefe225e0bbc922ba8
fetched_at: '2026-06-28T22:43:58.012258+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual no Demonstrativo
  de Médias
type: support-article
updated_at: '2025-06-03T14:07:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024606114-RH-Linha-Protheus-GPE-Coluna-Valor-Original-e-Valor-Atual-no-Demonstrativo-de-M%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32552578286743) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como é feito no Demonstrativo de Médias as Colunas de Valor Original e Valor Atual?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
As colunas são montadas considerando a seguinte fórmula:

**Valor Original** - Valor que foi pago na época.   
Por exemplo, em 07/2024 o funcionário possuía a remuneração de R$4.000,00, onde foram pagas um total de 11 horas extras a 55%.   
Salário: 4.000,00  
Salário hora: 18,18  
11 horas extras a 55%: **310,00** (18,18 \* 11 + 55%)

**Valor Atual** - Recálculo da verba com base na remuneração atual.   
Em 05/2025 o funcionário obteve um reajuste salarial, onde sua remuneração passou a ser de R$4.500,00. Então a verba de horas extras será recalculada com base no salário atual.   
Salário: 4.500,00  
Salário hora: 20,45  
11 horas extras a 55%: **348,75** (20,45 \* 11 + 55%)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32552578291095)

**Observação:** Quando a remuneração atual do funcionário for menor — por exemplo, se ele deixou de receber um adicional que recebia anteriormente — o sistema pode recalcular a verba e reduzir seu valor. Para esse cenário, existe o mnemônico P\_MEDORIG (parâmetro MV\_MEDORIG), que permite manter o valor original caso o valor recalculado seja inferior ao valor original. Saiba mais [aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012665411-RH-Linha-Protheus-GPE-Como-Configurar-as-M%C3%A9dias-para-que-o-valor-Atual-n%C3%A3o-seja-menor-do-que-o-Valor-Original)

**Saiba Mais**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias)  
[RH - Linha Protheus - GPE - Parâmetros e Mnemônicos utilizados para o cálculo de Média](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7011337477015-RH-Linha-Protheus-GPE-Par%C3%A2metros-e-Mnem%C3%B4nicos-utilizados-para-o-c%C3%A1lculo-de-M%C3%A9dia)  
[RH - Linha Protheus - GPE - Como demonstrar o salário Incorporado no Relatório de Médias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008859921-RH-Linha-Protheus-GPE-Como-demonstrar-o-sal%C3%A1rio-Incorporado-no-Relat%C3%B3rio-de-M%C3%A9dias-de-F%C3%A9rias?source=search)
