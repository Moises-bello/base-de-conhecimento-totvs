---
article_id: 360016330711
category: RH - 13º salário
content_hash: d9458f5e4d9bd07cdd1c749f72789528c1473b2824ef2f66ea221ebad886be70
fetched_at: '2026-06-28T22:44:00.799799+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Flexibilização das médias no cálculo do 13º Salário
type: support-article
updated_at: '2025-01-16T12:50:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016330711-RH-Linha-Protheus-GPE-Flexibiliza%C3%A7%C3%A3o-das-m%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio
---

**Dúvida**  
Flexibilização das médias no cálculo do 13º Salário  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Nos parâmetros para o cálculo do 13º Salário, existem duas perguntas: **"Data de Referência?"** e **"Referência para Média?"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012074972)

Para o sistema realizar a busca dos **avos de direito**, diferente da busca **das médias**, o Mnemônico **P\_REFMED** (Antigo parâmetro **MV\_REFMED)** deverá estar como **.T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012065691)

Caso o **parâmetro** esteja com **.F.** o sistema calculará as médias de acordo com a pergunta **"Data de Referência?"**

**Exemplo**

Parâmetro **MV\_MEDDIRE** está configurado como **N**, indicando que, após a apuração da média, o valor encontrado será dividido por 12 e multiplicado pelos avos de direito do 13º salário;

No cálculo da **1ª parcela do 13º salário**, as datas utilizadas como referência são: **31/10/2018 (para o cálculo das médias)** e **31/12/2018 (para a apuração dos avos de direito):**

Data Admissão: 18/02/2018

Total de Acumulados: 25.167,00

Meses para média: 8 meses (de março a outubro (referência para média)

Meses de direito: 10 meses (de março a dezembro (referência para Avos)

Valor da Média: 25.167,00/8 = 3.145,88

Valor da Média a ser pago na 1ª parcela: ((Média/12) \* Meses Direito)/2

Valor da Média a ser pago na 1ª parcela: ((3.145,88/12) \* 10)/2

Valor da Média a ser pago na 1ª parcela: 1.310,78

No cálculo da 2ª parcela do 13º salário, as datas utilizadas como referência são: 30/11/2018 (para o cálculo das médias) e 31/12/2018 (para a apuração dos avos de direito):

Admissão: 05/02/2018

Meses para Média: 10 (de fevereiro a novembro)

Meses direito: 11 (de fevereiro a dezembro)

Total acumulados de fevereiro a novembro: 27.589,50

Valor Média = 27.589,50/10 meses: 2.758,95

Valor da Média a ser pago na 2ª parcela: (Média/12) \* Meses Direito

Valor da Média a ser pago na 2ª parcela: (2.758,95/12) \* 11

Valor da Média a ser pago na 2ª parcela: 2.529,04

Cálculo Complemento 2ª Parcela na Folha de dezembro

Meses para média : 11 (de fevereiro a dezembro)

Meses direito: 11 (de fevereiro a dezembro)

Na Folha de dezembro, o funcionário teve 2.000,00 de Comissão + 500,00 de DSR de Comissão.

Total de acumulados de Fevereiro a Dezembro = **30.089,50** (27.589,50 + 2.500,00).

Recálculo da média da 2ª Parcela: 30.089,50/11 meses = **2.735,41**

Recálculo da média a ser pago na 2ª Parcela: (Média / 12) \* Meses Direito

Recálculo da média a ser pago na 2ª Parcela: (2.735,41 / 12) \* 11

Valor da média a ser pago na 2ª parcela recalculado = **2.507,46**

Neste caso não haveria diferença a ser paga na folha de dezembro

Haveria um desconto de 21,58 (2.507,46 (valor novo) - 2.529,04 (valor pago)), caso o parâmetro **MV\_DF13NEG** (descontar valor negativo de 13º salário) esteja configurado com "S".

**Observação**

Para conferência da média calculada, pode-se emitir o relatório de **Demonst. de Médias** , através da rotina: **Relatórios \ Lançamentos \ Demonst. de Médias (GPER080),** para que não ocorra divergências entro o valor pago e o valor apresentado no relatório, atente-se as perguntas **"Data base ?" e "Considera mês Atual?"**No calculo do 13° Salario o sistema apura os valores do Acumulado (SRD).

A pergunta **"Data de Referência"** é apresentada somente quando emitida a média de 13º Salário por dentro da rotina **Lançamentos por Funcionário.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10698219598615)

**Saiba Mais****Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>****[RH - Linha Protheus - GPE - Médias no cálculo do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016223611-RH-Linha-Protheus-GPE-M%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio)****[RH - Linha Protheus - GPE - Apuração das médias do 13º não batem com o cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896372-RH-Linha-Protheus-GPE-Apura%C3%A7%C3%A3o-das-m%C3%A9dias-do-13%C2%BA-n%C3%A3o-batem-com-o-c%C3%A1lculo)  
[RH - Linha Protheus - GPE - Como analisar médias no calculo de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015780592-RH-Linha-Protheus-GPE-Como-analisar-m%C3%A9dias-no-calculo-de-13%C2%BA-Sal%C3%A1rio)****[RH - Linha Protheus - GPE - Como gerar memória de calculo para conferência de médias da primeira parcela do 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000096841-RH-Linha-Protheus-GPE-Como-gerar-mem%C3%B3ria-de-calculo-para-confer%C3%AAncia-de-m%C3%A9dias-da-primeira-parcela-do-13%C2%BA)**
