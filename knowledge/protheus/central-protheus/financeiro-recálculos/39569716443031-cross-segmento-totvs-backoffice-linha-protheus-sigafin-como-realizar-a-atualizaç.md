---
article_id: 39569716443031
category: Financeiro - Recálculos
content_hash: 8357eb788b1a0f6c4e7869030d59712400095d3c3bbd6cdff7723088d22297ca
fetched_at: '2026-06-28T22:38:20.178679+00:00'
product: protheus
section_id: 1500001550362
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como realizar
  a atualização dos dados do cliente e fornecedor?
type: support-article
updated_at: '2026-04-14T18:38:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39569716443031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-realizar-a-atualiza%C3%A7%C3%A3o-dos-dados-do-cliente-e-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39569716437143) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
Qual é a origem e como são atualizados os campos de saldos, pedidos e histórico no Cadastro de Clientes e dos Fornecedores no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as releases  
  
**Solução**

Os campos do Cadastro de Clientes (SA1) são atualizados automaticamente pelo sistema, conforme as movimentações realizadas (títulos e pedidos).

Caso sejam identificadas divergências ou haja necessidade de implantação/reprocessamento de saldos, é possível utilizar a rotina **FINA410 (Refaz Dados Cli/For)**, que recalcula essas informações com base nos dados das tabelas principais de cada operação.

Além disso, por padrão, o sistema utiliza o parâmetro **MV\_ATUSA1 = .F.**, ou seja, o incremento automático permanece desativado. Nesse cenário, os saldos do cliente só são atualizados quando a rotina FINA410 é executada manualmente.

Se houver a necessidade de atualizar automaticamente os valores ao final dos lançamentos de títulos, é importante ajustar o parâmetro para **MV\_ATUSA1 = .T.**

**Principais campos atualizados**

**Cadastro de Clientes (SA1):**

* **Saldo Titulo - A1\_SALDUP**: Saldo de duplicatas do cliente
* **Sld.Moed.For - A1\_SALDUPM**: Saldo em moeda forte
* **Saldo LC Sec - A1\_SALFIN**: Saldo no limite de crédito secundário
* **Sld LC SE MF - A1\_SALFINM**: Saldo no limite secundário em moeda forte
* **Vlr.Acumul.  - A1\_VACUM****:** Valor acumulado de vendas no ano

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572363557655)

Ao optar pelo recálculo dos dados históricos (mv\_par02 = 1), também são atualizados:

* **Média Atraso - A1\_METR**: Média de atrasos
* **Maior Dupl. - A1\_MAIDUP**L: Maior duplicata
* **Atrasados - A1\_ATR:** Valor total de atrasos
* **Maior Atraso - A1\_MATR****:** Maior atraso
* **Pag. Atras. - A1\_PAGATR****:** Pagamentos realizados com atraso
* **Nro Pagtos  - A1\_NROPAG**: Número de pagamentos
* **Ult. Compra - A1\_ULTCOM**: Data da última compra
* **Maior Compra - A1\_MCOMPRA****:** Maior compra
* **Maior Saldo - A1\_MSALDO****:** Maior saldo do cliente
* **Nro Compras - A1\_NROCOM**: Número de compras  
    
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572363559319)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572387058071)

**Observação:**  
O campo **A1\_MSALDO (Maior Saldo)** armazena o maior saldo devedor já registrado para o cliente. Ele só será atualizado caso o novo valor calculado seja superior ao já existente.

---

**Cadastro de Fornecedores (SA2):**

* **Sld Duplict - A2\_SALDUP****:** Saldo de duplicatas
* **Sld Moed.For - A2\_SALDUPM**: Saldo em moeda forte
* **Maior Compra - A2\_MCOMPRA**: Maior compra (print 2)
* **Maior Nota - A2\_MNOTA****:** Maior nota (quando o campo existir)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572387063447)

> **Importante:** Os campos Sld Duplict (A2\_SALDUP) e Sld Moed.For (A2\_SALDUPM) podem estar desativados no configurador. Para vê-los na tela de fornecedores, verifique o flag de uso.

* ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572363565207)

Com recálculo histórico (mv\_par02 = 1):

* **No Compras  - A2\_NROCOM**: Número total de compras
* **Maior Saldo - A2\_MSALDO****:** Maior saldo credor  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572387067287)

---

Para alinhar ou corrigir os valores desses campos caso apresentem divergências:

1. Acesse o módulo Financeiro (SIGAFIN)
2. Vá em: Atualizações > Miscelânea > Recálculos > **Refaz Dados Cli/For (FINA410)**
3. Clique em **Parâmetros** e configure:
   1. Clientes/Fornecedores/Ambos: selecione **Clientes**
   2. Recalcula dados históricos: defina como **Sim**, se desejar atualizar também os campos históricos
4. Confirme a execução e aguarde o processamento  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572387068951)

---

O campo **A1\_LC (limite de crédito)** também pode ser ajustado pela rotina **FINAPP001**, caso necessário.

Saiba Mais:

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Processamento automático Limite de Crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36393896905111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-Processamento-autom%C3%A1tico-Limite-de-Cr%C3%A9dito)

**Importante:**

**MV\_ATUSA1** configurado como **T**, o sistema, ao incluir um novo título, apenas **incrementa o valor informado ao saldo já existente no cadastro do cliente (A1\_SALDUP)**, sem realizar uma reavaliação dos saldos, para não ocasionar lentidão.
