---
article_id: 360020572912
category: ADVPL - Ponto de Entrada
content_hash: d73e859cb6fc011d1ea4f2a4ae55b9d6f3de6f491175ceeb0c2c9b35dc914fed
fetched_at: '2026-06-28T22:40:11.824300+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  FINA010 MVC
type: support-article
updated_at: '2023-01-27T21:42:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020572912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-FINA010-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

THREAD ERROR ([XXXX], XXXXXXX, XXXXXX) xx/xx/xxxx xx:xx:xx

variable is not an object on FINA010BRA(FINA010BRA.PRW)   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Erro ocorre pois o nome do arquivo customizado .prw foi compilado com o nome da rotina.  
  
**Solução**Ao se escrever um fonte em MVC que será uma *User Function,* cuidado ao se atribuir o ID do modelo de dados (Model), pois ele não poderá ter o mesmo nome do fonte. Se o fonte tiver o nome FINA010, o ID do Modelo de Dados (Model) não poderá ser também FINA010, ou seja, o **nome do arquivo.prw** **não** poderá ser o mesmo da user function.

**Saiba mais**[Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968)
