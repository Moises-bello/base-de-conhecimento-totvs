---
article_id: 36176240519063
category: Financeiro - Smart View
content_hash: 7b3a4767c691eaff1b69f6667325a84684e2d2a28c31905a9574560fc4527414
fetched_at: '2026-06-28T22:37:44.643858+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Smartview - FINSV010
  não considera baixas realizadas pela rotina de faturas
type: support-article
updated_at: '2025-11-10T13:26:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36176240519063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Smartview-FINSV010-n%C3%A3o-considera-baixas-realizadas-pela-rotina-de-faturas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36176240487959)**Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
O relatório SV FINSV010 não está considerando as "baixas" feitas pela rotina FINA290 - Geração de Faturas.   
Ao comparar com o FINR190, percebemos algumas diferenças na forma como as informações são exibidas no novo objeto de negócio.  
  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210.

**Solução**

Esse comportamento ocorre porque o **FINSV010** utiliza um **grupo de perguntas diferente** do modelo anterior em ADVPL. No novo formato, o **SmartView não considera a baixa por fatura como uma baixa efetiva**, e sim como uma **renegociação ou agrupamento de títulos**.

É importante reforçar que a evolução dos objetos de negócio — de **ADVPL para SmartView** — **não é uma substituição direta**, mas sim uma **melhoria na forma de exibição dos relatórios**.

No modelo anterior, o **FINR190** utilizava o grupo de perguntas **FIN190**.  
Já o novo **FINSV010 (SmartView)** utiliza o grupo **FINT001**, criado especialmente para a nova estrutura de controle de baixas.

Por esse motivo, o FINSV010 **não exibe as baixas por fatura**, pois adota um conceito diferente de operação.  
Para esse tipo de análise, existe um objeto de negócio específico: o **FINSV032**, que apresenta **a fatura gerada e os títulos que a compõem**.

Você pode conferir mais detalhes do FINSV032 na documentação oficial:  
[FINSV032 – Demonstrativo de Faturas](https://tdn.totvs.com/pages/releaseview.action?pageId=790645284)

Nos demais relatórios, apenas as **baixas efetivas** serão demonstradas.

**Saiba mais**

[Financeiro - Smart View](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32632656432151-Financeiro-Smart-View)
