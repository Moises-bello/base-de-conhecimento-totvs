---
article_id: 360050187034
category: Gestão de Transportes (TMS)
content_hash: 9201ed1366d43420d7fd6e582f569253f640a1dd9afb8e67fdc1bd2266a46875
fetched_at: '2026-06-28T22:45:32.431499+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Principais parâmetros Contrato Carreteiro
type: support-article
updated_at: '2025-08-18T19:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050187034-Log%C3%ADstica-Linha-Protheus-TMS-Principais-par%C3%A2metros-Contrato-Carreteiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34272273171479)***Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Quais são os principais parâmetros para emissão do **Contrato Carreteiro**? **Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões **Solução**Os principais parâmetros relacionados a emissão do **Contrato Carreteiro** são:

* **MV\_FORGEN**- Código do fornecedor genérico.
* **MV\_NATCTC** - Define a **Natureza** para a geração de títulos a pagar do **Contrato de Carreteiro**.
* **MV\_NATPDG** - Código da **Natureza** utilizado para geração de títulos a pagar provenientes de valores de pedágios.
* **MV\_NATDEB** - Código da **Natureza** utilizado para geração de títulos a pagar provenientes de **Contratos de Carreteiros** para a **Filial de Débito**.
* **MV\_TPTCTC** - Indica o tipo do título proveniente do **Contrato de Carreteiro** a ser gerado no **Contas a Pagar**.
* **MV\_TPTPDG** - Indica o tipo do título proveniente dos valores de pedágio a ser gerado no **Contas a Pagar**.
* **MV\_DESCTC** - Indica o código da despesa do **Contrato de Carreteiro**, utilizado para gravar o custo de transporte dos **Contratos de Carreteiro**. Exemplo.: **Código da despesa contrato - 000001**.
* **MV\_DESPDG** - Código de **Despesa de Pedágio**.
* **MV\_LIBCTC** - Identifica se habilita o controle de liberação de **Contrato de Carreteiro**.
* **MV\_TMSGRPC** - Indica se o **Contrato de Carreteiro** pode gerar pedido de compra para pessoa jurídica.
* **MV\_GERTIT** - Identifica se o **Contrato de Carreteiro** deverá gerar **Contas a Pagar**.
* **MV\_CTCPREF** - Indica o prefixo dos títulos gerados em **Contrato de Carreteiro**, referentes ao pagamento do frete ao carreteiro.
* **MV\_ENTSOCO** - Permite gerar **Contrato de Carreteiro** para as viagens de entrega sem registro de ocorrência apontado.
* **MV\_COLSOCO** - Permite gerar **Contrato de Carreteiro** para as viagens de coleta sem registro de ocorrência apontado.
* **MV\_TMSRVOL** - Trata o rateio do valor do frete a pagar por volumes coletados e/ou entregues. O parâmetro define a divisão do valor do frete a pagar calculado no momento da criação/geração do **Contrato de Carreteiro**, proporcional aos volumes coletados ou entregues.
* **MV\_ULTDEST -**Define se utiliza o último destino da coleta/entrega.
* **MV\_TMSOPDG**- Utiliza **Operadora de Frota** e **vale-pedágio**.
* **MV\_TMSCTCA**- Considera somente os valores de abatimentos específicos do **Contrato Complementar** no pagamento de **Saldo de Carreteiro**.
* **MV\_TMSCDPG**- Considera a condição de pagamento informada no cadastro do fornecedor para geração de contrato de carreteiro por viagem.
* **MV\_MININSS** - Valor mínimo para retenção de **INSS -  Instituto Nacional do Seguro Social.** Caso o valor de **INSS** calculado no período seja inferior, o **INSS** não será retido.
* **MV\_LIMINSS** - Valor limite de retenção para o **INSS** de pessoa física.
* **MV\_INSBXCP** - Define momento do tratamento da retenção do imposto **INSS.** **1 = Na Baixa** ou **2 = Na Emissão** - *Default.*
* **MV\_TMSVDEP** - Esse parâmetro deve possuir o valor referente ao dependente de **IR - Imposto de Renda.**
