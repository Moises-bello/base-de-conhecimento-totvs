---
article_id: 23337764870295
category: Materiais - Compras (SIGACOM)
content_hash: d7904a8b666b266eedb0a5a846f677f517f5be03ce3103d1b5d4b1269668a439
fetched_at: '2026-06-28T22:41:16.172871+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Contabilização Compras
  utilizando campos da tabela F2D do novo configurador de tributos
type: support-article
updated_at: '2024-05-08T12:41:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23337764870295-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras-utilizando-campos-da-tabela-F2D-do-novo-configurador-de-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23337764841111) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como adequar  o sistema para que ocorra a contabilização das informações pelo novo configurador de tributos, utilizando o LP 650 do documento de entrada?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Hoje, as contabilizações dos impostos ocorrem diretamente pelo documento de entrada, pelos lançamentos padrão do compras ( por exemplo 650 ). Porém esse LP não verifica a tabela F2D do configurador de tributos. Para que essa contabilização ocorra utilizando o LP 650, é necessário seguir os passos abaixo :

Será necessário criar um novo índice na tabela F2D ( FD2\_FILIAL + F2D\_IDREL + F2D\_TRIB ).

E assim, no campo "Vlr Moeda, CT5\_VLR01" no lançamento padrão, utilizar o "Posicione" ou "GetAdvFVal" cujos exemplo podem ser verificaodos nos links abaixo, para realizar o posicionamento correto da informação na tabela F2D

[Posicione](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029397891-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Validar-fun%C3%A7%C3%A3o-Posicione)

[GetAdvFVal](https://tdn.totvs.com/pages/releaseview.action?pageId=6814929)

**Exemplo de configuração do LP :**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23337773965335)**

Foi aberta também uma solicitação de melhoria para a criação do índice na F2D diretamente no produto padrão.

[Solicitação de melhoria, criação de índice F2D para contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/community/posts/22343353420567-TOTVS-Backoffice-Linha-Protheus-Fiscal-Nova-publica%C3%A7%C3%A3o-TOTVS-Backoffice-Linha-Protheus-Fiscal-Contabiliza%C3%A7%C3%A3o-Tributo-Gen%C3%A9rico)

***Saiba Mais:***

*[Contabilização no compras](https://totvssuporte.zendesk.com/knowledge/editor/01HAAEH3EEY9X6H16WFHY2JYYV/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360027616491)*

*[Configurador de tributos do módulo fiscal](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.33#CFGTRIBConfiguradordeTributos12.1.33-Contabiliza%C3%A7%C3%A3odostributosgen%C3%A9ricos)*

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
