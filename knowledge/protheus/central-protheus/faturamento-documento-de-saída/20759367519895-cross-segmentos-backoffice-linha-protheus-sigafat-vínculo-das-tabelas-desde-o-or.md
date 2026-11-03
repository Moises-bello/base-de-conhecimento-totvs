---
article_id: 20759367519895
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c74ec3a6abd8659552fc4f7febfbf0e7fa575a6bff68463c4e85c5ad98fe2aa1
fetched_at: '2026-06-28T22:38:45.314079+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Vínculo das tabelas
  desde o orçamento de venda até o título a receber
type: support-article
updated_at: '2024-01-22T14:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20759367519895-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-V%C3%ADnculo-das-tabelas-desde-o-or%C3%A7amento-de-venda-at%C3%A9-o-t%C3%ADtulo-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20759367494423) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o vínculo das tabelas desde o orçamento de venda até o título a receber?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução**

Desde o processo do Orçamento de Venda (MATA415) até o título a receber, o sistema passa pelas tabelas principais:

SCJ, SCK, SC5, SC6, SC9, SF2, SD2 e SE1 criando vínculos com seus campos referenciando as tabelas entre si (campos estrangeiros).

SCJ - Cabeçalho do orçamento de venda (MATA415)

* "Status (CJ\_STATUS)" do orçamento recebe o valor "B" quando gerou-se um pedido de venda (legenda vermelha)

SCK - Itens do orçamento de venda (MATA415)

* "Numero (CK\_NUM)" recebe o "Numero (CJ\_NUM)" na geração do orçamento de venda
* "Num. PV (CK\_NUMPV)" recebe o "Numero (C6\_NUM)" ao gerar o pedido de venda

SC5 - Cabeçalho do pedido de venda (MATA410)

* "Nota (C5\_NOTA)" recebe o "Numero (F2\_DOC)" do último item a ser faturado
* "Série (C5\_SERIE)" recebe o "Série (F2\_SERIE)" do último item a ser faturado

SC6 - Itens do pedido de venda liberados (MATA410)

* "Numero (C6\_NUM)" recebe o "Numero (C5\_NUM)" ao ser gerado
* "Num. Orc. (C6\_NUMORC)" recebe o "Numero (CK\_NUM)" ao vir do orçamento
* "Nota (C6\_NOTA)" recebe o "Numero (D2\_DOC)" ao faturar
* "Série (C6\_SERIE)" recebe o "Série (D2\_SERIE)" ao faturar
* "DT Ult.Fat. (C6\_DATFAT)" recebe o "DT Emissão (D2\_EMISSAO)" ao faturar

SC9 - Itens do pedido de venda liberados (MATA460A)

* "Pedido (C9\_PEDIDO)" recebe o "Pedido (C6\_NUM)" ao ser liberado
* "Nota Fiscal (C9\_NFISCAL)" recebe o "Numero (D2\_DOC)" ao faturar
* "Serie NF (C9\_SERIENF)" recebe o "Série (D2\_SERIE)" ao faturar

SF2 - Cabeçalho do Documento de Saída (MATC090)

* "Num. Titulo (F2\_DUPL)" recebe o "Titulo (E1\_NUM)" ao ser faturado com duplicata

SD2 - Itens do Documento de Saída (MATC090)

* "Num. Docto (D2\_DOC)" recebe o "Numero (F2\_DOC)" ao ser gerado/faturado
* "No do Pedido (D2\_PEDIDO)" recebe o "Pedido (C6\_NUM)" ao ser faturado

SE1 - Título a receber (FINA740)

* "No. Titulo (E1\_NUM)" recebe o "Numero (F2\_DOC)" ao ser gerado
* "No. Pedido (E1\_PEDIDO)" recebe o "Numero (C5\_NUM)" ao ser faturado com duplicatas
