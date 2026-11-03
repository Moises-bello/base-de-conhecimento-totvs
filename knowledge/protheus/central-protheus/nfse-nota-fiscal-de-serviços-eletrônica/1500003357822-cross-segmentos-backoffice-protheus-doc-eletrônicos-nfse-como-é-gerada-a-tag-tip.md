---
article_id: 1500003357822
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8d0c932a7cc2f8eab5d77e0d595f2f6156f88a7fddced3772c83aff2e06e7fd2
fetched_at: '2026-06-28T22:39:56.374774+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Como é gerada
  a tag <tipotrib>7 pelo rdmake NFSEXMLENV?
type: support-article
updated_at: '2025-07-14T21:28:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003357822-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Como-%C3%A9-gerada-a-tag-tipotrib-7-pelo-rdmake-NFSEXMLENV
---

**Dúvida**Como e quais são as possibilidades para geração da tag <tipotrib> = 7 no remessa pelo rdmake NFSEXMLENV?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003419922/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Atualmente as possibilidades são essas abaixo, onde o conteúdo vindo desses campos **precisará ser = '05'** para entrar na condição:  
  
Se D2\_CLASFIS não estiver vazio e o FT\_CSTISS estiver vazio, será considerado o conteúdo do **D2\_CLASFIS**;  
Se D2\_CLASFIS não estiver vazio e o FT\_CSTISS **não** estiver vazio, será considerado o conteúdo do **FT\_CSTISS**.  
  
Exemplo: Em um cenário onde nas tabelas para uma nota tenha ***somente** o campo D2\_CLASFIS preenchido **e com conteúdo '05'**,* entrará na condição do print acima.  
 *Se ambos os campos tiverem conteúdos vazios, por padrão o array aCST receberá valor default: '50', não caindo nessa condição.*

Observações:  
Lembrando que o **D2\_CLASFIS** é montado com a junção dos campos: B1\_ORIGEM + F4\_SITTRIB;  
Já o **FT\_CSTISS** é montado com o conteúdo do campo F4\_CSTISS.
