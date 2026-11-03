---
article_id: 12750702835351
category: Financeiro - Reinf
content_hash: cdd175e6fcfc418fda77479797126264651bf97556b8f440ce5dc9ee682ec6aa
fetched_at: '2026-06-28T22:37:51.808165+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Compartilhamento
  das novas tabelas do REINF Financeiro
type: support-article
updated_at: '2023-10-05T14:40:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12750702835351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Compartilhamento-das-novas-tabelas-do-REINF-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17907339363735) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais compartilhamentos necessários para as novas tabelas do REINF no Financeiro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - REINF - A partir da versão 12.1.33  
  
**Solução**Quando a tabela **ImpostosXNat.Rend.XBaixas (FKY)** está com o compartilhamento diferente da tabela **Baixas a Pagar (FK2)**, é apresentado o seguinte help;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12750519163927)  
  
Este help é apresentado pois o compartilhamento da tabela **FKY** estão diferentes da **FK2** e **SE5** conforme , conforme descrito na documentação abaixo;

[Gravação dos Impostos x Natureza de rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=728637277)  
  
Segue o compartilhamento que deverá atualizar conforme documentação do REINF.  
[EFD-REINF](https://tdn.totvs.com/display/public/PROT/EFD-REINF)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12750617108631)  
  
**Saiba Mais**

[Compartilhamento de tabelas do módulo Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=307830478)
