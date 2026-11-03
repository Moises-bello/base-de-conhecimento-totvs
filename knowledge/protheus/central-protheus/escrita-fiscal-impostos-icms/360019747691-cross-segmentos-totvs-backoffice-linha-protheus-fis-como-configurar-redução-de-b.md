---
article_id: 360019747691
category: Escrita Fiscal - Impostos - ICMS
content_hash: d4b83cbddc06a2f99dc5aace3c91651851738de0b07e1a728c51f03bf02803de
fetched_at: '2026-06-28T22:39:26.030144+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS-Como configurar redução
  de base de cálculo do ICMS? '
type: support-article
updated_at: '2022-10-24T15:17:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019747691-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-redu%C3%A7%C3%A3o-de-base-de-c%C3%A1lculo-do-ICMS
---

**Dúvida**

Redução de Base de Cálculo de ICMS

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Cadastro TES:

Calc. ICMS (F4\_ICM) = S

%Red.do ICMS (F4\_BASEICM) "TES" ou %Red.do ICMS (F7\_BASEICM) "Exceção fiscal" = Informe o valor a ser calculado do ICMS próprio. No padrão, este valor é apresentado na coluna Tributada do Livro Fiscal.

Livro Fiscal ICMS (F4\_LFICM) = ISENTO/ OUTROS. Selecione uma das opções para informar onde será destacado o restante da operação Valor total da NF menos percentual informado no campo F4\_BASEICM.

Material de Consumo (F4\_CONSUMO)=NÃO

Exemplo:

%Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Isento(40%)

%Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Outros(40%)

**ATENÇÃO:**

**Há algumas exceções em que mesmo com redução de Base de Cálculo nenhum valor deve ser tributado para esta situação. Para isso existe o campo Material de Consumo (F4\_CONSUMO).**

Exemplos:

1º ) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = Isento

Material de Consumo (F4\_CONSUMO) = Sim

O valor do ICMS será dividido entre as colunas ISENTO (60%) e OUTROS.

2º) %Red.do ICMS (F4\_BASEICM) = 60

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = OUTROS

100% do valor será apresentado na coluna ISENTO.

3º) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = SIM

O valor do ICMS será dividido entre as colunas OUTROS (60%) e ISENTO.

4º) %Red.do ICMS (F4\_BASEICM) = 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS;

Material de Consumo (F4\_CONSUMO) = OUTROS.

100% do valor será apresentado na coluna OUTROS.
