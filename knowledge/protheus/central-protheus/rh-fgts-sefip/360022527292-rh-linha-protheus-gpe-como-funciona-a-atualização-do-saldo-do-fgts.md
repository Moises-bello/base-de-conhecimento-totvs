---
article_id: 360022527292
category: RH - FGTS / SEFIP
content_hash: ba3e2a6628d855f0c53feb345c556e981f4336cefc3a33bc55330c482e8290f7
fetched_at: '2026-06-28T22:43:41.369966+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona a atualização do saldo do FGTS
type: support-article
updated_at: '2025-08-07T13:35:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022527292-RH-Linha-Protheus-GPE-Como-funciona-a-atualiza%C3%A7%C3%A3o-do-saldo-do-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34012816014615) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como funciona a Atualização do saldo do FGTS?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

ATUALIZAÇÃO DO SALDO FGTS

Extrato disponibilizado da Caixa Econômica Federal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020005252)

TELA ATUALIZAÇÃO SALDO FGTS  
**Exemplo 1**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871071)

* Competência 01/2015
* Depósito realizado em 06/02/15 no valor de 460,98
* **Juros disponibilizado pela caixa em 10/02/15 com percentual de 0,334600**

O sistema sempre verificará a competência que foi calculada a folha de pagamento, pois irá buscar a verba 701 – FGTS do Mês para preencher a coluna Valor do Depósito na tela de Manutenção do Saldo do FGTS apresentada abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871171)

**Exemplo 2**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871271)**

* Competência 02/2015
* Depósito realizado em 06/02/15 no valor de 380,08
* **Juros disponibilizado pela caixa em 10/02/15 com percentual de 0,263400**

O sistema sempre verificará a competência que foi calculada a folha de pagamento, pois irá buscar a verba 701 – FGTS do Mês para preencher a coluna Valor do Depósito na tela de Manutenção do Saldo do FGTS apresentada abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020005672)**

**TELA DE MANUTENÇÃO DE SALDO FGTS – Conferência da aplicação dos juros.**

Nota: O primeiro registro corresponde ao lançamento do saldo final no ano de 2014. É necessário realizar o lançamento manual para início da rotina, pois anterior a isso, não há um processamento de cálculo feito pelo Protheus.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871471)

**Conclusão Exemplo 1:**

Analisando o extrato da caixa, identifiquei que o saldo em dezembro de 2014 é 22.261,81. Seria o valor apresentado na quebra de página de 22.336,29 menos 74,48 que corresponde aos juros referente ao JAM de 10/02/2015.

Esse saldo de 22.261,81 que foi lançado manualmente devido se a primeira vez que a rotina é utilizada.

Após executar a rotina de atualização de saldo na competência de folha 01/2015, o sistema criou a linha referente a esse período onde o saldo anterior é 22.261,81.

Os juros incluídos no parâmetro para executar a rotina da competência 01/2015 foi o percentual de 0,334600 apresentado no extrato da caixa com data de 10/02/15 (30 dias após o depósito recolhido na folha).

Diante disso, o Protheus realizou o seguinte cálculo:

Saldo Anterior (22.261,81) \* Percentual de Juros 10/02/15 (0,334600) resultando no valor de 74,48.

A coluna Valor de Depósito, foi alimentada conforme os acumulados da competência 01/15 (DATARQ = 01/2015), conforme tela no **Exemplo 01.**

Desta forma, a coluna Saldo Atual corresponde à somatória de 22.261,81 + 74,48 + 460,98 = 22.797,27.

A JAM de 0,334600 da data 10/02/2015 foi aplicado sobre o Saldo Anterior que refere-se de 01/2015, ou seja, o saldo de 01/2015 foi valorizado após 30 dias da data de depósito da folha competência 12/2014 de acordo com conceito utilizado no extrato da Caixa Econômica Federal.

**Conclusão Exemplo 2:**

A coluna Saldo Anterior do Mês/Ano de 02/2015 foi atualizada com o valor de 22.797,27 que corresponde à coluna Saldo Atual apresentado na competência 01/2015,

Após executar a rotina de atualização de saldo na competência de folha 02/2015, o sistema criou a linha referente a esse período.

Os juros incluídos no parâmetro para executar a rotina da competência 02/2015 foi o percentual de 0,263400 apresentado no extrato da caixa com data de 10/03/15 (30 dias após o depósito recolhido na folha).

Diante disso, o Protheus realizou o seguinte cálculo:

Saldo Anterior (22.797,27) \* Percentual de Juros 10/03/15 (0,263400) resultando no valor de 60,04

A coluna Valor de Depósito, foi alimentada conforme os acumulados da competência 02/15 (DATARQ = 02/2015), conforme tela no **Exemplo 02**.

Desta forma, a coluna Saldo Atual corresponde à somatória de 22.797,27 + 60,04 + 380,08 = 23.237,39.

A JAM de 0,263400 da data 10/03/2015 foi aplicado sobre o Saldo Anterior que refere-se de 02/2015, ou seja, o saldo de 02/2015 foi valorizado após 30 dias da data de depósito da folha competência 01/2015 de acordo com conceito utilizado no extrato da Caixa Econômica Federal.

Detalhei 2 exemplos para melhor entendimento do cálculo executado pelo Protheus que está de acordo com o conceito/extrato da Caixa Econômica Federal, onde podemos concluir que não foi apresentado erros.

Obs: Interrompi a atualização do saldo de FGTS, devido à divergência encontrada no valo do depósito na competência 12/2015, desta forma, o saldo final não será igual ao do extrato da caixa.

Analisando o Acumulado (Ficha Financeira), identifiquei  a seguinte situação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871591)

Verba 701 – 382,78

Verba 703 – 235,40

Total           - 618,18

Valor apresentado no acumulado de 12/2015, desta forma, a coluna valor depositado ficará com o valor 618,18, conforme tela de manutenção do saldo FGTS.

No extrato da caixa, foi depositado em 07/01/16 o valor de R$ 630,91, valor que não confere com o acumulado do funcionário. Desta forma, deverá ser analisada a situação, pois pode ter ocorrido algum problema com a importação na fase de implantação do Protheus ou o depósito na Caixa estar incorreto.

**Saiba Mais**  
[Artigos Gestão de Pessoal](%C2%A0https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
