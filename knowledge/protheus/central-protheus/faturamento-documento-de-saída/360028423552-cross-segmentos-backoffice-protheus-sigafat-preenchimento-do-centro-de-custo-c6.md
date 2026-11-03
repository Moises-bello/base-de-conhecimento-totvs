---
article_id: 360028423552
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: fe43cde4b9f817d241ef3a225ede0dd885df4085a79f1d597fe8b160b3abef10
fetched_at: '2026-06-28T22:38:44.137073+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do "Centro
  de Custo (C6_CC)" no faturamento
type: support-article
updated_at: '2024-04-26T17:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028423552-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-Centro-de-Custo-C6-CC-no-faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23082158083735)Tempo aproximado para leitura: 00:01:00 min**  
**Dúvida**Como preencher Centro de Custo no Documento de Saída?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

As informações partem do Pedido de Vendas (podendo ser vínculadas do Cadastro do Produto), e são levadas para o Documento de saída, conforme demonstrado abaixo:

* **Pedido de Vendas, a origem desde o produto até a nota fiscal ao faturar**:
  + B1\_CC **->** C6\_CC **->** D2\_CCUSTO
  + B1\_CONTA **->** C6\_CONTA **->** D2\_CONTA
  + B1\_ITEMCC **->** C6\_ITEMCTA **->** D2\_ITEMCC
  + B1\_CLVL **->** C6\_CLVL **->** D2\_CLVL

As informações **NÃO** são levados para o Financeiro. O faturamento documento de saída **NÃO** realiza este preenchimento:

* **D2\_CCUSTO -> E1\_CCC, E1\_CCD, E1\_CCUSTO**
* **D2\_ITEMCC -> E1\_ITEMC, E1\_ITEMD**
* **D2\_CLVL -> E1\_CLVLCR, E1\_CLVLDB**

O motivo é que o documento de saída pode ter vários itens com centros de custo diferentes e o título no Financeiro é único, não sendo possível determinar qual centro de custo deve ser gravado no título. **O preenchimento para os campos do Financeiro ocorre quando o título é incluído manualmente no Financeiro.** Quando a informação nasce no Faturamento, os dados são armazenados nas Tabelas do Faturamento.

Produtos que não movimentam estoque (não são produtos físicos) não possuem custo (podem possuir preço de venda; mas não possuem um custo para ser produzido). Desta forma, se não movimenta estoque, não vai alimentar/movimentar a Tabela AGH.

**OBSERVAÇÃO 1:** No Pedido de Vendas também é possível realizar o rateio:

* **Pedido de Vendas -> Ações relacionadas -> Rateio**
  + AGG\_CC **->** AGH\_CC
  + AGG\_ITEMCT **->** AGH\_ITEMCT
  + AGG\_CLVL **->** AGH\_CLVL

**OBSERVAÇÃO 2:** D2\_RATEIO = 1 - Sim

**OBSERVAÇÃO 3:** Caso possua o campo **C6\_CCUSTO** no pedido de vendas (MATA410) ao invés do campo **C6\_CC,** este campo "C6\_CCUSTO" foi descontinuado a partir do release 15 da Versão 12.

**OBSERVAÇÃO 4:** O faturamento não efetua importação de arquivo de centro de custo, toda e qualquer informação relacionada é inserida manualmente. Como o cadastro de centro de custo é um cadastro contábil, em caso de dúvidas de procedimento com centro de custos, acione a equipe Ativo e Contábil para auxiliar.

**Saiba mais:**

* **[FAT0117\_Centro\_de\_Custo\_no\_Documento\_de\_Saída](https://tdn.totvs.com/x/326ZDg)**
* **[Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA030-Cadastro-de-Centro-de-custo-CTT-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005702941-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA030-Cadastro-de-Centro-de-custo-CTT-)**
* **[MP-INTEGRAÇÃO-EAI-CENTRO-DE-CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006615172-MP-INTEGRA%C3%87%C3%83O-EAI-CENTRO-DE-CUSTO)**
* **[MP - SIGACTB - Relatórios com Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817912-MP-SIGACTB-Relat%C3%B3rios-com-Centro-de-Custo)**
* **[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Pré-requisitos para entrega](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Pr%C3%A9-requisitos-para-entrega)**
