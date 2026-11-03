---
article_id: 360052466194
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 63a0581634466aaa07465d7fdb87cf5407159f57f9a50ce84717c806ae097ca3
fetched_at: '2026-06-28T22:39:56.359036+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Código de
  Serviço através da CE1 (FISA052)
type: support-article
updated_at: '2025-07-14T21:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052466194-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-C%C3%B3digo-de-Servi%C3%A7o-atrav%C3%A9s-da-CE1-FISA052
---

**Dúvida**Como configurar para que o rdmake NFSEXMLENV considere o Código de Serviço cadastrado na CE1 (campo CE1\_CPRISS) para montagem do XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para que o rdmake filtre o registro correto na CE1, deverá informar no Pedido de Vendas os campos C5\_ESTPRES e C5\_MUNPRES com o mesmo conteúdo (estado/munípio) dos campos CE1\_ESTISS e CE1\_CMUISS da rotina FISA052.  
  
Também deverá habilitar o parâmetro **MV\_ISSXMUN** **= .T.** (Tipo Lógico).  
  
Exemplo abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086351933/mceclip3.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086355293/mceclip5.png)  
  
Note que mesmo no Cadastro de Produto estando o B1\_CODISS = 1401, foi utilizado o 1101 informado e cadastrado na rotina FISA052 (Alíquotas de ISS).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085171394/mceclip1.png)  
  
**Obs.: O rdmake NFSEXMLENV com essa tratativa é a partir de 19/03/2020.**
