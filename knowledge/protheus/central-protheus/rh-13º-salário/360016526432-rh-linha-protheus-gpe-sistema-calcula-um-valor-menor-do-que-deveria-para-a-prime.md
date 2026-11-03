---
article_id: 360016526432
category: RH - 13º salário
content_hash: db7d71bd114dadb63fa207b72aa20c161b6a179c4c0dfa431aac85005d53934c
fetched_at: '2026-06-28T22:44:01.627310+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema calcula um valor menor do que deveria para
  a primeira parcela do 13° salário
type: support-article
updated_at: '2025-07-23T12:59:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016526432-RH-Linha-Protheus-GPE-Sistema-calcula-um-valor-menor-do-que-deveria-para-a-primeira-parcela-do-13-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26914830273431)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O que verificar quando no cálculo da primeira parcela do décimo terceiro salário, é demonstrado um valor menor do que deveria?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esse incidente ocorre por um dos motivos abaixo:

**1.** Existem **afastamentos e/ou faltas** para o funcionário.  
Caso existam afastamentos dentro do ano corrente o **Sistema abaterá os valores**.

**2.** Caso possua mais de 15 faltas no mesmo mês ele **perderá o direito ao avo**;  
  
**3.** Nos parâmetros de cálculo da primeira parcela consta **data de referência** incorreta.  
Deixe a referência sempre como o último dia do ano **(31/12/XX)** para que o sistema considere os 12 meses como base de cálculo;  
  
**4.** Data de **admissão dentro do ano.**  
Sistema irá calcular somente o **proporcional aos meses trabalhados;****5.** Ausência de cálculo na SRD\* (Acumulados Anuais) para verbas com id. **0021** (Líquido de 13º), **0022** (Adiantamento de 13º Salário), **0023** (Desconto Primeira Parcela de 13º Salário) e **0163** (Diferença da Primeira Parcela de 13º Salário);  
  
**6.** No **cadastro de funcionários,**deixe o campo**RA\_MESESAN** (número de meses trabalhados) zerado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10221843883031)

**7.** Existem roteiros de cálculo específicos **com customizações.****Nota:**  
**\***Além da SRD diretamente, poder ser utilizado a Ficha Financeira para conferência - [RH - Linha Protheus - GPE - Como emitir Relatório Ficha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX1INgAQQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBiGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MDM5NjA3MzA3NzUtUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZW1pdGlyLVJlbGF0JUMzJUIzcmlvLUZpY2hhLUZpbmFuY2VpcmEGOwhUOg5zZWFyY2hfaWRJIikyYzU0MmM3Ny0zMTRmLTRkN2MtYjY3MC05NzM0ZDRhMTc2NzQGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlncGUgZmljaGEgZmluYW5jZWlyYQY7CFQ6EnJlc3VsdHNfY291bnRpAeo%3D--f3539e5fa684967f1062659ea9291b70f3124100)  
  
**Saiba Mais:**

**[RH - Linha Protheus - GPE - Sistema não calcula para alguns funcionários 1 parcela do 13 salario, Pela EndCalc() - S\_ADT13PGT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039131954-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-para-alguns-funcion%C3%A1rios-1-parcela-do-13-salario-Pela-EndCalc-S-ADT13PGT)**

**[RH - Linha Protheus - GPE - Como parametrizar o sistema para que a 1ª Parcela do 13º Salário considere até a competência atual ou até dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016125111-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-que-a-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-considere-at%C3%A9-a-compet%C3%AAncia-atual-ou-at%C3%A9-dezembro)**

**[RH - Linha Protheus - GPE - Como efetuar o cálculo da primeira parcela do 13º salário para um funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8191950951447-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-da-primeira-parcela-do-13%C2%BA-sal%C3%A1rio-para-um-funcion%C3%A1rio)**
