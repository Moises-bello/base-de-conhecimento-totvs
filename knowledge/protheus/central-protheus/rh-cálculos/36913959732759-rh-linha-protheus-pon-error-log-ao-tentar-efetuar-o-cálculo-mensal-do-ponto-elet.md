---
article_id: 36913959732759
category: RH - Cálculos
content_hash: fbda8d36cb889aaed76466a36f03f842abbe01d8b2d0a38ced40e8f3f7f49f00
fetched_at: '2026-06-28T22:44:51.637842+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON - Error log ao tentar efetuar o cálculo mensal do
  Ponto Eletrônico
type: support-article
updated_at: '2025-12-10T16:46:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36913959732759-RH-Linha-Protheus-PON-Error-log-ao-tentar-efetuar-o-c%C3%A1lculo-mensal-do-Ponto-Eletr%C3%B4nico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36913959718423) Tempo aproximado para leitura: **01:00:00 min**  
  
**Ocorrência**  
*Error log* ao tentar efetuar o cálculo mensal do Ponto Eletrônico: ***InterFunctionCall: cannot find function*** **GETMESESBH** ***in*** **AppMap** ***on*** **PNM070PROC(PONM070.PRX)**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
O *error log* ocorre por falta da função **GETMESESBH,** por falta de atualização do ambiente  
  
**Solução**  
Para correção do erro é necessário atualizar o ambiente com o pacote de expedição contínua:  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
