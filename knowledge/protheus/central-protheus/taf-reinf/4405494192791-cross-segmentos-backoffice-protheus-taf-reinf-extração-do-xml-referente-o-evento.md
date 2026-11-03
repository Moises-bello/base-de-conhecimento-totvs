---
article_id: 4405494192791
category: TAF - REINF
content_hash: 3cff10cd74a0cb98636ba293934dec586307bf80ce6af3e7be1f9c7265f7ea41
fetched_at: '2026-06-28T22:41:33.571481+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Extração do XML Referente
  o Evento R-2055
type: support-article
updated_at: '2023-03-31T17:06:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405494192791-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Extra%C3%A7%C3%A3o-do-XML-Referente-o-Evento-R-2055
---

**Dúvida**  
Como extrair o XML contendo as informações referente o evento R-2055 para conferencia?

**Ambiente**  
Linha Protheus - TAF - Versão 12  
  
**Solução**  
1-Inclua a rotina TAFA576 (R-2055 - Aquisição Produtor Rural) no menu do Protheus;

2-Acesse o Configurador (SIGACFG) acesse Ambiente/ Cadastros/ Menus e inclua, no menu do módulo Livros Fiscais (SIGAFIS), conforme especificação a seguir:

**Nome do Menu**: Atualizações

**Submenu**: Eventos Reinf

**Nome da Rotina**: R-2055 - Aquisição Produtor Rural

Programa: TAFA576

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405505040023/mceclip0.png)

3-Após incluir, poderá acessar o evento e R-2055 e acessar o XML no botão "Outras Ações"

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405506498967/mceclip1.png)
