---
article_id: 4411545088023
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 2a9481aaf9d0e8782f8a9592cf4ab9865927598817eaa7352547735132b8cceb
fetched_at: '2026-06-28T22:39:22.159116+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como incluir valor
  do saldo credor da Apuração de ICMS na DAPI - MG?
type: support-article
updated_at: '2021-10-26T19:56:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411545088023-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-incluir-valor-do-saldo-credor-da-Apura%C3%A7%C3%A3o-de-ICMS-na-DAPI-MG
---

**Dúvida**

Como incluir valor do saldo credor da Apuração de ICMS na DAPI - MG?

**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

Para que o saldo credor de ICMS gerado na **Apuração (MATA953)**, seja apresentado no arquivo da DAPI-MG, especificamente, na linha 87 (Saldo Credor do período anterior), é necessário informar o nome do arquivo .ic0 anterior, contido na system, através da opção de **parâmetros**, no campo de **Arquivo Período Anterior?**

Para localizar o arquivo do período, utilize a seguinte regra:

**AA010101.IC0**

A – Número do Livro Selecionado - Se for \* o sistema fixa a letra A, se no cadastro do TES for informado o número do livro e nos parâmetros da Apuração for informado o número do livro de 1 à 9 ele preenche com o próprio número do livro 1F010101.IC0

A – Mês de apuração de ICMS/IPI - Conforme tabela abaixo:

**A Janeiro B Fevereiro C Março D Abril E Maio F Junho G Julho H Agosto I Setembro J Outubro K Novembro L Dezembro**

**S Semestral X Anual**

01 – Ano de apuração - Últimos 2 dígitos.

01 – Código da Empresa.

01 – Código da Filial.

IC\* - Extensão do Arquivo - IC – ICMS, IP – IPI:

\* 1 – Primeiro Decêndio

\* 2 – Segundo Decêndio

\* 3 – Terceiro Decêndio

\* 0 – Mensal

\* 1 – Primeira Quinzena

\* 2 – Segunda Quinzena

a - LIVRO

l - MÊS

12 - ANO

02 - COD. DA EMPRESA

03 - COD. DA FILIAL

.ic0
