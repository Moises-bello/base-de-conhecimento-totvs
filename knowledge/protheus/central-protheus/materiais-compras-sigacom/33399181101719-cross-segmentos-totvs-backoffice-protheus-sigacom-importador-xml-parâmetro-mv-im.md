---
article_id: 33399181101719
category: Materiais - Compras (SIGACOM)
content_hash: 3a251019becd5a32a78f666b18179c8616b737e7b06f8ddfa26bc60bd0529a21
fetched_at: '2026-06-28T22:41:25.522310+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: ‭Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador Xml - Parâmetro
  MV_IMPXML sendo Desativado Automaticamente.
type: support-article
updated_at: '2025-07-11T12:12:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33399181101719--Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-Xml-Par%C3%A2metro-MV-IMPXML-sendo-Desativado-Automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33399181091095) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
O conteúdo do parâmetro MV\_IMPXML foi desativado sozinho   
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) -  Compras - A partir da release 12.1.2310  
  
**Causa**  
O parâmetro MV\_IMPXML é desativado automaticamente quando a rotina Configuração TOTVS Colaboração é executada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33399193314583)  
   
Isso ocorre, pois, para que a integração do Protheus com o TOTVS Colaboração funcione o parâmetro precisa estar desabilitado.

Por padrão no Protheus não podemos utilizar integração com o TOTVS Transmite e com o TOTVS Colaboração ao mesmo tempo. A integração é definida pelo parâmetro MV\_IMPXML que, por sua vez, pode receber apenas um conteúdo: .T. (integração com TOTVS Transmite) ou .F. (integração com TOTVS Colaboração).

***Saiba Mais :***

* [Importador XML x Transmite - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/display/public/PROT/Importador+XML+x+Transmite)
* [TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os principais parâmetros na Integração do Importador XML x TOTVS Transmite?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26961234993559-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-principais-par%C3%A2metros-na-Integra%C3%A7%C3%A3o-do-Importador-XML-x-TOTVS-Transmite)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais os Parâmetros utilizados no Importador XML?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004990632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-os-Par%C3%A2metros-utilizados-no-Importador-XML)
