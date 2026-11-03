---
content_hash: eca55af2878e537cd6b1e4f123678542f767f47d8d7a80eb105742400ea29671
fetched_at: '2026-06-29T00:09:19.206956+00:00'
page_id: '421388824'
product: rm
source: tdn-rm
title: Desconto de Duplicatas
type: documentation
url: https://tdn.totvs.com/display/LRM/Desconto+de+Duplicatas
version: 4
---

É uma antecipação de crédito decorrente de operações financeiras realizadas entre Bancos ou Factoring. Inicialmente ocorre uma negociação Financeira entre a empresa e a rede bancária ou Factoring.  Realizada a antecipação do crédito, então é feito o registro no Sistema.

**Procedimento**

1. Selecionar um Lançamento a Receber
2. Acessar: Processos / Desconto de Duplicatas
3. Valor do desconto: valor negociado de desconto sobre o título.
4. Data:  Data da operação de desconto
5. Data de Vencimento: é a data de vencimento do título, objeto da negociação.
6. Data da Compensação: compensação do extrato de caixa
7. Contabilização por evento contábil.
8. Executar

**Efeitos**

O lançamento será identificado por ícone específico e não poderá ser baixado. A baixa será realizada na efetivação do Desconto de Duplicatas.  
Será gerado o extrato de caixa na respectiva conta com operação "Desc. em aberto" com valor do lançamento menos o desconto oferecido. Esta operação será alterada para "Desc. Efetivado" quando for realizada a Efetivação do Desconto.

**Efetivar o desconto**

A baixa somente ocorrerá quando for realizada a "Efetivação do Desconto de Duplicatas". Para isso:  
1º. Selecione o Lançamento objeto do desconto de duplicatas (a conta caixa deverá estar preenchida na pasta Valores Gerais deste Lançamento).  
2º. Acesse: Processos / Efetivar Desconto de Duplicatas. Informe a data e o respectivo Evento Contábil.  
3º. O Lançamento será baixado no seu valor liquido e não gerará extrato. A diferença (valor do desconto pelo processo) deverá ser devidamente identificada pela Contabilização.

**Situações que impedem a conclusão do processo de Inclusão de Fatura**

* Lançamento negativado ou em processo de negativação.

**Cancelamento**

Acessar o Lançamento origem do Desconto de Duplicatas Acessar: Processos / Devolver Desconto de Duplicatas . A baixa do Lançamento de origem será cancelada. . Será gerado extrato de caixa no valor original do Lançamento (sem o desconto), pois o valor negociado no processo não retorna para a Empresa (perda).

**Observação**

Ao efetuar o Desconto de Duplicatas, se o parâmetro "Deduzir Tributos no Desconto de Duplicatas" estiver marcado, o Valor do Extrato será o (Valor Original – Valor dos Tributos do Lançamento).
