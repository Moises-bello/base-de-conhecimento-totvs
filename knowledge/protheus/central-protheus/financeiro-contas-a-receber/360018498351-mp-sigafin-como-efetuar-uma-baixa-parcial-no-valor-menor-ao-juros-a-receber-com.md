---
article_id: 360018498351
category: Financeiro - Contas a Receber
content_hash: 23349beaea4dff8e36c8185b99849b39d0f859f115d1f1a582684375a3a8e304
fetched_at: '2026-06-28T22:38:14.242816+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN  - Como efetuar uma baixa parcial no valor menor ao juros a receber
  com parâmetro MV_VLBXREC = 1 o sistema não está levando o saldo do juros para o
  campo acréscimo
type: support-article
updated_at: '2023-08-17T16:06:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018498351-MP-SIGAFIN-Como-efetuar-uma-baixa-parcial-no-valor-menor-ao-juros-a-receber-com-par%C3%A2metro-MV-VLBXREC-1-o-sistema-n%C3%A3o-est%C3%A1-levando-o-saldo-do-juros-para-o-campo-acr%C3%A9scimo
---

**Ocorrência**Como efetuar uma baixa parcial no valor menor ao juros a receber com parâmetro **MV\_VLBXREC** = 1 o sistema não está levando o saldo do juros para o campo acréscimo.

**Ambiente**Microsiga Protheus - Financeiro - A partir da versão 11.80

**Causa**Preenchimento do parâmetro**MV\_VLBXREC** incorreto.

**Solução**Quando o valor recebido é menor que o juros e multas, esse valor será abatido do saldo de multa e juros (valor acessório) e não afetará no saldo do título.

Nesse exemplo, será utilizado:

Valor do título:                 1.000,00

Emissão                            01/10/2018

Vencimento                       01/10/2018

Taxa Permanência              3,00

Ao baixar o título na data no dia 19/10/2018 o juros será R$ 54,00, porém o cliente efetuou o pagamento de R$ 34,00. Com o parâmetro **MV\_VLBXREC =1**, o sistema considera a baixa de R$ 34,00 como juros e o valor de R$ 20,00 restante será populado no campo **Acréscimo.**O sistema controlará o saldo destes valores acessórios, acrescentando ao saldo do acréscimo para que seja considerado e adicionado ao saldo do título em futuras baixas que este venha a sofrer.

**Importante:**  
Ao efetuar uma  baixa de valor menor ou igual a soma de juros e multa, a legenda do título não será alterada para baixa parcial pois não houve baixa do saldo do título mas sim do(s) acessório(s) do mesmo.  
 Nessa situação, o título continuará com suas características de inclusão até que seja efetuado uma baixa que incida sobre o saldo do título e / ou acréscimo.
