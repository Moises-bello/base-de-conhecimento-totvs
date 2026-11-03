---
article_id: 20342730762519
category: Materiais - Compras (SIGACOM)
content_hash: fc28cabbbe11ca20721b2fb8838257a2544dedf23a678674e5d97ad58908a360
fetched_at: '2026-06-28T22:41:14.246392+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Automatização da natureza
  de rendimento - Importador XML
type: support-article
updated_at: '2024-06-11T17:43:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20342730762519-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Automatiza%C3%A7%C3%A3o-da-natureza-de-rendimento-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20342745477015) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Como implementar a natureza de rendimento na rotina de importação XML. ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**Este documento tem como objetivo demonstrar a implementação da automatização da natureza de rendimento na rotina de importação XML.   
Para esta nova funcionalidade foi criado o campo **DT\_NATREN - (Natureza de Rendimento),**este campo será preenchido na importação do arquivo xml,  apenas para os tipos de nota: **NFS (319), CTE (214) e CTEOS** **(273)**, a edição do campo no monitor, também ficará disponível apenas para esses tipos.

Ao realizar a importação do arquivo o sistema verificará se se existe a natureza de rendimento no **complemento fiscal do produto - (FISA180**), se sim, replicará a mesma para o campo **DT\_NATREN,**conforme imagens abaixo**:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20342730723223)**

**Monitor:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20342745479063)**

**Importante**

Para documentos CTe -  (214 e 273), o sistema verificará se existe nota de origem, caso exista, pegará a natureza de rendimento da mesma, senão,  irá verificar o complemento fiscal do produto.

**Saiba mais :**

[Automatização da natureza de rendimento - Importador XML](https://tdn.totvs.com/pages/releaseview.action?pageId=811701660)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Cross Segmentos - Totvs Backoffice Protheus - Totvs Colaboração / Importador XML - Como são definidos os produtos e o Tipo de Documento na importação do Documento de Frete / CTe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027518891)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
