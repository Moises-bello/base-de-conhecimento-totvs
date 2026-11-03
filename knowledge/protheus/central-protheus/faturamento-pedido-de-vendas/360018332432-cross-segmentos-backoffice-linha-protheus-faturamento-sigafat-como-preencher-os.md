---
article_id: 360018332432
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bceab91df504d2cbf67741c78d1385bbbd926cec21c311995a449484750d4796
fetched_at: '2026-06-28T22:38:38.684348+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Como
  preencher os campos C5_NOTA e C5_SERIE
type: support-article
updated_at: '2022-09-21T12:15:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018332432-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Como-preencher-os-campos-C5-NOTA-e-C5-SERIE
---

**Dúvida**

Como é preenchido os campos **C5\_NOTA** e **C5\_SERIE**?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

Os campos **C5\_NOTA** e **C5\_SERIE** fazem parte do cabeçalho do Pedido; ou seja, guardam informações gerais do Pedido, e não, por Item do Pedido.

Deste modo, esses campos somente são preenchido com o Número/Serie da Nota ao faturar o Pedido por completo.

 Quando o Pedido não é Faturado por completo; porém, ocorre a Eliminação de seu Resíduo (**MATA500**), o campo **C5\_NOTA** recebe o conteúdo XXXXXX (6 ou 9 dígitos de acordo com sua configuração de numeração) e **C5\_SERIE** também com XX indicando que apesar de não ter sido faturado por completo, o Pedido encontra-se Encerrado.

**Saiba Mais**:  
**[Campos C5\_NOTA e C5\_SERIE](http://tdn.totvs.com/display/PROT/FAT0043+Campos+C5_NOTA+e+C5_SERIE+preenchidos+com+XXXXX)**
