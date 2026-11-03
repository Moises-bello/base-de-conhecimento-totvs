---
article_id: 360026760151
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: f51e922b19c725a814fa709620c4728cd4897cea8142f9b320fee4f9e8c84f3b
fetched_at: '2026-06-28T22:39:22.198118+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como gerar o saldo
  credor do período anterior na apuração de ICMS? '
type: support-article
updated_at: '2021-07-15T17:44:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026760151-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-saldo-credor-do-per%C3%ADodo-anterior-na-apura%C3%A7%C3%A3o-de-ICMS
---

**Dúvida**

Como gerar o saldo credor do período anterior na apuração de ICMS?   
   
 **Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Se desejar que os valores sejam levados automaticamente, configure o parâmetro abaixo:

**MV\_APURANT = T  -** Indica se o nome do arquivo de apuracão do período anterior devera ser informado automaticamente pela rotina de apuracão do ICMS (MATA953).

Ou informe o nome do arquivo .ic0 anterior, contido na system, através da opção de **parâmetros**, no campo de **Arquivo Período Anterior?**

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
