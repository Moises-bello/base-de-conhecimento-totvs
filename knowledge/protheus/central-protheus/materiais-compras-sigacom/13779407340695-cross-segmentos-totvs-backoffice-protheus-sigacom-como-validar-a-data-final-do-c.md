---
article_id: 13779407340695
category: Materiais - Compras (SIGACOM)
content_hash: 47ecbbd91065e98fb814aeb81adb7f517a762e141037a9516fcedf7887965cc8
fetched_at: '2026-06-28T22:41:16.098656+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como validar a Data
  Final do Contrato de Parceria expirado na Inclusão da Autorização de Entrega?
type: support-article
updated_at: '2024-07-12T10:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13779407340695-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-validar-a-Data-Final-do-Contrato-de-Parceria-expirado-na-Inclus%C3%A3o-da-Autoriza%C3%A7%C3%A3o-de-Entrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24831644374807) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como validar a Data Final do Contrato de Parceria expirado na Inclusão da Autorização de Entrega?  
  
**Ambiente**  
Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**Ajustar o parâmetro com conteúdo **MV\_CONTVLD = 1.**

Dessa forma, na roitna de Autorização de Entrega não serão trazidos os Contratos que possuem a "Data Final" do Contrato de Parceria anterior à data de Emissão que está na Autorização de Entrega.

Segue exemplo abaixo:

O Contrato Número 000004 tem a Data Final **05/03/2022.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13779281761431)

Ao acessar a Rotina de Autorização de Entrega com Data 12/04/2023 , dessa forma carregou somente os Contratos com **Data final** a Partir de 12/04/2023.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13779354062487)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13779732717847)

***Saiba Mais :***

* [MV\_CONTVLD - Validar a data final do contrato de parceria quando vinculado a Autorização de entrega.](https://tdn.totvs.com/pages/releaseview.action?pageId=838218434)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Permitir Autorização de Entrega para um fornecedor diferente do Contrato de Parceria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024138112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Permitir-Autoriza%C3%A7%C3%A3o-de-Entrega-para-um-fornecedor-diferente-do-Contrato-de-Parceria?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais os Pontos de Entrada disponíveis na rotina MATA125 - Contrato de Parceria ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025977452-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-os-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-MATA125-Contrato-de-Parceria-?source=search)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
