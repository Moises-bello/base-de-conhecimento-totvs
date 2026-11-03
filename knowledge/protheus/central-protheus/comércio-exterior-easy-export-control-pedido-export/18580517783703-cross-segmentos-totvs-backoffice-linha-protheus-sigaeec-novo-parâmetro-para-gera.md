---
article_id: 18580517783703
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: e0dbe330dd7b4b4237adc3edbe101867dc83a88529ec6e82ced6dcc696660f60
fetched_at: '2026-06-28T22:36:59.202413+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAEEC - Novo Parâmetro
  para Geração de Nota Fiscal de Devolução.
type: support-article
updated_at: '2023-10-26T16:51:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18580517783703-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Novo-Par%C3%A2metro-para-Gera%C3%A7%C3%A3o-de-Nota-Fiscal-de-Devolu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18580503810327) Tempo aproximado para leitura: **03:00min** **Dúvida**Novo Parâmetro **(MV\_EEC0045)** para Geração de Nota Fiscal de Devolução.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– A partir da versão 12.1.33.  
  
**Solução  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18580773233687)**

**- Procedimento para Utilização:** **Pré-Requisitos:**

* "**MV\_EECFAT = .T.**", "**MV\_AVG0131 = .T.**";
* Possuir um Tipo de Entrada e Saída **"TES",** de entrada com um código fiscal que corresponda a operação de devolução, em contra partida a nota fiscal de exportação/venda;
* Possuir uma **"TES"** de saída com um código fiscal que corresponda a operação de exportação/ venda;
* Possuir um pedido de exportação, utilizar a **"TES"** de Saída que deve ser cadastrado no sistema;
* Faturar o pedido no modulo do Faturamento e gerar a Nota Fiscal de Saída;
* Incluir um embarque de exportação, e preencher a data de embarque;
* Liquidar todas as parcelas de cambio que foram geradas para este processo.

**Sequencia 01:**

1. No Compras (**SIGACOM**) acesse "**Atualizações / Movimentos / Documento de Entrada**";
2. Clique em "**Incluir**";
3. Preencha o campo "**Tipo da Nota = Devolução**", "**Form. Prop. = Sim/Não**", no campo "**cliente**", informe o código do cliente utilizado no Pedido de exportação. Informe o campo "**Espec. Docum. = NF"**  e campo "**Uf.Origem = EX**";
4. Na linha dos itens informe o código do produto utilizado no pedido de exportação, e a TES de entrada que foi cadastrado;
5. Clique em "**Ações Relacionadas / Origem**" e selecione a NF de saída que foi gerado para o pedido de exportação no modulo do Faturamento e clique em "**Confirmar**";
6. Clique em "**Confirmar**" para gerar a "**Nota Fiscal de Devolução**".

**Saiba mais:**  
[**TTA389\_DT\_Novo Parametro para Geração de Nota Fiscal de Devolução**](https://tdn.totvs.com/pages/releaseview.action?pageId=220890199)
