---
article_id: 360029381291
category: RH - Provisão
content_hash: ad2cb4d1cb44090ddf1f2ab1b5ff6d9fd463e7a5e8ff3a087b5dfa3359a1841c
fetched_at: '2026-06-28T22:43:55.879273+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Conferência do calculo de provisão
type: support-article
updated_at: '2025-10-24T12:05:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029381291-RH-Linha-Protheus-GPE-Confer%C3%AAncia-do-calculo-de-provis%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998660485783)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como fazer a conferência da provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para conferir do cálculo, observe as seguinte informações:

1. Verifique a data base de férias do funcionário e compare com a data do cálculo para saber os avos  
2. Verifique o salário do funcionário.  
3. Verifique se existe médias e faltas.  
4. Verifique qual a Alíquota de INSS (% empresa, % Acidente de Trabalho e % Terceiros).  
5. Verifique qual a Alíquota de FGTS.  
6. Verifique o valor atual.  
7. Subtraia o valor atual do valor anterior para validar o valor no mês.  
  
**Exemplo abaixo:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030552272)  
  
Primeiro Cálculo - Mês 01/2015**

Data base de férias: **01/01/2015**  
Data base do cálculo: **31/01/2015**  
Salario do funcionário: **1.200,00**  
Valor da provisão (no mês): **1200,00 / 12 \* 1 = 100,00**  
1/3 de ferias na provisão **(valor dividido por 3) = 33,33**  
Total de ferias (Valor + 1/3) = **133,33**  
INSS:  **133,33 \* 28,8% (tabela S037 e S038) = 38,39**  
FGTS: **133,33 \* 8% = 10,66**  
Total: **38,39 + 10,66 = 49,05 (Encargos) + 133,33 (Valor Provisão) = 182,38**

**Segundo Cálculo - Mês 02/2015**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030521151)

Considerando os mesmos dados passados no exemplo anterior, agora, o Funcionário tem direito a **02/12 avos** de férias.  
  
**Valores Atuais**  
Salário / meses do ano \* avos de direito - **1200 / 12 \* 02 = 200**  
1/3 - Valor Atual / 3 = **66,67**  
Total Férias - Valor Atual + 1/3 - **200 + 66,67 = 266,67**  
Encargos - Valor Total \* Total de Encargos das tabelas S037 e S038 - **266,67 \* 28,8% = 76,80**  
FGTS -  Valor Total \* 8 - **266,67 \* 8% = 21,33**  
Total Geral - Soma do Total de Encargos + 1/3 + Valor Atual - **98,13 + 66,67 + 200 = 364,80**

**Linha "No Mês"** - Considerar oAtual – Anterior   
  
Valor Atual - Valor Anterior - **200 -100 = 100,00**  
1/3 - Valor Atual - Valor Anterior - **66,67 – 33,33 = 33,34**  
INSS - Valor Atual - Valor Anterior - **76,80 – 38,39 = 38,41**  
FGTS - Valor Atual - Valor Anterior - **21,33 – 10,66 = 10,67**Total Encargos - Valor Atual - Valor Anterior - **98,13 - 49,05 = 49,08**

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
