---
article_id: 360025580132
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 0a704524d8b49c5a0c3b7c4d09837d09daf510555b5bc7c5c122272033435147
fetched_at: '2026-06-28T22:36:59.006379+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro ao Integrar
  de Pedido de Exportação do Logix
type: support-article
updated_at: '2022-06-14T20:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025580132-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-ao-Integrar-de-Pedido-de-Exporta%C3%A7%C3%A3o-do-Logix
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:03:00 min  
  
Ocorrência**No Logix ao tentar integrar pedidos para o SIGAEEC é apresentada falha na integração:

="error">AJUDA:REGNOIS Não existe registro relacionado a este código. Tabela EE7 22/03/19 15:58:47 Pedido ERP - EE7\_PEDERP := 914076 Pedido - EE7\_PEDIDO := 914076 Cod. Import. - EE7\_IMPORT := 102117 Loja Import. - EE7\_IMLOJA := . Cod.Fornec. - EE7\_FORN := 10 < -- Invalido Loja Fornec. - EE7\_FOLOJA := .  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024769411/mceclip2.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões

**Causa**Posicionamento de campos (EE7\_FORN, EE7\_IMLOJA e EE7\_FORNDE) incorreto e identificação diferente de Fornecedor no cadastro de Fornecedor/Fabricante/Exportador.

**Solução**1- Posicionar corretamente os EE7\_FORN, EE7\_IMLOJA, EE7\_FORNDE, sempre obedecendo a sequência Código/Loja/Descrição, alteração das posições deve ser efetuada através do SIGACFG.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024769351/mceclip1.png)

2- No cadastro de Exp./forn./fabr. (EECAC115) alterar o cadastro, na aba Outros informar o campo Identificac. (A2\_ID\_FBFN) como 2- Fornecedor ou 3- Todos , caso este cadastro possa ser utilizado em mais de uma função nos processos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024756212/mceclip0.png)
