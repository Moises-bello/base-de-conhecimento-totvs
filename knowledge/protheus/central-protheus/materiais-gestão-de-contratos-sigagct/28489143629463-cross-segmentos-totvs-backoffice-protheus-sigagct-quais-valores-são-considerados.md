---
article_id: 28489143629463
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: af103ca20dc4695ad14f42eecb8b81a260408312f88b4225196f1c4b98addcee
fetched_at: '2026-06-28T22:37:24.079193+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais valores são considerados
  na base de cálculo do Valor de Caução retenção da Medição?
type: support-article
updated_at: '2024-12-13T11:10:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28489143629463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-valores-s%C3%A3o-considerados-na-base-de-c%C3%A1lculo-do-Valor-de-Cau%C3%A7%C3%A3o-reten%C3%A7%C3%A3o-da-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28489143605271) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais valores são considerados na base de cálculo do Valor de retenção da Medição?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos - Todas as versões  
  
**Solução**

A retenção é calculada considerando o total líquido(CND\_VLLIQD), subtraindo-se os valores do Desconto( CND\_DESCME ) e Aditivo(tabela CZY), além disso, considera as Multas/Bonificações que impactam o pedido(CNR\_FLGPED como 1=SIM), sobre o resultado é aplicado o percentual do caução(CN9\_MINCAU). A documentação [GCT0151\_Processo de Caução na retenção na nova rotina de medição (CNTA121)](https://tdn.totvs.com/x/c1aHK) foi atualizada para explicar esse processo. Atualmente não há uma forma de mudar esse calculo via parâmetro ou via ponto de entrada, só há como customizar o percentual de retenção [CN121VRE - Permite alterar o percentual de retenção na medição](https://tdn.totvs.com/pages/releaseview.action?pageId=271386185)

Saiba mais em :

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como é tratado o Controle de Cauções do Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022755132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-%C3%A9-tratado-o-Controle-de-Cau%C3%A7%C3%B5es-do-Gest%C3%A3o-de-Contratos)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Caução de Retenção - Como abater o valor da Retenção do caução na medição, do pedido gerado ou do título?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404860413847-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Cau%C3%A7%C3%A3o-de-Reten%C3%A7%C3%A3o-Como-abater-o-valor-da-Reten%C3%A7%C3%A3o-do-cau%C3%A7%C3%A3o-na-medi%C3%A7%C3%A3o-do-pedido-gerado-ou-do-t%C3%ADtulo)
* [Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
