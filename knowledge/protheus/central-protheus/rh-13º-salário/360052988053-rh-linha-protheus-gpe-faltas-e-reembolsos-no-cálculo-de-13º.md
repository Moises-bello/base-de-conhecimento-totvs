---
article_id: 360052988053
category: RH - 13º salário
content_hash: 85fd0210fd7bc46901a849d7284cb5cb4962f1995f697494c193ca2a4be772a5
fetched_at: '2026-06-28T22:44:00.782182+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Faltas e Reembolsos no cálculo de 13º
type: support-article
updated_at: '2025-11-28T12:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052988053-RH-Linha-Protheus-GPE-Faltas-e-Reembolsos-no-c%C3%A1lculo-de-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36637462884247)  Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**  
Como considerar Faltas e Reembolsos no cálculo de 13º  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para o abatimento de faltas no cálculo do 13º salário, o funcionário deve possuir as seguintes verbas de descontos com os id's abaixo presentes na tabela **SRD**(acumulados):  
  
**0054 - Desconto de Faltas**  
**0055 - Desconto de Atrasos**  
**0203 - Desconto de Falta Mês Anterior**  
**0242 - Desconto de Faltas (II)**  
**0243 - Atrasos (II)**  
  
Além destes, temos os Id's de cálculo para **abono de faltas e atrasos** que são:  
  
**0244 - Reembolso de Faltas**  
**0245 - Reembolso de Atrasos**  
  
  
**1- Configuração das Verbas**  
Acesse a rotina de cadastro de verbas em: **Atualizações/ Definições Cálculo/ Verba**.  
  
As verbas de Desconto e Reembolso devem possuir a seguinte configuração:  
**Qtde. Lancto.:** 9  
**Lcto Diário:** Sim  
  
No exemplo, utilizaremos a verba de id 0054 que seria do tipo desconto, porém as verbas de reembolso devem ser do tipo provento.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637493753239)  
  
Na **aba Médias**, o campo **Media 13º** está com conteúdo **S**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637493755543)

**2- Mnemônico P\_SEGFALT**  
Acesse a rotina em **Atualizações/ Definições Cálculo/ Mnemônicos**.  
  
O mnemônico P\_SEGFALT deve estar **habilitado.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637462890263)

**3- Lançamento das Verbas**  
As verbas de **Desconto Faltas** devem ser lançadas informando a sua **data de referência.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637462890647)**

Caso exista reembolso de faltas, como no mês seguinte por exemplo, as **Verbas de Reembolso** devem ser lançadas com a **data de referência em que houve o desconto da falta.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637462890903)

No exemplo acima, foram descontados 2 faltas referente aos dias 01/07 e 02/07 na folha de Julho. Em Agosto essas faltas foram devolvidas/reembolsadas, então o lançamento da verba de reembolso foi realizado com a data de referência de 01/07 e 02/07 também.

Os lançamentos das **verbas** devem estar **dentro do ano corrente** para serem consideradas no **cálculo do 13º.**

**4- Conferência**  
Utilize a rotina Consulta Genérica para extrair a SRD e conferir as faltas e reembolsos caso tenham.  
Menu **Consultas > Cadastros > Genéricos**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36637462891287)  
  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como incluir lançamentos no cálculo da Primeira Parcela do 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412601175191-RH-Linha-Protheus-GPE-Como-incluir-lan%C3%A7amentos-no-c%C3%A1lculo-da-Primeira-Parcela-do-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409855157399-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-da-1%C2%AA-parcela-do-13-Sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Sistema não calcula para alguns funcionários 1ª parcela do 13º salario, Pela EndCalc() - S\_ADT13PGT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039131954-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-para-alguns-funcion%C3%A1rios-1%C2%AA-parcela-do-13%C2%BA-salario-Pela-EndCalc-S-ADT13PGT?source=search)
