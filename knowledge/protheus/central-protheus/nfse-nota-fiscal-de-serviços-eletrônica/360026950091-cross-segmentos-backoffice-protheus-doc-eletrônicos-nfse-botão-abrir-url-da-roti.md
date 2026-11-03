---
article_id: 360026950091
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 656d348a29eea4ad8c2883076d6df8269511622702ccdc10e45c2e5caf0ddf17
fetched_at: '2026-06-28T22:39:56.327823+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Botão Abrir
  URL da rotina FISA022
type: support-article
updated_at: '2023-09-20T19:15:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026950091-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Bot%C3%A3o-Abrir-URL-da-rotina-FISA022
---

**Dúvida**Como habilitar o botão Abrir URL no menu Outras Ações da rotina FISA022?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução** **1.** Para habilitar o botão "Abrir URL" utilize o parâmetro **MV\_NFSLINK = .T.**  
Esse botão irá abrir no navegador o link da nota disponível no campo LINK\_NFSE da tabela SPED051.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074006533/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072818194/mceclip1.png)  
  
**2.** Após isso automaticamente será aberto em seu navegador padrão o PDF com a nota em questão.  
  
**Importante:**   
O campo LINK\_NFSE só possui conteúdo para prefeituras que retornam o link da nota no XML de retorno, dentro do campo XML\_RET da SPED053.
