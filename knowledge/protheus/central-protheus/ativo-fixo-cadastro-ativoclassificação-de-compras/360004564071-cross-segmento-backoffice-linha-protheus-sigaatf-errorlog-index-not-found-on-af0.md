---
article_id: 360004564071
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: a5e8d1cea3667fe6c8f988e1fd3cecdc72259eacdcadec635d3979a68f1619a8
fetched_at: '2026-06-28T22:41:48.271924+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - errorlog: Index not
  found. on AF012EST'
type: support-article
updated_at: '2023-11-30T12:01:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004564071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-errorlog-Index-not-found-on-AF012EST
---

**Ocorrência**No módulo **Ativo Fixo**, na inclusão ou classificação de bens, ocorre o errorlog:

SN2010: SetOrder - Index not found. on AF012EST(ATFA012.PRW) 14/05/2018 15:27:08 line : 11833

**Ambiente**  
Protheus – Ativo Fixo  Versão 12  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**Verifique em seu ambiente os índices para tabela SN2 em seu dicionário SIX.  
   
 Realize os procedimentos que seguem, primeiramente em ambiente de homologação.**

**Observe se o X2\_UNICO da tabela SN2 está conforme abaixo:**  
   
 **N2\_FILIAL+N2\_CBASE+N2\_ITEM+N2\_TIPO+N2\_SEQ+N2\_SEQUENC**  
   
**Após isso, crie o índice com a ordem = 2 em sua SIX, conforme abaixo:**  
   
 **N2\_FILIAL+N2\_CBASE+N2\_ITEM+N2\_TIPO+N2\_SEQ**  
   
 Veja mais  
   
 <http://tdn.totvs.com/display/public/PROT/DSERCTR1-9859_DT_Descricao_estendida_chave_duplicada>
